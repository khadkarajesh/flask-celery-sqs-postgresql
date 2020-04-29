from dotenv import load_dotenv
from flask import Flask

from extensions import db
from flask_celery import make_celery

load_dotenv('.env')

app = Flask(__name__)
app.config.from_object('config')
celery = make_celery(app)

with app.test_request_context():
    db.init_app(app)
    db.create_all()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
