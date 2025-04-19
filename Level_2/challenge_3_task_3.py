def num_obj(s):
    character_dict_list = []
    for num in s:
        num_dict = {str(num): chr(num)}
        character_dict_list.append(num_dict)
    return character_dict_list
