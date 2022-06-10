_registry_list: dict[list] = {}


class RegistryClass:
    def get(self, key):
        if key not in _registry_list:
            _registry_list[key] = []

        return _registry_list[key]

    def add(self, key, default_value=[]):
        global _registry_list
        _registry_list[key] = default_value

    def clear(self, key):
        global _registry_list
        _registry_list[key] = []


registries = RegistryClass()
