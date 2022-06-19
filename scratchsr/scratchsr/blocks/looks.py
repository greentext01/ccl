from scratchsr.user.create_block import create_block


def say(message):
    create_block({
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
