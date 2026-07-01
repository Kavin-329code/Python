def number_pattern(n):
    if not isinstance(n,int):
        return 'Argument must be an integer value.'

    if n < 1:
        return 'Argument must be an integer greater than 0.'
    result =[]    
    for i in range (1, n +1):#looping from 1 up to n
        result.append(str(i)) #making any number a string
    return " ".join(result)# joining list items in to one string.
    