dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]

def spell_check(word):
    if word in dictionary:
        print("Correct")
    else:
        print("Incorrect")

word_check = input()

spell_check(word_check)
