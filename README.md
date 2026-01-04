# 🎓 Student Exam Score Predictor (LightGBM Regressor)

This project is a **machine learning–based web application** built with **Python**, **LightGBM**, and **Streamlit** that predicts a **student’s exam score** based on academic, lifestyle, and study-related factors.

The system uses a carefully engineered **regression pipeline** with **manual categorical encoding**, **hyperparameter optimization using Optuna**, and a production-ready **Streamlit interface** for real-time predictions.

---

## 🚀 Features

- Predicts student **exam scores (0–100)**
- Fast and accurate **LightGBM regression model**
- Manual categorical encoding for optimal performance
- Hyperparameter tuning using **Optuna**
- Interactive **Streamlit web application**
- Pre-trained model loaded via **Pickle**
- Feature importance visualization support

---

## 🏋️ Input Parameters

The model predicts **exam score** using the following inputs:

| **Feature**      | **Description**                                      |
| ---------------- | ---------------------------------------------------- |
| Age              | Student age (years)                                  |
| Gender           | Male / Female / Other                                |
| Course           | Diploma / BA / B.Sc / B.Com / BBA / BCA / B.Tech     |
| Study Hours      | Average daily study hours                            |
| Class Attendance | Attendance percentage                                |
| Internet Access  | Yes / No                                             |
| Sleep Hours      | Average daily sleep duration                         |
| Sleep Quality    | Poor / Average / Good                                |
| Study Method     | Self-study / Group study / Online / Mixed / Coaching |
| Facility Rating  | Low / Medium / High                                  |
| Exam Difficulty  | Easy / Moderate / Hard                               |

---

## 🏗️ Machine Learning Pipeline

- **Target Variable:** `exam_score`
- **Model:** `LightGBMRegressor`
- **Encoding Strategy:** Manual ordinal mapping (best leaderboard score)
- **Evaluation Metric:** RMSE (Root Mean Squared Error)
- **Hyperparameter Tuning:** Optuna
- **Train–Validation Split:** 80 / 20
- **Prediction Clipping:** Ensures scores remain between 0–100

---

## 🧰 Technologies Used

- **Python**
- **LightGBM** – Primary regression model
- **Scikit‑learn** – Metrics & utilities
- **Optuna** – Hyperparameter optimization
- **Pandas / NumPy** – Data preprocessing
- **Streamlit** – Web UI
- **Pickle** – Model serialization
- **Jupyter Notebook** – Model development & experimentation

---

## 📁 Files Included

```
├── main.py                     # Streamlit web application
├── model/
│   └── lgbm_model.pkl          # Trained LightGBM model
├── notebook/
│   └── ml_pipeline.ipynb       # Notebook file
├── dataset/
│   └── dataset.csv             # Training dataset
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
└── LICENSE                     # MIT License
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Kalana-S/Student-Exam-Score-Predictor.git
   cd Student-Exam-Score-Predictor

2. **Create virtual environment (optional)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

4. **Run the app**:
   ```bash
   streamlit run main.py

---

## 📂 Dataset

The training dataset contains student-related academic and lifestyle features along with the target variable `exam_score`.

⚠️ Dataset is assumed to be pre-cleaned and free of missing values.

---

## 📊 Model Performance

- **Baseline LightGBM RMSE:** ~8.76
- **Optuna-tuned LightGBM RMSE:** ~8.71
- Model performance was consistently better with manual encoding than with One-Hot Encoding.

---

## 🎥 App Demo (Screen Recording)

Full app workflow — UI → Input → Prediction<br>

https://github.com/user-attachments/assets/c1e2dd79-023a-429f-85c4-765e1c35e3b2

---

## 🤝 Contribution

Contributions are welcome.

- Fork the repository
- Create a feature branch
- Submit a pull request

---

## 📜 License

This project is licensed under the **MIT License** – see the LICENSE file for details.
