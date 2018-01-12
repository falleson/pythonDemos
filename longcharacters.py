
def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    chars = list(line)
    first = chars[0]
    length = []
    j=1
    for i in range(1,len(chars)):
        if chars[i]==first:
            j+=1
        else:
            length.append(j)
            first=chars[i]
            j=1
    length.append(j) 

    print(max(length))
    

long_repeat("abcccdd")
