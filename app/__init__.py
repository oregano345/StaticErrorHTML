from flask import Flask, render_template, Blueprint
from flask_socketio import SocketIO
import gevent

socketio = SocketIO()
app = Flask(__name__)
app.register_blueprint(Blueprint('HTMLDisp', __name__, url_prefix='/', template_folder='templates'))
socketio.init_app(app)

@app.route('/')
def dispHTMLError():
    return render_template("patience.html"), 200
