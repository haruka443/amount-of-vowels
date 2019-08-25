vowels = 'aeiouy'
amountOfVowels = 0
writing = 'Ala ma kota'
for sign in writing.lower():
    if sign in vowels:
        amountOfVowels += 1
print (f'The amount of vowels in the writing "{writing}" is {amountOfVowels}')
