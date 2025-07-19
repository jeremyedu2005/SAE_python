import csv



def afficher_fausses_alertes(region): 
    departement=[]
    fausse_alertes=[]
    
    
    file= open('interventions_2021.csv', 'r')

    interventions_2021= csv.DictReader(file) # objet qui nous permet de lire le fichier csv
                              # facilement
    for i in interventions_2021:
        if i["Région"]==region: #ici mon dictionnaire se nomme i avec comme clé "Région" lorsque que la [Région] est équivalent  au paramètre region  qui est  dans ce cas la Région "île de france "    lorsque nous faison appelle à la fonction 
            
            departement.append(i['Département']) # cela ajoute dans le tableau "departement" la valeur de la clé du "Département"
            fausse_alertes.append(int(i["Fausses alertes"])) #puis ajoute dans le tableau la valeur numérique des nombres de fausses alertes reçus
            
    
    print(departement)#affiche les departements de la Région  dans le tableau 
    print(fausse_alertes)#affiche les appels reçus dus aux interventions pour les fausses alertes 
    
            

def afficher_gaz(region):
    departement=[]
    Fuite_de_gaz=[]
    
    
    file=open('interventions_2021.csv','r')
    interventions_2021=csv.DictReader(file)

    for f in interventions_2021:
        
        if f ["Région"]==region: #ici mon dictionnaire se nomme f avec comme clé "Région" lorsque que la [Région] est équivalent  au paramètre region  qui est  dans ce cas la Région "île de france "    lorsque nous faison appelle à la fonction 
           
            departement.append(f["Département"]) # cela  ajoute dans le tableau "departement" la valeur de la clé du "Département"
            Fuite_de_gaz.append(int(f["Odeurs - fuites de gaz"])) # puis ajoute dans le tableau la valeur numérique des interventions reçues dus au fuite de gaz 
            
    
    print(departement) #affiche les departements de la Région  dans le tableau 
    print(Fuite_de_gaz)#affiche les appels reçus dus aux interventions pour les fuites de gaz.
    


def afficher_circulation(region):
    
    departement=[]
    circulation=[]
    
    
    file=open('interventions_2021.csv','r')
    interventions_2021=csv.DictReader(file)

    for c in interventions_2021:

        if c["Région"]==region:  #ici mon dictionnaire se nomme c avec comme clé "Région" lorsque que la [Région] est équivalent  au paramètre region  qui est  dans ce cas la Région "île de france "    lorsque nous faison appelle à la fonction 
            
            departement.append(c["Département"]) #cela  ajoute dans le tableau "departement" la valeur de la clé du "Département"
            circulation.append(int(c["Accidents de circulation"])) # puis ajoute dans le tableau le tableau la valeur numérique des interventions reçues dus aux accidents de circulations
            
    
    print(departement)#affiche les departements de la Région  dans le tableau 
    print(circulation)#affiche les appels reçus dus aux interventions pour les accidents de circulation.
    

def afficher_accident_voie_publique(region):

    departement=[]
    accident=[]
    
    file=open('interventions_2021.csv', 'r')
    interventions_2021=csv.DictReader(file)

    for a in interventions_2021:
        if a["Région"]==region:#ici mon dictionnaire se nomme c avec comme clé "Région" lorsque que la [Région] est équivalent  au paramètre region  qui est  dans ce cas la Région "île de france "    lorsque nous faison appelle à la fonction 
            departement.append(a["Département"])  #cela  ajoute dans le tableau "departement" la valeur de la clé du "Département"
            accident.append(int(a["Accidents sur voie publique"])) # puis ajoute dans le tableau le tableau la valeur numérique des interventions reçues dus aux accidents sur la voie publique.
            
    
    print(departement)#affiche les departements de la Région  dans le tableau.
    print(accident)#affiche les appels reçus dus aux interventions pour les accidents sur la voie publique.
    


def afficher_secours_en_mer():
    departement=[]
    nombre_secours_en_mer=[]
    

    file=open('interventions_2021.csv', 'r')
    intervention_2021=csv.DictReader(file)
    for s in intervention_2021:
            if (int(s ["Secours en mer (FDSM)"]))!=0: # Mon dictionnaire se nomme s et ne  prend pas en compte les valeurs qui valent 0 
                departement.append(s["Département"]) #cela  ajoute dans le tableau "departement" la valeur de la clé du "Département"
                nombre_secours_en_mer.append(int(s["Secours en mer (FDSM)"])) #puis ajoute en valeur numérique le nombre d'appel pour les sauvetages en mer 
            else:
                pass

            
    
    print(departement)#affiche les departements  dans le tableau 
    print(nombre_secours_en_mer)#affiche les appels reçus dus aux interventions pour les secours en mers.


    
    
    
    
###### MAIN ######                                 





afficher_fausses_alertes("Île-de-France") #ici je vais appel à la fonction avec comme paramètre "la region Île-de-France"
afficher_gaz("Île-de-France") #ici je vais appel à la fonction avec comme paramètre la région Île-de-France"
afficher_circulation("Île-de-France") #ici je vais appel à la fonction avec comme paramètre "la région Île-de-France"
afficher_accident_voie_publique("Île-de-France") #ici je vais appel à la fonction avec comme paramètre "la région île de france"
afficher_secours_en_mer() 



                       

                                 
                                 
                                 
                   
       
        
            
            
        


    

        
        



        
    
    

   
    


    





    

