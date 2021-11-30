# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1
# Spelers die gescoord hebben
player_0 = 'Ruud Gullit'
player_1 = 'Marco van Basten'

# Minuten waarin in gescoord
goal_0 = 32
goal_1 = 54

# Wanneer wie heeft gescoord
scorers = player_0 + ' ' + str(goal_0) +  ', ' + player_1 + ' ' + str(goal_1)
print(scorers)

# gebruikmaken van de f-string
report = f'{player_0} scored in the {goal_0}nd minute\n{player_1} scored in the {goal_1}th minute'
print(report)

# Part 2
# Volledige naam van speler
player = 'Ruud Gullit'

# Vinden van de spatie
space = player.find(' ')
print(space)

# De voornaam losmaken van achternaam
first_name = player[:space]
print(first_name)

# Achternaam los maken van voornaam
last_name_len = (len(player[space + 1:]))
print(last_name_len)
# voorletter + achternaam
name_short = first_name[:1] + '.' + player[space:]
print(name_short)

# juigen voornaam speler keer het aantal letter van speler (4x)
chant = ((len(first_name)) * (first_name + '! '))[:-1]

# zeker weten dat de laatste karakter geen spatie is
good_chant = (chant[len(chant):] != ' ')
print(good_chant)