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
Ccolor = {"Développement d'outil de visualisation":['LightGreen', 'MediumSeaGreen'], 
          "Développement du traitement de données":['LightSkyBlue', 'SteelBlue'], 
          "Prise en main du code initial":['PaleVioletRed', 'MediumVioletRed '], 
          "Utilisation des outils de réseau":['Plum', 'Orchid'],
          "Rédaction de contenu scientifique":['Tan', 'Sienna'],
          "Titre":['black', 'black']
          }

###  3. CONTENT
odf = pd.DataFrame([
        # section
        dict(Task="<b>1. Prise en main de l'environnement de travail</b>", 
             Start='01-04-2021', Finish='01-04-2021', Completion_pct=0,                 
             Category="Titre", 
             Note=''),
             
    # subsection
    dict(Task="<b>1.1</b> Prise en main de git",
         Start='01-04-2021', Finish='02-04-2021', Completion_pct=100, 
         Category="Utilisation des outils de réseau", 
         Note="Téléchargement du code."),
        
    dict(Task="<b>1.2</b> Prise en main du jeu de données du Great Meteor Seamont", 
         Start='01-04-2021', Finish='02-04-2021', Completion_pct=100, 
         Category="Prise en main du code initial", 
         Note="Téléchargement d'un jeu de données légé mais présentant de<br>"
              "nombreux problèmes de déviation."),
    
    dict(Task="<b>1.3</b> Reproduction et étude de figure d'article",
         Start='02-04-2021', Finish='03-04-2021', Completion_pct=100, 
         Category="Prise en main du code initial", 
         Note="figure 3 de van Haren, H., Laan, M., Buijsman, D. J., Gostiaux<br>"
              "L., Smit, M. G., & Keijzer, E. (2009). NIOZ3: Independent<br>"         
              "temperature sensors sampling yearlong data at a rate of 1 Hz.<br>"
              "IEEE Journal of Oceanic Engineering, 34(3), 315-322."),
    
    dict(Task="<b>1.4</b> Recherche d'une nouvelle interface de code", 
         Start='06-04-2021', Finish='07-04-2021', Completion_pct=75, 
         Category="Prise en main du code initial", 
         Note="Essaie de Visual Studio Code avant de retourner à Pyzo."),
         
    dict(Task="<b>1.4</b> Recherche d'une nouvelle interface de code", 
         Start='14-04-2021', Finish='15-04-2021', Completion_pct=50, 
         Category="Prise en main du code initial", 
         Note="Nouvel essaie de configuration de Visual Studio Code avant de<br>"
              "retourner à Pyzo."),
         
    dict(Task="<b>1.5</b> Configuration du VPN et de l'accès au calculateur de l'ECL", 
         Start='02-04-2021', Finish='10-04-2021', Completion_pct=100, 
         Category="Utilisation des outils de réseau", 
         Note="Problème de configuration du VPN sur KDE donc aide avec le<br>"
              "responsable informatique du calculateur et formation de groupe<br>"
              "à l'accès au calculateur."),
         
         
        dict(Task="<b>2. Développement de l'espace de travail</b>",
             Start='01-04-2021', Finish='01-04-2021', Completion_pct=0,                 
             Category="Titre", 
             Note=''),
             
    dict(Task="<b>2.1</b> Création du schéma d'arboressence de stockage des résultats", 
         Start='06-04-2021', Finish='10-04-2021', Completion_pct=100, 
         Category="Développement du traitement de données", 
         Note="Les informations de calibraions sont stockées dans le noms de fichier<br>"
              "et les noms de dossiers."),
              
    dict(Task="<b>2.2</b> Développement du système de processing", 
         Start='06-04-2021', Finish='14-04-2021', Completion_pct=100, 
         Category="Développement du traitement de données", 
         Note="Définiton d'une plage de temps prenant en compte l'ensemble des<br>"
              "données disponibles et test des diverses fonctions d'autoscale."),
              
    dict(Task="<b>2.3</b> Développement du système de plotting", 
         Start='06-04-2021', Finish='12-04-2021', Completion_pct=100, 
         Category="Développement d'outil de visualisation", 
         Note="Mise en forme des profils de température, du profil du gradient<br>"
              "vertical et horizontal de température et des profils intermédiaires<br>"
              "entre deux autoscaling adjacents."),
    
    dict(Task="<b>2.4</b> Matrice de diagnostique de l'efficacité de la correction", 
         Start='12-04-2021', Finish='14-04-2021', Completion_pct=75, 
         Category="Développement d'outil de visualisation", 
         Note="Diagnostique de vérification de l'effet de l'autoscaling sur la<br>"
              "moyenne et l'écart-type d'un ensemble de température."),
              
    dict(Task="<b>2.5</b> Mise au propre général de l'ensemble du code produit", 
         Start='13-04-2021', Finish='17-04-2021', Completion_pct=100, 
         Category="Développement du traitement de données", 
         Note="Louis Gostiaux m'a aidé à remettre en forme l'ensemble du code<br>"
              "pour le rentre d'avantage polyvalent, robuste à l'utilisation en<br>"
              "terminal pour le calculateur et diffusable pour un tier."),
    
    
        dict(Task="<b>3. Développement d'un nouveau moyen d'autoscalling</b>",
             Start='01-04-2021', Finish='01-04-2021', Completion_pct=0,                 
             Category="Titre", 
             Note=''),
             
    dict(Task="<b>3.1</b> Autoscalling à variation de température discrete", 
         Start='19-04-2021', Finish='21-04-2021', Completion_pct=100, 
         Category="Développement du traitement de données", 
         Note="En utilisant \Delta T = T_{n} - (T_{n+1} + T_{n-1})/2 sur la<br>"
              "moyenne temporelle des températures de chaque capteur, il est<br>"
              "possible de compenser à l'ordre 0 les décalges d'un capteur<br>"
              "relativement au autres. Ce même calcul peut être effectué sur<br>"
              "les T à tout temps permettant alors de compenser la déviation<br>"
              "à l'ordre 1 d'un capteur en effectuant une régression linéaire<br>"
              "du nuage de point issu de \Delta T = f(T)."),
              
    dict(Task="<b>3.2</b> Autoscalling avec utilisation de splines", 
         Start='21-04-2021', Finish='27-04-2021', Completion_pct=100, 
         Category="Développement du traitement de données", 
         Note="La correction de la déviation à l'ordre 0 est réalisée en <br>"
              "utilisant un spline sur l'ensemle des moyennes temporelles des<br>"
              "capteurs. La correction à l'ordre 1 est réalisée en utilisant un<br>"
              "spline par morceaux afin d'estimer à un temps donnés l'écart de<br>"
              "température entre le spline et les data."),
              
    dict(Task="<b>3.3</b> Implémentation de la nouvelle méthode dans le code initial", 
         Start='28-04-2021', Finish='30-04-2021', Completion_pct=100, 
         Category="Développement du traitement de données", 
         Note="Implémentation du code développé dans la librairie initiale<br>"
              "et mise au propre."),
             
             
        dict(Task="<b>4. Mise en forme des résultats pour la diffusion</b>",
             Start='01-04-2021', Finish='01-04-2021', Completion_pct=0,                 
             Category="Titre", 
             Note=''),
             
    dict(Task="<b>4.1</b> Exportation des données en hdf5", 
         Start='27-04-2021', Finish='30-04-2021', Completion_pct=100, 
         Category="Développement du traitement de données", 
         Note="Mise en forme des données en une unique matrice en concatenant<br>"
              "l'ensemble des différentes calibrations réalisées à chaque temps"
              "et système de vérification de la bonne sauvegarde."),
              
    dict(Task="<b>4.1</b> Exportation des données en hdf5", 
         Start='06-05-2021', Finish='01-06-2021', Completion_pct=100, 
         Category="Développement du traitement de données", 
         Note="Remise en forme du système de concatenation pour optimiser le<br>"
              "temps de calcul et la mise en mémoire dans le cas de gros fichier<br>"
              "de données."),
              
    dict(Task="<b>4.2</b> Coopération avec un autre stagiaire pour la visualisation", 
         Start='17-05-2021', Finish='16-07-2021', Completion_pct=90, 
         Category="Développement d'outil de visualisation", 
         Note="Un autre stagiaire de l'IRIS est chargé de la représentation<br>"
              "des données calibrées sur mur d'écran. Diverse directive lui ont<br>"
              "été données, des réunions on été réalisés."),
              
    dict(Task="<b>4.3</b> Remise en forme de l'arborescence du code", 
         Start='25-06-2021', Finish='27-06-2021', Completion_pct=100, 
         Category="Développement du traitement de données", 
         Note="L'ensemble de l'arborescence du code est revu afin de simplifier<br>"
              "l'interaction avec lui et l'implémentation de nouveaux mouillages."),
              
    dict(Task="<b>4.4</b> Mise au propre du code", 
         Start='26-06-2021', Finish='16-07-2021', Completion_pct=75, 
         Category="Développement du traitement de données", 
         Note="Le code est mis au propre, les documentations de fonctions sont<br>"
              "revues et des commentaires sont ajoutés. Enfin, des sorties<br>"
              "visuelles de contrôle en ascii art sont aussi développées afin<br>"
              "de pouvoir suivre l'avancé du code et aussi l'état des mouillages."),
              
    
        dict(Task="<b>5. Amélioration de la qualité des résultats de calibration</b>",
             Start='01-04-2021', Finish='01-04-2021', Completion_pct=0,                 
             Category="Titre", 
             Note=''),
    
    dict(Task="<b>5.1</b> Mise en forme de résultats de calibration optimaux", 
         Start='29-04-2021', Finish='15-06-2021', Completion_pct=100, 
         Category="Développement du traitement de données", 
         Note="Utilisation du calculateur en faisant varier les différents<br>"
              "paramètres. Les seuils de calibrations sont modifiés, des capteurs<br>"
              "à isoler sont mis en évidence, l'interpolation des données manquantes<br>"
              "est réalisée et diverse remise en forme du code sont réalisés."),
              
    dict(Task="<b>5.2</b> Interpolation des calibrations entre chaque plage de temps", 
         Start='20-05-2021', Finish='08-06-2021', Completion_pct=100, 
         Category="Développement du traitement de données", 
         Note="Mise en place d'un système d'interpolation des valeurs de calibration<br>"
              "pour un ensemble de plage de temps défini automatiquement afin de<br>"
              "réduire les problèmes de chevauchements entre calibrations et de<br>"
              "créer des fichiers de calibrations unique pour l'ensemble de la plage<br>"
              "de temps."),
    
    dict(Task="<b>5.3</b> Parallélisation avancée du code sur calculateur", 
         Start='26-05-2021', Finish='29-05-2021', Completion_pct=95, 
         Category="Développement du traitement de données", 
         Note="Le nouveau code développé à nécessité une méthode de parallélisation<br>"
              "plus poussée en faisant communiquer les coeurs de calcul entre eux."),
              
    dict(Task="<b>5.4</b> Développement d'un nouveau système de visualisation", 
         Start='27-05-2021', Finish='12-06-2021', Completion_pct=100, 
         Category="Développement d'outil de visualisation", 
         Note="Mise en forme d'une visualisation des futurs fichiers de<br>"
              "calibration unique avec une grande superposition entre chaque panel<br>"
              "et ce automatiquement pour différentes plage de temps."),       
    
    dict(Task="<b>5.5</b> Mise en place d'un système de réduction des artefacts de calibration", 
         Start='01-06-2021', Finish='11-06-2021', Completion_pct=75, 
         Category="Développement du traitement de données", 
         Note="Le sytème de calibration actuel engendre des oscillations de<br>"
              "température entre les capteurs autour de la valeur à priori idéal.<br>"
              "Pondérer la température de référence de la calibration ne résoud<br>"
              "pas ce problème. Cela vient de la correction à l'ordre 0 initiale."),
              
    dict(Task="<b>5.6</b> Système de visualisation des données de calibration et loi de calibration", 
         Start='31-05-2021', Finish='18-06-2021', Completion_pct=100, 
         Category="Développement d'outil de visualisation", 
         Note="L'ensemble de données de calibration calculées sont représentées<br>"
              "graphiquement en fonction du temps pour tous les capteurs d'une<br>"
              "plage de temps donnée. Les données binaires de tempérautre sont tracées<br>"
              "en fonction des données calibrées. La différence entre les données<br>"
              "ayant subi un autoscale ou non est étudiée en fonction des données<br>"      
              "binaires."), 
              
    dict(Task="<b>5.7</b> Développement d'une sur couche de traitement", 
         Start='15-06-2021', Finish='21-06-2021', Completion_pct=100, 
         Category="Développement du traitement de données", 
         Note="Afin d'afiner d'avantage la calibration, une sur correction à<br>"
              "l'ordre 0 est mise en place sur des plages de temps plus courtes.<br>"
              "L'architecture du code est revue pour plus de modularité."),
              
    dict(Task="<b>5.8</b> Système de d'estimation visuelle d'incertitudes", 
         Start='11-06-2021', Finish='28-06-2021', Completion_pct=60, 
         Category="Développement d'outil de visualisation", 
         Note="La même plage de temps calibrée est représentée avec une échelle<br>"
              "de couleur dont la quantification varie selon plusieurs plannels.<br>"
              "Cela permet de mettre en avant la limite à partir de laquelle la<br>"
              "précision des données peut être remise en cause.<br>"), 
              
    
        dict(Task="<b>6. Mise en place d'un Gantt</b>",
             Start='01-04-2021', Finish='01-04-2021', Completion_pct=0,                 
             Category="Titre", 
             Note=''),
         
    dict(Task="<b>6.1</b> Élaboration d'un Gantt à l'aide de Plotly", 
         Start='18-05-2021', Finish='24-05-2021', Completion_pct=90, 
         Category="Développement d'outil de visualisation", 
         Note="L'ensemble de ce Gantt a été codé."),
    
    dict(Task="<b>6.2</b> Remplissage du Gantt avec l'état actuel du stage", 
         Start='20-05-2021', Finish='21-05-2021', Completion_pct=100, 
         Category="Développement d'outil de visualisation", 
         Note="Reprise de l'ensemble des notes initalement réalisées sur un fichier<br>"
              "txt et estimation du travail à venir."),        
             
    
        dict(Task="<b>7. Réanalyse d'autres jeux de données</b>",
             Start='01-04-2021', Finish='01-04-2021', Completion_pct=0,                 
             Category="Titre", 
             Note=''),
             
    dict(Task="<b>7.1</b> Réanalyse des données d'un mouillage de la Fosse Romanche", 
         Start='21-06-2021', Finish='08-07-2021', Completion_pct=80, 
         Category="Développement du traitement de données", 
         Note="Application du système actuel de calibration à un nouveau jeu de<br>"
              "données."),
              
    dict(Task="<b>7.2</b> Réanalyse des données d'un mouillage en mer Méditerranée", 
         Start='08-07-2021', Finish='16-07-2021', Completion_pct=0, 
         Category="Développement du traitement de données", 
         Note="Application du système actuel de calibration à un nouveau jeu de<br>"
              "données plus sensible."),
        
        
        dict(Task="<b>8. Rédaction du rapport de stage</b>",
             Start='01-04-2021', Finish='01-04-2021', Completion_pct=0,                 
             Category="Titre", 
             Note=''),
    
    dict(Task="<b>8.1</b> Recherche bibliographique", 
         Start='01-04-2021', Finish='21-07-2021', Completion_pct=30, 
         Category="Rédaction de contenu scientifique", 
         Note="Lecture des papiers initiaux de l'offre de stage et ouverture."),
         
    dict(Task="<b>8.2</b> Rédaction du rapport de stage à proprement dit", 
         Start='24-05-2021', Finish='01-08-2021', Completion_pct=20, 
         Category="Rédaction de contenu scientifique", 
         Note="Rédaction du maximum de contenu pour le rapport de stage."),
        
    dict(Task="<b>8.3</b> Prise de contact avec les différents chercheurs mis en jeu", 
         Start='21-06-2021', Finish='21-07-2021', Completion_pct=60, 
         Category="Rédaction de contenu scientifique", 
         Note="Il serait intéressant de rencontrer Hans van Haren ou encore <br>"
              "Raffaele Marino afin de discuter des possibles retomber de ce <br>"
              "jeux de données."),
         
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
fig.write_html("example_pygantt.html")
fig.show()