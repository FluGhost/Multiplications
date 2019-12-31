# -*- coding: utf-8 -*-

def compteur(nb, max=10):
    i = 0 # Notre compteur
    while i < max:
    # Tant que i est strictement inférieure à max (par defaut 10)
        print(str(i + 1) + " * " + str(nb) + " = " + str((i + 1) * nb))
        # On envoie le message
        i += 1 # On incrémente i de 1 à chaque tour de boucle.

def verifications(reponse):
    if reponse:
    # si il y a une réponse (l'utilisateur pourrait tres bien appuyer sur entree)
        if reponse == "q" or reponse == "Q":
        # si la réponse est "q" alors on arrete le programme
            print("Script by : FluGhost#7007 (on Discord).")
            quit()

        else:
        # si c'est une autre réponse
            try:
                reponse = int(reponse)
                # on essaye de convertir la réponse (string) en nombre
                assert reponse != 0
                # on vérifie que la réponse n'est pas 0
                if type(reponse) == int:
                # si on a réussit
                    compteur(reponse)
                    # on lance la fonction qui va compter

            except ValueError as exeption_out_value_error:
            # si il y a une erreur (ici c'est parce que la personne a écrit un string ex: "io")
                print("########################################")
                print("# Erreur de conversion.                #")
                print("# Cette variable n'a pas le bon type.  #")
                print("# Au lieu d'etre un nombre, c'est un : #")
                print("#", type(reponse),"                       #")
                print("########################################")
                print("Erreur a communiquer au developpeur :")
                print(exeption_out_value_error)
                print("-----------------------------")
                print("Veuillez ecrire des NOMBRES ENTIERS svp.")

            except AssertionError as exeption_out_assertion_error:
            # si la personne a mis 0 on lui dit que c'est pas bien
                print("###################################")
                print("# Erreur de nombre.               #")
                print("# Vous ne pouvez pas mettre de 0. #")
                print("###################################")

            except:
            # si il y a une autre erreur rappeler l'utilisateur
                print("Veuillez ecrire des NOMBRES ENTIERS svp.")

def main():
    reponse_0 = input("Bonjour ! Quelle table voulez vous apprendre aujourd'hui ? (type q for stop)")
    # on demande une première fois avec un bonjour pour rester poli
    verifications(reponse_0)
    # on envoie la réponse dans une fonction qui va effectuer des vérifications et va éxecuter une autre fonction.

    while True:
            reponse_1 = input("Et maintenant ? Quelle table voulez vous apprendre ? (type q for stop)")
            # on redemande
            verifications(reponse_1)

main()