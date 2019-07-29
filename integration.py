#from main import app as app1
#from dashboard import app as app2
from werkzeug.wsgi import DispatcherMiddleware
import dash
import dash_html_components as html
from flask import Flask
from werkzeug.serving import run_simple

flask_app = Flask(__name__)

@flask_app.route('/')
def index():
    return 'Hello Flask app'



app1 = dash.Dash(
    __name__,
    requests_pathname_prefix='/app1/'
)



app2 = dash.Dash(
    __name__,
    requests_pathname_prefix='/app2/'
)

app2.layout = html.Div("Dash app 2")

app1.layout = html.Div("Dash app 1")

application = DispatcherMiddleware(flask_app, {
    '/app1': app1.server,
    '/app2': app2.server,
})


if __name__ == '__main__':
    run_simple('localhost', 8050, application)