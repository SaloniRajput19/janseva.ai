# Janseva.ai 🇮🇳

Janseva.ai is an AI-powered government scheme assistance platform that helps users
discover relevant government schemes and understand their eligibility and benefits.

The system combines structured government scheme data, retrieval-based search,
eligibility rules, and an AI-based response system to provide users with
relevant and easy-to-understand information.

---

## 📌 Problem Statement

People may find it difficult to discover suitable government schemes because
information is spread across different sources and eligibility conditions can
be difficult to understand.

Janseva.ai aims to simplify this process by allowing users to interact with
government scheme information through an AI-powered interface.

---

## 🎯 Objectives

- Help users discover relevant government schemes.
- Provide information about scheme benefits and eligibility.
- Retrieve relevant scheme information from the available dataset.
- Provide AI-assisted responses to user queries.
- Support rule-based eligibility checking.
- Provide speech-to-text and text-to-speech functionality.

---

## ✨ Features

- 🔎 Government scheme information retrieval
- 🤖 AI-assisted question answering
- ✅ Eligibility checking using predefined rules
- 📚 Retrieval of relevant scheme information
- 🗣️ Speech-to-Text support
- 🔊 Text-to-Speech support
- 🖥️ Streamlit-based user interface
- 🗄️ Supabase-based data storage

---

## 🏗️ System Workflow

The overall workflow of Janseva.ai is:

```text
Government Scheme Dataset
          ↓
Data Cleaning & Analysis
          ↓
Chunking of Scheme Information
          ↓
Embedding / Indexing
          ↓
Supabase Database
          ↓
User Query
          ↓
Query Processing
          ↓
Relevant Scheme Retrieval
          ↓
Eligibility Rules + AI/LLM
          ↓
Final Response
          ↓
Streamlit Interface
```

For voice-based interaction:

```text
User Speech
     ↓
Speech-to-Text
     ↓
User Query
     ↓
Retrieval + Eligibility + AI
     ↓
Response
     ↓
Text-to-Speech
     ↓
Audio Output
```

---

## 🧰 Technologies Used

### Programming Language
- Python

### Frontend
- Streamlit

### Database
- Supabase

### AI / LLM
- Large Language Model (LLM)
- Retrieval-based question answering

### Data Processing
- Pandas
- Data cleaning
- Text chunking
- Embeddings

### Voice
- Speech-to-Text (STT)
- Text-to-Speech (TTS)

### Development Tools
- Jupyter Notebook
- VS Code
- Git
- GitHub

---

## 📂 Project Structure

```text
janseva.ai/
│
├── backend/
│   ├── config.py
│   ├── db.py
│   ├── graph.py
│   ├── llm.py
│   ├── retrieval.py
│   ├── rules.py
│   ├── schemes.py
│   ├── stt.py
│   ├── test_db.py
│   ├── test_setup.py
│   └── tts.py
│
├── data/
│   ├── processed/
│   │   ├── cleaned_janseva_schemes.csv
│   │   └── schemes_clean.csv
│   │
│   ├── raw/
│   └── updated_data.csv
│
├── frontend/
│   └── streamlit_app.py
│
├── notebooks/
│   ├── 01_dataset_analysis.ipynb
│   └── 02_chunking.ipynb
│
├── Scripts/
│   ├── chunk_and_embed.py
│   └── ingest_schemes.py
│
├── tests/
│   ├── test_graph.py
│   ├── test_retrieval.py
│   ├── test_rules.py
│   └── test_stt_tts.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/SaloniRajput19/janseva.ai.git
```

### 2. Move into the project directory

```bash
cd janseva.ai
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

For Windows:

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root.

Use `.env.example` as a reference for the required environment variables.

Example:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_SERVICE_KEY=your_supabase_service_key
```

Add other API credentials required by the project to the `.env` file.

> **Important:** Never upload the `.env` file to GitHub because it may contain
> private API keys and credentials.

The `.env` file is excluded using `.gitignore`.

---

## ▶️ Running the Application

After activating the virtual environment and installing the dependencies,
run the Streamlit application:

```bash
streamlit run frontend/streamlit_app.py
```

The application will start in your browser.

---

## 📊 Data Processing Pipeline

The project includes notebooks and scripts for preparing the government
scheme data.

### Dataset Analysis

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Cleaned Dataset
```

### Chunking and Embedding

```text
Cleaned Scheme Data
        ↓
Text Chunking
        ↓
Embedding Generation
        ↓
Storage / Indexing
```

The processed scheme information can then be used for retrieval when answering
user queries.

---

## 🧪 Testing

The project contains test files for different components:

```text
tests/
├── test_graph.py
├── test_retrieval.py
├── test_rules.py
└── test_stt_tts.py
```

These tests help verify the functionality of retrieval, rules, graph-related
logic, and speech components.

---

## 🔒 Security

Sensitive credentials such as API keys and database keys should be stored in
the `.env` file.

The following files and directories are excluded from Git tracking:

- `.env`
- `.venv/`
- `__pycache__/`
- `*.pyc`
- `.ipynb_checkpoints/`

---

## 🚀 Future Improvements

Possible future improvements include:

- Improving scheme recommendation accuracy.
- Supporting more government schemes and datasets.
- Improving multilingual support.
- Enhancing voice-based interaction.
- Improving eligibility matching.
- Adding more advanced analytics and user interaction features.

---

## 👩‍💻 Author

**Saloni Singh Rajput**

GitHub:  
https://github.com/SaloniRajput19