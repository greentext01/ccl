from scratchsr.core import registry
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


def build_block(field: dict):
    fields = BLOCK_DEFAULTS | field

    for required_field in BLOCK_FIELDS:
        if required_field not in fields:
            raise MissingFieldError(required_field)

    registry.registries.get("blocks").append(fields)

def build_blocks(blocks):
    for block in blocks:
        build_block(block)
