import dash_bootstrap_components as dbc
from src.configs import APP_NAME
from dash import html


class Footer(html.Footer): # pragma: no cover
    def __init__(self):
        super().__init__([
            html.Section(
                [
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.H6(
                                                APP_NAME,
                                                className=" fw-bold mb-4",
                                            ),
                                            html.P(
                                                "Your dash template for building beautiful apps.",
                                            ),
                                        ],
                                        className="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4",
                                    ),
                                    html.Div(
                                        [
                                            html.H6(
                                                "Products",
                                                className="fw-bold mb-4",
                                            ),
                                            html.P(
                                                html.A(
                                                    "Showcase 1",
                                                    href="#",
                                                    className="text-reset",
                                                )
                                            ),
                                            html.P(
                                                html.A(
                                                    "Showcase 2",
                                                    href="#",
                                                    className="text-reset",
                                                ),
                                            ),
                                            html.P(
                                                html.A(
                                                    "Showcase 3",
                                                    href="#",
                                                    className="text-reset",
                                                ),
                                            ),
                                        ],
                                        className="col-md-2 col-lg-2 col-xl-2 mx-auto mb-4",
                                    ),
                                    html.Div(
                                        [
                                            html.H6(
                                                "Useful links",
                                                className="fw-bold mb-4",
                                            ),
                                            html.P(
                                                dbc.NavLink(
                                                    "FAQ",
                                                    href="/info",
                                                    className="text-reset",
                                                ),
                                            ),
                                            html.P(
                                                dbc.NavLink(
                                                    "Privacy Policy",
                                                    href="/info",
                                                    className="text-reset",
                                                ),
                                            ),
                                            html.P(
                                                dbc.NavLink(
                                                    "Impressum",
                                                    href="/info",
                                                    className="text-reset",
                                                ),
                                            ),
                                            html.P(
                                                dbc.NavLink(
                                                    "Terms of Service",
                                                    href="/info",
                                                    className="text-reset",
                                                ),
                                            ),
                                        ],
                                        className="col-md-3 col-lg-2 col-xl-2 mx-auto mb-4",
                                    ),
                                    html.Div(
                                        [
                                            html.H6(
                                                "Contact",
                                                className="text-uppercase fw-bold mb-4",
                                            ),
                                            html.P(
                                                [
                                                    html.I(
                                                        className="fas fa-home me-3",
                                                    ),
                                                    "New York, NY 10012, US",
                                                ]
                                            ),
                                            html.P(
                                                [
                                                    html.I(
                                                        className="fas fa-envelope me-3"
                                                    ),
                                                    "info@example.com",
                                                ]
                                            ),
                                            html.P(
                                                [
                                                    html.I(
                                                        className="fas fa-phone me-3"
                                                    ),
                                                    "+ 01 234 567 88",
                                                ]
                                            ),
                                            html.P(
                                                [
                                                    html.I(
                                                        className="fas fa-print me-3"
                                                    ),
                                                    "+ 01 234 567 89",
                                                ]
                                            ),
                                        ],
                                        className="col-md-4 col-lg-3 col-xl-3 mx-auto mb-md-0 mb-4",
                                    ),
                                ],
                                className="row mt-3",
                            ),
                        ],
                        className="container text-center text-md-start p-5",
                    ),
                ],
                className="bg-body-tertiary text-muted", id="contact",
            ),
        ],
        )
