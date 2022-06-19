from scratchsr.util.gen_id import gen_id


def link(blocks):
    out = {}
    if len(blocks) == 0:
        return

    previous = None
    current = gen_id()
    next = gen_id()

    for i, block in enumerate(blocks):
        out[current] = block["content"]

        if i < len(blocks) - 1:
            out[current]["next"] = next
        else:
            out[current]["next"] = None

        out[current]["parent"] = previous
        if previous == None:
            out[current]["x"] = 50
            out[current]["y"] = 50
            out[current]["topLevel"] = True
        else:
            out[current]["topLevel"] = False

        previous = current
        
        # If build_block wants to specify a custom id
        if len(blocks) > i + 1 and blocks[i + 1].get("id") != None:
            current = blocks[i + 1]["id"]
        else:
            current = next

        next = gen_id()
        

    return out
