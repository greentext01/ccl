from scratchsr.user.create_block import create_block
from scratchsr.errors.scratch_error import ScratchError
from scratchsr.util.gen_id import gen_id
from scratchsr.user.sprite import Sprite

RANDOM = "_random_"
MOUSE = "_mouse_"


def go_to(position):
    id = gen_id()

    if position == RANDOM or position == MOUSE:
        create_block({
            "opcode": "motion_goto",
            "inputs": {
                "TO": [
                    1,
                    id,
                ]
            }
        })
        create_block({
            "opcode": "motion_goto_menu",
            "fields": {
                "TO": [
                    position,
                    None,
                ]
            },
            "shadow": False
        }, id)
    
    elif isinstance(position, Sprite):
        create_block({
            "opcode": "motion_goto",
            "inputs": {
                "TO": [
                    1,
                    id,
                ]
            }
        })
        create_block({
            "opcode": "motion_goto_menu",
            "fields": {
                "TO": [
                    position.__class__.__name__,
                    None,
                ]
            },
            "shadow": False
        }, id)
    else:
        raise ScratchError("Invalid argument for go_to")


def turn_right(degrees):
    create_block({
        "opcode": "motion_turnright",
        "inputs": {
            "DEGREES": [
                1,
                  [
                      4,
                      str(degrees)
                  ]
            ]
        },
    })


def turn_left(degrees):
    create_block({
        "opcode": "motion_turnleft",
        "inputs": {
            "DEGREES": [
                1,
                [
                    4,
                    str(degrees)
                ]
            ]
        },
    })


def move(steps):
    create_block({
        "opcode": "motion_movesteps",
        "inputs": {
            "STEPS": [
                1,
                [
                    4,
                    str(steps)
                ]
            ]
        }
    })
