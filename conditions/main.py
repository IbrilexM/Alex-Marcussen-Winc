# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action(weather, time_of_day, cow_need_milking, location_cows, season, slurry_tank, grass_status):
    if location_cows == 'pasture' and (time_of_day == 'night' or weather == 'rainy'):
        return 'take cows to cowshed'

    elif cow_need_milking == True:
        if location_cows == 'cowshed':
            return 'milk cows'
        else: 
            return 'take cows to cowshed\nmilk cows\ntake cows back to pasture'

    elif slurry_tank == True:
        if location_cows == 'cowshed' and (weather != 'sunny' or weather != 'windy'):
            return 'fertilize pasture'
        else: 
            return 'take cows to cowshed\nfertilize pasture\ntake cows back to pasture'

    elif grass_status == True and season == 'spring' and weather == 'sunny':
        if location_cows != 'pasture':
            return 'mow grass'
        else:
            'take cows to cowshed\nmow grass\ntake cows back to pasture'

    else:
        return 'wait'

print(farm_action('sunny', 'day', True, 'pasture', 'spring', False, True) + '\n')
print(farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True) + '\n')
print(farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True) + '\n')
print(farm_action('windy', 'night', True, 'cowshed', 'winter', True, True) + '\n')
print(farm_action('bowling', 'night', False, 'cowshed', 'winter', False, True) + '\n')
print(farm_action('sunny', 'night', True, 'cowshed', 'summer', False, True))