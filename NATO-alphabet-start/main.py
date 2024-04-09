import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
dict_1 = {row.letter: row.code for (index, row) in df.iterrows()}
print(dict_1)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
results = [dict_1[letter] for letter in user_input]
print(results)
