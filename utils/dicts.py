def get_val(collection, key, default='git'):
    if collection.get(key) is None:
        return default
    return collection[key]