_registry_list: dict[list] = {}


class RegistryClass:
    def get(self, key) -> list:
        if key not in _registry_list:
            _registry_list[key] = []

        return _registry_list[key]

    def add(self, key):
        _registry_list[key] = []

    def clear(self, key):
        _registry_list[key] = []


registries = RegistryClass()
