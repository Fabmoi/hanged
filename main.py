import random

choix = ["television", "ordinateur", "clavier", "affichage", "souris", "micro", "camera"]
solution = random.choice(choix)


essais = 7
mot_a_trouver = ""
parties_trouvees = ""

for lettres in solution:
    mot_a_trouver = mot_a_trouver + "_ "

print("Bienvenue dans mon jeu du pendu.\nVous avez 7 essais pour trouver la bonne réponse.")
print("Chaque mauvaise réponse vous rapprochera de la mort\nBonne chance!")
print("ASTUCE: Les chiffres et caractères spéciaux ne doivent pas être choisis sous peine de perte d'essais")


while essais > 0:
    print("\nVoici le mot à trouver : ", mot_a_trouver)
    choix = input("Choisissez une lettre : ")[0:1].lower()

    if choix in solution:
        parties_trouvees = parties_trouvees + choix
        print("===> BON CHOIX!")
    else:
        essais = essais - 1
        print("===> ERREUR!\n")
        if essais == 0:
            print("Vous avez perdu. Le mot secret était " + solution + ".")
            print("Pendez-le sur la place publique !!!")
            print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄")
        if essais <= 1:
            print("   \██//      |   ")
        if essais <= 2:
            print("   /██/      \㋡  ")
        if essais <= 3:
            print("  //██\       @乀  ")
        if essais <= 4:
            print(" // ██ \\     / \  ")
        if essais <= 5:
            print("//  ██  \\         ")
        if essais <= 6:
            print("████████████████████")

    mot_a_trouver = ""
    for x in solution:
        if x in parties_trouvees:
            mot_a_trouver += x + " "
        else:
            mot_a_trouver += "_ "

    if "_" not in mot_a_trouver:
        print("Vous avez trouvé, vous pouvez rester en vie.")
        break

print("\n----- Fin de la partie -----")

