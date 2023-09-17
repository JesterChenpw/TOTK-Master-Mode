import json

# AttachmentActorInfo à faire manuellement sur 0.3.7

with open('restbl.json') as json_file:
    json_restbl = json.loads(json_file.read())

with open('totk_strings.json') as json_file:
    strings = json.loads(json_file.read())

def to_rcl():

    edits = ''

    for entry in json_restbl:
        if entry in strings:
            edits = edits + '* ' + entry + ' = ' + str(json_restbl[entry]) + '\n'

        else:
            edits = edits + '+ ' + entry + ' = ' + str(json_restbl[entry]) + '\n'

    with open('master_mode.rcl', 'w') as file:
        file.write(edits)

to_rcl()