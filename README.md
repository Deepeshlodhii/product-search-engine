
# 🛒 Product Search Engine Microservice

A high-performance product search microservice built using **FastAPI** that ranks e-commerce products intelligently based on customer intent, product attributes, and relevance.

This system simulates a real-world search engine used in large e-commerce platforms serving millions of products.

---

## 🚀 Project Overview

Search lies at the heart of every e-commerce platform. When a user searches for a product, the system must:

✅ Understand user intent  
✅ Handle spelling mistakes  
✅ Support natural language queries  
✅ Rank products intelligently  
✅ Return results in milliseconds  

This microservice achieves all of the above using modern backend engineering practices.

---

## 🧠 Key Features

### ✅ Intelligent Ranking Algorithm
Products are ranked using a weighted scoring system based on:

- Title similarity
- Description similarity
- Product rating
- Stock availability
- Discount value
- Customer price intent (cheap/budget/sasta)
- Latest product boost

---

### ✅ Typo-Tolerant Search
Supports spelling corrections such as:

```

ifone → iphone
aplpe → apple
samsng → samsung

```

Ensuring better user experience.

---

### ✅ Hinglish Intent Detection
Understands Indian search patterns:

Example queries supported:

- "sasta iphone"
- "cheap phone"
- "budget laptop"

Products with higher discounts are ranked higher for such searches.

---

### ✅ Metadata Support
Products can be enriched with attributes like:

- RAM  
- Storage  
- Screen Size  
- Color  
- Brightness  

Allowing future extensibility for advanced filtering.

---

### ✅ Exception Handling
Global exception handlers ensure the API never crashes and always returns meaningful responses.

---

### ✅ In-Memory Data Store
For fast retrieval (<1000ms latency), products are stored in memory.

This simulates a high-speed cache layer often used in production systems.

---

## 🏗️ Architecture

```

Client → FastAPI → Ranking Engine → In-Memory Database

````

### Components:

**FastAPI**
- Handles HTTP requests
- Provides automatic Swagger documentation

**Ranking Engine**
- Computes relevance score
- Sorts products dynamically

**In-Memory Store**
- Dictionary-based storage
- Ultra-fast reads

---

## ⚙️ Tech Stack

- **Python**
- **FastAPI**
- **Pydantic**
- **RapidFuzz** (fuzzy matching)
- **TextBlob** (spelling correction)
- **Uvicorn**

---

## 📦 Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd product-search-engine
````

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

**Mac/Linux**

```bash
source .venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Server

```bash
uvicorn main:app --reload
```

Server starts at:

```
http://127.0.0.1:8000
```

---

## 📘 API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# 🔥 API Endpoints

---

## ✅ Store Product

### POST `/api/v1/product`

Adds a product to the catalog.

### Example Request:

```json
{
  "title": "iPhone 15",
  "description": "128GB Black",
  "rating": 4.5,
  "stock": 20,
  "price": 70000,
  "mrp": 80000,
  "currency": "INR"
}
```

---

## ✅ Update Metadata

### PUT `/api/v1/product/meta-data`

Adds additional attributes to a product.

Example:

```json
{
  "productId": 101,
  "Metadata": {
    "ram": "8GB",
    "storage": "128GB",
    "color": "Black"
  }
}
```

---

## ✅ Search Products

### GET `/api/v1/search/product?query=iphone`

Returns ranked products based on relevance.

Example queries:

```
iphone
cheap iphone
latest samsung
budget laptop
iphone cover
```

---

## 🧮 Ranking Algorithm Explained

Final Score is calculated as:

```
Score =
0.45 × Title Similarity
+ 0.25 × Description Similarity
+ Rating Boost
+ Stock Boost
+ Discount Weight
+ Intent Matching Bonus
```

### Ranking Priorities:

✔ Relevant title matches
✔ Higher rated products
✔ In-stock items
✔ Better discounts
✔ Newer models

This ensures customers see the most useful products first.

---

## 🧪 Testing the System

### Recommended Flow:

1️⃣ Add products
2️⃣ Update metadata
3️⃣ Perform searches

Try searching:

```
sasta iphone
latest phone
cheap headphones
```

Observe ranking behavior.

---

## ⚠️ Important Note

Since the system uses an **in-memory database**, all data will be lost when the server restarts.

This design was chosen for speed and simplicity.

---

## 🚀 Future Improvements

* Persist catalog using PostgreSQL / MongoDB
* Integrate ElasticSearch for semantic search
* Add Redis caching
* Deploy using Docker
* Implement async processing
* Add recommendation engine

---

## 💡 Engineering Highlights

✔ Clean API design
✔ Modular code
✔ Customer-centric ranking
✔ Fault-tolerant architecture
✔ Production-style validation

---

## 👨‍💻 Author

**Deepesh Lodhi**

If you found this project interesting, feel free to connect!

```

---
