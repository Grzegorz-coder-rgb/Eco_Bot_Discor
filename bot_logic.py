import random

recykling = [
    "Rakieta z recyklingu (zabawkowa, oczywiście!)",
    "Organizer na biurko",
    "Zamek lub forteca z kartonów"
]

odpady = {
    "papier": "Rozkłada się od 2 do 6 tygodni.",
    "plastik": "Rozkłada się od 100 do 1000 lat.",
    "szkło": "Nie ulega rozkładowi, ale można je w pełni przetworzyć.",
    "metal": "Rozkłada się od 50 do 200 lat.",
    "resztki jedzenia": "Rozkładają się od kilku dni do kilku tygodni."
}

def recl_pomysl():
    return random.choice(recykling)

def new_pomysl(pomysl):
    recykling.append(pomysl)
    return f"Dodano nowy pomysł do recyklingu: {pomysl}"

def rec_rozklad():
    odpowiedzi = ""
    for odpad, czas in odpady.items():
        odpowiedzi += f"{odpad}: {czas}\n"  # Dodajemy każdą linię do ciągu tekstowego
    return odpowiedzi.strip()  # Usuwamy ewentualny nadmiarowy znak nowej linii na końcu