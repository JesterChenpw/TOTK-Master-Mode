import json
import byml
import os

banc_path = r"Banc"

mainfield_files = ['Banc\\MainField\\' + file.replace('.zs', '') for file in os.listdir(banc_path + '\\MainField') if '.byml.zs' in file]
sky_files = ['Banc\\MainField\\Sky\\' + file.replace('.zs', '') for file in os.listdir(banc_path + '\\MainField\\Sky') if '.byml.zs' in file]
castle_files = ['Banc\\MainField\\Castle\\' + file.replace('.zs', '') for file in os.listdir(banc_path + '\\MainField\\Castle') if '.byml.zs' in file]
cave_files = ['Banc\\MainField\\Cave\\' + file.replace('.zs', '') for file in os.listdir(banc_path + '\\MainField\\Cave') if '.byml.zs' in file]
chasm_files = ['Banc\\MainField\\DeepHole\\' + file.replace('.zs', '') for file in os.listdir(banc_path + '\\MainField\\DeepHole') if '.byml.zs' in file]
minusfield_files = ['Banc\\MinusField\\' + file.replace('.zs', '') for file in os.listdir(banc_path + '\\MinusField') if '.byml.zs' in file]

rank_up_dict = {
    "Enemy_Bokoblin_Junior": "Enemy_Bokoblin_Middle",
    "Enemy_Bokoblin_Middle": "Enemy_Bokoblin_Senior",
    "Enemy_Bokoblin_Seinor": "Enemy_Bokoblin_Dark",
    "Enemy_Bokoblin_Dark": "Enemy_Bokoblin_Gold",
    "Enemy_Bokoblin_Armor_Junior": "Enemy_Bokoblin_Armor_Middle",
    "Enemy_Bokoblin_Armor_Middle": "Enemy_Bokoblin_Armor_Senior",
    "Enemy_Bokoblin_Armor_Senior": "Enemy_Bokoblin_Armor_Dark",
    "Enemy_Bokoblin_Armor_Dark": "Enemy_Bokoblin_Armor_Gold",
    "Enemy_Bokoblin_Boss_Junior": "Enemy_Bokoblin_Boss_Middle",
    "Enemy_Bokoblin_Boss_Middle": "Enemy_Bokoblin_Boss_Senior",
    "Enemy_Bokoblin_Boss_Senior": "Enemy_Bokoblin_Boss_Dark",
    "Enemy_Bokoblin_Boss_Dark": "Enemy_Bokoblin_Boss_Gold",
    "Enemy_Bokoblin_Guard_Junior": "Enemy_Bokoblin_Guard_Middle",
    "Enemy_Bokoblin_Guard_Junior_Ambush": "Enemy_Bokoblin_Guard_Middle_Ambush",
    "Enemy_Bokoblin_Guard_Junior_Cliff": "Enemy_Bokoblin_Guard_Middle_Cliff",
    "Enemy_Bokoblin_Guard_Junior_TreeHouseTop": "Enemy_Bokoblin_Guard_Middle_TreeHouseTop",
    "Enemy_Moriblin_Junior": "Enemy_Moriblin_Middle",
    "Enemy_Moriblin_Junior_LongSight": "Enemy_Moriblin_Middle",
    "Enemy_Moriblin_Lookout_Cliff": "Enemy_Moriblin_Middle",
    "Enemy_Moriblin_Middle": "Enemy_Moriblin_Senior",
    "Enemy_Moriblin_Senior": "Enemy_Moriblin_Dark",
    "Enemy_Moriblin_Dark": "Enemy_Moriblin_Gold",
    "Enemy_Lizalfos_Junior": "Enemy_Lizalfos_Middle",
    "Enemy_Lizalfos_Guard_Junior": "Enemy_Lizalfos_Guard_Middle",
    "Enemy_Lizalfos_Guard_Junior_LongVisibility": "Enemy_Lizalfos_Guard_Middle_LongVisibility",
    "Enemy_Lizalfos_Middle": "Enemy_Lizalfos_Senior",
    "Enemy_Lizalfos_Senior": "Enemy_Lizalfos_Dark",
    "Enemy_Lizalfos_Dark": "Enemy_Lizalfos_Gold",
    "Enemy_Lynel_Junior": "Enemy_Lynel_Middle",
    "Enemy_Lynel_Middle": "Enemy_Lynel_Senior",
    "Enemy_Lynel_Senior": "Enemy_Lynel_Dark",
    "Enemy_Lynel_Dark": "Enemy_Lynel_Gold",
    "Enemy_Lynel_Boss": "Enemy_Lynel_Boss_Middle",
    "Enemy_Lynel_Boss_Middle": "Enemy_Lynel_Boss_Senior",
    "Enemy_Lynel_Boss_Senior": "Enemy_Lynel_Boss_Dark",
    "Enemy_Lynel_Boss_Gold": "Enemy_Lynel_Boss_Gold",
    "Enemy_Horablin_Junior": "Enemy_Horablin_Middle",
    "Enemy_Horablin_Guard_Junior": "Enemy_Horablin_Guard_Middle",
    "Enemy_Horablin_Middle": "Enemy_Horablin_Senior",
    "Enemy_Horablin_Senior": "Enemy_Horablin_Dark",
    "Enemy_Horablin_Dark": "Enemy_Horablin_Gold"
}

def change_map_file(file, folder, file_path):

    has_changed = False

    with open(file_path, 'rb') as file_base_data:
        map_parser = byml.Byml(file_base_data.read())
        map_data = map_parser.parse()

    if 'Actors' in map_data:

        for actor_data in map_data['Actors']:

            if actor_data['Gyml'] in rank_up_dict:
                actor_data['Gyml'] = rank_up_dict[actor_data['Gyml']]
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

    for file in list_files:

        file_name = str(file).split('\\')[-1]
        folder_name = 'test\\'
        if len(str(file).split('\\')) == 3:
            folder_name = folder_name + str(file).split('\\')[0] + '\\' + str(file).split('\\')[1]
        else:
            folder_name = folder_name + str(file).split('\\')[0]
        
        change_map_file(file_name, folder_name, banc_path.replace('Banc', '') + file)

change_map_files_of_one_type(mainfield_files)