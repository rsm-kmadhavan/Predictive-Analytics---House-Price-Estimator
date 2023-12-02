from flask import request, render_template

import pandas as pd
import joblib as pkl
model = pkl.load('assets/rr_model.pkl')

def index():
    estimated_price = None
    form_data = {}

    if request.method == 'POST':
        # Assume you have a function to calculate the price based on form inputs
        form_data = request.form
        estimated_price = calculate_price(form_data)
        # Format the price
    return render_template('index.html', estimated_price=estimated_price, form_data=form_data)


def calculate_price(form_data):
    user_inputs = pd.DataFrame({
        'area': [form_data['area']],
        'bedrooms': [form_data['bedrooms']],
        'bathrooms': [form_data['bathrooms']],
        'stories': [form_data['stories']],
        'mainroad': [form_data['mainroad']],
        'guestroom': [form_data['guestroom']],
        'basement': [form_data['basement']],
        'hotwaterheating': [form_data['hotwaterheating']],
        'airconditioning': [form_data['airconditioning']],
        'parking': [form_data['parking']],
        'prefarea': [form_data['prefarea']],
        'furnishingstatus':[form_data['furnishingstatus']]
    })
    try:
        output = model.predict(user_inputs)[0]
        if output<0:
            output = 0
        # print(user_inputs)
        return "${:,.0f}".format(output)
    except:
        return 'There was an error processing your request'




def index_controller():    
    return "200 OK"