#!/usr/bin/env python
# coding: utf-8

# # Painel Fretes 2023

# In[38]:


# Bibliotecas
import os
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import subprocess
import re
import warnings
import plotly.express as px  
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
#from jupyter_dash import JupyterDash
import dash_bootstrap_components as dbc

warnings.filterwarnings("ignore")


# In[39]:


# Caminho atual
path_atual = os.getcwd()
path_git = 'https://github.com/luismmodolo/dashboard_python/raw/main/painel_teste.xlsx'


# In[40]:


# Base fretes
df = pd.read_excel(path_git, sheet_name='base_fretes')
print(len(df)) 
df.head(2)  


# In[41]:


tipo_carga=list(df['tipo_carga'].unique())
tipo_carga.append("Todas")


# In[42]:


# Base infos
df_info = pd.read_excel('painel_teste.xlsx', sheet_name='infos')
print(len(df_info)) 
df_info.head(2)  


# In[44]:


#fig = px.scatter(df, x='distancia', y='tarifa_ton', color='empresa', trendline='ols', title='Curva de Frete')
#fig.update_layout(paper_bgcolor='#242424',
#                  plot_bgcolor='#242424',
#                  autosize=True,
#                  #margin=dict(l=10, r=10, t=10, b=10),
#                  template='plotly_dark',
#                  showlegend=True)
#fig.show()


# In[45]:


app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

app.layout = dbc.Container(children=[
    html.H1(children="Painel de Fretes ILOS", style={"background-color": "#242424"}),
    html.H5(children="Selecione o tipo da carga", style={"background-color": "#242424"}),
    dcc.Dropdown(tipo_carga, value='Todas', id='tipo_carga'),
    dcc.Graph(id="curva_frete", figure=fig, style={"background-color": "#242424"}),
],style={"background-color": "#242424"})


# In[46]:


@app.callback(
    Output('curva_frete', 'figure'),
    Input('tipo_carga', 'value')
)
def update_output(value):
    if value == "Todas":
        fig = px.scatter(df, x='distancia', y='tarifa_ton', color='empresa', trendline='ols', title='Curva de Frete')
        fig.update_layout(paper_bgcolor='#242424',
                          plot_bgcolor='#242424',
                          autosize=True,
                          #margin=dict(l=10, r=10, t=10, b=10),
                          template='plotly_dark',
                          showlegend=True)
    else:
        df_filtrado = df.loc[df['tipo_carga']==value, :]
        fig = px.scatter(df_filtrado, x='distancia', y='tarifa_ton', color='empresa', trendline='ols', title='Curva de Frete')
        fig.update_layout(paper_bgcolor='#242424',
                          plot_bgcolor='#242424',
                          autosize=True,
                          #margin=dict(l=10, r=10, t=10, b=10),
                          template='plotly_dark',
                          showlegend=True)
    return fig


# In[ ]:


if __name__ == '__main__':
    app.run_server(debug=True)


# In[ ]:




