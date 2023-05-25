import easygui


def format_card(card, stats):
    formatted = f"{card}\n"
    for stat, score in stats.items():
        formatted += f"has a  score of {score} in {stat}\n"
    return f"{formatted}\n"


def check_for_string(question, title):
    output = easygui.enterbox(question, title=title)
    if type(output) != str:
        option_control()
    return output


def check_for_number(question):
    output = easygui.integerbox(question, upperbound=25, lowerbound=0)
    if type(output) != int:
        option_control()
    return output


def check_if_card_right(card, stats):
    while easygui.buttonbox(f"Is this right?\n\n{format_card(card, stats)}", choices=["Yes", "No"]) != "Yes":
        fix = easygui.buttonbox(f"which is wrong", choices=["speed", "strength", "cunning", "stealth"])
        stats[fix] = check_for_number(f"what should {card}'s {fix} be")
    return stats


def typo_checker(text1, text2):
    if text1 == text2:
        return True
    for mistake1 in range(1, len(text1)):
        test = text1[0:mistake1] + text1[(mistake1+1):]
        if test == text2:
            return True
        for mistake2 in range(1, len(text2)):
            test1 = text2[0:mistake2] + text2[mistake2+1:]
            if test == test1:
                return True
    for mistake2 in range(1, len(text2)):
        test = text2[0:mistake2] + text2[mistake2+1:]
        if text1 == test:
            return True


def add_new_card():
    card = {}
    name = check_for_string("what is the monsters name", "add new card")
    for stat in ["speed", "strength", "cunning", "stealth"]:
        card[stat] = check_for_number(f"what is the {stat} of {name}")
    cards[name] = check_if_card_right(name, card)


def search_for_card():
    query = check_for_string("what card are you looking for", "search for card")
    for name, card in cards.items():
        if typo_checker(name, query) == True:
            if easygui.buttonbox(f"are you after {name}", choices=["yes", "no"]) == "yes":
                check_if_card_right(name, card)



def delete_card():
    target = check_for_string("what card do you want to delete?", "delete card")
    for name, card in cards.items():
        if typo_checker(target, name) == True:
            if easygui.buttonbox(f"do you want to delete\n {format_card(name, card)}", choices=["yes", "no"]) == "yes":
                cards.pop(name)
                easygui.msgbox(f"{name} deleted")
            option_control()



def print_all_cards():
    for card, stats in cards.items():
        print(format_card(card, stats))


def option_control():
    options = ["delete card", "print all cards", "search for card", "add new card", "exit"]
    action_defs = [delete_card, print_all_cards, search_for_card, add_new_card, exit]
    action = easygui.buttonbox("what are you trying to do?", choices=options)
    for i in range(0, len(options)):
        if action == options[i]:
            action_defs[i]()
    option_control()


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


option_control()
