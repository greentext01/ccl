from scratchsr.util import registry
from ..errors.missing_field_error import MissingFieldError


BLOCK_DEFAULTS = {
    "next": None,
    "parent": None,
    "fields": {},
    "inputs": {},
    "shadow": False,
    "topLevel": None,
}

BLOCK_FIELDS = {
    "opcode",
    "next",
    "parent",
    "inputs",
    "fields",
    "shadow",
    "topLevel"
}


def create_block(field: dict, id=None):
    fields = BLOCK_DEFAULTS | field

    for required_field in BLOCK_FIELDS:
        if required_field not in fields:
            raise MissingFieldError(required_field)

    registry.registries.get("blocks").append({
        "content": fields, "id": id
    })
