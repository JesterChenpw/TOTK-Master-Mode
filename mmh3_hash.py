import mmh3

String = 'PictureBookData.Weapon_Sword_016.State'

print(hex(mmh3.hash(String, signed = False)))