#!/usr/bin/env python
# coding: utf-8

# In[5]:


pip install jupyterlab


# In[6]:


import pandas as pd
import csv
import numpy as np 
import matplotlib.pyplot as plt 
from decimal import Decimal
import plotly.express as px
df = pd.read_csv('alunos-ingressantes.csv', sep=';',encoding='latin-1')

df["Curso"]=df["Curso"].replace(["Física - Licenciatura", "Matemática - Licenciatura","Química - Licenciatura","Educação Física - Licenciatura","Ciências Biológicas - Licenciatura"],["Física", "Matemática","Química","Educação Física","Ciências Biológicas"])
display(df)


# In[7]:


df2=df[df["NivelAgrupado"] == "Graduação"]
df3=df2[df2["Campus"] == "Florestal"]
df4=df2[df2["Campus"] == "Viçosa"]
df5=df2[df2["Campus"] == "Rio Paranaíba"]
df3


# In[8]:


df_group1 = df3.groupby("AnoAdmissao").count().reset_index()
df_group1[['AnoAdmissao','Campus']]
dg1=df_group1[['AnoAdmissao','Campus']].rename(columns={
    "AnoAdmissao": "AnoAdmissao",
    "Campus": "Florestal"})
dg1


# In[9]:


df_group2 = df4.groupby("AnoAdmissao").count().reset_index()
df_group2[['AnoAdmissao','Campus']]

dg2=df_group2[['AnoAdmissao','Campus']].rename(columns={
    "AnoAdmissao": "AnoAdmissao",
    "Campus": "Viçosa"})
dg2


# In[10]:


data_df = df3.groupby(['AnoAdmissao', 'Curso']).agg(avg_age=('AnoAdmissao', 'mean'), count=('AnoAdmissao', 'count'))
  
data_df = data_df.reset_index() 
print(data_df.head()) 
data_df.shape 


# In[11]:


t=df3.groupby(['AnoAdmissao', 'Curso']).agg(avg_age=('AnoAdmissao', 'mean'), count=('AnoAdmissao', 'count'))


# In[12]:


t


# In[13]:


# replace column values with collection


# In[14]:


fig = px.bar(data_df, x="AnoAdmissao", y="count", color="Curso", barmode="group")
fig


# In[15]:


df_group3 = df5.groupby("AnoAdmissao").count().reset_index()
df_group3[['AnoAdmissao','Campus']]

dg3=df_group3[['AnoAdmissao','Campus']].rename(columns={
    "AnoAdmissao": "AnoAdmissao",
    "Campus": "Rio Paranaíba"})
dg3


# In[16]:


m = pd.merge(dg1, dg2, on = "AnoAdmissao")
m


# In[17]:


m1 = pd.merge(m, dg3, on = "AnoAdmissao")
m1


# In[18]:


m1.plot(x="AnoAdmissao", y=["Florestal","Rio Paranaíba","Viçosa"], kind="bar", figsize=(9, 7))


# In[19]:


dh3=df3[df3["SituacaoAluno"] == "Conclusão"]
dh4=df4[df4["SituacaoAluno"] == "Conclusão"]
dh5=df5[df5["SituacaoAluno"] == "Conclusão"]
dh3


# In[20]:


data_dh = dh3.groupby(['AnoAdmissao', 'Curso']).agg(avg_age=('AnoAdmissao', 'mean'), count=('AnoAdmissao', 'count'))
  
data_dh = data_dh.reset_index() 
print(data_dh.head()) 
data_dh.shape 


# In[21]:


df_group3 = dh3.groupby("AnoAdmissao").count().reset_index()
df_group3[['AnoAdmissao','Campus']]

dt=df_group3[['AnoAdmissao','Campus']].rename(columns={
    "AnoAdmissao": "AnoAdmissao",
    "Campus": "Florestal"})
dt


# In[22]:


fig2 = px.line(data_dh, x="AnoAdmissao", y="count", color="Curso")
fig2


# In[23]:


pd.set_option('display.max_rows', None)
df_group4 = df3.groupby("Naturalidade").count().reset_index()
df_group4[['Naturalidade','Campus']]

dl=df_group4[['Naturalidade','Campus']].rename(columns={
    "Naturalidade": "Naturalidade",
    "Campus": "Florestal"})

dl.sort_values(by='Florestal', ascending=False)

 


# In[24]:


pd.set_option('display.max_rows', None)
df_group5 = df4.groupby("Naturalidade").count().reset_index()
df_group5[['Naturalidade','Campus']]

dk=df_group5[['Naturalidade','Campus']].rename(columns={
    "Naturalidade": "Naturalidade",
    "Campus": "Viçosa"})

dk.sort_values(by='Viçosa', ascending=False)
dv=dk.sort_values(by='Viçosa', ascending=False)
dv
 


# In[25]:


pd.set_option('display.max_rows', None)
df_group6 = df5.groupby("Naturalidade").count().reset_index()
df_group6[['Naturalidade','Campus']]

dk1=df_group6[['Naturalidade','Campus']].rename(columns={
    "Naturalidade": "Naturalidade",
    "Campus": "Rio Paranaíba"})

dk1.sort_values(by='Rio Paranaíba', ascending=False)
drp=dk1.sort_values(by='Rio Paranaíba', ascending=False)
drp


# In[26]:


dm=dl.sort_values(by='Florestal', ascending=False)
dm


# In[27]:


dfAM = pd.read_csv('Alunos Matriculados.csv', sep=';',encoding='latin-1')

display(dfAM)


# In[28]:


data_dfAM = dfAM.groupby(['Ano', 'Áreas/Cursos']).agg(avg_age=('Ano', 'mean'), count1=('Mat. Sem. 1 Total', 'sum'), count2=('Mat. Sem. 2 Total', 'sum'))
  
data_dfAM = data_dfAM.reset_index() 
print(data_dfAM.head()) 
data_dfAM.shape


# In[29]:


data_dgAM = data_dfAM.groupby(['Ano']).agg(avg_age=('Ano', 'mean'), Semestre_1=('count1', 'sum'), Semestre_2=('count2', 'sum'))
  
data_dgAM = data_dgAM.reset_index() 
print(data_dgAM.head()) 
data_dgAM.shape


# In[30]:


data_dfAD = dfAM.groupby(['Ano', 'Áreas/Cursos']).agg(avg_age=('Ano', 'mean'), count1=('Dip. Sem. 1 Total', 'sum'), count2=('Dip. Sem. 2 Total', 'sum'))
  
data_dfAD = data_dfAD.reset_index() 
print(data_dfAD.head()) 
data_dfAD.shape


# In[31]:


data_dgAD = data_dfAD.groupby(['Ano']).agg(avg_age=('Ano', 'mean'), Semestre_1=('count1', 'sum'), Semestre_2=('count2', 'sum'))
  
data_dgAD = data_dgAD.reset_index() 
print(data_dgAD.head()) 
data_dgAD.shape


# In[32]:


f = data_dgAD.eval('Formandos =Semestre_1+ Semestre_2')
print(f)


# In[33]:


cid0=df3.loc[(df3["Naturalidade"] == 'Belo Horizonte') | (df3["Naturalidade"] == 'Betim')| (df3["Naturalidade"] == 'Pará de Minas')]
cid = cid0.groupby(['AnoAdmissao', 'Naturalidade']).agg(avg_age=('AnoAdmissao', 'mean'), count=('AnoAdmissao', 'count'))
cid = cid.reset_index()  
cid


# In[ ]:





# In[34]:


cidc=df3.loc[(df3["Naturalidade"] == 'Belo Horizonte') | (df3["Naturalidade"] == 'Betim')| (df3["Naturalidade"] == 'Pará de Minas')]
cidcc = cidc.groupby(['AnoAdmissao', 'Naturalidade','Curso']).agg(avg_age=('AnoAdmissao', 'mean'), count=('AnoAdmissao', 'count'))
cidcc = cidcc.reset_index()  
cidcc


# In[35]:


# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, dcc, html, Input, Output, callback, dash_table

import plotly.express as px
import dash_bootstrap_components as dbc
from dash import html
import plotly.graph_objects as go

app = Dash(__name__,external_stylesheets = [dbc.themes.BOOTSTRAP])
server=app.server
 
external_stylesheets = [dbc.themes.BOOTSTRAP]



# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

 
fig = px.bar(data_df, x="AnoAdmissao", y="count", color="Curso", barmode="group")
opcoes=list(data_df['Curso'].unique())
opcoes.append('Todos os cursos')

a1=px.line(m1, x="AnoAdmissao", y=["Florestal","Rio Paranaíba","Viçosa"],width=750, height=400)
# print bar graph
a2=px.bar(m1,x="AnoAdmissao", y=["Florestal","Rio Paranaíba","Viçosa"],barmode="group",width=750, height=400)


a3=px.bar(data_dgAM,x="Ano", y=["Semestre_1","Semestre_2"],barmode="group",width=850, height=400, text_auto='', title="Alunos Matriculados no campus UFV-Florestal")
a3.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)

a4=px.bar(f,x="Ano", y="Formandos",width=650, height=400, text_auto='', title="Formandos no campus UFV-Florestal")
a4.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)

a5=px.line(cid, x="AnoAdmissao", y="count",color="Naturalidade", width=750, height=400, title="Campus UFV-Florestal por cidade")

a6=px.line(cidcc, x="AnoAdmissao", y="count",color="Curso", width=750, height=400, title="CDC por cidade")
 


app.layout = html.Div([
     dbc.Row(
            [
                   html.H1(
                     children='Entrada de alunos na UFV desde 2010',
                     style={
                    'textAlign': 'center'}
                     ),
            ]),
     
         dbc.Row(
            [    dbc.Col(     
                         dcc.Graph( id='example-graph-4',
                 figure=a2), 
                      width=6,
                         
     ),
     dbc.Col(
                 dcc.Graph( id='example-graph-3',
                 figure=a1), 
         width=6
         
      ),
            ]),

    
 dbc.Row([    
html.Div( [
     dbc.Row([ 
                  html.Label('Entrada de alunos por curso-UFV-Florestal'),
                  dcc.Dropdown(opcoes, value='Todos os cursos',id= 'Curso', 
                  style={'padding': 4, 'flex': 1}),       
                   
                 dcc.Graph(
                 id='example-graph-2',
                 figure=fig),
     ]),
    
        dbc.Row(
            [ 
                dbc.Col(
                    dcc.Graph( id='example-graph-5',
                 figure=a3), 
                    width=7
                ), 
                dbc.Col(
                    dcc.Graph( id='example-graph-6',
                 figure=a4),
                    width=5
                ),
            ]),
    dbc.Row([
         dbc.Col(
               dcc.Graph( id='example-graph-7',
                 figure=a5), 
             width=6
         ),          
          dbc.Col(
               dcc.Graph( id='example-graph-8',
                 figure=a6), 
             width=6
         ),                         
        
    ]),
     dbc.Row([    
       
    html.H4('Cidades dos alunos matriculados nos campi da UFV'),
   dbc.Col(
         dash_table.DataTable(
    data=dm.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in dm.columns],
    page_size=10,
    style_cell=dict(textAlign='left'),
    style_header=dict(backgroundColor="paleturquoise"),
    style_data=dict(backgroundColor="lavender"),
),
           width=3,
       ),
         
         dbc.Col(
         dash_table.DataTable(
    data=dv.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in dv.columns],
    page_size=10,
    style_cell=dict(textAlign='left'),
    style_header=dict(backgroundColor="paleturquoise"),
    style_data=dict(backgroundColor="lavender"),
),
           width=3,
       ),
   dbc.Col(
         dash_table.DataTable(
    data=drp.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in drp.columns],
    page_size=10,
    style_cell=dict(textAlign='left'),
    style_header=dict(backgroundColor="paleturquoise"),
    style_data=dict(backgroundColor="lavender"),
),
           width=3,
       ),
         
 ],
     style={"height":"10vh"}, 
 ),
 
    
]),



     
 ]),              

])            
 
 
@app.callback(
    Output(component_id='example-graph-2', component_property='figure'),
    Input(component_id='Curso', component_property='value')
)
def update_output(value):

    return fig

 

if __name__ == '__main__':
    app.run(port=8051)(debug=True)


# In[ ]:






# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




