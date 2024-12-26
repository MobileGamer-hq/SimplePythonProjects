import string
import math

words = [
    "david",
    "daniel",
    "somto",
    "ini",
    "jason",
    "joseph",
    "pineapple"
]

def getLetters():
    letters_count= {}
    letters = string.ascii_lowercase
    count = 0
    for word in letters:
        letters_count[word] = count
        count += 1

    return letters_count

letters_count = getLetters()
final_list = []
def groupWords(_list, index = 0):
    for letter in list(letters_count.keys()):
        letter_words = []
        for word in _list:
            if word[index] is letter:
                letter_words.append(word)

        if len(letter_words) > 1 :
            groupWords(letter_words, index + 1)
        elif len(letter_words) == 1:
            final_list.append(letter_words[0])


groupWords(words, 0)

word = 'joseph'
final_index = []

def searchWords(start = 0, stop = len(final_list), index = 0, matchCount = 0): 
    mid =  math.floor((start + stop) / 2)

    if len(final_list[start:stop]) == 2: 
        if final_list[start] == word:
            final_index.append(start)
        else:
            final_index.append(stop)
        return
    

    if  index < len(final_list[mid]):
        # print(start, stop, mid, index)
        # print(letters_count[final_list[mid][index]], letters_count[word[index]])
        # print(final_list[mid], word[index])
        
        # print(final_list[start:stop])

        if letters_count[final_list[mid][index]] > letters_count[word[index]]:

            searchWords(start, mid)
            
        elif letters_count[final_list[mid][index]] < letters_count[word[index]]:

             searchWords(mid, stop)
             matchCount += 1
           
        else:

            searchWords(start, stop, index + 1, matchCount)
    else:
        final_index.append(mid)
    


print(final_list)    
searchWords()
print(final_index[0])        



