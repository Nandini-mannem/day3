# a=5
# if(a<10):
#     print("true")
# else:
#     prit("false")


# rcb won the match=True
# if(True):
#    print("rcb won the match")
# else:
#     print("rcb lost the match")


# a=7
# if(a<10):
#     print("true")

if(True):
    print("won")
else:
    print("lost")


def match_status(team,match_won):
    if(match_won):
        print(f"{team}won the match")
    else:
        print(f"{team}lost the match")
match_status("rcb",True)
match_status("csk",False)
match_status("mi",False)