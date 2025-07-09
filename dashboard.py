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

df = pd.read_csv("HIST_PAINEL_COVIDBR_13mai2021.csv", sep=';')
df_states = df[~df["estado"].isna() & (df["codmun"].isna())]
df_brasil = df[df["regiao"] == "Brasil"]
df_states.to_csv("df_state.csv")
df_brasil.to_csv("df_brasil.csv")
