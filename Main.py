import easygui


def format_card(card, stats):
    formatted = f"{card}\n"
    #add card title
    for stat, score in stats.items():
        formatted += f"has a  score of {score} in {stat}\n"
        #add each stat of card
    return f"{formatted}\n"
    #return the formated card


def check_for_string(question, title):
    output = ""
    while type(output) != str or output in cards or output == "":
        #checking to make sure input is valid
        output = easygui.enterbox(question, title=title)
    return output


def check_for_number(question, title):
    output = easygui.integerbox(
        question, upperbound=25, lowerbound=0, title=title)
    if type(output) != int:
        #checks wheater user pressed cancel making output null
        option_control()
    return output


def check_if_card_right(card, stats):
    while easygui.buttonbox(
            f"Are there any mistakes here?\n\n{format_card(card, stats)}",
            choices=["Yes", "No"], title="stat checker") != "Yes":
        #keep on ask if finished
        fix = easygui.buttonbox(f"which is wrong?",
                                choices=["strength", "speed",
                                         "stealth", "cunning"],
                                title="checking which stat")
        #asking what stat is wrong
        stats[fix] = check_for_number(
            f"what should {card}'s {fix} be?",
            f"checking what {card}'s {fix} should be")
        #asking what it is and changing it
    return stats


def typo_checker(text1, text2):
    if text1 == text2:
        return True
    #testing if already right
    for mistake1 in range(1, len(text1)):
        test = text1[0:mistake1] + text1[(mistake1+1):]
        if test == text2:
            return True
        #testing if one letter off
        for mistake2 in range(1, len(text2)):
            test1 = text2[0:mistake2] + text2[mistake2+1:]
            if test == test1:
                return True
            #testing if 2 letters off
    for mistake2 in range(1, len(text2)):
        test = text2[0:mistake2] + text2[mistake2+1:]
        if text1 == test:
            return True
        #testing if one letter is off


def add_new_card():
    card = {}
    name = check_for_string("what is the monsters name?", "add new card")
    #getting new cards name
    for stat in ["speed", "strength", "cunning", "stealth"]:
        card[stat] = check_for_number(f"what is the {stat} of {name}?",
                                      f"inputing {stat}")
        #getting new cards stats
    cards[name] = check_if_card_right(name, card)
    #checking if filled in right


def search_for_card():
    query = easygui.choicebox("what card are you looking for?",
                              "search for card")
    #getting what card thier after
    for name, card in cards.items():
        if query == name:
            #checking if this is the card
            if easygui.buttonbox(f"are you after {name}?",
                                 choices=["yes", "no"]) == "yes":
                #chechking if this the one they want
                check_if_card_right(name, card)


def delete_card():
    choices = []
    for name, card in cards.items():
        choices.append(name)
        #puts all the card names into a list
    cards.pop(easygui.choicebox("what card do you want to delete?",
                                title="delete card", choices=choices))
    #check which card to remove


def print_all_cards():
    for card, stats in cards.items():
        print(format_card(card, stats))
        #prints all the cards


def option_control():
    options = ["print all cards",
               "search for card", "add new card", "delete card", "exit"]
    #prepare text for option buttons
    action_defs = [print_all_cards,
                   search_for_card, add_new_card, delete_card, exit]
    #line it up with a list of the corresponding functions
    action = easygui.buttonbox("what are you trying to do?", choices=options)
    #asking what they want
    for i in range(0, len(options)):
        if action == options[i]:
            #checking which button I pressed
            action_defs[i]()
            #and running it
    option_control()
    #making it a loop


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
#recording starting cards

option_control()
#starting program
