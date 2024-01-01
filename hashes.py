import mmh3

# Whatever you want here
actor_list = ["Enemy_Bokoblin_Boss_Gold", "Enemy_Bokoblin_Boss_Gold_R"]

def hash(value):
    hash = hex(mmh3.hash(value, signed=False))
    while len(hash) != 10:
        hash = hash[:2] + '0' + hash[2:] # add 0's to pad to the right length, just remove if unwanted
    return hash

# Just bump the value after the < if you want it to be further to the right
def format(actor, prefix='', suffix=''):
    return f"{prefix + actor + suffix:<45}{': ' + hash(prefix + actor + suffix)}"

with open('hashes.txt', 'w') as file:
    for actor in actor_list:
        print(format(actor), file=file)
        print(format(actor, 'PictureBookData.'), file=file)
        print(format(actor, 'PictureBookData.', '.IsNew'), file=file)
        print(format(actor, 'PictureBookData.', '.State'), file=file)
        if "Item_" in actor or "Weapon_" in actor:
            print(format(actor, 'IsGet.'), file=file)
            print(format(actor, 'IsGetAnyway.'), file=file)
        print('', file=file) # add a newline to separate individual actors