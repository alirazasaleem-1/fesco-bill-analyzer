# ⚡ FESCO Bill Analyzer

A Python-based web application that retrieves and analyzes FESCO electricity bill information using a reference number.

Built with **Streamlit**, **Requests**, and **BeautifulSoup**, this project demonstrates web scraping, HTML parsing, and data extraction from real-world web pages.

---

## 📌 Features

* Retrieve bill information using a FESCO reference number
* Extract key bill details automatically
* Clean and simple Streamlit interface
* Fast and lightweight implementation
* Demonstrates real-world web scraping techniques

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Requests
* BeautifulSoup4

---

## 📂 Project Structure

```text
fesco-bill-analyzer/
│
├── app.py           # Streamlit user interface
├── scraper.py       # Retrieves bill data from source
├── parser.py        # Extracts and processes bill information
├── requirements.txt # Project dependencies
└── README.md
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/alirazasaleem-1/fesco-bill-analyzer.git
cd fesco-bill-analyzer
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser automatically.

---

## 📖 How It Works

1. User enters a FESCO reference number.
2. The application sends a request to the bill source.
3. Bill data is retrieved as HTML.
4. BeautifulSoup parses the HTML content.
5. Relevant bill information is extracted and displayed.

---

## ⚠️ Limitations

This project depends on the availability and structure of the external bill source website.

If the source website is unavailable, changes its HTML structure, or blocks requests, the application may not function correctly.

This project is intended for educational and learning purposes to demonstrate web scraping and data extraction techniques.

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience with:

* Web scraping
* HTML parsing
* Streamlit application development
* Error handling
* Real-world debugging
* Working with third-party data sources

---

## 👨‍💻 Author

**Ali Raza Saleem**

BS Computer Science Student
University of Agriculture Faisalabad

GitHub: https://github.com/alirazasaleem-1

LinkedIn: https://www.linkedin.com/in/ali-raza-saleem-9906323a1/

---

## 📜 License

This project is open-source and available under the MIT License.
