import timeit
from nltk.corpus import words
# import nltk
# nltk.download('words')

def english_likeness_score(text):
    english_words = set(words.words())
    text = text.lower()  # Convert text to lowercase for comparison
    word_count = len(text.split())
    english_word_count = sum(1 for word in text.split() if word in english_words)
    
    if word_count == 0:
        return 0.0  # Avoid division by zero

    return english_word_count / word_count

# Example usage:
# text1 = 'hello i am a person'
# text2 = 'hello, i am hjakfhskrfj'
# text3 = 'lasgbldbgsdiufgrs'

# score1 = english_likeness_score(text1)
# score2 = english_likeness_score(text2)
# score3 = english_likeness_score(text3)

# print(f'Score for text1: {score1}')
# print(f'Score for text2: {score2}')
# print(f'Score for text3: {score3}')

print('Timing...')
command = 'english_likeness_score("Pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol hswohila, aoha uva h dvyk jvbsk il thkl vba.")'
print(timeit.timeit(command, number=1000, globals=globals()))
print('Done.')