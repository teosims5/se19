from flask import Flask, redirect, url_for, send_file, \
    render_template, request, session, flash, g, make_response


home = open("paragraph/index.html", "r")
style = open("paragraph/styles/style.css", "r")
about_page = open("paragraph/about.html", "r")
app = Flask(__name__,)
not_found = open("paragraph/not_found.html", "r")
webpages_so_far = "home, about_page"

top_seven_books = [
    {'name': 'Why do we sleep: unlocking the power of sleep and dreams', 'rating': '4,9 stars'},
    {'name': 'Make it stick: the science of successful learning', 'rating': '4,8 stars'},
    {'name': 'Crice', 'rating': '4,89 stars'},
    {'name': 'Girls against god', 'rating': '4,5 stars'},
    {'name': 'These violent delights', 'rating': '4,45 stars'},
    {'name': 'To paradise', 'rating': '4,13 stars'},
    {'name': 'The greek myths: complete edition', 'rating': '4,12 stars'},
]

app.config.from_object('config')

@app.route('/')
def index():
    return home
    

@app.route('/about')
def about():
    return about_page

@app.route('/<slug>')
def check(slug):
    if slug in webpages_so_far:
        return slug
    else:
        return not_found
    

# @app.route('/<slug>')
# def book2(slug):
#     if slug in top_seven_books:
#         return '<h1>' + top_seven_books[slug]['name'] + '</h1>' + '<p>' + top_seven_books[slug]['price'] + '</p>'
#     else:
#         return 'Sorry we could not find that cookie.' 

app.run()
