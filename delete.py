import easygui

def Format_Card(card,stats):
    formated = f"{card}\n"
    for stat, score in stats.items():
        formated += f"has a  score of {score} in {stat}\n"
    return f"{formated}\n"
def delete_card():
    def check_if_to_delete(name, card):
        if easygui.buttonbox(f"do you want to delete\n {Format_Card(name, card)}",choices=["yes", "no"]) == "yes":
            card.pop(name)
    target = easygui.enterbox("what card do you want to delete?")
    for name,card in cards.items():
        if target == name:
            check_if_to_delete(name,card)
        for mistake1 in range(1,len(target)):
            test = target[0:mistake1] + target[(mistake1+1):]
            if test == name:
                check_if_to_delete(name,card)
                break
            for mistake2 in range(1,len(name)):
                test1 = name[0:mistake2] + name[mistake2+1:]
                if test == test1:
                    print(f"{test}     {test1}")
                    check_if_to_delete(name,card)
        for mistake2 in range(1,len(name)):
            test = name[0:mistake2] + name[mistake2+1:]
            if target == test:
                check_if_to_delete(name,card)


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
