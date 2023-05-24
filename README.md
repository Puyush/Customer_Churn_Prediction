# Customer Churn prediction

Churn prediction is predicting which customers are at high risk of leaving your company or canceling a subscription to a service, based on their behavior with your product. When predicting churn, you're not just identifying at-risk customers, you’re also identifying pain points leading up to churn and helping to increase overall customer retention and satisfaction.

In this repository, I have performed the end to end Exploratory Data Analysis, and idenfitied the characteristics of the customers that are more likely to churn, and I have created a model to predict whether a customer will churn or not, and lately, have deployed the model. For each customer at any given time, it tells us how high the risk is of losing them in the future. Technically, it’s a binary classifier that divides clients into two groups (classes) — those who leave and those who don’t.

I have uploaded the dataset as Telco-Customer-Churn.csv
The Telco customer churn data is a good source of data to predict customer churn, which contains information about a fictional telco company that provided home phone and Internet services to customers. It indicates which customers have left, stayed, or signed up for their service.

Dataset has following features: 

--> Customer Personal Information：

customerID: Customer Id of customer

gender: Whether the customer is a male or a female

SeniorCitizen: Whether the customer is a senior citizen or not (1, 0)

Partner: Whether the customer has a partner or not (Yes, No)

Dependents: Indicates if the customer lives with any dependents (Yes, No). Dependents could be children, parents, grandparents, etc.


--> Business Information:

tenure: Indicates the total amount of months that the customer has been with the company by the end of the quarter specified above.

PhoneService: Whether the customer has a phone service or not (Yes, No)

MultipleLines: Whether the customer has multiple lines or not (Yes, No, No phone service)

InternetService: Customer’s internet service provider (DSL, Fiber optic, No)

OnlineSecurity: Whether the customer has online security or not (Yes, No, No internet service)

OnlineBackup: Whether the customer has online backup or not (Yes, No, No internet service)

DeviceProtection: Whether the customer has device protection or not (Yes, No, No internet service)

TechSupport: Whether the customer has tech support or not (Yes, No, No internet service)

StreamingTV: Whether the customer has streaming TV or not (Yes, No, No internet service)

StreamingMovies: Whether the customer has streaming movies or not (Yes, No, No internet service)


--> Customer Account Information:

Contract: The contract term of the customer (Month-to-month, One year, Two year)

PaperlessBilling:Whether the customer has paperless billing or not (Yes, No)

PaymentMethod: The customer’s payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic))

MonthlyCharges: The amount charged to the customer monthly

TotalCharges: The total amount charged to the customer


About Model:

As the dataset is bit imbalanced, I have used SMOTEENN from the imbalanced-learn library to resample the dataset. Then, We will be using a Multi-Layer Stacking, a ensemble technique to predict better predictions. Along with this, for each model used in stacking layers, we will be tuning Hyper-Parameters also to get the best estimator for our model. And all this thing is happening in a ML Pipeline which is unifying all this steps in a single unified framework.

Thank You.
