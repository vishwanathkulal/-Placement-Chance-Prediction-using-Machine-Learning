# -Placement-Chance-Prediction-using-Machine-Learning

# 🎓 Placement Chance Prediction using Machine Learning

A machine learning project that predicts the likelihood of a student getting placed based on their academic performance, skills, and test scores. This project demonstrates regression and classification techniques on a **self-created dataset**, with deployment using **Streamlit** for a user-friendly web interface.

---

## 📌 Problem Statement

Many students are unsure about their job placement chances based on their academic and extracurricular profiles. This project aims to:

- **Predict placement chances** as a continuous score (Regression).
- **Classify students** into "Likely to be placed" or "Not likely" categories (Classification).
- Help students **identify areas to improve** for increasing placement success.

---

## 🎯 Objectives

- 📊 Build a regression model to estimate **Placement Probability**.
- ✅ Use a classification model to predict **placement outcome**.
- 🎯 Improve prediction accuracy through feature engineering and model tuning.
- 📈 Deploy a **Streamlit web application** for real-time predictions.

---

## 🧠 Hypotheses

1. Higher **CGPA** and **Aptitude scores** lead to better placement chances.
2. Strong **communication** and **programming skills** improve placement outcomes.
3. Students involved in more **internships or projects** are more likely to be placed.

---

## 📁 Dataset Overview

We created a custom dataset with the following features:

| Feature               | Description                          |
|------------------------|--------------------------------------|
| `CGPA`               | Academic score (0–10 scale)          |
| `Internships`        | Number of internships completed      |
| `Projects`           | Number of major projects             |
| `AptitudeScore`      | Aptitude test score (0–100)          |
| `MockTestScore`      | Mock interview/test score (0–100)    |
| `ProgrammingSkill`   | Rating from 1 (Low) to 5 (Excellent) |
| `CommunicationSkill` | Rating from 1 (Low) to 5 (Excellent) |
| `PlacementChance`    | Target variable for regression (0–1) |
| `Placed`             | Binary outcome for classification    |

---

## 🛠️ Models Used

### 🔹 Regression:
- **Linear Regression** (baseline)
- **Random Forest Regressor** (final)
  
> **Best Regression Results (after tuning):**  
> - R² Score: `0.6701`  
> - MSE: `0.0032`  
> - RMSE: `0.0565`  
> - MAE: `0.0444`

---

## 🌐 Streamlit Web App

We created an interactive Streamlit app where users can:

✅ Enter profile details  
📈 Get predicted placement chance  
🧠 Receive suggestions/animations based on confidence  
🎨 Clean and user-friendly interface

---

## 🚀 How to Run

1. Clone the repository or download the code.
2. Make sure you have Python 3.10+ installed.
3. Install the required packages:

```bash
pip install -r requirements.txt

📌 Conclusion
This project bridges academic analytics and career prediction using real-world ML techniques. The regression model gives a score, while the classifier gives a binary outcome to help students and institutions understand placement readiness.

🙋‍♂️ Contributions
Project by Vishwanath Kulal
Undergraduate in Electronics & Communication Engineering
Mangalore
