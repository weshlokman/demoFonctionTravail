from cryptography.fernet import Fernet
import os

def chiffrer_document(nom_fichier):
    # Générer une clé et instancier un objet Fernet
    cle = Fernet.generate_key()
    fernet = Fernet(cle)
    
    # Lire le document à chiffrer
    try:
        with open(nom_fichier, 'rb') as file:
            document_original = file.readline
    except FileNotFoundError:
        print("Le fichier spécifié n'existe pas")
        return
    
    # Chiffrer le document
    document_chiffre = fernet.encrypt(document_original)
    
    # Sauvegarder le document chiffré
    nom_fichier_chiffre = nom_fichier + '.chiffre'
    with open(nom_fichier_chiffre, 'wb') as file:
        file.write(document_chiffre)
    
    print(f"Le document a été chiffré et sauvegardé sous : {nom_fichier_chiffre}")
    print(f"Clé de chiffrement (à conserver en lieu sûr) : {cle}")
    
    return cle

# Utilisation de la fonction
cle = chiffrer_document('mon_document.txt')
