from pprint import pprint
import string

sentence = "He fumbled in the darkness " \
           "looking for the light switch, but when he finally " \
           "found it there was someone already there.Toddlers feeding raccoons"

from collections import defaultdict

word_freq_dict = defaultdict(list)

for letter in string.ascii_lowercase:
    word_freq_dict[letter]

print(word_freq_dict)

for letter in sentence:
    if letter in word_freq_dict: word_freq_dict[letter].append(letter)

# formatted_data = {
#     key: len('#' * word_freq_dict.key), value in word_freq_dict.items()
# }
# pprint(word_freq_dict.items())

