import json

# AttachmentActorInfo à faire manuellement sur 0.3.7

with open('restbl.txt') as rstb_text:
    rstb_txt = rstb_text.readlines()

rstb_dict = {}
rstb_txt = sorted(rstb_txt)

for line in rstb_txt:
    if not line == '\n' and not 'RSDB' in line:
        line = line[:-1]
        entry, size = line.split(' : ')
        #print(entry, size)
        rstb_dict[entry] = int(size)

with open('totk_strings.json') as json_file:
    strings = json.loads(json_file.read())

def to_rcl():

    edits = ''

    for entry in rstb_dict:
        if entry in strings:
            edits = edits + '* ' + entry + ' = ' + str(rstb_dict[entry]) + '\n'

        else:
            edits = edits + '+ ' + entry + ' = ' + str(rstb_dict[entry]) + '\n'

    with open('master_mode.rcl', 'w') as file:
        file.write(edits)

to_rcl()