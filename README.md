# Selenium + Playwright Python Automation Framework

A side-by-side comparison framework to learn and evaluate **Playwright** vs **Selenium** for browser automation.
This project is part of my learning journey as an automation engineer transitioning from Selenium to Playwright.

---

## 🚀 Goals

- Build a Python test automation framework that supports both **Selenium** and **Playwright**
- Compare them using real-world test cases
- Use **Pytest**, **Page Object Model**, and other best practices
- Explore differences in speed, stability, setup, and test writing

---

## ✅ What's Included

- Reusable **Page Objects** for both frameworks
- Pytest-based test suite with shared fixtures
- Configurable driver selection (Selenium or Playwright)
- Structured folder layout for scalability

---

## ⚙️ Setup Instructions

Follow these steps to set up and run the project locally:

---

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/your-username/python-automation-framework.git
cd python-automation-framework
> Replace `your-username` with your actual GitHub username.
```
---

### 🐍 2. Create a Virtual Environment

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🌐 4. Install Playwright Browsers

```bash
playwright install
```

This will download the required browser binaries (Chromium, Firefox, WebKit).

---

### ▶️ 5. Run Tests

You can run tests with either **Playwright** or **Selenium** by passing a custom `--browser` argument.

**Playwright Example:**

```bash
pytest --engine=playwright
```

**Selenium Example:**

```bash
pytest --engine=selenium
```
---

### 🧪 Example Test Command

```bash
pytest tests/test_login.py --engine=playwright
```

---

### 📌 Notes

- Python 3.9 or higher is recommended  
- This is a learning project – not production-ready  
- If you find issues, feel free to fork and experiment!

