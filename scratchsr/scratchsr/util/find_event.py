EVENTS = {
    "on_flag_clicked"
}

def find_event(event_name):
    for event in EVENTS:
        if event_name.startswith(event):
            return event
    
    return None