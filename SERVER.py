# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 19:26:18 2015

@author: Utilisateur
"""

""" Créer la connexion principale du server qui doit accepter plusieurs client."""

import socket
import select

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(50)

serveur_lance = True
clients_connectes = []
while serveur_lance:
    connexions_demandees, wlist, xlist = select.select([connexion_principale],
        [], [], 0.05)    
    for connexion in connexions_demandees:
        connexion_avec_client, infos_connexion = connexion.accept()
        # On ajoute le socket connecté à la liste des clients
        clients_connectes.append(connexion_avec_client)
        
    clients_a_lire = []
    try:
        clients_a_lire, wlist, xlist = select.select(clients_connectes,
                [], [], 0.05)
    except select.error:
        pass
    else:
        # On parcourt la liste des clients à lire
        for client in clients_a_lire:
            # Client est de type socket
            msg_recu = client.recv(1024)
            # Peut planter si le message contient des caractères spéciaux
            msg_recu = msg_recu.decode()
            
            if (msg_recu.startwith('login:') == True):
                if (msg_recu[6:] == 'admin537774112dcab6de00d4c03e8a34f8e3'):
                    """ SI C'EST UN ADMIN ALORS ON CREE UNE NOUVELLE SAVE DU NOM ENVOYE """                    
                    client.send(b'recu_login')
                    nom_save = client.recv(1024)
                    nom_save = nom_save.decode()
                    try:
                        fichier = open('/data/save/' + nom_save + '.txt', 'w')
                    except:
                        pass
                    nom_save = client.recv(1024).decode()
                    while (nom_save != '/fin'):
                        fichier.write(nom_save)
                        client.send(b'recu')
                        nom_save = client.recv(1024).decode()
                    fichier.close()
                else:
                    """ Test des logins pour voir si ils sont true"""
                    complete = msg_recu[6:]
                    fichier = open('./docs/mot_de_passe.txt', 'r')                    
                    gnl = fichier.readline()
                    i = 0
                    database = []
                    for ligne in fichier:
                        database.append(ligne)
                    while i < len(database):
                        if complete == database[i]:
                            Profil = True
                            i +=1
                        else:
                            i += 1
                    fichier.close()
                    if (Profil == True):
                        client.send(b'connected')
                        """ début du ping pong de données"""
                        nom_save = client.recv(1024)
                        nom_save = nom_save.decode()
                        try:
                            open('/data/save/' + nom_save + '.txt', 'r')
                        except:
                            pass

                        
                    else:
                        client.send(b'error')
                        
                        
                        
            if (msg_recu == "fin"):
                serveur_lance = False

print("Fermeture des connexions")
for client in clients_connectes:
    client.close()

connexion_principale.close()