# 💳 Credit Card Approval Prediction using Machine Learning

## 📌 Project Overview

This project predicts whether a customer is likely to be approved for a credit card based on their personal, financial, and credit history information. The objective is to help financial institutions automate the credit approval process using Machine Learning techniques.

The project includes data preprocessing, exploratory data analysis (EDA), feature engineering, model training, evaluation, and hyperparameter tuning.

---

## 🎯 Objective

The main objectives of this project are:

- Predict whether a customer is a good or bad credit risk.
- Compare the performance of different Machine Learning algorithms.
- Improve prediction performance using feature engineering and hyperparameter tuning.
- Build an accurate and efficient credit approval prediction model.

---

## 📂 Dataset

This project uses two datasets.

### 1. application_record.csv

Contains customer demographic and financial information.

Features include:

- ID
- Gender
- Car Ownership
- Property Ownership
- Number of Children
- Annual Income
- Income Type
- Education
- Family Status
- Housing Type
- Age
- Employment Duration
- Occupation
- Family Members

### 2. credit_record.csv

Contains customers' monthly credit repayment history.

Features:

- ID
- MONTHS_BALANCE
- STATUS

---

## 🛠 Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib

---

## 📊 Project Workflow

### Step 1: Data Collection

- Load application dataset
- Load credit history dataset

### Step 2: Data Preprocessing

- Handle missing values
- Merge datasets
- Create target variable
- Remove unnecessary columns
- Convert days into age and employment years
- Encode categorical features

### Step 3: Exploratory Data Analysis (EDA)

- Missing value analysis
- Target distribution
- Income distribution
- Age distribution
- Correlation heatmap
- Boxplots
- Count plots

### Step 4: Feature Engineering

- AGE
- YEARS_EMPLOYED

### Step 5: Data Splitting

- Train-Test Split
- Feature Scaling (for applicable models)

### Step 6: Model Building

The following Machine Learning models were implemented:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)

### Step 7: Hyperparameter Tuning

- RandomizedSearchCV
- Optimized Random Forest

### Step 8: Model Evaluation

Evaluation metrics used:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- ROC-AUC Score

### Step 9: Model Saving

The best-performing model is saved using Joblib.

---

## 📈 Results

| Model | Accuracy |
|--------|----------|
| Logistic Regression | 98.31% |
| Decision Tree | 98.27% |
| Random Forest | 98.12% |
| KNN | 98.15% |
| SVM | 98.31% |

Although Logistic Regression and SVM achieved the highest accuracy, Random Forest showed better capability in identifying bad credit customers by achieving higher Precision, Recall, and F1-score.

---

## 📁 Project Structure

```
Credit-Card-Approval-Prediction/
│
├── application_record.csv
├── credit_record.csv
├── ML.ipynb
├── credit_card_final_dataset.csv
├── credit_card_approval_model.pkl
├── scaler.pkl
├── README.md
└── requirements.txt
```

---

## ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Credit-Card-Approval-Prediction.git
```

Move to the project folder:

```bash
cd Credit-Card-Approval-Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Project

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```
ML.ipynb
```

Run all cells sequentially.

---

## 📦 Required Libraries

```text
numpy
pandas
matplotlib
seaborn
scikit-learn
joblib
```

Install all packages:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn joblib
```

---

## 📌 Future Enhancements

- Handle class imbalance using SMOTE.
- Deploy the model using Streamlit or Flask.
- Build a web-based user interface.
- Integrate with a real-time credit approval system.

---

## 🎓 Learning Outcomes

Through this project, the following Machine Learning concepts were applied:

- Data Cleaning
- Data Preprocessing
- Exploratory Data Analysis
- Feature Engineering
- Label Encoding
- Train-Test Split
- Feature Scaling
- Model Building
- Hyperparameter Tuning
- Model Evaluation
- Model Serialization

---

## 👨‍💻 Author

**Pradeep**

Machine Learning Project

Credit Card Approval Prediction

---

## ⭐ If you found this project useful, please consider giving it a star on GitHub!