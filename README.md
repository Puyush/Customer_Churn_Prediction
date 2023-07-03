# Customer Churn Prediction

Churn prediction is predicting which customers are at high risk of leaving your company or canceling a subscription to a service, based on their behavior with your product. When predicting churn, we're not just identifying at-risk customers but also identifying pain points leading up to churn and helping to increase overall customer retention and satisfaction.

In this repository, I have performed the end to end Exploratory Data Analysis, and idenfitied the characteristics of the customers that are more likely to churn, and I have created a model to predict whether a customer will churn or not, and lately, have deployed the model. For each customer at any given time, it tells us how high the risk is of losing them in the future. Technically, it’s a binary classifier that divides clients into two groups (classes) — those who leave and those who don’t.

I have uploaded the dataset as Telco-Customer-Churn.csv
The Telco customer churn data is a good source of data to predict customer churn, which contains information about a fictional telco company that provided home phone and Internet services to customers. It indicates which customers have left, stayed, or signed up for their service.

Dataset has following features: 

--> Customer Personal Information：

1. customerID: Customer Id of customer

2. gender: Whether the customer is a male or a female

3. SeniorCitizen: Whether the customer is a senior citizen or not (1, 0)

4. Partner: Whether the customer has a partner or not (Yes, No)

5. Dependents: Indicates if the customer lives with any dependents (Yes, No). Dependents could be children, parents, grandparents, etc.


--> Business Information:

1. tenure: Indicates the total amount of months that the customer has been with the company by the end of the quarter specified above.

2. PhoneService: Whether the customer has a phone service or not (Yes, No)

3. MultipleLines: Whether the customer has multiple lines or not (Yes, No, No phone service)

4. InternetService: Customer’s internet service provider (DSL, Fiber optic, No)

5. OnlineSecurity: Whether the customer has online security or not (Yes, No, No internet service)

6. OnlineBackup: Whether the customer has online backup or not (Yes, No, No internet service)

7. DeviceProtection: Whether the customer has device protection or not (Yes, No, No internet service)

8. TechSupport: Whether the customer has tech support or not (Yes, No, No internet service)

9. StreamingTV: Whether the customer has streaming TV or not (Yes, No, No internet service)

10. StreamingMovies: Whether the customer has streaming movies or not (Yes, No, No internet service)


--> Customer Account Information:

1. Contract: The contract term of the customer (Month-to-month, One year, Two year)

2. PaperlessBilling:Whether the customer has paperless billing or not (Yes, No)

3. PaymentMethod: The customer’s payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic))

4. MonthlyCharges: The amount charged to the customer monthly

5. TotalCharges: The total amount charged to the customer



>>> About Model:

As the dataset is bit imbalanced, I have used SMOTEENN from the imbalanced-learn library to resample the dataset. Then, I made a Multi-Layer Stacking, a ensemble technique to predict better predictions. Along with this, for each model used in stacking layers, I have tuned Hyper-Parameters also to get the best estimator for our model. And all this steps are going in a ML Pipeline which is unifying all these steps in a single unified framework.

⭐️ If you find this project useful or interesting, please consider giving it a star! ⭐️

# Thank You.
