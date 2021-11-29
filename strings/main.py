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

# Begin en einde van voornaam
print(player.find('Ruud'))
print(player.find('d'))

first_name = player[:4]


# Lengte achternaam
print(player.find('Gullit'))
print(len(player))

# Achternaam los maken van voornaam
last_name_len = (len(player[5:11]))

# voorletter + achternaam
name_short = player[:1] + '.' + player[4:]

# juigen voornaam speler keer het aantal letter van speler (4x)
chant = ((len(first_name)) * (first_name + '! '))[:-1]

# zeker weten dat de laatste karakter geen spatie is
print(len(chant))
good_chant = (chant[22:] != ' ')