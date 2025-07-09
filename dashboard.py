#%%

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, ClientsideFunction
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

import numpy as np
import pandas as pd
import json

# Filtrando apenas os dados nescessarios 

# df = pd.read_csv("HIST_PAINEL_COVIDBR_13mai2021.csv", sep=';')
# df_states = df[~df["estado"].isna() & (df["codmun"].isna())]
# df_brasil = df[df["regiao"] == "Brasil"]
# df_states.to_csv("df_states.csv")
# df_brasil.to_csv("df_brasil.csv")


df_states = pd.read_csv("df_states.csv")
df_brasil = pd.read_csv("df_brasil.csv")

df_states_ = df_states[df_states["data"] == "2020-05-13"]

brazil_states = json.load(open("geojson/brazil_geo.json"))

#=========================================
# Instanciação do Dash

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

fig = px.choropleth_mapbox(df_states, locations="estado", color="casosNovos",
                           center={"lat": -16.95, "lon": -47.78},
                           geojson=brazil_states, color_continuous_scale="Redor", opacity=0.4,
                           hover_data={"casosAcumulado": True, "casosNovos": True, 
                                       "obitosNovos": True, "estado": True})

fig.update_layout(
    mapbox_style= "carto-darkmatter"
)

#=========================================
# Layout

app.layout = dbc.Container(
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="choropleth-map", figure=fig)
        ])
    ])
)

if __name__ == "__main__":
    app.run(debug=True)


# %%
