# twtk-ceo-creator
Program that automates the process title + armor if need for characters for Total War: Three Kingdoms

# Running the program:

Installation

# Step 1: Clone or Download the Repository

To obtain the code, either clone the repository or download the zip file:

## Clone the Repository:

`git clone https://github.com/Ironictw2st/twtk-ceo-creator.git`
`cd twtk-ceo-creator`

## Download the Zip File:

Visit the repository on GitHub.
Click the green "Code" button and select "Download ZIP."

Extract the contents to a desired folder.

# Step 2: Run the Application

Open a terminal (or command prompt) and navigate to the directory containing ceocreator.py.

Run the script using Python:

`python ceocreator.py`

# Step 3: Directory

Have the directory lead to 

`...\Steam\steamapps\common\Total War THREE KINGDOMS\raw_data\db_import`

# Step 4: After creation 

Follow these tables, hitting the import csv button and apply changes

`ceos --> ceo_groups --> ceo_group_ceos --> ceo_permissions --> ceo_permissions_groups --> ceo_scripted_permissions --> ceo_scripted_permissions_to_permissions --> ceo_initial_data_stages --> ceo_initial_data_scripted_permissions --> ceo_initial_data_equipments --> ceo_initial_data_active_ceos --> ceo_initial_datas --> ceo_initial_data_to_stages --> ceo_template_manager_ceo_limits --> ceo_thresholds --> ceo_effect_lists --> ceo_nodes  --> ceo_threshold_nodes --> ceo_effect_list_to_effects`

If you have created just a title for a character in ceo_initial_data_stages, for stage 3, you need to give them the generic ancillaries depending on their classd
