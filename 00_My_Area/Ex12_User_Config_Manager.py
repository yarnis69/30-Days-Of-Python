
def add_setting(settings_dict, updated_setting):

    updated_setting = tuple(key_value.lower() for key_value in updated_setting)

    if updated_setting[0] in settings_dict.keys():
        return f"Setting '{updated_setting[0]}' already exists! Cannot add a new setting with this name."

    else:
        settings_dict.update({updated_setting[0]:updated_setting[1]})
        return f"Setting '{updated_setting[0]}' added with value '{updated_setting[1]}' successfully!"



def update_setting(settings_dict, updated_setting):

    updated_setting = tuple(key_value.lower() for key_value in updated_setting)

    if updated_setting[0] in settings_dict.keys():
        settings_dict.update({updated_setting[0]:updated_setting[1]})
        return f"Setting '{updated_setting[0]}' updated to '{updated_setting[1]}' successfully!"

    else:
        return f"Setting '{updated_setting[0]}' does not exist! Cannot update a non-existing setting."



def delete_setting(settings_dict, setting_key):
    setting_key = setting_key.lower()

    if setting_key in settings_dict.keys():
        settings_dict.pop(setting_key)
        return f"Setting '{setting_key}' deleted successfully!"

    else:
        return "Setting not found!"



def view_settings(settings_dict):

    if settings_dict == {}:
        return 'No settings available.'

    else:
        output = "Current User Settings:"

        for setting in settings_dict:
            output+=(f"\n{str(setting).strip('()').capitalize()}: {settings_dict[setting]}")

        output +='\n'

        return str(output)

test_settings = {'TITLE':'HELLO', 'COLOUR':'RED'}

print(view_settings(test_settings))
