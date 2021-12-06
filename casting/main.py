# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
# part 1 
leek_price = 2
leek_price = str(leek_price)
print('Leek is ' + leek_price + ' euro per kilo.')

# part 2
word_leek_price = 'Leek 4'
second_price_leek = word_leek_price[word_leek_price.find(' '):][-1:]
sum_total = (int(second_price_leek) * int(leek_price))
print(sum_total)

# part 3
price_broccoli = 2.34
order = 1.6
total_price = round(price_broccoli * order, 2)
order = str(order)
total_price = str(total_price)
print(order + 'kg broccoli costs ' + total_price + 'e')