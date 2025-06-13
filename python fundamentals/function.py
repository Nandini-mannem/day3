def food_items(*items):
     print(items)
food_items("idly","dosa","puri")


def stud(name,age,gender,qualification):
    print("name:",name)
    print("age:",age)
    print("gender:",gender)
    print("qualification:",qualification)
stud("nandu",22,"female","cse")


def traveller_bus(passengername,fromplace,toplace,buspartner="abhibus"):
    return f"hello {passengername} greetings from {buspartner}.your journney from {fromplace} to {toplace} is confirmed.happy journey"
print(traveller_bus("prasu","kandukur","ongole"))
