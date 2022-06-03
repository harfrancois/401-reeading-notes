
import re
from collections import Counter


def most_common_word(string):
    words = re.findall(r'\w+', string)
    most_common = Counter(words).most_common(1)
    print(most_common)


string = 'No. Try not. Do or do not. There is no try.'
most_common_word(string)