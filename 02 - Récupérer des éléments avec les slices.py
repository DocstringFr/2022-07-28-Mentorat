def test_trois_premiers(liste: list[int]) -> list[int]:
    # Les trois premiers employés ("Maxime", "Martine" et "Christopher") dans une liste trois_premiers.
    # start = 0     [default]
    # stop = 3
    # increment = 1 [default]
    # trois_premiers = liste[start:stop:increment]
    trois_premiers = liste[:3]
    assert trois_premiers == ["Maxime", "Martine", "Christopher"], "La variable trois_premiers ne contient pas la bonne valeur."


def test_trois_derniers(liste: list[int]) -> list[int]:
    # Les trois derniers employés ("Carlos", "Michael" et "Éric") dans une liste trois_derniers.
    # start = -3
    # stop = None  [default]
    # increment = 1 [default]
    # trois_derniers = liste[start:stop:increment]
    trois_derniers = liste[-3:]
    assert trois_derniers == ["Carlos", "Michael", "Eric"], "La variable trois_derniers ne contient pas la bonne valeur."


def test_milieu(liste: list[int]) -> list[int]:
    # Tous les employés sauf le premier et le dernier dans une liste milieu.
    # start = 1
    # stop = -1
    # increment = 1 [default]
    # milieu = liste[start:stop:increment]
    # milieu = liste[1:-1:]
    milieu = liste[1:-1]
    assert milieu == ["Martine", "Christopher", "Carlos", "Michael"], "La variable milieu ne contient pas la bonne valeur."
    
    
def test_premier_dernier(liste: list[int]) -> list[int]:
    # Le premier et le dernier employé dans une liste premier_dernier.
    # start = 0     [default]
    # stop = None   [default]
    # increment = len(liste) - 1
    # premier_dernier = liste[start:stop:increment]
    premier_dernier = liste[::len(liste) - 1]
    assert premier_dernier == ["Maxime", "Eric"], "La variable premier_dernier ne contient pas la bonne valeur."
    
    
if __name__ == "__main__":
    liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]
    
    test_trois_premiers(liste)
    test_trois_derniers(liste)
    test_milieu(liste)
    test_premier_dernier(liste)
