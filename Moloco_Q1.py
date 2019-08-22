## Moloco SWE Q1 - Chirag Rao

def equalsWhenOneCharRemoved(x, y):

    len_x = len(x)
    len_y = len(y)

    # Cannot have both strings of same lengths as removal of one character will result in unequal strings
    if len_x == len_y:
        return False

    # Difference in the lengths of two strings should be strictly 1
    if abs(len_x - len_y) > 1:
        return False

    string_1 = None
    string_2 = None
    if len_x > len_y:
        string_1 = x
        string_2 = y
    else:
        string_1 = y
        string_2 = x

    count = 0
    i = 0
    j = 0

    while i < len(string_1) and j < len(string_2):
        char_1 = string_1[i]
        char_2 = string_2[j]

        if char_1 != char_2:
            if count > 0:
                return False
            i = i + 1
            count = count + 1
            #continue

        else:
            i = i + 1
            j = j + 1
            #continue

    return True

## Test cases:

#print(equalsWhenOneCharRemoved("x","y"))
#print(equalsWhenOneCharRemoved("x","XX"))
#print(equalsWhenOneCharRemoved("yy","yx"))
#print(equalsWhenOneCharRemoved("abcd","abxcd"))
#print(equalsWhenOneCharRemoved("xyz","xz"))
#print(equalsWhenOneCharRemoved("","x"))
#print(equalsWhenOneCharRemoved("",""))
