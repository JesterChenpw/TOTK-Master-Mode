import mmh3

String = 'StringToHash'

print(hex(mmh3.hash(String, signed = False)))