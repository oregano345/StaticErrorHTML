from flask import Flask, render_template, Blueprint
from flask_socketio import SocketIO
import gevent

if __name__ == '__main__':
    socketio = SocketIO()
    app = Flask(__name__)
    socketio.init_app(app)
    app.register_blueprint(Blueprint('HTMLDisp', __name__, url_prefix='/', template_folder='templates'))

    @app.route('/')
    def dispHTMLError():
        return render_template("patience.html"), 200

    socketio.run(app, host="0.0.0.0", port=5000)
