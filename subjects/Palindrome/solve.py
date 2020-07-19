import re

# Manacher's algorithm
def palindrom() :
    s_input = input().lower()

    # Strip all whitespace
    s = re.sub('[\s+]', '', s_input)

    # Insert '|' between every char
    s = '|' + '|'.join(a for a in s)  + '|'

    l = len(s)
    P = [0] * l # Array to store palindrome lengths
    R = 0 # Next element to examine
    C = 0 # The largest/left-most palindrome whose right boundary is R-1
    mirror = lambda i : C - (i - C) # Palindrome mirroring i from C
    m = 0 # Walking index
    n = 0 # Walking index

    for i in range(1, l):
        if i > R:
            P[i] = 0
            m = i - 1
            n = i + 1
        else:
            mir = mirror(i)
            if P[mir] < R - i - 1 :
                P[i] = P[mir]
                m = -1 # bypasses the loop below
            else:
                P[i] = R - i
                n = R + 1
                m = i * 2 - n
        while m >= 0 and n < l and s[m] == s[n]:
            P[i] += 1
            m -= 1
            n += 1
        if i + P[i] > R:
            C = i
            R = i + P[i]

    out_l = 0
    c = 0
    for i in range(1, l):
        if out_l < P[i]:
            out_l = P[i]
            c = i
    s = s[c - out_l:c + out_l + 1]
    s = re.sub('[|]', '', s)

    print(s)

if __name__ == "__main__":
    palindrom()
