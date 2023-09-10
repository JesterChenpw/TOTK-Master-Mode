import json

with open('restbl.txt') as rstb_text:
    rstb_txt = rstb_text.readlines()

rstb_dict = {}
rstb_txt = sorted(rstb_txt)

for line in rstb_txt:
    if not line == '\n':
        line = line[:-1]
        entry, size = line.split(' : ')
        #print(entry, size)
        rstb_dict[entry] = int(size)

with open('restbl.json', 'w') as json_file:
    json_file.write(json.dumps(rstb_dict, indent = 2))