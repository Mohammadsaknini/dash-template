from dash import Dash, html, page_container, dcc, callback, Input, Output, State
from dash_bootstrap_components.icons import FONT_AWESOME
from dash_bootstrap_components.themes import FLATLY
from dash.exceptions import PreventUpdate
from src.components import Navbar, Footer
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from src.configs import APP_NAME, setup
import logging
setup()

logger = logging.getLogger("MyNewApp") # make sure to change the name in logging.conf

class DashApp(Dash):
    """
    Custom Dash app index to handle scss files
    """
    def interpolate_index(self, **kwargs):
        temp = ""
        for i in kwargs["css"].split("\n"):
            if "scss" in i:
                continue
            temp += i + "\n"   
        kwargs["css"] = temp
        return '''
        <!DOCTYPE html>
        <html>
            <head>
                {metas}
                <title>{title}</title>
                {favicon}
                {css}
            </head>
            <body>
                <!--[if IE]><script>
                alert("Dash v2.7+ does not support Internet Explorer. Please use a newer browser.");
                </script><![endif]-->
                {app_entry}
                <footer>
                    {config}
                    {scripts}
                    {renderer}
                </footer>
            </body>
        </html>
        '''.format(
            metas=kwargs['metas'],
            title=kwargs['title'],
            favicon=kwargs['favicon'],
            css=kwargs['css'],
            app_entry=kwargs['app_entry'],
            config=kwargs['config'],
            scripts=kwargs['scripts'],
            renderer=kwargs['renderer'])

app = DashApp(__name__, use_pages=True,
           assets_folder='src/assets',
           pages_folder='src/pages',
           title=APP_NAME,
           update_title=None,
           external_stylesheets=[FLATLY, FONT_AWESOME],
           suppress_callback_exceptions=True,
           meta_tags=[
               {"name": "viewport", "content": "width=device-width, initial-scale=1"}
           ])

app.layout = dmc.MantineProvider(
    html.Div([
        dmc.NotificationProvider(id="notifcation-provider", autoClose=5000),
        dcc.Location(id="url"),
        html.Div(id="notifcation-container"),
        Navbar(),
        dbc.Spinner(page_container, fullscreen=True, color="info", delay_show=100),
        Footer()
    ], id="app_container"))

@callback(
    Output("app_container", "children"),
    Input("url", "pathname"),
    State("app_container", "children"),
)
def display_page(pathname, children):
    if pathname != "/":
        return [*children[:4], dbc.Spinner(page_container, fullscreen=True, color="info", delay_show=100)]
    else:
        raise PreventUpdate
    
    
server = app.server
if __name__ == '__main__':
    logger.info(f"Starting {APP_NAME}")
    app.run("0.0.0.0", debug=True, port=80)  # pragma: no cover
