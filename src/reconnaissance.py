from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    l=[]
    s=0
    n=-1
    indice=0
    image = image.binarisation(S)
    image=image.localisation()
    for models in liste_modeles:
        models=models.binarisation(S)
        models=models.localisation()
        models=models.resize(100, 60)
        image = image.resize(100, 60)
        i=image.similitude(models)
        l.append(i)
    for j in l:
        n=n+1
        if j>s:
            s=j
            indice=n
    return indice

