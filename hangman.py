import random
from random_word import list_of_random_words

# word = 'alfabet'
# list_of_random_words = ['papagal', 'caiet', 'calculator']
word = random.choice(list_of_random_words)

word_list = []
unique_letter = set(word)

for item in word:
    if item != word[0] and item != word[-1]:
        word_list.append('_')
    else:
        word_list.append(item.lower())
        if item in unique_letter:
            unique_letter.remove(item)

print(word_list)
print(' '.join(word_list))
word_len = len(unique_letter)
count_nr = 1
list_already_checked = []
new_word = ' '.join(word_list)

while count_nr <= word_len + 1:
    user_letter = input("Alege o litera: ").lower()

    if user_letter == '':
        print('Introdu o litera: ')
        continue
    if user_letter in word_list:
        print('Litera este deja afisata pe ecran')
    elif user_letter in list_already_checked:
        print(f'Litera a fost deja incercata, literele deja incercate: {" ".join(list_already_checked)}')
    else:
        if user_letter in word:
            print('Litera exista in cuvant')
            for i, value in enumerate(word):
                if user_letter == value:
                    word_list[i] = user_letter
            print(' '.join(word_list))
        else:
            count_nr += 1
        if '_' not in ''.join(word_list):
            print('Ai castigat!')
            break
        elif count_nr > word_len:
            print(f'Ai pierdut! Cuvantul era {word}')
            break
        list_already_checked.append(user_letter)

