# ⚡ Electricity Usage — Linear Regression (Flask App)

A simple end‑to‑end machine learning project that predicts electricity usage using **Linear Regression**, wrapped in a minimal **Flask** web app.

> Edit any placeholders (🔧) to match your exact dataset columns and screenshots.

---

## 📑 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Train the Model](#train-the-model)
  - [Run the App](#run-the-app)
- [Dataset](#-dataset)
- [Modeling](#-modeling)
- [API (Optional)](#-api-optional)
- [Evaluation](#-evaluation)
- [Results & Screenshots](#-results--screenshots)
- [Troubleshooting](#-troubleshooting)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

---

## 📌 Overview
This project predicts **electricity usage** (target variable) from historical/real‑time features using a **Linear Regression** model. It includes:
- Data preprocessing & scaling
- Model training script producing `model.pkl` and `scaler.pkl`
- Flask app with a simple UI (`templates/index.html`) to submit inputs and view predictions

Use this as a template to learn or showcase an end‑to‑end ML workflow.

---

## ✨ Features
- Clean train/predict pipeline (`train_model.py`, `app.py`)
- Persisted artifacts with `pickle`
- Optional REST endpoint for programmatic predictions
- Reproducible environment via `requirements.txt`

---

## 🗂 Project Structure
```bash
Electricity_usage-LR-/
├─ app.py                  # Flask app: loads model & scaler, serves UI/API
├─ train_model.py          # Train Linear Regression, save artifacts
├─ data.csv                # 🔧 Your dataset (or place in /data and update paths)
├─ model.pkl               # Saved Linear Regression model (after training)
├─ scaler.pkl              # Saved scaler/transformer (after training)
├─ requirements.txt        # Python dependencies
└─ templates/
   └─ index.html           # Simple form to collect inputs & show predictions
```
> If your repo structure differs, update this section accordingly.

---

## 🧰 Tech Stack
- **Python**, **Flask**
- **pandas**, **numpy**, **scikit‑learn**
- **Jinja2** (Flask templates)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+ recommended
- `pip` and (optional) `virtualenv`

### Installation
```bash
# 1) Clone the repo
git clone https://github.com/Elakiya-bcs22/Electricity_usage-LR-.git
cd Electricity_usage-LR-

# 2) Create & activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 3) Install dependencies
pip install -r requirements.txt
```

### Train the Model
Make sure `data.csv` exists and columns in `train_model.py` match your dataset.
```bash
python train_model.py
```
This will generate `model.pkl` and `scaler.pkl` in the project root (or the path configured in the script).

### Run the App
```bash
# Option A: Run directly
python app.py

# Option B: Using Flask
set FLASK_APP=app.py        # Windows (CMD)
$env:FLASK_APP="app.py"    # Windows (PowerShell)
export FLASK_APP=app.py     # macOS/Linux
flask run
```
App will be available at: `http://127.0.0.1:5000/`

---

## 🧾 Dataset
- File: `data.csv` (🔧 replace with your path/name if different)
- Target: `electricity_usage` (🔧 rename if your project uses another target)
- Example features (🔧 update to match your columns):
  - `temperature`, `humidity`, `hour_of_day`, `day_of_week`, `is_holiday`, `appliance_load`

If your dataset needs cleaning, handle missing values & outliers inside `train_model.py`.

---

## 🧠 Modeling
- **Algorithm:** `LinearRegression` from scikit‑learn
- **Preprocessing:** standard scaling for numeric features (via `StandardScaler`)
- **Artifacts:**
  - `model.pkl` — trained regression model
  - `scaler.pkl` — fitted scaler for input transformation

> Keep the **same feature order** during prediction as used in training.

---

## 🔌 API (Optional)
If enabled in `app.py`, you can POST JSON to get predictions.

**Endpoint**: `POST /predict`

**Request (example)**
```json
{
  "features": {
    "temperature": 30,
    "humidity": 60,
    "hour_of_day": 14,
    "day_of_week": 2,
    "is_holiday": 0,
    "appliance_load": 1.2
  }
}
```

**Response (example)**
```json
{
  "prediction": 3.47
}
```
> Numbers are illustrative. Ensure your feature names/types match the training pipeline.

---

## 📊 Evaluation
During training, print/log common metrics:
- **MAE** (Mean Absolute Error)
- **MSE** (Mean Squared Error)
- **RMSE** (Root MSE)
- **R²** (Coefficient of Determination)

Example (console output):
```
MAE:  0.214
MSE:  0.091
RMSE: 0.302
R2:   0.86
```

---

## 🖼 Results & Screenshots
Add a UI preview and any charts here.

```html
<!-- 🔧 Replace with your actual screenshot(s) -->
<img src="./assets/ui_home.png" alt="App Home" width="600"/>
```

- Include a short paragraph summarizing insights, e.g., "Usage peaks at 7–9 PM; temperature positively correlates with consumption."

---

## 🛠 Troubleshooting
- **`ModuleNotFoundError`** → Run `pip install -r requirements.txt` inside your virtualenv.
- **Model not found** → Run `python train_model.py` to generate `model.pkl` and `scaler.pkl`.
- **Feature mismatch** → Ensure feature order and preprocessing in `app.py` mirrors `train_model.py`.
- **Port in use** → Change port in `app.py` (e.g., `app.run(port=5001)`).

---

## 🗺 Roadmap
- [ ] Add feature importance/coefficients table
- [ ] Add EDA notebook & plots
- [ ] Improve UI/UX and validation
- [ ] Add Dockerfile & CI
- [ ] Log predictions/feedback for continuous improvement

---

## 🤝 Contributing
Pull requests are welcome! Please open an issue to discuss changes.

---

## 📄 License
This project is open‑sourced under the MIT License. (🔧 Replace if you use a different license.)

---

### 🙌 Acknowledgements
- scikit‑learn team and docs
- Flask community
- Any datasets or references you used (🔧 list here)

