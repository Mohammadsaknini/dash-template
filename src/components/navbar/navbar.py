from dash import html
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify as di
from ...configs import TERTIARY_COLOR, TRANSLATE, APP_NAME
from . import callbacks # This is needed to register the callbacks

class Navbar(html.Div):
    def __init__(self, **kwargs):
        lang = kwargs.get("lang", "en")
        kwargs.pop("lang", None)
        super().__init__(**kwargs)
        self.children = [
            dbc.NavbarSimple(
                children=[
                    html.Div([
                        dbc.NavItem(dbc.NavLink(TRANSLATE[lang]["Home"], href="/")),
                        dbc.NavItem(dbc.NavLink(TRANSLATE[lang]["SVM"], href="/svm")),
                        dbc.NavItem(dbc.NavLink(TRANSLATE[lang]["Neural Network"], href="/neural-network")),
                        html.Div([
                            dmc.Menu([
                                dmc.MenuTarget(dmc.Avatar(di(icon="fontisto:male", color=TERTIARY_COLOR), radius="xl", size="md",
                                                          style={"cursor": "pointer"}, className="ms-3")),
                                dmc.MenuDropdown([
                                    dmc.MenuItem(TRANSLATE[lang]["Profile"], leftSection=di(
                                        icon="ic:baseline-account-circle")),
                                    dmc.MenuItem(TRANSLATE[lang]["Settings"], leftSection=di(
                                        icon="ic:baseline-settings")),
                                    dmc.MenuItem(
                                        dmc.Switch(
                                            onLabel=di(
                                                icon="emojione:flag-for-germany", width=24),
                                            offLabel=di(
                                                icon="emojione:flag-for-united-states", width=24),
                                            size="md",
                                            id="lang-toggle",
                                            persistence=True,
                                            persistence_type="local",
                                        ),
                                    leftSection=di(icon="ic:baseline-translate")),
                                    dmc.MenuDivider(),
                                    dmc.MenuItem(TRANSLATE[lang]["Logout"], leftSection=di(
                                        icon="ic:baseline-exit-to-app"), color="red"),
                                ])
                            ], trigger="hover", closeDelay=250),


                        ], className="d-flex gap-2 p-2"),
                    ], className="d-flex align-items-center", style={"height": "5vh", "marginLeft":"auto"}),
                ],
                brand=html.Div(html.H3(APP_NAME), className="ms-3"),
                brand_href="/",
                color="primary",
                dark=True,
                fluid=True,
                className="nav-header")
        ]



