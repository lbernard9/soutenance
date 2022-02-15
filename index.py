import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

from navbar import navbar
from menu import menu
from app import app

import content

items = [("Présentation","/presentation"),
         ("Données","/data"),
         ("Premiers modèles","/first_model"),
         ("Modèles Deep","/deep_model"),
         ("Analyse","/analysis"),
         ("Segmentation","/segmentation"),
         ("Résultats","/results"),
         ("Conclusion","/ending"),
         ("Demo","/demo")]


header = navbar()
page = html.Div(
    [
        dcc.Location(id='url', refresh=True, pathname=items[0][1]),
        dbc.Row(
            [
                dbc.Col(menu(items), width=2 , align="start",style={"padding-left":"2em"}),
                dbc.Col(html.Div("Content"), width={"size": 9,"offset":1},id='content',
                        style={"padding-right":"2em"}),
            ],
            style={"margin-top":"100px"}, justify="center",
        ),
    ],style={"overflow-x":"hidden"}
)
footer = dbc.Navbar([dbc.Row([dbc.Col(
                            html.P(["Soutenance de projet, formation Data Scientist (Datascientest) : Laure BERNARD",
                                    html.A([html.Img(src="./assets/linkedin.png", style={"height":"1.5em","margin-left":"1em"})],
                                           href="https://www.linkedin.com/in/laurebernard38/",target="_blank",)
                                    ],style={"color":"#fff"})
                                ,
                                width={"size": 12,"offset":4})])
                            ]
                    ,
                    color="primary",
                    dark=True,
                    fixed="bottom"
                     )

# Contenu selon le menu sélectionné
@app.callback(Output('content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    fct = "content." + pathname[1:]+'()'
    return eval(fct)

# Retourne la page : entête, contenu, pied de page
def index():
    return html.Div([header, page, footer])


app.layout=index()

if __name__ == "__main__":
    # set debug to false when deploying app
    app.run_server(host='0.0.0.0',port='80',debug=False)