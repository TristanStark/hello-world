# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 12:08:26 2016

@author: rety_t
"""

from getpass import getpass  #♣get mdp
import hashlib   #hash md5 mdp
import os    #os.cls
import socket   #communication inter client
from threading import Thread   #thread reçu et envoyé
from time import strftime   #get time  for the time out


"""module de connexion au réseau """ 


get_profil = input("Do you have a profil yet? ")

if (get_profil.lower() == 'yes' or get_profil.lower() == 'oui'):
    login = input('Login ')
    mdp = getpass('Tapez votre mot de passe(il ne s\'affichera pas): ')
    mdp = mdp.encode()
    mdp = hashlib.md5(mdp)
    complete = login + mdp.hexdigest()
    
    """ Envoyer le mot complete au réseau du serveur afin de pouvoir tester le truc """
    
elif (get_profil.lower() == 'no' or get_profil.lower() == 'non'):
    login2 = input('Login:   ')
    mot_de_passe2 = getpass("Tapez votre mot de passe :    ")
    os.system('cls')
    print('Votre profil a bien été créé')
    mot_de_passe2 = mot_de_passe2.encode()
    mot_de_passe2 = hashlib.md5(mot_de_passe2)
    complete = login2 + mot_de_passe2.hexdigest()

