import json

with open('rstbel.txt') as rstb_text:
    rstb_txt = rstb_text.readlines()
    for text in range(len(rstb_txt)):
        rstb_txt[text] = rstb_txt[text][:-1]

with open('restbl.json', 'w') as json_file:
    json_file.write(json.dumps(sorted(rstb_txt), indent = 2))