from typing import Dict
from flask import Flask , render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1,10)
    current_year = datetime.datetime.now().year
    return render_template("index.html",num=random_number, year=current_year)

@app.route('/guess/<user_name>')
def guess(user_name):
    
    gender_url = f"https://api.genderize.io?name={user_name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    
    Age_url = f"https://api.agify.io?name={user_name}"
    age_response = requests.get(Age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html",name = user_name, gender=gender,age=age)
if __name__ == 'main':
    app.run(debug=True)