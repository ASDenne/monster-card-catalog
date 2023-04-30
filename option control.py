import easygui
def test_1():
    print("test output 1")
def test_2():
    print("test output 2")
options = ["test input 1","test input 2","exit","a","a","b"]
action_defs = [test_1, test_2, exit]
action = easygui.buttonbox("what are you trying to do?",choices=options)
for i in range(0,len(options)):
    if action == options[i]:
        action_defs[i]()
