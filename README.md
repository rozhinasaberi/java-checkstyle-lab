# CheckstyleLab

A Java style-checking lab with a Streamlit tutor app that teaches readable code and Checkstyle-friendly formatting.

## What This Project Is About

This repository began as a small Eclipse lab for Checkstyle setup and code-style practice. It now includes a Streamlit tutor app that walks through messy versus clean Java code and explains why naming, indentation, spacing, and structure matter in professional software development.

This is a **Java style and tooling lab with an AI tutor style Streamlit app**.

## What The Tutor App Teaches

- why consistent formatting improves readability
- how naming choices affect maintainability
- what Checkstyle is trying to enforce
- how to turn style feedback into better habits

## Project Structure

- `app.py` - Streamlit tutor app
- `requirements.txt` - Python dependencies for the tutor app
- `src/module-info.java`
- `.checkstyle`
- Eclipse project files: `.project`, `.classpath`, `.settings/`

## Run The Streamlit App

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Tech Stack

- Java
- Python
- Streamlit
- Eclipse
- Checkstyle
