# 🧠 NeuroSleep Insight

**NeuroSleep Insight** is a Streamlit-based sleep quality and performance prediction system developed as part of an undergraduate Computer Science final-year research project.

The system uses machine learning to predict sleep quality from lifestyle and health-related factors, then provides performance and neuroscience-inspired interpretation based on sleep, fatigue, attention, productivity, and brain-network function.

---

## 📌 Project Title

**Sleep Pattern Analysis and Performance Prediction**

---

## 🚀 Application Features

- Predicts **Quality of Sleep** from user input
- Provides **Performance Readiness** interpretation
- Shows **Fatigue Risk**, **Focus Level**, and **Productivity Insight**
- Includes a **Neuroscience Insight** section
- Connects prediction results to concepts such as:
  - functional connectivity
  - brain-state stability
  - memory consolidation
  - attention networks
  - sleep-related performance

---

## 🧠 Machine Learning Model

The machine learning model predicts **Quality of Sleep** using selected lifestyle and health-related features.

### Input Features

- Sleep Duration
- Stress Level
- Physical Activity Level
- Daily Steps
- Heart Rate
- Age
- Gender
- BMI Category
- Sleep Disorder
- Occupation

### Models Compared

| Model | MAE | MSE | RMSE | R² Score |
|---|---:|---:|---:|---:|
| Decision Tree Regressor | 0.039 | 0.021 | 0.145 | 0.986 |
| Random Forest Regressor | 0.045 | 0.026 | 0.160 | 0.983 |
| Linear Regression | 0.121 | 0.051 | 0.227 | 0.966 |

The **Decision Tree Regressor** was selected as the best-performing model and saved as:

```text
sleep_quality_model.pkl
