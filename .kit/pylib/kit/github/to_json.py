def to_json(thing):
    if isinstance(thing, list):
        return convert_list_of_github_objects_to_json(thing)
    else:
        return convert_github_object_to_json(thing)


def convert_github_object_to_json(github_obj):
    return github_obj._rawData


def convert_list_of_github_objects_to_json(github_objects):
    new_list = []
    for github_obj in github_objects:
        new_list.append(to_json(github_obj))
    return new_list
