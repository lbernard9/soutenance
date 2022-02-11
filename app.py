import dash
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.FLATLY]
app = dash.Dash(__name__,  external_stylesheets=external_stylesheets,title="BloodCells : Projet Computer Vision")
app._favicon = "./lymphocyte.ico"