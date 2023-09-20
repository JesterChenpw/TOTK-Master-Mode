import json
import byml
import os

banc_path = r"Banc"

mainfield_files = ['Banc\\MainField\\' + file.replace('.zs', '') for file in os.listdir(banc_path + '\\MainField') if '.byml' in file]
castle_files = ['Banc\\MainField\\Castle\\' + file.replace('.zs', '') for file in os.listdir(banc_path + '\\MainField\\Castle') if '.byml' in file]
cave_files = ['Banc\\MainField\\Cave\\' + file.replace('.zs', '') for file in os.listdir(banc_path + '\\MainField\\Cave') if '.byml' in file]
minusfield_files = ['Banc\\MinusField\\' + file.replace('.zs', '') for file in os.listdir(banc_path + '\\MinusField') if '.byml' in file]

def change_map_file(file, folder, file_path):

    has_changed = False

    with open(file_path, 'rb') as file_base_data:
        map_parser = byml.Byml(file_base_data.read())
        map_data = map_parser.parse()

    if 'Actors' in map_data:

        for actor_data in map_data['Actors']:

            if 'Dynamic' in actor_data:
                if 'EquipmentUser_Attachment_Arrow' in actor_data['Dynamic']:
                    if actor_data['Dynamic']['EquipmentUser_Attachment_Arrow'] in ['Item_Enemy_15', 'FireFruit']:
                        actor_data['Dynamic']['EquipmentUser_Attachment_Arrow'] = 'Item_Ore_B'
                        has_changed = True
                    elif actor_data['Dynamic']['EquipmentUser_Attachment_Arrow'] in ['Item_Enemy_17', 'IceFruit']:
                        actor_data['Dynamic']['EquipmentUser_Attachment_Arrow'] = 'Item_Ore_C'
                        has_changed = True
                    elif actor_data['Dynamic']['EquipmentUser_Attachment_Arrow'] in ['Item_Enemy_16', 'ElectricalFruit']:
                        actor_data['Dynamic']['EquipmentUser_Attachment_Arrow'] = 'Item_Ore_D'
                        has_changed = True

        if has_changed:

            new_folder = os.path.join(folder)
            os.makedirs(new_folder, exist_ok = True)
            writer = byml.Writer(map_data, be = False, version = 7)
            with open(new_folder + '/' + file, 'wb') as new_file:
                writer.write(new_file)

            total_name = new_folder + '/' + file
            print(f'Added {total_name}')

    return has_changed

def change_map_files_of_one_type(list_files):

    files_changed = []

    for file in list_files:

        file_name = str(file).split('\\')[-1]
        folder_name = 'Basket\\'
        if 'MinusField' in file:
            folder_name = folder_name + 'MinusField'
        elif 'Castle' in file:
            folder_name = folder_name + 'MainField\\Castle'
        elif 'Cave' in file:
            folder_name = folder_name + 'MainField\\Cave'
        else:
            folder_name = folder_name + 'MainField'
        
        if change_map_file(file_name, folder_name, banc_path.replace('Banc', '') + file):
            files_changed.append(banc_path.replace('Banc', '') + file)

    return files_changed

def do_all():

    restbl_changes = []

    for file_list in [mainfield_files, castle_files, cave_files, minusfield_files]:

        file_list_changed_files = change_map_files_of_one_type(file_list)

        for file in file_list_changed_files:
            restbl_changes.append(file)

    with open('BasketRestbl.json', 'w') as json_file:
        json_file.write(json.dumps(restbl_changes, indent = 2))

    input('\n\nFinished processing all map files. Press any key to close.')

def main():

    do_all()

if __name__ == '__main__':
    main()