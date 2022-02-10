import dash_bootstrap_components as dbc
from dash import html

button_github  = dbc.Button(
    "Code Source github",
    outline=True,
    color="primary",
    href="https://github.com/lbernard9/bloodcells",
    id="gh-link",
    style={"text-transform": "none"},
)


def navbar():
    nav_bar = dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    # Use row and col to control vertical alignment of logo / brand
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src='./assets/lymphocyte.jpg', height="50px")),
                            dbc.Col(dbc.NavbarBrand("Reconnaissance des cellules sanguines", className="ms-2")),
                        ],
                        align="center",
                        className="g-0",
                    ),
                    href="#",
                    style={"textDecoration": "none"},
                ),
                dbc.NavItem(dbc.Button("Source Github", outline=True,
                                color="secondary", href="https://github.com/lbernard9/bloodcells")),
            ]
        ),
        color="primary",
        dark=True,
        fixed="top"
    )
    return nav_bar

