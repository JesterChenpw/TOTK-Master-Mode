import json
import byml
import os

banc_path = r"Banc"

mainfield_files = ['Banc\\MainField\\' + file.replace('.zs', '') for file in os.listdir(banc_path + '\\MainField') if '.byml' in file]
sky_files = ['Banc\\MainField\\Sky\\' + file.replace('.zs', '') for file in os.listdir(banc_path + '\\MainField\\Sky') if '.byml' in file]
castle_files = ['Banc\\MainField\\Castle\\' + file.replace('.zs', '') for file in os.listdir(banc_path + '\\MainField\\Castle') if '.byml' in file]
cave_files = ['Banc\\MainField\\Cave\\' + file.replace('.zs', '') for file in os.listdir(banc_path + '\\MainField\\Cave') if '.byml' in file]
minusfield_files = ['Banc\\MinusField\\' + file.replace('.zs', '') for file in os.listdir(banc_path + '\\MinusField') if '.byml' in file]
dungeon_files = ['Banc\\LargeDungeon\\' + file.replace('.zs', '') for file in os.listdir(banc_path + '\\LargeDungeon') if '.byml' in file]
shrine_files = ['Banc\\SmallDungeon\\' + file.replace('.zs', '') for file in os.listdir(banc_path + '\\SmallDungeon') if '.byml' in file]

rank_up_dict = {
    "Enemy_Zonau_Robot_Junior": "Enemy_Zonau_Robot_Middle",
    "Enemy_Zonau_Robot_Middle": "Enemy_Zonau_Robot_Senior",
    "Enemy_Zonau_Robot_Senior": "Enemy_Zonau_Robot_Dark",
    "Enemy_Zonau_Robot_Dark": "Enemy_Zonau_Robot_Gold",
    "Enemy_Zonau_Golem_Junior": "Enemy_Zonau_Golem_Middle",
    "Enemy_Zonau_Golem_Middle": "Enemy_Zonau_Golem_Senior",
    "Enemy_Zonau_Golem_Senior": "Enemy_Zonau_Golem_Dark",
    "Enemy_Zonau_Golem_Dark": "Enemy_Zonau_Golem_Gold"
}

def change_map_file(file, folder, file_path):

    has_changed = False

    with open(file_path, 'rb') as file_base_data:
        map_parser = byml.Byml(file_base_data.read())
        map_data = map_parser.parse()

    if 'Actors' in map_data:

        for actor_data in map_data['Actors']:

            if 'Gyaml' in actor_data and actor_data['Gyaml'] in rank_up_dict:
                actor_data['Gyaml'] = rank_up_dict[actor_data['Gyaml']]
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
        folder_name = 'ScaleUpOutput\\'
        if 'MinusField' in file:
            folder_name = folder_name + 'MinusField'
        elif 'Sky' in file:
            folder_name = folder_name + 'MainField\\Sky'
        elif 'Castle' in file:
            folder_name = folder_name + 'MainField\\Castle'
        elif 'Cave' in file:
            folder_name = folder_name + 'MainField\\Cave'
        elif 'SmallDungeon' in file:
            folder_name = folder_name + 'SmallDungeon'
        elif 'Dungeon' in file:
            folder_name = folder_name + 'LargeDungeon'
        else:
            folder_name = folder_name + 'MainField'
        
        if change_map_file(file_name, folder_name, banc_path.replace('Banc', '') + file):
            files_changed.append(banc_path.replace('Banc', '') + file)

    return files_changed

def do_all():

    restbl_changes = []

    for file_list in [mainfield_files, sky_files, castle_files, cave_files, minusfield_files, dungeon_files, shrine_files]:

        file_list_changed_files = change_map_files_of_one_type(file_list)

        for file in file_list_changed_files:
            restbl_changes.append(file)

    with open('ScaleUpOutputRestbl.json', 'w') as json_file:
        json_file.write(json.dumps(restbl_changes, indent = 2))

    input('\n\nFinished processing all map files. Press any key to close.')

def main():

    do_all()

if __name__ == '__main__':
    main()