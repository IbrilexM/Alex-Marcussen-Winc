# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
# 1 The language spoken the most in Switzerland is the same as in Spain.
spain_most_spoken_language = 'Spanish'
switzerland_most_spoken_language = 'German'
print(spain_most_spoken_language == switzerland_most_spoken_language)

# 2 The most prevalent religion in Switzerland is the same as in Spain.
religion_spain = 'Roman Catholic'
religion_switzerland = 'Roman Catholic'
print(religion_switzerland == religion_spain)

# 3 The name length of Spain's capital does not equal that of Switzerland.
name_length_cap_spain = len('Madrid')
name_length_cap_switzerland = len('Bern')
print(name_length_cap_spain != name_length_cap_switzerland)

# 4 Switzerland's GDP is greater than Spain's GDP.
gdp_spain = 1714860000000
gdp_switzerland = 590710000000000
print(gdp_spain > gdp_switzerland)

# 5 The population growth is less than 1% in Switzerland and Spain.
pop_growth_spain = 0.03
pop_growth_switzerland = 0.65
print(pop_growth_spain and pop_growth_switzerland < 1)

# 6 At least one of the two countries has a population count of over 10 million.
spain_pop_count = 47260584
switzerland_pop_count = 8453550
print(spain_pop_count | switzerland_pop_count > 10000000)

# 7 Exactly one of the two countries has a population count of over 10 million.
print(spain_pop_count ^ switzerland_pop_count > 10000000)