from flask import Flask

def create_app():
    app = Flask(__name__) # __name__ represents the filename
    app.config['SECRET_KEY'] = 'dev'

    from website.views import views

    app.register_blueprint(views, url_prefix='/')
    
    return app
