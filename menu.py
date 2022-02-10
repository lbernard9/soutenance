import dash_bootstrap_components as dbc
from dash import html
import numpy as np
from dash.dependencies import Input, Output, ALL
from app import app



def group_item(index, title, href):
    return dbc.ListGroupItem(title, id={"type": "button", "index": index}, href=href)

def menu(items):
    html_menu = html.Div(
    [
        dbc.ListGroup(
            [group_item(i, item[0], item[1]) for i, item in enumerate(items)

             ]
            , id="menu"
        )
    ]
    )
    return html_menu


@app.callback(Output({"type": "button", "index": ALL}, "active"), [Input({"type": "button", "index": ALL}, "n_clicks_timestamp")])
def clicked(n_clicks_timestamp):
    n_clicks = np.array(n_clicks_timestamp, np.float)
    state_btn = np.zeros(len(n_clicks), int)
    if np.isnan(n_clicks).sum() == len(n_clicks_timestamp):
        # Aucun bouton cliqué=> 1er élément du menu
        state_btn[0]=1
    else:
        state_btn[np.nanargmax(np.array(n_clicks, np.float))] = 1
    return list(state_btn)



