from flask import Flask, redirect, url_for, send_file, \
    render_template, make_response
import json

home = open("paragraph/index.html", "r")
style = open("paragraph/styles/style.css", "r")
about_page = open("paragraph/about.html", "r")
app = Flask(__name__,)
not_found = open("paragraph/not_found.html", "r")
webpages_so_far = "home, about_page"
stored = open("paragraph/iphone.json", "r")
stored_python = json.loads(stored)


# top_seven_books = [
#     {'name': 'Why do we sleep: unlocking the power of sleep and dreams', 'rating': '4,9 stars'},
#     {'name': 'Make it stick: the science of successful learning', 'rating': '4,8 stars'},
#     {'name': 'Crice', 'rating': '4,89 stars'},
#     {'name': 'Girls against god', 'rating': '4,5 stars'},
#     {'name': 'These violent delights', 'rating': '4,45 stars'},
#     {'name': 'To paradise', 'rating': '4,13 stars'},
#     {'name': 'The greek myths: complete edition', 'rating': '4,12 stars'},
# ]

#I wanted to use make a little data storage variable and call out info to be displayed on the page depending on what URL you typed in, but that doesn't make much sense 
#because you wouldn't do that in real life so then i tried another approach and got confused 
#also my CSS isn't working if i put it through the app.py suddenly. is it because of render_template?

app.config.from_object('config')

@app.route('/')
def index():
    return home
    

@app.route('/about')
def about():
    return about_page

@app.route('/data')
def data():
    return '<h1>' + json[data]['title'] + '</h1>' + '<p>' + json[data]['price'] + '</p>'

@app.route('/<slug>')
def check(slug):
    if slug in webpages_so_far:
        return slug
    else:
        return not_found
    



app.run()
