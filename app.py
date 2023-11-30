from flask import Flask, render_template, request, redirect, url_for
from food import predict  

app = Flask(__name__)
from joblib import load
model = load('trained_model.joblib')
@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        age = float(request.form['age'])
        gender = request.form['gender']
        marital_status = request.form['marital_status']
        occupation = request.form['occupation']
        monthly_income = float(request.form['monthly_income'])
        family_size = float(request.form['family_size'])
        feedback = float(request.form['feedback'])

        


        features = [[age, gender, marital_status, occupation, monthly_income, family_size, feedback]]


        prediction = model.predict(features)


        
        return render_template('result.html', prediction=prediction)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
