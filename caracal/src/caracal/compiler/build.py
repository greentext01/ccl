from glob import glob
import importlib.util
import json
import os
import sys
from caracal.compiler.ast_mod import modify_ast
from caracal.compiler.gen_id import gen_id
from caracal.errors.missing_path_error import MissingPathError
from caracal.core.registry import registries


def build():
    if not os.path.exists("sprites"):
        raise MissingPathError("sprites")

    for filename in glob("sprites/**/*.ccl.py"):
        modify_ast(filename)

        spec = importlib.util.spec_from_file_location(filename, filename)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        print(registries.get("events"))

    for sprite_class in registries.get("sprites"):
        sprite = sprite_class()
        build_events(sprite_class)


def build_events(sprite_class):
    # Instantiate the sprite
    sprite = sprite_class()

    # Find events
    for prop in sprite_class.__dict__.keys():
        if prop.startswith("on_") and callable(sprite_class.__dict__[prop]):
            # Add event block
            registries.get("blocks").append({
                "opcode": "event_whenflagclicked",
                "inputs": {},
                "fields": {},
                "shadow": False,
                "topLevel": True,
                "x": 282,
                "y": 126
            })

            # Run event"s function, extracting blocks
            registries.clear("blocks")
            getattr(sprite, prop)()
            print(json.dumps(link(registries.get("blocks"))))


def link(blocks):
    out = {}
    if len(blocks) == 0:
        return

    previous = None
    current = gen_id()
    next = gen_id()

    for i, block in enumerate(blocks):
        out[current] = block

        if i < len(blocks) - 1:
            out[current]["next"] = next
        else:
            out[current]["next"] = None

        out[current]["parent"] = previous
        if previous == None:
            out[current]["x"] = 50
            out[current]["y"] = 50

        previous = current
        current = next
        next = gen_id()

    return out
