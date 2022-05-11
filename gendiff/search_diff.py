def search_diff(first_dict, second_dict):
    first_keys = first_dict.keys()
    second_keys = second_dict.keys()
    difference = {}
    for key in sorted(first_keys & second_keys):
        if first_dict[key] == second_dict[key]:
            difference['  {key}'.format(key=key)] = first_dict[key]
        else:
            difference['- {key}'.format(key=key)] = first_dict[key]
            difference['+ {key}'.format(key=key)] = second_dict[key]
    for key in sorted(first_keys - second_keys):
        difference['- {key}'.format(key=key)] = first_dict[key]
    for key in sorted(second_keys - first_keys):
        difference['+ {key}'.format(key=key)] = second_dict[key]

    return difference
