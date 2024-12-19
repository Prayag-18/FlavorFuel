from flask import Flask, render_template, request, redirect, url_for
from flavorfuel import *
from flavorgames import *

app = Flask(__name__)

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'pass123':
            return redirect(url_for('explore'))
        else:
            return redirect(url_for('login'))
    return render_template('login_signup.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/explore', methods=['GET', 'POST'])
def explore():
    if request.method == 'POST':
        selected_category = request.form['category']
        if selected_category == 'Culinary Explorers':
            return redirect(url_for('culinary_explorers'))
        elif selected_category == 'Health-Conscious Individuals':
            return redirect(url_for('health_conscious'))
        elif selected_category == 'Fitness Enthusiasts':
            return redirect(url_for('fitness_enthusiasts'))
        elif selected_category == 'Dietitians and Nutritionists':
            return redirect(url_for('dietitians_nutritionists'))
    return render_template('explore.html')

@app.route('/culinary-explorers')
def culinary_explorers():
    return render_template("culinary_explorers.html")

@app.route('/health-conscious')
def health_conscious():
    return render_template("health_conscious.html")

@app.route('/fitness-enthusiasts')
def fitness_enthusiasts():
    return render_template("fitness_enthusiasts.html")

@app.route('/dietitians-nutritionists')
def dietitians_nutritionists():
    return render_template("dietitians_nutritionists.html")

# print(app.jinja_loader.searchpath)


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug = True)