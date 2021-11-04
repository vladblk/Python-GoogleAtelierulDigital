# declararea unei liste care să conțină elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine).
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(my_list)

# afișarea unei alte liste ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)
# asc_list = my_list[0:].sort()
asc_list = sorted(my_list)
print(asc_list)

# afișarea unei liste ordonată descendent (lista inițială trebuie păstrată în aceeași formă)
# desc_list = my_list[0:].reverse()
desc_list = asc_list[::-1]
print(desc_list)

# afișarea numerelor pare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)
even_nums = asc_list[1::2]
print(even_nums)

# afișarea numerelor impare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)
odd_nums = asc_list[::2]
print(odd_nums)

# afișarea elementelor multipli ai lui 3.
res = []
for el in my_list:
    if el % 3 == 0:
        res.append(el)
print(res)

res1 = [el for el in my_list if el % 3 == 0]
print(res1)