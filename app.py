from flask import Flask, request, render_template
from flask_restful import Api
from flask_migrate import Migrate
import config
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
    'app_name':'EPAM'
    }
)

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix = SWAGGER_URL)
#import models, routes




if __name__ == '__main__':
    from rest.rest_posts import Smoke, PostsList_Api
    api.add_resource(Smoke, '/smoke', strict_slashes=False)
    api.add_resource(PostsList_Api, '/posts','/posts/<uuid>', strict_slashes=False)


    @app.route("/")
    @app.route("/home")
    def home():
        return render_template("index.html")


    app.run(debug=True)