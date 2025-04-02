def challenge_01():
    # 1 it's a local variable sinc it's assigned insode the function.
    outer_value = 42

    print(f"The value from outside is: {outer_value}")

def challenge_02():
    # 2 it's a global variable. inside the function outer value has no assignment.
    print(f"The value from outside is: {outer_value}")

inner_value = 42

def challenge_03():
    # 3 this causes an unboundlocalerror because the assignment for inner value is after it's called.
    # it's a local variable that hasn't been assigned a value.
    # i moved it above so that it can run correctly
    print(f"The value from outside is: {inner_value}")


def challenge_04():
    # 4 causes another unboundlocalerror like in challenge 3. 
    # outer value is a local variable, also like challenge 3. 
    print(f"The value from outside is: {outer_value}")

    outer_value = 42

outer_value = 1729