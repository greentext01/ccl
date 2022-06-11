from scratchsr.core.block import build_block


def say(message):
    build_block({
        "opcode": "looks_say",
        "inputs": {
            "MESSAGE": [
                1,
                [
                    10,
                    message
                ]
            ]
        },
    })
