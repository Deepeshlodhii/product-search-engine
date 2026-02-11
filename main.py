from fastapi import FastAPI, HTTPException
from typing import Dict, List
from rapidfuzz import fuzz
import uvicorn

app = FastAPI()

# In-memory database
products_db: Dict[int, dict] = {}
product_counter = 100


############################
# Ranking Function
############################

def rank_products(query: str, product: dict):

    score = 0
    query = query.lower()

    # Text similarity
    title_score = fuzz.partial_ratio(query, product["title"].lower())
    desc_score = fuzz.partial_ratio(query, product["description"].lower())

    score += 0.45 * title_score
    score += 0.25 * desc_score

    # Rating boost
    score += product.get("rating", 0) * 6

    # Stock logic
    if product.get("stock", 0) > 0:
        score += 15
    else:
        score -= 40   # heavy penalty

    # Discount logic
    discount = product["mrp"] - product["price"]
    score += discount / 800

    # Cheap intent detection
    if any(word in query for word in ["sasta", "cheap", "budget", "low price"]):
        score += discount / 400

    # Latest intent detection
    if "latest" in query or "new" in query:
        if "16" in product["title"] or "17" in product["title"]:
            score += 20

    return score



############################
# API 1 — Store Product
############################

@app.post("/api/v1/product")
def store_product(product: dict):
    
    global product_counter
    
    product_counter += 1
    products_db[product_counter] = product
    
    return {"productId": product_counter}


############################
# API 2 — Update Metadata
############################

@app.put("/api/v1/product/meta-data")
def update_metadata(data: dict):
    
    product_id = data.get("productId")
    metadata = data.get("Metadata")
    
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    
    products_db[product_id]["Metadata"] = metadata
    
    return {
        "productId": product_id,
        "Metadata": metadata
    }


############################
# API 3 — Search Products
############################

@app.get("/api/v1/search/product")
def search_product(query: str):
    
    if not products_db:
        return {"data": []}
    
    ranked = []
    
    for pid, product in products_db.items():
        score = rank_products(query, product)
        ranked.append((score, pid, product))
    
    ranked.sort(reverse=True)
    
    result = []
    
    for score, pid, product in ranked:
        temp = product.copy()
        temp["productId"] = pid
        result.append(temp)
    
    return {"data": result}


############################

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
