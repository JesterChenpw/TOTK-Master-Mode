import json
from restbl import ResourceSizeTable

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

def to_rcl_updated(version):
    
    edits = ''
    restbl_path = f'Master Mode v1.0\\romfs\\System\\Resource\\ResourceSizeTable.Product.{version}.rsizetable.zs'

    with open(restbl_path, 'rb') as file:
        table = ResourceSizeTable.from_binary(file.read())

    for entry in rstb_dict:
        if table.get_size(entry) is None:
            edits = edits + '+ ' + entry + ' = ' + str(rstb_dict[entry]) + '\n'

        else:
            edits = edits + '* ' + entry + ' = ' + str(rstb_dict[entry]) + '\n'

    with open('master_mode.rcl', 'w') as file:
        file.write(edits)
    
to_rcl_updated('110')