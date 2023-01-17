#!/usr/bin/python3
def best_score(a_dictionary):
    try:
        max_key = max(a_dictionary, key=a_dictionary.get)
    except:
        return None
    else:
        return max_key
