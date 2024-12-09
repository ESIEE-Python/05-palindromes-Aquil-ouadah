#### Fonction secondaire


#### Fonction secondaire
"""Ce code permet de vérifier si une chaîne de caractère est un palindrome"""

def ispalindrome(s):
    """Fonction qui vérifie si une chaîne de caractère s est un palindrome"""
    s = s.lower()

    changement_de_var = str.maketrans('éèêëàâäîïôöùûüç', 'eeeeaaaiioouuuc', ' ",?;.:/!\'-')
    s = s.translate(changement_de_var)
    s_inv = s[::-1]
    return s == s_inv

#### Fonction principale


def main():
    """Cette fonction est la fonction principale"""

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
