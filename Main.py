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
def Add_new_card():
    name = easygui.enterbox("what is the monsters name")
    strength = easygui.integerbox(f"what is the strength of {name}",upperbound=25,lowerbound=0)
    speed = easygui.integerbox(f"what is the speed of {name}",upperbound=25,lowerbound=0)
    stealth = easygui.integerbox(f"what is the stealth of {name}",upperbound=25,lowerbound=0)
    cunning = easygui.integerbox(f"what is the cunning of {name}",upperbound=25,lowerbound=0)
    card = {"strength":strength,"speed":speed,"stealth":stealth,"cunning":cunning}
    card = check_if_card_right(name, card)
    cards[name] = card
def search_for_card():
    def check_if_card(name):
        if easygui.buttonbox(f"are you after {name}",choices=["yes","no"]) == "yes":
            check_if_card_right(name,card)
    query = easygui.enterbox("what card are you looking for")
    for name,card in cards.items():
        if query == name:
            check_if_card_right(name,card)
        for mistake1 in range(1,len(query)):
            test = query[0:mistake1] + query[(mistake1+1):]
            if test == name:
                check_if_card(name)
                break
            for mistake2 in range(1,len(name)):
                test1 = name[0:mistake2] + name[mistake2+1:]
                if test == test1:
                    print(f"{test}     {test1}")
                    check_if_card(name)
        for mistake2 in range(1,len(name)):
            test = name[0:mistake2] + name[mistake2+1:]
            if query == test:
                check_if_card(name)
def delete_card():
    def check_if_to_delete(name, card):

        if easygui.buttonbox(f"do you want to delete\n {Format_Card(name, card)}",choices=["yes", "no"]) == "yes":
            cards.pop(name)
        global message
        message = f"{name} deleted"
    global message
    target = easygui.enterbox("what card do you want to delete?")
    message = f"no card called {target} found"
    for name,card in cards.items():
        if target == name:
            check_if_to_delete(name,card)
            break
        else:
            for mistake1 in range(1,len(target)):
                test = target[0:mistake1] + target[(mistake1+1):]
                if test == name:
                    check_if_to_delete(name,card)
                    break
                for mistake2 in range(1,len(name)):
                    test1 = name[0:mistake2] + name[mistake2+1:]
                    if test == test1:
                        check_if_to_delete(name,card)
                        break
            for mistake2 in range(1,len(name)):
                test = name[0:mistake2] + name[mistake2+1:]
                if target == test:
                    check_if_to_delete(name,card)
                    break
    easygui.msgbox(message)
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
while True:
    options = ["delete card","print all cards","search for card","add new card","exit"]
    action_defs = [delete_card, print_all_cards ,search_for_card ,Add_new_card , exit]
    action = easygui.buttonbox("what are you trying to do?",choices=options)
    for i in range(0,len(options)):
        if action == options[i]:
            action_defs[i]()
