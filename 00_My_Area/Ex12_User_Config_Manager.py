
def add_setting(settings_dict, updated_setting):

    updated_setting = tuple(key_value.lower() for key_value in updated_setting)

    if updated_setting[0] in settings_dict.keys():
        print(f"Setting '{updated_setting[0]}' already exists! Cannot add a new setting with this name.")

    else:
        settings_dict.update({updated_setting[0]:updated_setting[1]})
        print(f"Setting '{updated_setting[0]}' added with value '{updated_setting[1]}' successfully!")



def update_setting(settings_dict, updated_setting):

    updated_setting = tuple(key_value.lower() for key_value in updated_setting)

    if updated_setting[0] in settings_dict.keys():
        settings_dict.update({updated_setting[0]:updated_setting[1]})
        print(f"Setting '{updated_setting[0]}' updated to '{updated_setting[1]}' successfully!")

    else:
        print(f"Setting '{updated_setting[0]}' does not exist! Cannot update a non-existing setting.")



def delete_setting(settings_dict, setting_key):
    pass

    

#test_settings_dict = {'abc':'efg', 'ert':'hrq'}
#test_setting_tuple = ('ABC', 'YYY')
#update_setting(test_settings_dict,test_setting_tuple)