# Online Food Order Prediction

This project involves predicting online food orders using machine learning techniques. The dataset includes various customer demographics, feedback, and order-related features to train a model that predicts whether an order will occur based on given input variables.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Dataset](#dataset)
5. [Modeling Process](#modeling-process)
6. [Results](#results)
7. [How to Use](#how-to-use)
8. [Future Enhancements](#future-enhancements)
9. [License](#license)

---

## Project Overview

This project aims to develop a machine learning model that accurately predicts online food orders based on various customer and order-related features. The model leverages customer data like age, gender, occupation, monthly income, and feedback to understand patterns and make predictions.

---

## Features

- **Data Preprocessing:** Handling missing values and encoding categorical variables.
- **Model Training:** Utilized a **RandomForestClassifier** to predict the target variable.
- **Model Evaluation:** Used performance metrics like accuracy, precision, and recall.
- **Model Deployment:** Saved the trained model using the `Joblib` library for future predictions.

---

## Technologies Used

- **Programming Language:** Python
- **Libraries:** pandas, scikit-learn, numpy, joblib
- **Tools:** Jupyter Notebook, GitHub

---

## Dataset

The dataset, `onlinefoods1.csv`, contains the following key features:

1. **Age**: Customer's age.
2. **Gender**: Customer's gender.
3. **Marital Status**: Whether the customer is married or not.
4. **Occupation**: Type of occupation.
5. **Monthly Income**: Customer's income bracket.
6. **Family Size**: Number of members in the customer's family.
7. **Feedback**: Customer's feedback on past orders.
8. **Output (Target Variable)**: Indicates whether an order occurred.

---

## Modeling Process

1. **Data Loading:** Imported and explored the dataset.
2. **Preprocessing:**
   - Addressed missing values.
   - Encoded categorical variables.
3. **Model Selection:**
   - Trained a **RandomForestClassifier**.
   - Performed hyperparameter tuning for optimal performance.
4. **Model Evaluation:**
   - Assessed the model using metrics like accuracy and F1 score.
5. **Model Saving:**
   - Saved the trained model using the `Joblib` library for deployment.

---

## Results

The model demonstrated strong predictive capabilities, with the following results:
- **Accuracy:** 94%

---

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yashwanthyg/Online-food-order-prediction.git
   ```
2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook to explore the dataset and train the model.

---

## Future Enhancements

- Add more features to improve model accuracy.
- Experiment with other machine learning models like **Gradient Boosting** or **XGBoost**.
- Integrate a web application to accept user inputs and predict online food orders in real-time.
- Deploy the model using platforms like Flask or FastAPI.

---

## License

This project is open-source and available for use under the MIT License.
