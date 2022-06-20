import math
 
def unique_characters(string):
    checker = 0
    """
    Checker will keep the char that I've already checked.
    OR will help me to keep the char that I've already checked
    a = 1 (0001)
    b = 2 (0010)
    c = 3 (0011) -> (1 << bit_index) -> 0110 
    """

    for index in range(len(string)):
        bit_index = ord(string[index]) - ord('a') 
        ### I will get the index of char at the table. A = 97 and Z = 122, but ord('a') - ord('a') => 0
 
        if ((bit_index) > -1): # Less than -1 is invalid argument
            if ((checker & ((1 << bit_index))) > 0):
                ### It will make a AND (&). Ex. 0001 & 0010 = 0000
                ### That's why I need to compare > 0, because of 0010 & 0010 => 0010 => 2.
                return False

            checker = checker | (1 << bit_index)
            ### It will make a OR (|). Ex. 0001 | 0010 = 0011
    return True

unique_characters("bacci")
