# pdf‑educator: AI‑Powered Academic Companion

Turn your curriculum into dynamic question papers and tailor‑made study notes—instantly! Leveraging the power of OpenAI’s models and a Retrieval‑Augmented Generation (RAG) pipeline, **pdf‑educator** transforms student‑provided PDFs into custom exam papers and concise, high‑quality summaries.

---

## 🚀 Features

* **Smart Question‑Paper Generator**
    * Ingest past-year papers and user prompts
    * Combine your own question bank with AI‑generated prompts
    * Craft balanced mock exams in seconds

* **RAG‑Driven Notes Creator**
    * Parse uploaded textbooks & PPTs (PDFs)
    * Retrieve topic‑relevant passages, then summarize with OpenAI
    * Produce clear, structured notes tailored to your syllabus

* **Modular Django Backend**
    * Clean RESTful APIs
    * Asynchronous PDF parsing & embed‑indexing
    * Secure user upload & management

* **Scalable Architecture**
    * PostgreSQL for metadata & user data
    * Vector database (e.g. Pinecone, FAISS) for embeddings
    * Celery + Redis for background tasks

---

## ⚙️ Tech Stack

| Layer | Tools & Libraries |
| :--- | :--- |
| **Backend** | Django, Django REST Framework, Celery, Redis |
| **AI & Embeddings** | OpenAI API, LangChain, FAISS/Pinecone |
| **Parsing** | pdfminer.six, PyPDF2, python‑pptx |
| **Database** | PostgreSQL |
| **Deployment** | Docker, Gunicorn, Nginx |

---

## 📦 Installation & Setup

1.  **Clone the repo**

    ```bash
    git clone [https://github.com/krinew/pdf-educator.git](https://github.com/krinew/pdf-educator.git)
    cd pdf-educator
    ```

2.  **Create & activate virtual env**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure environment variables**

    ```bash
    cp .env.example .env
    # Set OPENAI_API_KEY, DATABASE_URL, REDIS_URL, VECTOR_DB_URL, etc.
    ```

5.  **Run migrations & start services**

    ```bash
    python manage.py migrate
    celery -A pdfeducator worker --loglevel=info &
    python manage.py runserver
    ```

---

## 🎯 Current Progress & Roadmap

* ✅ **PDF Parsing Module**
* 🟡 **OpenAI Integration** (Question‑Paper Generation)
* 🟡 **RAG Pipeline** (Notes Generation)
* 🔲 User Authentication & Profiles
* 🔲 Frontend UI (React)
* 🔲 Deployment Scripts & CI/CD
* 🔲 Automated Testing & Coverage

*Stay tuned: more features coming soon!*

---

## 🤝 Contributing

We welcome collaborators!

1.  Fork this repo
2.  Create a feature branch (`git checkout -b feature/my-cool-feature`)
3.  Commit your changes (`git commit -m "Add awesome feature"`)
4.  Push to GitHub (`git push origin feature/my-cool-feature`)
5.  Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

**Ready to revolutionize your study workflow?**
Let’s build the future of academic learning—one AI‑powered mock test and note at a time! 😃
