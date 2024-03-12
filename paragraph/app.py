from flask import Flask, redirect, url_for, send_file



app = Flask(__name__)

app.config.from_object('config')

# cookies_data = {
#     'chocolate-chip' : {'name': 'Chocolate Chip', 'price': '$1.50'},
#     'oatmeal-raisin' : {'name': 'Oatmeal Raisin', 'price': '$1.00'},
#     'sugar' : {'name': 'Sugar', 'price': '$0.75'},
#     'peanut-butter' : {'name': 'Peanut Butter', 'price': '$0.50'},
#     'oatmeal' : {'name': 'Oatmeal', 'price': '$0.25'},
#     'salted-caramel' : {'name': 'Salted Caramel', 'price': '$1.00'},
# }


cookies_data = [
    {'name': 'Chocolate Chip', 'price': '$1.50'},
    {'name': 'Oatmeal Raisin', 'price': '$1.00'},
    {'name': 'Sugar', 'price': '$0.75'},
    {'name': 'Peanut Butter', 'price': '$0.50'},
    {'name': 'Oatmeal', 'price': '$0.25'},
    {'name': 'Salted Caramel', 'price': '$1.00'},
]

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/about')
def about():
    return 'I like cookies'

@app.route('/about-me')
def about_me():
    return redirect(url_for('about'))

@app.route('/cookies/<slug>')
def cookie(slug):
    if slug in cookies_data:
        return '<h1>' + cookies_data[slug]['name'] + '</h1>' + '<p>' + cookies_data[slug]['price'] + '</p>'
    else:
        return 'Sorry we could not find that cookie.' 

@app.route('/cookies/<int:id>')
def cookie(id):
    return '<h1>' + cookies_data[id]['name'] + '</h1>' + '<p>' + cookies_data[id]['price'] + '</p>'

app.run()
