import mmh3 

String = 'PictureBookData.Enemy_Zonau_Robot_Gold.State'

print(hex(mmh3.hash(String, signed = False)))