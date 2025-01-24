import tkinter as tk
from tkinter import ttk
import os
import csv
import uuid
import random
    
# Determine the path to the script's directory
script_directory = os.path.dirname(os.path.realpath(__file__))

# Create the main window
root = tk.Tk()
root.title("CEO Automatic Creator")

# Create a label for the name input
name_label = tk.Label(root, text="Enter character name like (yue_jiu):")
name_label.pack()

# Create an entry widget for name input
name_entry = tk.Entry(root)
name_entry.pack()

option_label = tk.Label(root, text="Type to create, choose Class, and Gender:")
option_label.pack()

# Create a label for the dropdown
dropdown_label = tk.Label(root, text="Select an option:")
dropdown_label.pack()

# Create a variable to store the selected option
selected_option = tk.StringVar()

 #Create a dropdown (OptionMenu) with options
options = ["armour", "title", "unique"]
option_menu = ttk.OptionMenu(root, selected_option, options[0], *options)
option_menu.pack()





elements = ["metal", "wood", "earth", "fire", "water"]
element_var = tk.StringVar()
element_frame = ttk.Frame(root)
element_dropdown = ttk.OptionMenu(root, element_var, elements[0], *elements)
element_dropdown.pack()


gender = ["male", "female"]
gender_var = tk.StringVar()
gender_frame = ttk.Frame(root)
gender_dropdown = ttk.OptionMenu(root, gender_var, gender[0], *gender)
gender_dropdown.pack()

# Create a list to store names
name_list = []

# Function to handle adding a name
def add_name():
    name = name_entry.get()
    if name:
        if selected_option.get() == "unique":
            name_list.append((name, "armour", element_var.get(), gender_var.get()))
            name_list.append((name, "title", element_var.get(), gender_var.get()))
        else:
            name_list.append((name, selected_option.get(), element_var.get(), gender_var.get()))
        update_name_display()
        name_entry.delete(0, tk.END)
# Function to update the displayed names
# Function to update the displayed names
# Function to handle removing the last added name
def remove_last_name():
    if name_list:
        name_list.pop()
        update_name_display()

# Function to update the displayed names
def update_name_display():
    name_display.config(state=tk.NORMAL)
    name_display.delete(1.0, tk.END)
    for name, option, element, gender in name_list:
        name_display.insert(tk.END, f"{name} - {option} - {element} - {gender}\n")
    
    # Count the number of lines in the widget






# Create a button to add a name, option, and element
add_name_button = tk.Button(root, text="Add Name", command=add_name)
add_name_button.pack()


# Create a text widget to display the names, options, and elements
name_display = tk.Text(root, height=5, width=30)
name_display.config(state=tk.DISABLED)
name_display.pack()

remove_name_button = tk.Button(root, text="Remove Last Name", command=remove_last_name)
remove_name_button.pack()

# Create a label for directory input
dir_label = tk.Label(root, text="Enter a directory:")
dir_label.pack()

# Create an entry widget for directory input
dir_entry = tk.Entry(root)
dir_entry.pack()

# Function to check if the directory file exists and fill the directory line
def check_and_fill_directory():
    file_path = os.path.join(script_directory, "directory.txt")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            directory = file.read().strip()
            if os.path.isdir(directory):
                dir_entry.insert(0, directory)

# Create a button to check and fill the directory
fill_dir_button = tk.Button(root, text="Check and Fill Directory", command=check_and_fill_directory)
fill_dir_button.pack()



# Function to handle running the application
def run_application():
    # Your code to process the entered data and the directory goes here
    # You can access the name_list and the directory using name_list and dir_entry.get()
    directory = dir_entry.get()
    if not os.path.exists(directory):
        # Handle the case where the specified directory does not exist
        return
    
    # Create a CSV file in the specified directory
    ceo_csv_path = os.path.join(directory, "ceos.csv")
    
    # ORIGINAL POINT START WITH CEOS
    with open(ceo_csv_path, mode='w', newline='') as csv_file:
        fieldnames = ['UUID', 'key', 'exists_in_location', 'category', 'priority', 'turns_to_expire', 'point_change_per_turn_if_inactive', 'point_change_per_turn_while_active', 'provides_scripted_permissions_on_spawn', 'can_be_looted_post_battle', 'inheritance_chance', 'can_be_traded_in_diplomacy', 'can_be_stolen', 'rarity', 'can_be_unequipped', 'can_be_transferred_if_equipped', 'cannot_reequip_until_next_round_if_unequipped', 'equipped_in_location', 'point_change_per_turn_while_equipped']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()
        for name, option, element, gender in name_list:
            if option == "armour":
                option = "3k_main_ceo_category_ancillary_armour"
                key_name = "3k_main_ancilliary_armour_" + name + "_armour_unique"
                rarity = "unique"
            if option == "weapon":
                option = "3k_main_ceo_category_ancillary_weapon"
                key_name = "3k_main_ancillary_weapon_" + name + "_unique"
                rarity = "unique"
            if option == "title":
                option = "3k_main_ceo_category_career"
                key_name = "3k_main_ceo_career_historical_" + name
                rarity = "common"

            # UUID	key	exists_in_location	category	priority	turns_to_expire	point_change_per_turn_if_inactive	point_change_per_turn_while_active	provides_scripted_permissions_on_spawn	can_be_looted_post_battle	inheritance_chance	can_be_traded_in_diplomacy	can_be_stolen	rarity	can_be_unequipped	can_be_transferred_if_equipped	cannot_reequip_until_next_round_if_unequipped	equipped_in_location	point_change_per_turn_while_equipped
            generated_uuid = uuid.uuid4()
            strUUID = '{' + str(generated_uuid) + '}'


            writer.writerow({'UUID': strUUID, 'key': key_name, 'exists_in_location': "character_ceo_manager", 'category': option, 'priority': 1, 'turns_to_expire': 0, 'point_change_per_turn_if_inactive': 0, 'point_change_per_turn_while_active': 0, 'provides_scripted_permissions_on_spawn': "", 'can_be_looted_post_battle': "false", 'inheritance_chance': 0, 'can_be_traded_in_diplomacy': "false", 'can_be_stolen': "false", 'rarity': rarity, 'can_be_unequipped': "false", 'can_be_transferred_if_equipped': "true", 'cannot_reequip_until_next_round_if_unequipped': "true", 'equipped_in_location': "character_equipment", 'point_change_per_turn_while_equipped': 0})
    
    
    ## start with armour - very simple just a lot of tables.
    

        # Start with ceo_groups able to go multiple directory
        ceo_group_csv_path = os.path.join(directory, "ceo_groups.csv")
        with open(ceo_group_csv_path, mode='w', newline='') as csv_file:
            fieldnames = ['key']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for name, option, element, gender in name_list:
                if option == "armour":
                    key_name = '3k_main_ceo_group_ancillary_armour_character_specific_' + name 
                    writer.writerow({'key': key_name})
            


        ## finish off ceo_group
        ceo_group_ceos_csv_path = os.path.join(directory, "ceo_group_ceos.csv")

        with open(ceo_group_ceos_csv_path, mode='w', newline='') as csv_file:
            fieldnames = ['ceo_group', 'ceo', 'trigger_weighting', 'auto_id']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for name, option, element, gender in name_list:
                if option == "armour":
                    ceo_group_name = '3k_main_ceo_group_ancillary_armour_character_specific_' + name 
                    ceo_name = "3k_main_ancilliary_armour_" + name + "_armour_unique"
                    writer.writerow({'ceo_group': ceo_group_name, 'ceo': ceo_name, 'trigger_weighting': 0.1, 'auto_id': random.randint(100000, 9999999)})
                    writer.writerow({'ceo_group': '3k_main_ceo_group_ancillary_armour_type_character_specific', 'ceo': ceo_name, 'trigger_weighting': 0.1, 'auto_id': random.randint(100000, 9999999)})
                    writer.writerow({'ceo_group': '3k_main_ceo_group_ancillary_armour_character_all', 'ceo': ceo_name, 'trigger_weighting': 0.1, 'auto_id': random.randint(100000, 9999999)})
                if option == "title":
                    ceo_name = "3k_main_ceo_career_historical_" + name
                    writer.writerow({'ceo_group': '3k_main_ceo_group_career_all', 'ceo': ceo_name, 'trigger_weighting': 1, 'auto_id': random.randint(100000, 9999999)})

        ##ceo_permissions

        ceo_permissions_csv_path = os.path.join(directory, "ceo_permissions.csv")

        with open(ceo_permissions_csv_path, mode='w', newline='') as csv_file:
            fieldnames = ['key']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for name, option, element, gender in name_list:
                if option == "armour":
                    perm_key = "3k_main_ceo_permissions_ancillary_armour_character_specific_" + name 
                    writer.writerow({'key': perm_key})


        ##ceo_permissions_groups

        ceo_permissions_groups_csv_path = os.path.join(directory, "ceo_permissions_groups.csv")
        with open(ceo_permissions_groups_csv_path, mode='w', newline='') as csv_file:
            fieldnames = ['permissions', 'group', 'point_gain_enabled_override', 'point_gain_disabled_override', 'state_active_override', 'state_inactive_override', 'auto_id']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for name, option, element, gender in name_list:
                if option == "armour":
                    perm_key = "3k_main_ceo_permissions_ancillary_armour_character_specific_" + name 
                    key_name = '3k_main_ceo_group_ancillary_armour_character_specific_' + name 
                    writer.writerow({'permissions': perm_key, 'group': key_name, 'point_gain_enabled_override': "true", 'point_gain_disabled_override': "false", 'state_active_override': "true", 'state_inactive_override': "false", 'auto_id': random.randint(100000, 9999999)})

        ## ceo_scripted_permissions
        ceo_scripted_permissions_csv_path = os.path.join(directory, "ceo_scripted_permissions.csv")

        with open(ceo_scripted_permissions_csv_path, mode='w', newline='') as csv_file:
            fieldnames = ['key', 'exists_in_and_provides_permission_to_location']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for name, option, element, gender in name_list:
                if option == "armour":
                    perm_key = "3k_main_ceo_permissions_ancillary_armour_character_specific_" + name 
                    writer.writerow({'key': perm_key, 'exists_in_and_provides_permission_to_location': "character_ceo_manager"})

        ##ceo_scripted_permissions_to_permissions
        ceo_scripted_permissions_to_permissions_csv_path = os.path.join(directory, "ceo_scripted_permissions_to_permissions.csv")

        with open(ceo_scripted_permissions_to_permissions_csv_path, mode='w', newline='') as csv_file:
            fieldnames = ['scripted_permissions', 'permissions', 'auto_id']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for name, option, element, gender in name_list:
                if option == "armour":
                    perm_key = "3k_main_ceo_permissions_ancillary_armour_character_specific_" + name 
                    writer.writerow({'scripted_permissions': perm_key, 'permissions': perm_key, 'auto_id': random.randint(100000, 9999999)})


        ##ceo_initial_data_stages

        ceo_initial_data_stages_path = os.path.join(directory, "ceo_initial_data_stages.csv")

        with open(ceo_initial_data_stages_path, mode='w', newline='') as csv_file:
            fieldnames = ['key']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for name, option, element, gender in name_list:
                if option == "armour":
                    initial_data_key = "3k_main_ceo_initial_data_character_historical_" + name + "_ancillaries" 
                    
                    writer.writerow({'key': initial_data_key})
                if option == "title":
                    initial_career_key = "3k_main_ceo_initial_data_stage_character_traits_historical_" + name
                    writer.writerow({'key': initial_career_key})

        ##ceo_initial_data_scripted_permissions
        ceo_initial_data_scripted_permissions_path = os.path.join(directory, "ceo_initial_data_scripted_permissions.csv")

        with open(ceo_initial_data_scripted_permissions_path, mode='w', newline='') as csv_file:
            fieldnames = ['initial_data_stage', 'scripted_permissions', 'auto_id']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for name, option, element, gender in name_list:
                if option == "armour":
                    initial_data_key = "3k_main_ceo_initial_data_character_historical_" + name + "_ancillaries" 
                    perm_key = "3k_main_ceo_permissions_ancillary_armour_character_specific_" + name 
                    writer.writerow({'initial_data_stage': initial_data_key, 'scripted_permissions' : perm_key, 'auto_id': random.randint(100000, 9999999)})
                    if element == "fire":
                        writer.writerow({'initial_data_stage': initial_data_key, 'scripted_permissions' : "3k_main_ceo_permissions_ancillary_weapon_character_spear_two_handed_long_enable", 'auto_id': random.randint(100000, 9999999)})
                        writer.writerow({'initial_data_stage': initial_data_key, 'scripted_permissions' : "3k_main_ceo_permissions_ancillary_weapon_character_axe_two_handed_enable", 'auto_id': random.randint(100000, 9999999)})
                        writer.writerow({'initial_data_stage': initial_data_key, 'scripted_permissions' : "3k_main_ceo_permissions_ancillary_weapon_character_spear_two_handed_enable", 'auto_id': random.randint(100000, 9999999)})
                    if element == "earth":
                        writer.writerow({'initial_data_stage': initial_data_key, 'scripted_permissions' : "3k_main_ceo_permissions_ancillary_weapon_character_sword_one_handed_enable", 'auto_id': random.randint(100000, 9999999)})
                        writer.writerow({'initial_data_stage': initial_data_key, 'scripted_permissions' : "3k_main_ceo_permissions_ancillary_weapon_character_axe_one_handed_enable", 'auto_id': random.randint(100000, 9999999)})
                        writer.writerow({'initial_data_stage': initial_data_key, 'scripted_permissions' : "3k_main_ceo_permissions_ancillary_weapon_character_sword_dual_enable", 'auto_id': random.randint(100000, 9999999)})
                        writer.writerow({'initial_data_stage': initial_data_key, 'scripted_permissions' : "3k_main_ceo_permissions_ancillary_weapon_character_axe_dual_enable", 'auto_id': random.randint(100000, 9999999)})
                    if element == "water":
                        writer.writerow({'initial_data_stage': initial_data_key, 'scripted_permissions' : "3k_main_ceo_permissions_ancillary_weapon_character_sword_one_handed_enable", 'auto_id': random.randint(100000, 9999999)})
                    if element == "wood":
                        writer.writerow({'initial_data_stage': initial_data_key, 'scripted_permissions' : "3k_ytr_ceo_permissions_ancillary_weapon_character_mace_two_handed_enable", 'auto_id': random.randint(100000, 9999999)})
                        writer.writerow({'initial_data_stage': initial_data_key, 'scripted_permissions' : "3k_ytr_ceo_permissions_ancillary_weapon_character_staff_two_handed_enable", 'auto_id': random.randint(100000, 9999999)})
                        writer.writerow({'initial_data_stage': initial_data_key, 'scripted_permissions' : "3k_main_ceo_permissions_ancillary_weapon_character_spear_two_handed_enable", 'auto_id': random.randint(100000, 9999999)})
                        writer.writerow({'initial_data_stage': initial_data_key, 'scripted_permissions' : "3k_main_ceo_permissions_ancillary_weapon_character_axe_two_handed_enable", 'auto_id': random.randint(100000, 9999999)})
                        writer.writerow({'initial_data_stage': initial_data_key, 'scripted_permissions' : "3k_main_ceo_permissions_ancillary_weapon_character_spear_two_handed_long_enable", 'auto_id': random.randint(100000, 9999999)})
                    if element == "metal":
                        writer.writerow({'initial_data_stage': initial_data_key, 'scripted_permissions' : "3k_main_ceo_permissions_ancillary_weapon_character_axe_dual_enable", 'auto_id': random.randint(100000, 9999999)})
                        writer.writerow({'initial_data_stage': initial_data_key, 'scripted_permissions' : "3k_main_ceo_permissions_ancillary_weapon_character_axe_one_handed_enable", 'auto_id': random.randint(100000, 9999999)})
                        writer.writerow({'initial_data_stage': initial_data_key, 'scripted_permissions' : "3k_ytr_ceo_permissions_ancillary_weapon_character_mace_dual_enable", 'auto_id': random.randint(100000, 9999999)})
                        writer.writerow({'initial_data_stage': initial_data_key, 'scripted_permissions' : "3k_main_ceo_permissions_ancillary_weapon_character_sword_dual_enable", 'auto_id': random.randint(100000, 9999999)})
                        writer.writerow({'initial_data_stage': initial_data_key, 'scripted_permissions' : "3k_main_ceo_permissions_ancillary_weapon_character_sword_one_handed_enable", 'auto_id': random.randint(100000, 9999999)})
                            
            ##ceo_initial_data_active_ceos

            ceo_initial_data_active_ceos_path = os.path.join(directory, "ceo_initial_data_active_ceos.csv")

            with open(ceo_initial_data_active_ceos_path, mode='w', newline='') as csv_file:
                fieldnames = ['initial_data_stage', 'active_ceo', 'starting_points_delta', 'auto_id']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for name, option, element, gender in name_list:
                    if option == "armour":
                        initial_data_key = "3k_main_ceo_initial_data_character_historical_" + name + "_ancillaries" 
                        key_name = "3k_main_ancilliary_armour_" + name + "_armour_unique"
                        writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': key_name, 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                        if element == "wood":
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_main_ancillary_weapon_hook_sickle_sabre_common", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_main_ancillary_weapon_two_handed_axe_common", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_main_ancillary_weapon_two_handed_spear_common", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_main_ancillary_weapon_halberd_common", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_ytr_ancillary_weapon_2h_ball_mace_common", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_main_ancillary_mount_brown_horse", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                        if element == "fire":
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_main_ancillary_mount_red_horse", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_main_ancillary_weapon_two_handed_axe_common", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_main_ancillary_weapon_hook_sickle_sabre_common", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_main_ancillary_weapon_two_handed_spear_common", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_main_ancillary_weapon_halberd_common", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                        if element == "water":
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_main_ancillary_weapon_single_edged_sword_common", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_main_ancillary_mount_black_horse", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_main_ancillary_weapon_dual_swords_common", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_main_ancillary_weapon_double_edged_sword_common", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                        if element == "metal":
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_main_ancillary_weapon_sword_and_shield_common", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_main_ancillary_weapon_dual_swords_common", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_main_ancillary_mount_grey_horse", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_main_ancillary_weapon_single_edged_sword_common", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_main_ancillary_weapon_double_edged_sword_common", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_main_ancillary_weapon_one_handed_axe_common", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_ytr_ancillary_weapon_dual_maces_common", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                        if element == "earth":
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_main_ancillary_weapon_sword_and_shield_common", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_main_ancillary_weapon_dual_swords_common", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_main_ancillary_weapon_one_handed_axe_common", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_main_ancillary_weapon_single_edged_sword_common", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_main_ancillary_weapon_double_edged_sword_common", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})                           
                            writer.writerow({'initial_data_stage': initial_data_key , 'active_ceo': "3k_main_ancillary_mount_white_horse", 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                    if option == "title":
                        initial_career_key = "3k_main_ceo_initial_data_stage_character_traits_historical_" + name
                        key_name = "3k_main_ceo_career_historical_" + name
                        class_type = "3k_main_ceo_class_" + element
                        
                        writer.writerow({'initial_data_stage': initial_career_key , 'active_ceo': key_name, 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})
                        writer.writerow({'initial_data_stage': initial_career_key , 'active_ceo': class_type, 'starting_points_delta': 0, 'auto_id': random.randint(100000, 9999999)})

        
            ##ceo_initial_data_equipments
                            
            ceo_initial_data_equipments_path = os.path.join(directory, "ceo_initial_data_equipments.csv")

            with open(ceo_initial_data_equipments_path, mode='w', newline='') as csv_file:
                fieldnames = ['initial_data_stage', 'category', 'slot_index', 'equipped_ceo', 'auto_id', 'target']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for name, option, element, gender in name_list:
                    if option == "armour":
                        initial_data_key = "3k_main_ceo_initial_data_character_historical_" + name + "_ancillaries" 
                        key_name = "3k_main_ancilliary_armour_" + name + "_armour_unique"
                        writer.writerow({'initial_data_stage': initial_data_key, 'category': "3k_main_ceo_category_ancillary_armour", 'slot_index': 0, 'equipped_ceo': key_name, 'auto_id': random.randint(100000, 9999999), 'target': "character_equipment"})
                        if element == "wood":
                            writer.writerow({'initial_data_stage': initial_data_key, 'category': "3k_main_ceo_category_ancillary_mount", 'slot_index': 0, 'equipped_ceo': "3k_main_ancillary_mount_brown_horse", 'auto_id': random.randint(100000, 9999999), 'target': "character_equipment"})
                            writer.writerow({'initial_data_stage': initial_data_key, 'category': "3k_main_ceo_category_ancillary_weapon", 'slot_index': 0, 'equipped_ceo': "3k_main_ancillary_weapon_two_handed_spear_common", 'auto_id': random.randint(100000, 9999999), 'target': "character_equipment"})
                        if element == "earth":
                            writer.writerow({'initial_data_stage': initial_data_key, 'category': "3k_main_ceo_category_ancillary_mount", 'slot_index': 0, 'equipped_ceo': "3k_main_ancillary_mount_white_horse", 'auto_id': random.randint(100000, 9999999), 'target': "character_equipment"})
                            writer.writerow({'initial_data_stage': initial_data_key, 'category': "3k_main_ceo_category_ancillary_weapon", 'slot_index': 0, 'equipped_ceo': "3k_main_ancillary_weapon_single_edged_sword_common", 'auto_id': random.randint(100000, 9999999), 'target': "character_equipment"})
                        
                        if element == "fire":
                            writer.writerow({'initial_data_stage': initial_data_key, 'category': "3k_main_ceo_category_ancillary_mount", 'slot_index': 0, 'equipped_ceo': "3k_main_ancillary_mount_red_horse", 'auto_id': random.randint(100000, 9999999), 'target': "character_equipment"})
                            writer.writerow({'initial_data_stage': initial_data_key, 'category': "3k_main_ceo_category_ancillary_weapon", 'slot_index': 0, 'equipped_ceo': "3k_main_ancillary_weapon_two_handed_spear_common", 'auto_id': random.randint(100000, 9999999), 'target': "character_equipment"})
                        
                        if element == "water":
                            writer.writerow({'initial_data_stage': initial_data_key, 'category': "3k_main_ceo_category_ancillary_mount", 'slot_index': 0, 'equipped_ceo': "3k_main_ancillary_mount_black_horse", 'auto_id': random.randint(100000, 9999999), 'target': "character_equipment"})
                            writer.writerow({'initial_data_stage': initial_data_key, 'category': "3k_main_ceo_category_ancillary_weapon", 'slot_index': 0, 'equipped_ceo': "3k_main_ancillary_weapon_single_edged_sword_common", 'auto_id': random.randint(100000, 9999999), 'target': "character_equipment"})
                        
                        if element == "metal":
                            writer.writerow({'initial_data_stage': initial_data_key, 'category': "3k_main_ceo_category_ancillary_mount", 'slot_index': 0, 'equipped_ceo': "3k_main_ancillary_mount_grey_horse", 'auto_id': random.randint(100000, 9999999), 'target': "character_equipment"})
                            writer.writerow({'initial_data_stage': initial_data_key, 'category': "3k_main_ceo_category_ancillary_weapon", 'slot_index': 0, 'equipped_ceo': "3k_main_ancillary_weapon_double_edged_sword_common", 'auto_id': random.randint(100000, 9999999), 'target': "character_equipment"})
                        
            ##ceo_initial_datas
            ceo_initial_datas_path = os.path.join(directory, "ceo_initial_datas.csv")

            with open(ceo_initial_datas_path, mode='w', newline='') as csv_file:
                fieldnames = ['key', 'template_manager']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for name, option, element, gender in name_list:
                    data_key = "3k_main_ceo_initial_data_character_historical_" + name 
                    writer.writerow({'key': data_key, 'template_manager': "character_ceo_manager"})
                            

            ##ceo_initial_data_to_stages
            ceo_initial_data_to_stages_path = os.path.join(directory, "ceo_initial_data_to_stages.csv")

            with open(ceo_initial_data_to_stages_path, mode='w', newline='') as csv_file:
                fieldnames = ['ceo_initial_data', 'stage', 'initial_data_stage']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for name, option, element, gender in name_list:
                    data_key = "3k_main_ceo_initial_data_character_historical_" + name 
                    initial_data_key = "3k_main_ceo_initial_data_character_historical_" + name + "_ancillaries"     
                    initial_career_key = "3k_main_ceo_initial_data_stage_character_traits_historical_" + name
                    if element == "wood":
                        equipment = "3k_main_ceo_initial_data_equipment_permissions_unique_wood"
                        childhood = "3k_main_ceo_initial_data_stage_character_childhood_wood"
                    if element == "earth":    
                        equipment = "3k_main_ceo_initial_data_equipment_permissions_unique_earth"        
                        childhood = "3k_main_ceo_initial_data_stage_character_childhood_earth"           
                    if element == "fire":                    
                        equipment = "3k_main_ceo_initial_data_equipment_permissions_unique_fire"
                        childhood = "3k_main_ceo_initial_data_stage_character_childhood_fire"
                    if element == "water":
                        equipment = "3k_main_ceo_initial_data_equipment_permissions_unique_water"
                        childhood = "3k_main_ceo_initial_data_stage_character_childhood_water"
                    if element == "metal":
                        equipment = "3k_main_ceo_initial_data_equipment_permissions_unique_metal"
                        childhood = "3k_main_ceo_initial_data_stage_character_childhood_metal"
                    if gender == "male": 
                        identity = "3k_main_ceo_initial_data_stage_character_gender_male"
                    if gender == "female":
                        identity = "3k_main_ceo_initial_data_stage_character_gender_female"

                    writer.writerow({'ceo_initial_data': data_key, 'stage': 11, 'initial_data_stage': initial_career_key})
                    writer.writerow({'ceo_initial_data': data_key, 'stage': 3, 'initial_data_stage': initial_data_key})
                    writer.writerow({'ceo_initial_data': data_key, 'stage': 21, 'initial_data_stage': "3k_dlc04_ceo_initial_data_character_give_political_support_random"})
                    writer.writerow({'ceo_initial_data': data_key, 'stage': 2, 'initial_data_stage': "3k_main_initial_data_character_ancillaries_global"})
                    writer.writerow({'ceo_initial_data': data_key, 'stage': 15, 'initial_data_stage': "3k_main_ceo_initial_data_stage_character_wealth_random"})
                    writer.writerow({'ceo_initial_data': data_key, 'stage': 14, 'initial_data_stage': "3k_main_ceo_initial_data_stage_character_protagonist"})
                    writer.writerow({'ceo_initial_data': data_key, 'stage': 10, 'initial_data_stage': "3k_main_ceo_initial_data_stage_character_traits_shared_global_permissions"})
                    writer.writerow({'ceo_initial_data': data_key, 'stage': 17, 'initial_data_stage': childhood})
                    writer.writerow({'ceo_initial_data': data_key, 'stage': 4, 'initial_data_stage': equipment})
                    writer.writerow({'ceo_initial_data': data_key, 'stage': 13, 'initial_data_stage': identity})
                          
                        
            ##ceo_template_manager_ceo_limits
            ceo_template_manager_ceo_limits_path = os.path.join(directory, "ceo_template_manager_ceo_limits.csv")

            with open(ceo_template_manager_ceo_limits_path, mode='w', newline='') as csv_file:
                fieldnames = ['template_manager', 'scoped_limit_or_local_only_limit', 'ceo_to_limit', 'ceo_node_to_limit', 'ceo_category_to_limit', 'max_limit_that_can_exist_at_once', 'auto_id']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for name, option, element, gender in name_list:
                    if option == "armour":
                        key_name = "3k_main_ancilliary_armour_" + name + "_armour_unique"
                        writer.writerow({'template_manager': "3k_main_ceo_template_manager_world_generic", 'scoped_limit_or_local_only_limit': "true", 'ceo_to_limit': key_name, 'ceo_node_to_limit': "", 'ceo_category_to_limit': "", 'max_limit_that_can_exist_at_once': 1, 'auto_id': random.randint(100000, 9999999)})

            ##ceo_thresholds
            ceo_thresholds_path = os.path.join(directory, "ceo_thresholds.csv")

            with open(ceo_thresholds_path, mode='w', newline='') as csv_file:
                fieldnames = ['key', 'ceo', 'point_threshold_to_activate', 'point_theshold_to_destroy', 'starting_points', 'max_points', 'resets_to_starting_points_when_deactivated']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for name, option, element, gender in name_list:
                    if option == "armour":
                        key_name = "3k_main_ancilliary_armour_" + name + "_armour_unique"
                        writer.writerow({'key': key_name, 'ceo': key_name, 'point_threshold_to_activate': 1, 'point_theshold_to_destroy': 0, 'starting_points': 1, 'max_points': 1, 'resets_to_starting_points_when_deactivated': "false"})
                    if option == "title":
                        ceo_name = "3k_main_ceo_career_historical_" + name
                        writer.writerow({'key': ceo_name, 'ceo': ceo_name, 'point_threshold_to_activate': 1, 'point_theshold_to_destroy': 0, 'starting_points': 1, 'max_points': 1, 'resets_to_starting_points_when_deactivated': "false"})


            ##ceo_effect_lists
            ceo_effect_lists_path = os.path.join(directory, "ceo_effect_lists.csv")

            with open(ceo_effect_lists_path, mode='w', newline='') as csv_file:
                fieldnames = ['key']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for name, option, element, gender in name_list:
                    if option =="armour":
                        key_name = "3k_main_ancilliary_armour_" + name + "_armour_unique"
                        writer.writerow({'key': key_name})
                    if option == "title":
                        key_name = "3k_main_ceo_career_historical_" + name
                        writer.writerow({'key': key_name})

            ##ceo_nodes
            ceo_nodes_path = os.path.join(directory, "ceo_nodes.csv")

            with open(ceo_nodes_path, mode='w', newline='') as csv_file:
                fieldnames = ['key', 'ceo_effect_list', 'point_change_per_turn_if_active', 'title', 'description', 'icon_path', 'opinion_topic_modifier']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for name, option, element, gender in name_list:
                    if option == "armour":
                        key_name = "3k_main_ancilliary_armour_" + name + "_armour_unique"
                        icon_path = "armours/3k_main_ancillary_"+ element + "_armour_unique.png"

                        writer.writerow({'key': key_name, 'ceo_effect_list': key_name, 'point_change_per_turn_if_active': 0, 'title': "placeholder", 'description': "placeholder", 'icon_path': icon_path, 'opinion_topic_modifier': ""})
                    if option == "title":
                        key_name = "3k_main_ceo_career_historical_" + name
                        icon_path = ""
                        writer.writerow({'key': key_name, 'ceo_effect_list': key_name, 'point_change_per_turn_if_active': 0, 'title': "placeholder", 'description': "placeholder", 'icon_path': icon_path, 'opinion_topic_modifier': ""})

            ##ceo_threshold_nodes
            ceo_threshold_nodes_path = os.path.join(directory, "ceo_threshold_nodes.csv")

            with open(ceo_threshold_nodes_path, mode='w', newline='') as csv_file:
                fieldnames = ['ceo_threshold', 'ceo_node', 'points_threshold_to_activate_node', 'can_downgrade_to_previous_node', 'auto_id']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for name, option, element, gender in name_list:
                    if option == "armour":
                        key_name = "3k_main_ancilliary_armour_" + name + "_armour_unique"
                        writer.writerow({'ceo_threshold': key_name, 'ceo_node': key_name, 'points_threshold_to_activate_node': 1, 'can_downgrade_to_previous_node': "false", 'auto_id': random.randint(100000, 9999999)})
                    if option == "title": 
                        key_name = "3k_main_ceo_career_historical_" + name
                        writer.writerow({'ceo_threshold': key_name, 'ceo_node': key_name, 'points_threshold_to_activate_node': 1, 'can_downgrade_to_previous_node': "false", 'auto_id': random.randint(100000, 9999999)})


            ceo_effect_list_to_effects_path = os.path.join(directory, "ceo_effect_list_to_effects.csv")

            with open(ceo_effect_list_to_effects_path, mode='w',newline='') as csv_file:
                fleidnames = ['effect_list', 'effect', 'value', 'effect_scope', 'auto_id', 'optional_only_in_game_mode']
                writer = csv.DictWriter(csv_file, fieldnames=fleidnames)
                writer.writeheader()
                for name, option, element, gender in name_list:  
                    if option == "title":
                        key_name = "3k_main_ceo_career_historical_" + name
                        writer.writerow({'effect_list': key_name, 'effect': '3k_main_effect_character_num_lives', 'value': 1, 'effect_scope': 'character_to_character_own', 'auto_id': random.randint(100000, 9999999), 'optional_only_in_game_mode': ''})
                        writer.writerow({'effect_list': key_name, 'effect': '3k_main_character_wealth', 'value': 2, 'effect_scope': 'character_to_character_own', 'auto_id': random.randint(100000, 9999999), 'optional_only_in_game_mode': ''})
                    if option == "armour":
                        key_name = "3k_main_ancilliary_armour_" + name + "_armour_unique"
                        
                        if element == "fire":
                            point_key = "3k_main_effect_character_attribute_instinct_mod"
                        if element == "earth":
                            point_key = "3k_main_effect_character_attribute_authority_mod"
                        if element == "water":
                            point_key = "3k_main_effect_character_attribute_cunning_mod"
                        if element == "wood":
                            point_key = "3k_main_effect_character_attribute_resolve_mod"
                        if element == "metal":
                            point_key = "3k_main_effect_character_attribute_expertise_mod"

                        writer.writerow({'effect_list': key_name, 'effect': '3k_dummy_effect_ceo_subcategory_armour_unique', 'value': 0, 'effect_scope': 'character_to_character_own', 'auto_id': random.randint(100000, 9999999), 'optional_only_in_game_mode': ''})
                        writer.writerow({'effect_list': key_name, 'effect': point_key, 'value': 18, 'effect_scope': 'character_to_character_own', 'auto_id': random.randint(100000, 9999999), 'optional_only_in_game_mode': ''})


        change_name_path = os.path.join(directory, "change_name.csv")

        with open(change_name_path, mode='w', newline='') as csv_file:
                fieldnames = ['key']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for name, option, element, gender in name_list:
                    if option =="armour":
                        key_name = "SAD_" + name + "_" + element
                        writer.writerow({'key': key_name})
                    
    # Display "Program was run successfully" in a text widget
    result_display.config(state=tk.NORMAL)
    result_display.delete(1.0, tk.END)
    result_display.insert(tk.END, "Program was run successfully")
    result_display.config(state=tk.DISABLED)

# Create a "Run" button
run_button = tk.Button(root, text="Run", command=run_application)
run_button.pack()

# Create a text widget to display the result
result_display = tk.Text(root, height=2, width=30)
result_display.config(state=tk.DISABLED)
result_display.pack()

# Start the main event loop
root.mainloop()
