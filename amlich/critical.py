import ephem
print(ephem)
# find new moon 
print(ephem.next_new_moon('1984/1/18 14:05:10'))

# find full moon
print(ephem.next_full_moon('1984/1/18 14:05:10'))

# find 
print(ephem.next_solstice('1984/1/18 14:05:10'))