# 📜 Quote API (FastAPI + MongoDB)

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-109989?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white" />
  <img src="https://img.shields.io/badge/PyMongo-3670A0?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" />
  <img src="https://img.shields.io/badge/Python_Dotenv-3776AB?style=for-the-badge&logo=python&logoColor=white" />
</p>

---

A simple FastAPI project that serves random quotes from a MongoDB database.  
Deployed on **Vercel** for serverless hosting.  

🌐 **Live API URL:**  
👉 [https://quote-fastapi-y4ty36w72-raxs-projects-61c34981.vercel.app/](https://quote-fastapi-y4ty36w72-raxs-projects-61c34981.vercel.app/)

---

## 📂 Project Structure
```

.
├── main.py          # FastAPI app
├── requirements.txt # Dependencies
├── .env             # Environment variables (URI for MongoDB)
└── README.md        # Project docs

```

---

## 🔑 Environment Variables
Create a `.env` file in the root directory with:

```

URI=your\_mongodb\_connection\_string

````

---

## ▶️ Running Locally
1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/quote-api.git
   cd quote-api
   ````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

4. Open in browser:

   * Home: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   * Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🌐 API Endpoints

### `GET /`

**Description:** Welcome route.
**Response:**

```json
{
  "hello": "user",
  "welcome": "quote api"
}
```

---

### `GET /quote`

**Description:** Fetches a random quote from MongoDB.
**Response:**

```json
{
  "quote": "If you tell the truth, you don't have to remember anything.",
  "author": "Mark Twain",
  "_id": "68a70f275aa90ecebabdf11d"
}
```

---

### `GET /status`

**Description:** API health check.
**Response:**

```json
"i'am alive"
```

---

## 📦 Deployment

Deployed on **Vercel**:
➡️ [https://quote-fastapi-y4ty36w72-raxs-projects-61c34981.vercel.app/](https://quote-fastapi-y4ty36w72-raxs-projects-61c34981.vercel.app/)

---


