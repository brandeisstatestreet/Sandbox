import dash
import dash_html_components as html
import dash_core_components as core

app = dash.Dash(
    __name__,
    requests_pathname_prefix='/app1/'
)

app.layout = html.Div("Dash app 1")

