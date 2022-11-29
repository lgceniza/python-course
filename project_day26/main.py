import pandas as pd

nato_df = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row[0]: row[1] for (_, row) in nato_df.iterrows()}


word_input = input("Enter a word: ")
output = [nato_dict[c.upper()] for c in word_input]
print(output)
