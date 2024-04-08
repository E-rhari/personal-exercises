def spacedPrint(string:str):
    print(string, end="\n\n")


def thematicBreakPrint(string:str, topRule:bool=False, bottomRule:bool=True, breaker="\n-------------------------\n"):
    if(topRule):
        print(breaker)
 
    print(string)

    if(bottomRule):
        print(breaker)