"""
Copyright 2021 Louis Héraut, Louis Gostiaux

This file is part of Pygantt.

Pygantt is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Pygantt is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Pygantt.  If not, see <https://www.gnu.org/licenses/>.

 /\ /\
= 0 0 =
 """""

###  1. LIBRARY
import plotly.graph_objects as go
import pandas as pd
import datetime
import numpy as np


###  2. GENERAL INFORMATIONS
## 2.1. date time info
start = datetime.datetime.strptime("01-04-2021", "%d-%m-%Y")
end = datetime.datetime.strptime("31-07-2021", "%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days, 7)]

## 2.2. colors by category
Ccolor = {"Category 1":['LightGreen', 'MediumSeaGreen'], 
          "Category 2":['LightSkyBlue', 'SteelBlue'], 
          "Category 3":['PaleVioletRed', 'MediumVioletRed '], 
          "Category 4":['Plum', 'Orchid'],
          "Category 5":['Tan', 'Sienna'],
          "Title":['black', 'black']
          }

###  3. CONTENT
odf = pd.DataFrame([
        # section
        dict(Task="<b>1. Section</b>", 
             Start='01-07-2021', Finish='01-07-2021', Completion_pct=0,                 
             Category="Title", 
             Note=''),
             
    # subsection
    dict(Task="<b>1.1</b> Subsection 1",
         Start='01-07-2021', Finish='10-07-2021', Completion_pct=100, 
         Category="Category 1", 
         Note="foo"),
        
    dict(Task="<b>1.2</b> Subsection 2", 
         Start='08-07-2021', Finish='20-07-2021', Completion_pct=60, 
         Category="Category 2", 
         Note="foo<br>"
              "foobar<br>"
              "foooobar<br>"),
    # ...
])


###  4. DATA PROCESSING
df = odf.copy()
df["Start"] = pd.to_datetime(df["Start"], format="%d-%m-%Y")
df["Finish"] = pd.to_datetime(df["Finish"], format="%d-%m-%Y")
df["Completion_date"] = pd.to_datetime((df["Finish"] - df["Start"]) * df["Completion_pct"] / 100 + df["Start"], format="%d-%m-%Y")
df["Duration"] = (df["Finish"] - df["Start"])


###  5. PLOTTING
## 5.1. bars
fig = go.Figure()
for cat in df['Category']:
    sdf = df[df['Category'] == cat]
    
    # full bar
    fig.add_trace(go.Bar(base=sdf["Start"],
                                x=np.array((sdf["Finish"] - sdf["Start"]))/1E6,
                                y=sdf["Task"],
                                orientation='h', 
                                marker_color=Ccolor[cat][0],
                                marker_line_width=0, 
                                width=0.9,
                                customdata=odf[odf['Category'] == cat],
                                hovertemplate='%{customdata[0]}<br><br>Du %{customdata[1]} au %{customdata[2]}<br>Complété à %{customdata[3]} %<br>Catégorie: %{customdata[4]}<br>Note: %{customdata[5]}<extra></extra>',
                                showlegend=not(cat in [data['name'] for data in list(fig.data)]),
                                name=cat,
                                legendgroup=cat))
                                
    # completion bar
    fig.add_trace(go.Bar(base=sdf["Start"],
                        x=np.array((sdf["Completion_date"] - sdf["Start"]))/1E6,
                        y=sdf["Task"],
                        orientation='h', 
                        marker_color=Ccolor[cat][1],
                        marker_line_width=0, 
                        width=0.9,
                        customdata=odf[odf['Category'] == cat],
                        hovertemplate='%{customdata[0]}<br><br><b>Date: </b> %{customdata[1]} / %{customdata[2]}<br><b>Complété à:</b> %{customdata[3]} %<br><b>Catégorie:</b> %{customdata[4]}<br><b>Note</b>: %{customdata[5]}<extra></extra>',
                        legendgroup=cat,
                        showlegend=False
                        ))
                        
    # text bar
    fig.add_trace(go.Bar(base=sdf["Start"],
                        x=np.array((sdf["Finish"] - sdf["Start"]))/1E6,
                        y=sdf["Task"],
                        orientation='h', 
                        marker_color='rgba(255, 0, 0, 0)',
                        marker_line_width=0, 
                        width=0.9,
                        text=sdf["Completion_pct"],
                        texttemplate='<b>%{text:.0f} %</b>',
                        textposition='inside', 
                        insidetextanchor='start', 
                        textfont=dict(color='white', family="Lato", size=20),
                        hoverinfo='skip',
                        legendgroup=cat,
                        showlegend=False
                        ))

## 5.2. other info
# marker for today
today = datetime.datetime.today().strftime("%d-%m-%Y")
fig.add_trace(go.Scatter(x=[pd.to_datetime(today, format="%d-%m-%Y") for i in range(len(df))], 
                         y=df["Task"],
                         mode='lines',
                         line=dict(color='Gray', dash='dot', width=1), 
                         hovertemplate="Aujourd'hui: {}<extra></extra>".format(today),
                         name="Aujourd'hui"
                         ))

## 5.3. layout
fig.update_yaxes(autorange="reversed")

fig.update_xaxes(
    type="date",
    tickformat="%d %b %Y",
    # tickvals = [pd.to_datetime(date.strftime("%d-%m-%Y"), format="%d-%m-%Y") for date in date_generated],
    range=(pd.to_datetime('01-04-2021', format="%d-%m-%Y"), pd.to_datetime('31-07-2021', format="%d-%m-%Y")),
    tickfont=dict(size=13, family="Lato"),
    showline=True,
    linewidth=2, 
    linecolor='SlateGrey',
    showgrid=True,
    gridcolor='LightGrey',
    gridwidth=0.5, 
    ticks="outside",
    tickcolor='SlateGrey',
    ticklen=4,
    tickwidth=2,
    tickangle=0,
    ticklabelmode='period',
    nticks=12
)

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=7, label="1 semaine", step="day", stepmode="backward"),
            dict(count=14, label="2 semaine", step="day", stepmode="backward"),
            dict(count=1, label="1 mois", step="month", stepmode="backward"),
            dict(label="toute la période", step="all")
        ])),
    tickformatstops = [
        dict(dtickrange=[None, 86400000], value="%e %b"),
        dict(dtickrange=[86400000, 604800000], value="sem. %W"),
        dict(dtickrange=[604800000, None], value="%b %Y"),
        ]
)

fig.update_yaxes(
    title='',
    tickfont=dict(size=13, family="Lato"),
    type='category',
    categoryorder='category ascending',
    showline=True,
    linewidth=2, 
    linecolor='SlateGrey',
    ticks="outside",
    tickcolor='SlateGrey',
    ticklen=4,
    tickwidth=2,
    fixedrange=True
)

fig.update_layout(
    title={'text': "<b>Avancement du stage de Louis Héraut encadré par Louis Gostiaux</b><br>Séries temporelles de température dans l'océan profond: ré-analyse des données haute résolution de thermistors NIOZ-HST sur la<br>période 2006-2016 visant à l'étude des statistiques d'ordre élevé dans les écoulements géophysiques avec rotation et stratification",
        'font':dict(size=18),
        'y':0.96,
        'x':0.085},
    barmode='overlay',
    margin=dict(l=80, r=10, t=140, b=60),
    plot_bgcolor='white', 
    height=1100, 
    width=1300)

# plotting
fig.write_html("pygantt.html")
fig.show()