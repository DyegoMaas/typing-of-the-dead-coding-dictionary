import random

def mix(original_set):
    terms_list = list(original_set)
    random.shuffle(terms_list)
    return set(terms_list)
