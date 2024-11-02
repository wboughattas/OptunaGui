from functools import reduce


def dict_depth(_dict, level=1):
    if not isinstance(_dict, dict) or not _dict:
        return level
    return max(dict_depth(_dict[key], level + 1) for key in _dict)


def deep_get(_dict, keys, default=None):
    return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("."), dict(_dict))


def deep_insert(dictionary, keys, value):
    keys_list = keys.split(".")
    reduce(lambda d, key: d.setdefault(key, {}), keys_list[:-1], dictionary)[keys_list[-1]] = value


def deep_delete(dictionary, keys):
    keys_list = keys.split(".")
    parent = reduce(lambda d, key: d.get(key, {}), keys_list[:-1], dictionary)
    if isinstance(parent, dict) and keys_list[-1] in parent:
        del parent[keys_list[-1]]
