def challenge_01():
    apples = 1729
    oranges = 42
    papaya = apples
    # 1 apples, papaya = 1729
    # oranges = 42
    apples = apples + oranges
    # 2 apples = 1771
    # papaya = 1729

def challenge_02():
    apples = 1729
    oranges = 42
    bananas = [apples, oranges]
    # 3 apples = 1729
    # oranges = 42
    bananas = [1729, 42]

def challenge_03():
    apples = 1729
    oranges = 42
    bananas = [apples, oranges]

    challenge_03_helper(bananas)

def challenge_03_helper(kiwis):
    mangos = 315
    kiwis.append(mangos)
    # 4 apples = 1729
    # oranges = #42
    # bananas  = [1729, 42, 315] the object is a shared list
    # kiwis is the same list object as bananas, that's what it refers.
    # mangos = 315
    # apples, oranges, and mangos are immutable. 