from flask import Blueprint, render_template

# Blueprint = file that contains routes
views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template("index.html")

@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/products')
def products():
    return render_template("products.html")

@views.route("/downloads")
def downloads():
    return render_template("downloads.html")

@views.route("/partners")
def partners():
    return render_template("partners.html")