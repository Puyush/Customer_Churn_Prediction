import joblib
import numpy as np
import pandas as pd
from flask import Flask, request, render_template

model = joblib.load('Customer_Churn_Model.pkl')


# Flask turn the current file into web application
app = Flask(__name__)

# Here, Use the following function for this route. app.route let's us define what route should be associated with the following function.


@app.route("/")
# The loadPage method calls our index.html. render_template find this index.html file in templates, grab it's contents and return it
def loadPage():
    return render_template('index.html')

# request gives access to the HTTP request
# Unlike GET, POST doesn't leak user information in URL. It doesn't put paramters in URL instead it puts it inside the virtual envelope.
# i.e. it's still being sent from browser to server but it's not getting remembered by the browser in URL.


@app.route("/predict", methods=['POST'])
def predict_churn():
    senior_citizen = int(request.form.get('senior_citizen'))
    partner = request.form.get('partner')
    dependents = request.form.get('dependents')
    internet_service = request.form.get('internet_service')
    online_security = request.form.get('online_security')
    online_backup = request.form.get('online_backup')
    device_protection = request.form.get('device_protection')
    tech_support = request.form.get('tech_support')
    streaming_tv = request.form.get('streaming_tv')
    streaming_movie = request.form.get('streaming_movie')
    contract = request.form.get('contract')
    paperless_billing = request.form.get("paperless_billing")
    payment_method = request.form.get("payment_method")
    monthly_charges = float(request.form.get('monthly_charges'))
    total_charges = float(request.form.get('total_charges'))
    tenure = request.form.get("tenure")

    result = model.predict(
        np.array([[senior_citizen, partner, dependents, internet_service, online_security, online_backup, device_protection, tech_support, streaming_tv, streaming_movie, contract, paperless_billing, payment_method, monthly_charges, total_charges, tenure]], dtype=object))

    if result[[0]] == 1:
        result = "This customer is likely to be churned!!"
    else:
        result = "This customer is likely to continue with the services!!"

    # result is a parameter here which I'm passing into template
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
