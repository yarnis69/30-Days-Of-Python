alphabet = 'abcdefg'
shifted_alphabet = 'cdefghi'
translation_table = str.maketrans(alphabet,shifted_alphabet)
print(translation_table) # the unicode ordinal is two higher for each shifted alphabet value
