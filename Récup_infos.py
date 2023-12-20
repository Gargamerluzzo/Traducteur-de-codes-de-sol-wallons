import json 

#On extrait les données du fichier

with open('Total.json') as f: 
    dictionnaire = json.load(f)

while True:
    
    #On demande d'insérer un code sol et on stocke l'info

    code = input("\nEntrer un code de sol indéchiffrable : \n\n")

    #Check pour erreurs ou blagues

    if code not in dictionnaire :
        print("\nLe code recherché n'existe pas. Petit malin ça ne passe pas avec moi mdr")
    
    #Si le code existe, on récupère le sous-dictionnaire qui y est associé et on imprime tout son contenu

    else:
        for k, v in dictionnaire[str(code)].items():
            print("\n" + str(k) + ' ' + str(v))

    #On demande à l'utilisateur s'il veut continuer, et sinon le programme s'interrompt.

    continuer = input("\nEncore ? Tape 'oui' pour continuer, et n'importe quoi d'autre sinon (sauf des gens).\n\n")

    if continuer != "oui":
        break