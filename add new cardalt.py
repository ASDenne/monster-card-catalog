import easygui
def Format_Card(card,stats):
    formated = f"{card}\n"
    for stat, score in stats.items():
        formated += f"has a  score of {score} in {stat}\n"
    return f"{formated}\n"
def check_if_card_right(card,stats):
    while easygui.buttonbox(f"Is this right?\n\n{Format_Card(card,stats)}",choices=["Yes","No"]) != "Yes":
        fix = easygui.buttonbox(f"which is wrong",choices=["speed","strength","cunning","stealth"])
        stats[fix] = easygui.integerbox(f"what should {card}'s {fix} be",upperbound=25,lowerbound=0)
    return stats

def check_for_output_type(question,format):
    output = ""
    while type(output) != format:
        output = easygui.integerbox(question,upperbound=25,lowerbound=0)
    return output
def Add_new_card():
    card = {}
    name = easygui.enterbox("what is the monsters name")
    for stat in ["speed", "strength", "cunning", "stealth"]:
        card[stat] = check_for_output_type(f"what is the {stat} of {name}",int)
    card = check_if_card_right(name, card)
    cards[name] = card



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
print(type(easygui.integerbox("exit")))
Add_new_card()
