# 🛡️ Fraud Detection Platform (ML + Risk Engine + Dashboard)

An end-to-end **enterprise-style fraud detection system** built from scratch.  
This project combines:

- Machine Learning (XGBoost classifier)
- Unsupervised Anomaly Detection (IsolationForest)
- Risk-tier decision engine
- FastAPI scoring service
- Logging + audit trail storage
- Streamlit case-review dashboard
- Human-in-the-loop **fraud labeling workflow**

Designed for beginners learning production-grade ML systems, but structured like a real fintech backend.

---

## 🚀 Features

### 🔹 Fraud Scoring Engine
- Extracts behavioral features (amount, hour-of-day, recency gaps, etc.)
- Uses:
  - **XGBoost** for supervised fraud probability
  - **IsolationForest** for anomaly score
- Produces a combined **final risk score**

### 🔹 Risk Policy Layer
Risk tiers instead of binary outputs:

| Risk Level  | Action   |
|-----------|---------|
| low       | allow   |
| elevated  | review  |
| medium    | review  |
| high      | block   |
| critical  | block   |

### 🔹 Explainability
Each decision includes human-readable reasons like:
"High amount compared to user history"
"Unusual transaction hour"
"Short interval since previous transaction"


### 🔹 API Service (FastAPI)
Endpoints:
- `GET /` health check
- `POST /score` → returns scores, risk, action, explanation

### 🔹 Event Logging
Every scored transaction is stored in: logs/events.csv


Includes:
- features
- scores
- decision
- explanation
- analyst label (fraud / legit / unknown)

### 🔹 Case Viewer Dashboard (Streamlit)
- View scored transactions
- Filter by risk + action
- Inspect case details
- Assign **labels** for retraining dataset

---

## 🧩 Project Structure

Fraud_platform/
│
├── data/ # training + sample data
├── models/ # trained model files
├── logs/
│ └── events.csv # scored transaction history
│
├── src/
│ ├── features.py # feature engineering
│ ├── train.py # model training
│ ├── predict.py # scoring pipeline
│ ├── risk.py # risk tier classifier
│ ├── logger.py # event logging
│ ├── score_api.py # FastAPI service
│ └── dashboard.py # Streamlit case viewer
│
└── README.md


---

## ⚙️ Installation

```bash
git clone <repo>
cd Fraud_platform
pip install -r requirements.txt

🏋️ Train Model
python src/train.py


Models are saved into:

models/

🧠 Run Fraud Scoring API
uvicorn src.score_api:app --reload


Open:

http://127.0.0.1:8000/docs


Send a test transaction via Swagger UI.

📊 Run Case Viewer Dashboard
streamlit run src/dashboard.py


Open:

http://localhost:8501


You can:

inspect transactions

see scores & risk level

assign labels (fraud / legit / unknown)

Labels are written back into logs/events.csv.

🔁 Retraining Workflow (Human-in-Loop)

Model scores transactions

Analysts label cases in dashboard

Labeled rows become retraining dataset

Train updated model using real outcomes

This mirrors real-world fraud ops pipelines.

🛠️ Tech Stack

Python

Pandas

XGBoost

Scikit-learn

FastAPI

Streamlit

Joblib

🎯 Future Enhancements (Roadmap)

drift monitoring

model versioning

streaming transaction simulator

case comments & review audit log

auto-retraining pipeline

ensemble calibration metrics

database instead of CSV logs

📌 Educational Purpose

This project is for learning ML engineering, system design, and fraud analytics concepts — not production banking use.

🤝 Contributions

Pull requests welcome. Don’t break things carelessly. The system already does that on its own sometimes.

🧑‍💻 Author

Built as a guided learning project to understand:

ML pipelines

backend integration

risk engineering

explainable AI

dashboard tooling


