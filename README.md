<div align="center">

# 🦜🔗 LangChain Output Parsers Playground

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![LangChain](https://img.shields.io/badge/LangChain-LCEL-green)
![HuggingFace](https://img.shields.io/badge/HuggingFace-LLM-yellow?logo=huggingface)
![Pydantic](https://img.shields.io/badge/Pydantic-Validation-orange)
![Status](https://img.shields.io/badge/Status-Learning%20Project-blueviolet)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

### Developed by **[Ghulam Muhammad]**
*Building the foundation for Agentic AI in 2026*

---
</div>

This repository documents hands-on experiments with **LangChain output parsers**, focusing on how to reliably structure, validate, and chain LLM outputs using HuggingFace-hosted models.

The goal is to understand **when and why to use different output parsing strategies** and how they behave in single-step and multi-stage LLM pipelines.

---

## 🧠 Concepts Covered

* JSON-based structured outputs
* Schema validation using Pydantic
* Plain string output parsing
* Two-stage LLM pipelines (generation → summarization)
* Prompt chaining with and without output parsers

All examples use **LangChain Expression Language (LCEL)** and `ChatHuggingFace` with DeepSeek And `Qwen/Qwen3-Coder-Next` models.

---

## 📂 Project Structure

```
langchain-output-parsers-playground/
├── json_output_parser.py
├── pydantic_output_parser.py
├── with_stroutputparser.py
├── Two-Stage LLM Pipeline.py
├── without_parser.py
```

## 📄 File Overview

### 1️⃣ `json_output_parser.py`
Demonstrates how to:
- Enforce structured JSON output
- Use `JsonOutputParser`
- Build a clean chain using LCEL

**Use case:** When you want lightweight structured data without strict schema validation.

---

### 2️⃣ `pydantic_output_parser.py`
Demonstrates how to:
- Define a strict schema using Pydantic
- Enforce type safety and validation
- Parse LLM output into a Python object

**Use case:** When correctness and validation matter (production-grade outputs).

---

### 3️⃣ `with_stroutputparser.py`
Demonstrates:
- A two-stage LLM pipeline
- First LLM generates a detailed report
- Second LLM summarizes the report
- Uses `StrOutputParser` with different temperatures

**Use case:** Agent-style pipelines and report → summary workflows.

---

### 4️⃣ `Two-Stage LLM Pipeline.py`
Demonstrates:
- Multi-prompt chaining without intermediate routing
- Sequential LLM calls using string outputs
- Simpler version of a multi-step pipeline

**Use case:** Quick prototyping without complex routing logic.

---

### 5️⃣ `without_parser.py`
Demonstrates:
- Manual prompt invocation
- Raw `.content` handling
- No output parsing or validation

**Use case:** Baseline example to understand why output parsers matter.

---

## 🚀 Key Learnings

- Output parsers dramatically reduce prompt brittleness
- Pydantic parsers provide the strongest guarantees
- LCEL makes multi-stage pipelines readable and composable
- Temperature tuning matters in multi-LLM workflows

## ⚙️ Setup & Usage

### Clone the Repository

```bash
git clone https://github.com/<your-username>/langchain-output-parsers-playground.git
cd langchain-output-parsers-playground
````

### Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
# venv\Scripts\activate    # Windows
```


## 🛠️ Requirements

- Python 3.10+
- LangChain
- langchain-huggingface
- python-dotenv
- pydantic

### Install Dependencies

```bash
pip install langchain langchain-huggingface python-dotenv pydantic
```

### Environment Setup

Create a `.env` file:

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
```

## ▶️ Running the Examples

```bash
python json_output_parser.py
python pydantic_output_parser.py
python with_stroutputparser.py
python Two-Stage LLM Pipeline.py
python without_parser.py
```

---

## 📌 Notes

* HuggingFace access token must be set via `.env`
* Models used: `deepseek-ai/DeepSeek-V3.2` and `Qwen/Qwen3-Coder-Next`
* Examples are intentionally minimal for learning clarity

---

## 📜 License

This repository is created for **learning and experimentation purposes**.
Feel free to explore, fork, and adapt.
