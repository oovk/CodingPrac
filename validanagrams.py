#two strings are anagrams if they are made from same charater

def anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    freq1 = {}
    freq2 = {}

    for ch in s1:#for each char in s1
        if ch in freq1:#if it is already in hashmap 
            freq1[ch] += 1 #increase count by 1
        else:
            freq1[ch] = 1 #if not set the count to 1
    for ch in s2:
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1
    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
    return True


print(anagrams("nameless", "salesmen"))

""" 
from collections import Counter

def anagrams(s1,s2):Counter maintains the frequency table
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)


def anagrams(s1,s2):Can be done by sorting and string matching
    if len(s1) != len(s2):
        return False
    return Sorted(s1) == Sorted(s2)

 """