from helpers import random_koala_fact

__winc_id__ = 'c0dc6e00dfac46aab88296601c32669f'
__human_name__ = 'while'

# This block is only executed if this script is run directly (python main.py)
# 1.
def unique_koala_facts(number):
    unique_facts = []
    start = 0
    while number > start:
        new_fact = random_koala_fact()
        if new_fact not in unique_facts:
            unique_facts.append(new_fact)    
        start = start + 1
    return unique_facts

# 2.
def num_joey_facts():
    unique_joey_facts = []
    joeys = 0 
    fact_counter = 0
    while fact_counter != 10:
        fact = random_koala_fact()
        unique_joey_facts.append(fact)
        fact_counter = unique_joey_facts.count(fact)
    new_list = []
    for only_fact in unique_joey_facts:
        if only_fact not in new_list:
            if 'joey' in only_fact:
                joeys = joeys + 1
            new_list.append(only_fact) 
    return joeys

# 3.
def koala_weight():
    stop = 0
    weight_fact = ''
    while stop != 10:
        fact = random_koala_fact()
        if 'weight' and 'kg' in fact:
            weight_fact = fact
            stop = 10
    weight = int(fact[fact.find('kg')-2:fact.find('kg')])
    return weight

# It is not run if you import this file as a module.
if __name__ == '__main__':
    print(random_koala_fact())
    # 1.
    print(unique_koala_facts(5))
    # 2.
    print(num_joey_facts())
    # 3.
    print(koala_weight())