import importlib.util
import json
from caracal.compiler.blocks.linker import link
from caracal.errors.invalid_event_error import InvalidEventError
from caracal.core.registry import registries
from caracal.util.find_event import find_event
import importlib.util
import json
import os
from caracal.core.registry import registries

def build_blocks(sprite_class):
    # Instantiate the sprite
    sprite = sprite_class()

    blocks = {}

    # Find events
    for prop in sprite_class.__dict__.keys():
        if prop.startswith("on_") and callable(sprite_class.__dict__[prop]):
            registries.clear("blocks")
            if event := find_event(prop):
                # Add event block
                build_event(event)
            else:
                raise InvalidEventError(prop)

            # Run event's function, extracting blocks
            getattr(sprite, prop)()
            
            # "Flatten" blocks
            blocks = blocks | link(registries.get("blocks"))

    return blocks


def build_event(event_name):
    spec = importlib.util.find_spec(f"caracal.blocks.events.{event_name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
