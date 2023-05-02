import easygui

def Format_Card(card,stats):
    formated = f"{card}\n"
    for stat, score in stats.items():
        formated += f"has a  score of {score} in {stat}\n"
    return f"{formated}\n"

def print_all_cards():
    for card,stats in  cards.items():
        print(Format_Card(card,stats))

cards = {
    "stoneling": {"strength": 7, "speed": 1, "stealth": 25, "cunning": 15},
    "vexscream": {"strength": 1, "speed": 6, "stealth": 21, "cunning": 19},
    "dawnmrage": {"strength": 5, "speed": 15, "stealth": 18, "cunning": 22},
    "blazegolem": {"strength": 15, "speed": 20, "stealth": 23, "cunning": 6},
    "websnake": {"strength": 7, "speed": 15, "stealth": 10, "cunning": 5},
    "moldvine": {"strength": 21, "speed": 18, "stealth": 14, "cunning": 5},
    "vortexwinf": {"strength": 19, "speed": 13, "stealth": 19, "cunning": 2},
    "rotthing": {"strength": 16, "speed": 7, "stealth": 4, "cunning": 12},
    "froststep": {"strength": 14, "speed": 14, "stealth": 17, "cunning": 4},
    "wispghoul": {"strength": 17, "speed": 19, "stealth": 3, "cunning": 2}
}
print_all_cards()
