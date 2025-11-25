# Import the flask class and create an instance of it
from flask import Flask, render_template

app = Flask(__name__)

# Define a route and view function
@app.route('/')
def hello():
    return render_template('index.html', name='Justin') 

@app.route('/about')
def about():
    fruits_list = ["apple","mango","banana"]
    return render_template('about.html', fruits=fruits_list, title='About', description='This is a simple Flask web app.')

@app.route('/profile')
def show_profile():
    user = {"name": "Alice", "age":30}
    return render_template ("profile.html", user=user)

# Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)