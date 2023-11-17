# 55282025_Churning_Customers

<!--toc:start-->

- [Problem](#problem)
- [Steps Used](#steps-used)
- [Chosen Features](#chosen-features)
- [Model Architecture](#model-architecture)
- [Demo Video](#demo-video)
<!--toc:end-->

## Problem

Customer churn is a significant problem and one of the most essential concerns for large companies. Due to the direct effect on the companies' revenues, especially in the telecom field, companies seek to develop means to predict potential customer churn. Therefore, finding factors that increase customer churn is vital to take necessary actions to reduce this churn. The main contribution of your work is to develop a churn prediction model that assists telecom operators in predicting customers who are most likely subject to churn. Perform the following operations as you create the much-needed deep-learning application.

**Solution:** A churn prediction model that helps determine if a particular customer will churn or not.

### Dataset Description

| Columns          | Meaning                                                                                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------------------ |
| customerID       | The ID of the customer                                                                                             |
| gender           | Whether male or female                                                                                             |
| SeniorCitizen    | Whether the customer is a senior citizen or not (1, 0)                                                             |
| Partner          | Whether the customer has a partner or not (Yes, No)                                                                |
| Dependents       | Whether the customer has dependents or not (Yes, No)                                                               |
| tenure           | Number of months the customer has stayed with the company                                                          |
| PhoneService     | Whether the customer has a phone service or not (Yes, No)                                                          |
| MultipleLines    | Whether the customer has multiple lines or not (Yes, No, No phone service)                                         |
| InternetService  | Customer’s internet service provider (DSL, Fiber optic, No)                                                        |
| OnlineSecurity   | Whether the customer has online security or not (Yes, No, No internet service)                                     |
| OnlineBackup     | Whether the customer has online backup or not (Yes, No, No internet service)                                       |
| DeviceProtection | Whether the customer has device protection or not (Yes, No, No internet service)                                   |
| TechSupport      | Whether the customer has tech support or not (Yes, No, No internet service)                                        |
| StreamingTV      | Whether the customer has streaming TV or not (Yes, No, No internet service)                                        |
| StreamingMovies  | Whether the customer has streaming movies or not (Yes, No, No internet service)                                    |
| Contract         | The contract term of the customer (Month-to-month, One year, Two year)                                             |
| PaperlessBilling | Whether the customer has paperless billing or not (Yes, No)                                                        |
| PaymentMethod    | The customer's payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic)) |
| MonthlyCharges   | The amount charged to the customer monthly                                                                         |
| TotalCharges     | The total amount charged to the customer                                                                           |
| Churn            | Whether the customer churned or not (Yes or No)                                                                    |

## Steps Used

- [x] Exploratory Data Analysis
- [x] Data Visualization and Pre-processing
- [x] Feature Extraction
- [x] Training a Multi-Layer Perceptron with Keras Functional API
- [x] Model Evaluation (Hyperparameter Tuning)
- [x] Deployment

## Chosen Features

1. tenure
2. MonthlyCharges
3. TotalCharges
4. gender
5. MultipleLines
6. InternetService
7. OnlineSecurity
8. OnlineBackup
9. DeviceProtection
10. TechSupport
11. Contract
12. PaperlessBilling
13. PaymentMethod

## Model Architecture

**N.B.** Grid search and cross-validation were used to find the best hyperparameters, while the RMSprop optimizer was used 

## Demo Video

- YouTube link: [https://youtu.be/JNzIrH0MBQo](https://youtu.be/JNzIrH0MBQo)


