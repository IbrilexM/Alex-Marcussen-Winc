from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = 'c545bc87620d4ced81cbddb8a90b4a51'
__human_name__ = 'for'


""" Write your functions here. """
# 1.
def shortest_names(country_names):
    list_shortest_names = []
    longest_name = 999
    # pak de minst lange naam van een land uit een lijst
    for country in country_names:
        if len(country) <= longest_name:
            longest_name = len(country)
    # zet alle minst lange namen van landen in een andere lijst 
    for country in country_names:
        if len(country) <= longest_name:
            list_shortest_names.append(country)
            longest_name = len(country)
    print(list_shortest_names)

# 2.
def most_vowels(list_of_longest_names):
    list_of_longest_names.sort(key=len, reverse=True)
    print(list_of_longest_names[:3])

# 3.
def alphabet_set(all_countries):
    country_list = []
    check_letter_list =['a', 'b', 'c', 'd', 'e', 'f', 'g',
                        'h', 'i', 'j', 'k', 'l', 'm', 'n',
                        'o', 'p', 'q', 'r', 's', 't', 'u',
                        'v', 'w', 'x', 'y', 'z']
    letter_list = []
    for country in all_countries:
        for letter in country:
            letter.lower()
            if letter in check_letter_list:
                if letter not in letter_list:
                    letter_list.append(letter)
                    letter_list.sort()
                    if country not in country_list:
                        newest_country = country
                        country_list.append(newest_country)
    print(country_list)
        

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == '__main__':
    countries = get_countries()

    """ Write the calls to your functions here. """
    # 1.
    shortest_names(countries)
    # 2. 
    most_vowels(countries)
    # 3.
    alphabet_set(countries)