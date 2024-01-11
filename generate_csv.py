import mmh3

def hash(value):
    hash = hex(mmh3.hash(value, signed=False))
    while len(hash) != 10:
        hash = hash[:2] + '0' + hash[2:]
    return hash

def create_line(variable_name: str):
    variable_type = 'Enum' if '.State' in variable_name else 'Bool'
    return str(hash(variable_name))[2:] + ';' + variable_type + ';' + variable_name + '\n'
    #return 'deadbeef' + ';' + variable_type + ';' + variable_name + '\n'

def create_lines_stuff(object_name: str):
    string = ''
    if object_name.startswith('Item_') or object_name.startswith('Weapon_'):
        string = string + create_line('IsGet.' + object_name) + create_line('IsGetAnyway.' + object_name)
        if not object_name in ['Item_Enemy_900', 'Item_Enemy_900_R']:
            string = string + create_line('PictureBookData.' + object_name + '.IsNew') + create_line('PictureBookData.' + object_name + '.State')
    elif object_name.startswith('Enemy_'):
        string = string + create_line('PictureBookData.' + object_name + '.IsNew') + create_line('PictureBookData.' + object_name + '.State')

    return string

final_list = [
    "Enemy_Bokoblin_Gold",
    "Enemy_Bokoblin_Gold_R",
    "Enemy_Moriblin_Gold",
    'Enemy_Moriblin_Gold_R',
    'Enemy_Lizalfos_Gold',
    "Enemy_Lizalfos_Gold_R",
    "Enemy_Bokoblin_Boss_Gold",
    "Enemy_Bokoblin_Boss_Gold_R",
    "Enemy_Horablin_Gold",
    "Enemy_Horablin_Gold_R",
    "Enemy_Lynel_Gold",
    "Enemy_Lynel_Gold_R",
    "Enemy_Zonau_Robot_Gold",
    "Enemy_Zonau_Golem_Gold",
    "Enemy_Zonau_BlockMaster_Gold"
    "Enemy_Drake_Lord",
    "Enemy_Giant_Gold",
    "Enemy_Golem_Gold",
    "Enemy_Sandworm_Gold",
    "Enemy_Mogurudo_Gold",
    "Enemy_Mogurudo_Baby_Gold",
    "Weapon_Sword_016",
    "Weapon_Sword_017",
    "Weapon_Sword_018",
    "Weapon_Sword_200",
    "Weapon_Sword_Ganondorf",
    "Weapon_Lsword_016",
    "Weapon_Lsword_017",
    "Weapon_Lsword_018",
    "Weapon_Lsword_200",
    "Weapon_Lsword_300",
    "Weapon_Lsword_666",
    "Weapon_Lsword_Ganondorf",
    "Weapon_Spear_016",
    "Weapon_Spear_017",
    "Weapon_Spear_018",
    "Weapon_Spear_200",
    "Weapon_Spear_Ganondorf",
    "Weapon_Shield_200",
    "Weapon_Bow_200",
    "Item_Enemy_900",
    "Item_Enemy_901",
    "Item_Enemy_902",
    "Item_Enemy_903",
    "Item_Enemy_904",
    "Item_Enemy_905",
    "Item_Enemy_906",
    "Item_Enemy_907",
    "Item_Enemy_908",
    "Item_Enemy_909",
    "Item_Enemy_910",
    "Item_Enemy_911",
    "Item_Enemy_912",
    "Item_Enemy_913",
    "Item_Enemy_914",
    "Item_Enemy_915",
    "Item_Enemy_916",
    "Item_Enemy_917",
    "Item_Ganondorf",
    "Item_Enemy_900_R",
    "Item_Enemy_901_R",
    "Item_Enemy_902_R",
    "Item_Enemy_903_R",
    "Item_Enemy_904_R",
    "Item_Enemy_905_R",
    "Item_Enemy_906_R",
    "Item_Enemy_906_RR",
    "Item_Enemy_906_RRR"
]

final_string = ''
for object in final_list:
    final_string = final_string + create_lines_stuff(object)

with open('for_save_file.csv', 'w') as file:
    file.write(final_string[:-1])