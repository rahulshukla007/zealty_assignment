# Assignment 2:
# Write a python class that is able to return the meaning of an English language word provided to it
# in the terminal. (Use https://dictionaryapi.dev/)

import requests

Word = input('please enter a word ')

#(Use https://dictionaryapi.dev/)
url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/{}".format(Word)

response = requests.get(url)
#print(response)
data = response.json()

try:
    # print(data)
    word = data[0]['word']
    part_of_speech = data[0]['meanings'][1]['partOfSpeech']
    definiation = data[0]['meanings'][1]['definitions'][0]['definition']

    data_list = [word, part_of_speech, definiation]

    #joining the result by dot
    result = '.'.join(data_list)
    print(result)

except Exception as e:
    if e == 0:
        print('word not found')
    else:
        print(e)


