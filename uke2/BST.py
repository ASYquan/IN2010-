"""
Et binært søketre er et binærtre som oppfyller følgende egenskap
    ⊙ For hver node v så er v.element
        ⊙ større enn alle elementer i venstre subtre, og
        ⊙ mindre enn alle elementer i høyre subtre
⊙ Merk at vi kan si større eller lik dersom vi ønsker å tillate duplikater
⊙ For at vi skal kunne bruke binære søketrær må elementene være sammenlignbare
⊙ Binære trær er spesielt gode når de er balanserte
    ⊙ Dette er tema for neste uke
"""


class Node:
    def __init__(self, x=None):
        self.element = x
        # større enn alle elementer i venstre subtre og mindre enn alle elementer i høyre subtre
        self.left = None
        self.right = None


"""
SAMMENHENG MELLOM BINÆRSØK OG BINÆRE SØKETRÆR
⊙ Idéen bak binærsøk er å halvere søkerommet hver gang vi gjør en sammenligning,
som gir O(log(n)) tid på oppslag
⊙ Det fungerer strålende, men fordrer at vi har et sortert array
⊙ Et problem oppstår når vi trenger en dynamisk struktur
    ⊙ En datastruktur hvor vi stadig legger til og fjerner elementer
⊙ Et binært søketre er en datastruktur
    ⊙ som gjør binærsøk enkelt
    ⊙ støtter effektiv innsetting og sletting
"""


def insert(v, x):
    """
    Kompleksitet O(h), for h: høyde
    Worst case: O(n), for n antall noder
    Worst case, dersom treet er balansert: O(log(n))
    """
    if not v:
        v = Node(x)
    elif x < v.element:
        v.left = insert(v.left, x)
    elif x > v.element:
        v.right = insert(v.right, x)
    return v


def search(v, x):
    if not v:
        return None
    if v.element == x:
        return v
    if x < v.element:
        return search(v.left, x)
    if x > v.element:
        return search(v.right, x)


def find_min(v):
    if not v.left:
        return v
    return find_min(v.left)


def remove(v, x):
    """
    SLETTING
    ⊙ Sletting fra et binærtre er litt vanskeligere enn innsetting og oppslag
        ⊙ men har samme kompleksitet!
    ⊙ Vi må passe på å tette eventuelle ”hull”
    ⊙ Vi skiller mellom tre tilfeller
        ⊙ Noden vi vil slette har ingen barn
        ⊙ Noden vi vil slette har ett barn
        ⊙ Noden vi vil slette har to barn

    """
    if not v:
        return None
    if x < v.element:
        v.left = remove(v.left, x)
        return v
    if x > v.element:
        v.right = remove(v.right, x)
        return v
    if not v.left:
        return v.right
    if not v.right:
        return v.left
    u = find_min(v.right)
    v.element = u.element
    v.right = remove(v.right, u.element)
    return v


def preorder_traversal(v, operation=None):
    """
    v: A node that cannot be null

    """
    res = []
    if v:
        res.append(v.element)
        res = res + preorder_traversal(v.left)
        res = res + preorder_traversal(v.right)
    return res


if __name__ == "__main__":
    root = None
    root = insert(root, 5)
    insert(root, 4)
    insert(root, 6)
    insert(root, 3)
    insert(root, 2)
    insert(root, 1)
    print(find_min(root).element)
    # print(search(root, 4).element)
    remove(root, 1)
    print(preorder_traversal(root))
    remove(root, 5)
    print(preorder_traversal(root))
