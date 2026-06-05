# 🌐 Flask Framework

## 🔹 Core Components
1. **WSGI (Web Server Gateway Interface)**
2. **Jinja2 Template Engine**

---

## 🧠 What is Flask?
**Flask** is a lightweight Python web framework used to build web applications and APIs quickly.

---

## ⚙️ Flask Overview

- **Type:** Micro web framework (Python)  
- **Use:** Build web apps & REST APIs  
- **Key Idea:** Minimal core, extend with libraries  

### ✨ Features
- Routing  
- Templates (Jinja2)  
- Request handling  

### ✅ Pros
- Simple  
- Flexible  
- Beginner-friendly  

### ❌ Cons
- Fewer built-in features compared to full frameworks  

---

## 🔄 Flask Flow

### ⚙️ Steps
1. **Web Server (Nginx/Apache)** → Receives request  
2. **WSGI Server (Gunicorn/uWSGI)** → Forwards request to Flask  
3. **Flask App** → Creates contexts (application + request)  
4. **Worker** → Executes view function using `request`, `current_app`  
5. **Response** → Sent back to client  

---

## 🧩 Core Concepts

- **Application Context** → Global app-level data  
- **Request Context** → Request-specific data  
- **View Function** → Handles logic and returns response  

---

# 🧠 Jinja2 Template Engine

## 📌 Definition
Jinja2 is a template engine for Python used to generate dynamic HTML by embedding Python-like expressions inside templates.

---

## 🎯 Uses
- Combine **HTML + dynamic data**  
- Used in Flask/Django for frontend rendering  
- Separates **backend logic (Python)** from **UI (HTML)**  

---

## 💡 Concept
> **HTML = Structure**  
> **Jinja2 = Dynamic Data Injection**

Example: Displaying a user name on a webpage.

---

## 🧾 Example (Flask + Jinja2)

### 🐍 Python (Flask)
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", name="Subayan")

<h1>Hello {{ name }}</h1>
```
Output: 
Hello Subayan
  ---
## Key Syntax
```
{{ }} → Display variables**
{% %} → Logic (if, for loops)**
{# #} → Comments**
```