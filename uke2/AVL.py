"""
⊙ AVL-trær oppfyller de samme egenskapene som ordinære binære søketrær
⊙ I tillegg må de oppfylle følgende egenskap:
    ⊙ for hver node i et AVL-tre, så må høydeforskjellen på venstre og høyre subtre være 
    mindre eller lik 1.
    ⊙ høyde : det lengste av av barna til noden nedover- 
⊙ Denne invarianten må opprettholdes ved innsetting og sletting
    ⊙ (oppslag er helt uforandret)
"""
import trees
from BST import *


class Node:
    """
    ⊙ Ved innsetting og sletting må vi vedlikeholde høydene

    ⊙ Vi antar at vi har en prosedyre Height som:
            ⊙ returnerer −1 dersom den får null som input
            ⊙ returnerer v.height for alle noder v
    """

    def __init__(self, x=None):
        self.element = x
        self.left = None
        self.right = None
        self.h = None


"""
OVERORDNET IDÉ
⊙ Vi bruker metodene for sletting og innsetting fra ordinære binære søketrær
⊙ Etter operasjonen er utført, balanserer vi hver node lokalt fra der operasjonen ble
utført og opp til roten (hvis det er nødvendig)
    ⊙ Vi balanserer når høydeforskjellen mellom venstre og høyre subtre er mer enn 1
⊙ For å balansere en node, vil vi anvende rotasjoner
⊙ Underveis må vi passe på å oppdatere høydene
⊙ Husk at AVL innsetting og sletting bare fungerer på AVL-trær!
    ⊙ Altså kan vi anta at treet ikke har høydeforskjeller større enn 1
    ⊙ Ved én innsetting eller sletting i et AVL-tre vil vi bare forårsake
    en midlertidig høydeforskjell på 2
"""


def LeftRotate(z):
    y = z.right
    T_1 = y.left

    y.left = z
    z.right = T_1

    z.height = 1 + max(trees.height(z.left), trees.height(z.right))
    y.height = 1 + max(trees.height(y.left), trees.height(y.right))

    return y


def RightRotate(z):
    y = z.left
    T_2 = y.right

    y.right = z
    z.left = T_2

    z.height = 1 + max(trees.height(z.left), trees.height(z.right))
    y.height = 1 + max(trees.height(y.left), trees.height(y.right))

    return y


def BalanceFactor(v):
    """
    Forteller hvor tung en retning i treet er.
    0 betyr at treet er balansert.
    Balansefaktor > 0 : VENSTRE TUNGT
    Balansefaktor < 0 : HØYRE TUNGT
    """
    if not v:
        return 0
    return trees.height(v.left) - trees.height(v.right)


def balance(v):
    if BalanceFactor(v) < -1:
        if BalanceFactor(v.right) > 0:
            v.right = RightRotate(v.right)
        return LeftRotate(v)
    if BalanceFactor(v) > 1:
        if BalanceFactor(v.left) < 0:
            v.left = LeftRotate(v.left)
        return RightRotate(v)
    return v


def insert(v, x):
    if not v:
        v = Node(x)
    elif x < v.element:
        v.left = insert(v.left, x)
    elif x > v.element:
        v.right = insert(v.right, x)
    v.height = 1 + max(trees.height(v.left), trees.height(v.right))
    return balance(v)


def preOrder(v):
    if not v:
        return
    print("{0} ".format(v.element), end=" \n")
    # print("\n")
    preOrder(v.left)
    preOrder(v.right)


if __name__ == "__main__":
    root = None
    root = insert(root, 12)
    # insert(root, 45)
    # insert(root, 17)
    # insert(root, 60)
    # insert(root, 40)
    # insert(root, 70)
    # insert(root, 11)
    # insert(root, 5)
    # insert(root, 4)
    # insert(root, 10)
    # print(root.right.element)
    lst = [8, 18, 5, 11, 17, 4, 19, 20]
    for x in lst:
        insert(root, x)
    preOrder(root)
