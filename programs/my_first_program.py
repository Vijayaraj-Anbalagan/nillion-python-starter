from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    
    # Inputs from party1
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))
    
    # Conditional operations based on comparison of my_int1 and my_int2
    if my_int1 > my_int2:
        result = my_int1 * my_int2  # Product if my_int1 is greater
    elif my_int1 < my_int2:
        result = my_int2 - my_int1  # Difference if my_int2 is greater
    else:
        result = my_int1 * my_int1  # Square if they are equal
    
    # Return the result as an output to party1
    return [Output(result, "conditional_output", party1)]
