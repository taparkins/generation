import math
import random

class Phonology(object):
    def __init__(self, consonants, vowels):
        self.consonants = consonants
        self.vowels = vowels

    def __repr__(self):
        return f'C: {self.consonants} | V: {self.vowels}'

def generate_syllables(phonology, density):
    possibilities = [
        f'{c}{v}'
        for c in phonology.consonants
        for v in phonology.vowels
    ]

    delete_count = math.floor(len(possibilities) * (1 - density))
    for i in range(delete_count):
        del_index = random.randint(0, len(possibilities) - 1)
        del possibilities[del_index]

    return possibilities

def generate_syllabic_word(syllables, length):
    word = ''
    for i in range(length):
        word += syllables[random.randint(0, len(syllables) - 1)]
    return word

def generate_syllabic_words(syllables, count, len_generator):
    vocab = []
    for i in range(count):
        vocab.append(generate_syllabic_word(syllables, len_generator()))
    return vocab
