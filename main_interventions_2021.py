# Author : Jérémy RAODSON 
           # SAE PYTHON 
           # InterventionS_2021_Pompiers

# Ce script a pour but de parcourir le fichier csv intervention_2021.csv converti en dictionnaire 
# et de récupèrer les donnés des départetements souhaités dans un premier tableau et les types d'interventions dans un second tableau . 
# Par la suite, l'objectif est de générér pour chaque fonction un fichier html qui va : 
    # Créer un tableau avec comme colonnes les tableaux créer dans chacune des fonctions avec leur valeur respective
    # Crée un diagramme en bâtons avec : 
                #axe des abscisses le premier tableau
                #axe des ordonnées le second tableau 

# En sortie,  On obtient une page web à visulaier avec l'extention Live Server. 

# Toutes les fonctions utilisées pour ce script ont comme modèle le code tp_correction_graphe.py  
#Fonctions définies : 
            #def afficher_fausses_alertes ()
            #def afficher_fuites_de_gaz ()
            #def afficher_accident_de_circulation ()
            #def afficher_accident_voie_publique ()
            #def afficher_secours_en_mer()
            
#  !!!!!! IMPORTANT !!!!!! :  
# Pour générer le site html il y a deux façons : 
#      1er façon    - ouvrir le dossier principal SAE1_PYTHON_RAODSON sur un exploreur de fichier 
#                   - faire clique droit sur le fichier interventions_2021.html
#                   - ouvrir avec : Choisir le navigateur web de son choix 
#      
#      2e façon     - ouvrir le dossier principal SAE1_PYTHON_RAODSON sur Visual Code 
#                   - faire clique droit / (ou ouvrir le fichier) le fichier interventions_2021.html 
#                   - Clique droit + Ouvrir avec Live Server 
#

#########################################################################################



# -*- coding: utf-8 -*-
import csv



def afficher_fausses_alertes(region):

    file_csv = open('interventions_2021.csv', 'r')  
    interventions_2021 = csv.DictReader(file_csv)
    file_html = open('Alertes.html', 'w',encoding='utf-8')

    file_html.write('''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="interventions_2021.css">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.7.1/chart.min.js"></script>
        
        <title>Fausses alertes</title>
    </head>
    <body>
        <p id="Fausses"class="h"> <strong> Fausses alertes (Région Île-de-France) </strong></p>
        <p class="blabla"> Introduction: Étant originaire d'Ile-de-France, je me suis intéressé aux fausses alertes et qu'il m'a semblé intéressant de connaître les interventions des pompiers sur l'année 2021. En effet, j'ai appris par le biais de plusieurs témoignages de mon entourage que les pompiers refusaient d'intervenir dans certaines villes d'Ile-de-France pour cause d'abus.</p>
        
        <table border="1" width="100%">
            <tr>
                <th>Département</th>
                <th>Fausses alertes</th>
            </tr>
''')

    departement = []  #premier tableau pour les axes des abscisses
    fausse_alertes = []#premier tableau pour les axes des ordonnées
    
    for i in interventions_2021:
        if i["Région"] == region:
            departement.append(i["Département"])
            fausse_alertes.append(i["Fausses alertes"])
            
            #Remplir le tableau présent dans la page html "alertes.html" avec les valeurs des deux tableaux "departement" et "fausses_alertes" 
            file_html.write(f'''<tr>
                                <td>{i["Département"]}</td> 
                                <td>{i["Fausses alertes"]}</td>
                            </tr>''')

    
    
    #graphique avec bâtons 
    file_html.write('''</table>
    <div class="chart-container">
        <canvas id="barCanvas" aria-label="chart" role="img"></canvas>
    </div>
    
    <script>
        document.addEventListener("DOMContentLoaded", function () {
            const barCanvas = document.getElementById("barCanvas");
            const barchart = new Chart(barCanvas, {
                type: "bar",
                data: {
                    labels: ''' + str(departement) + ''',
                    datasets: [{
                        label: 'Fausses alertes',
                        data: ''' + str(fausse_alertes) + ''',
                        backgroundColor: ["red", "green", "orange", "yellow", "green"]
                    }]
                }
            });
        });
    </script>
    
    <p class="bas"> Constats: Le Val d'Oise détient le chiffre le plus bas au niveau des fausses alertes. Habitant dans ce département, cela est rassurant. En effet, je pense que ça n'influera pas le choix des pompiers à intervenir dans mon département.</p>
</body>
</html>''')

    file_html.close()
    


def afficher_fuites_de_gaz(region):


    file_csv = open('interventions_2021.csv', 'r')  
    interventions_2021 = csv.DictReader(file_csv)
    file_html = open('Fuites_gaz.html', 'w',encoding='utf-8')

    file_html.write('''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="interventions_2021.css">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.7.1/chart.min.js"></script>
        <title>Odeurs fuite de gaz</title>
    </head>
    <body>
        <h3 id="Fuite"><strong> Odeurs fuite de gaz (Île-de-France) </strong></h3>
        <p class="Odeurs"> Introduction: J'ai donc développé une fonction ( voir code python "def afficher(region)" ) qui permet de connaître selon la région de son choix ( de préférence la région où l'on réside)  et donc son département, les endroits où les fuites de gaz ont été les plus courantes.</p>
        
        <table border="1" width="100%">
            <tr>
                <th>Département</th>
                <th>Fuites de gaz</th>
            </tr>
    ''')
    
    departement = []#deuxième tableau pour les axes des abscisses
    fuite_de_gaz = []#deuxième tableau pour les axes des ordonnées 
    
    for gaz in interventions_2021:
        if gaz["Région"] == region:
            departement.append(gaz["Département"])
            fuite_de_gaz.append(int(gaz["Odeurs - fuites de gaz"]))
           
            #Remplir le tableau présent dans la page html "Fuites_gaz.html" avec les valeurs des deux tableaux "departement" et "fuite_de_gaz" 
            file_html.write(f'''<tr>
                                <td>{gaz["Département"]}</td>
                                <td>{gaz["Odeurs - fuites de gaz"]}</td>
                            </tr>''')
    
    #graphique avec bâtons 
    file_html.write('''</table>
    <div class="chart-container">
        <canvas id="barCanvas2" aria-label="chart" role="img"></canvas>
    </div>
    
    <script>
        document.addEventListener("DOMContentLoaded", function () {
            const barCanvas2 = document.getElementById("barCanvas2");
            const barchart2 = new Chart(barCanvas2, {
                type: "bar",
                data: {
                    labels: ''' + str(departement) + ''',
                    datasets: [{
                        label: 'Fuites de gaz',
                        data: ''' + str(fuite_de_gaz) + ''',
                        backgroundColor: ["black", "red", "orange", "orange", "red"]
                    }]
                }
            });
        });
    </script>
    <p class="gaz"> Conclusion: Les fuites de gaz sont un problème sérieux qui peut avoir des conséquences potentiellement dangereuses. Bien que les infrastructures de gaz récentes soient conçues pour être sûres et efficaces, elles ne sont pas à l’abri des problèmes. Les fuites peuvent être causées par divers facteurs, y compris des défauts de construction, des erreurs d’installation, des dommages accidentels et même l’usure normale.</p>
</body>
</html>''')

    file_html.close()
    

def afficher_accident_de_circulation(region):
    
    file_csv = open('interventions_2021.csv', 'r')  
    interventions_2021 = csv.DictReader(file_csv)
    file_html = open('Accident_de_circulation.html', 'w',encoding='utf-8')
    

    file_html.write('''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="interventions_2021.css">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.7.1/chart.min.js"></script>
        <title>Accidents de circulation</title>
    </head>
    <body>
        <h4 id="Circulation"><strong> Accident de circulation (Île-de-France) </strong></h4>
        <p class="rien">  Introduction: L'Ile - de - France, comme la plus part des grandes régions, à la particularité d'avoir un trafic routier très fréquenté. J'ai donc fait le choix de connaître le département en Ile - de - France qui recense le plus grand nombre d'accident routier .</p>
        
        <table border="1" width="100%">
            <tr>
                <th>Département</th>
                <th>Accident de ciculation</th>
            </tr>
    ''')


    departement=[]#troisième tableau pour les axes des abscisses
    circulation_nombre=[]#troisième tableau pour les axes des ordonnées
    for circulation in interventions_2021:
        if circulation["Région"] == region:
            departement.append(circulation["Département"])
            circulation_nombre.append(circulation["Accidents de circulation"])
            
             #Remplir le tableau présent dans la page html "Accident_de_circulation;html" avec les valeurs des deux tableaux "departement" et "circulations_nombre" 
            file_html.write(f'''<tr>
                                <td>{circulation["Département"]}</td>
                                <td>{circulation["Accidents de circulation"]}</td>
                            </tr>''')

    #graphique avec bâtons 
    file_html.write('''</table>
     <div class="chart-container">
        <canvas id="barCanvas3" aria-label="chart" role="img"></canvas>
    </div>
    
    <script>
        document.addEventListener("DOMContentLoaded", function () {
            const barCanvas3 = document.getElementById("barCanvas3");
            const barchart3 = new Chart(barCanvas3, {
                type: "bar",
                data: {
                    labels: ''' + str(departement) + ''',
                    datasets: [{
                        label: 'Accident de circulation',
                        data: ''' + str(circulation_nombre) + ''',
                        backgroundColor: ["black", "red", "orange", "orange", "red"]
                    }]
                }
            });
        });
    </script>
    <p class="route"> Constats: Je suis assez surpris des résultats. Je ne m'attendais pas à ce que les Yvelines  détienne le nombre le moins  important d'intervention. Je pense particulièrement à l'autoroute A86 qui  est très chargée.<br>
        Paris enregistre le nombre le plus important. Ce qui, dans ce cas, est cohérent ( autoroute A1 .... ).</p>
    
    </body>
</html>''')
    
    file_html.close()
    
 

def afficher_accident_voie_publique(region):

    file_csv = open('interventions_2021.csv', 'r')  
    interventions_2021 = csv.DictReader(file_csv)
    file_html = open('Accidents voie publique.html', 'w',encoding='utf-8')
    
    file_html.write('''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="interventions_2021.css">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.7.1/chart.min.js"></script>
        <title>Accident sur voie publique </title>
    </head>
    <body>
        <h5 id="Accidents"><strong> Accident sur voie publique (Île-de-France) </strong></h5>
        <p class="Publique"> Introduction: Les accidents impliquant des piétons sur la voie publique en Île-de-France sont une préoccupation majeure en matière de sécurité routière.</p>
        <table border="1" width="100%">
            <tr>
                <th>Département</th>
                <th>Accident sur voie publique</th>
            </tr>
    ''')
    
    departement = []#quatrième tableau pour les axes des abscisses
    accident_nombre = []#quadrième tableau pour les axes des abscisses
    
    for accident in interventions_2021:
        if accident["Région"] == region:
            departement.append(accident["Département"])
            accident_nombre.append(int(accident["Accidents sur voie publique"]))
            
            #Remplir le tableau présent dans la page html "Accident voie publique.html" avec les valeurs des deux tableaux "departement" et "accident_nombre" 
            file_html.write(f'''<tr>
                                <td>{accident["Département"]}</td>
                                <td>{accident["Accidents sur voie publique"]}</td>
                            </tr>''')
    #graphique avec bâtons 
    file_html.write('''</table>
    <div class="chart-container">
        <canvas id="barCanvas4" aria-label="chart" role="img"></canvas>
    </div>
    
    <script>
        document.addEventListener("DOMContentLoaded", function () {
            const barCanvas4 = document.getElementById("barCanvas4");
            const barchart4 = new Chart(barCanvas4, {
                type: "bar",
                data: {
                    labels: ''' + str(departement) + ''',
                    datasets: [{
                        label: 'Accident sur voie publique',
                        data: ''' + str(accident_nombre) + ''',
                        backgroundColor: ["black", "red", "green", "red", "red"]
                    }]
                }
            });
        });
    </script>
    <p class="Lois"> Constats: Les accidents sur la voie publique en Île-de-France, et plus particulièrement à Paris, sont en hausse. Cette augmentation est notamment due aux accidents impliquant des trottinettes électriques.</br>Face à cette situation, une loi a été votée pour retirer les trottinettes électriques en libre-service à Paris. Suite à un vote citoyen tenu le dimanche 2 avril 2023, les Parisiens et Parisiennes ont majoritairement voté pour la fin des trottinettes en libre-service.</p>
</body>
</html>''')
    

    file_html.close()
    


def afficher_secours_en_mer():

    file_csv = open('interventions_2021.csv', 'r')  
    interventions_2021 = csv.DictReader(file_csv)
    file_html = open('Secours_en_Mer.html', 'w',encoding='utf-8')
    
    file_html.write('''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="interventions_2021.css">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.7.1/chart.min.js"></script>
        <title>Secours en mer</title>
    </head>
    <body>
        <h6 id="Secours"><strong> SECOURS EN MER   </strong></h6>
        <p class="moi">  Introduction: N'étant pas très bon nageur, je souhaiterais me renseigner sur la localisation des zones à risques dans les plages. Je suppose que les zones à risques sont celles qui ont enregistré le plus d'accidents.</p>
        
        <table border="1" width="100%">
            <tr>
                <th>Département</th>
                <th>Secours en mer</th>
            </tr>
    ''')

    departement=[]#cinquième tableau pour les axes des abscisses
    nombre_secours_en_mer=[]#cinquième tableau pour les axes des ordonnées 
    for s in interventions_2021:
        if int(s["Secours en mer (FDSM)"]) != 0: #Ne prend pas en compte les valeurs qui valent 0 pour faire de la place pour le graphique en bâton.
            departement.append(s["Département"])
            nombre_secours_en_mer.append(int(s["Secours en mer (FDSM)"]))

            #Remplir le tableau présent dans la page html "Secours_en_Mer.html" avec les valeurs des deux tableaux "departement" et "nombre_secours_en_mer" 
            file_html.write(f'''<tr>
                                <td>{s["Département"]}</td>
                                <td>{s["Secours en mer (FDSM)"]}</td>
                            </tr>''')
        else :
            pass
    
    #graphique avec bâtons 
    file_html.write('''</table>
     <div class="chart-container">
        <canvas id="barCanvas5" aria-label="chart" role="img"></canvas>
    </div>
    
    <script>
        document.addEventListener("DOMContentLoaded", function () {
            const barCanvas5 = document.getElementById("barCanvas5");
            const barchart5 = new Chart(barCanvas5, {
                type: "bar",
                data: {
                    labels: ''' + str(departement) + ''',
                    datasets: [{
                        label: 'nombre secours en mer',
                        data: ''' + str(nombre_secours_en_mer) + ''',
                        backgroundColor: ["blue"]
                    }]
                }
            });
        });
    </script>
    <p class="ouf">  Constats: La Vendée est le département qui recense le plus d’accidents. En effet, ce département est proche de l’océan Atlantique. Le danger s’accentue avec la présence des baïnes. <br>En 2023, d’après un article de presse de France Bleu datant d’août 2023, il a été dénombré “quatre décès par noyade en une semaine sur les plages vendéennes”. <br>Par ailleurs, le nombre d’accidents est nettement inférieur pour la Gironde qui est pourtant proche de l’Océan Atlantique. </p>
    
    </body>
</html>''')
    

    file_html.close()
    
#############################################
#### Main #### 
afficher_fausses_alertes("Île-de-France")
afficher_fuites_de_gaz("Île-de-France")
afficher_accident_de_circulation("Île-de-France")
afficher_accident_voie_publique("Île-de-France")
afficher_secours_en_mer()