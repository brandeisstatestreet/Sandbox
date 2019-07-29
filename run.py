from main import server
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from app1 import app as app1


application = DispatcherMiddleware(server, {
    '/app1': app1.server,
})

if __name__ == '__main__':
    run_simple('localhost', 8050, application, use_debugger=True)
    app1.enable_dev_tools(debug=True)

