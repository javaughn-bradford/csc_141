#08_11_archeive_messages

def show_messages(messages):
    """Print each message from the list."""
    for message in messages:
        print(message)

def send_messages(messages):
    """Print each message and move it to sent_messages."""
    sent_messages = []
    
    while messages:
        message = messages.pop(0)  
        print(message)             
        sent_messages.append(message)  
    return sent_messages

print("Messages:")
text_messages = [
    "Hi, how are you?",
    "Nice day, today",
    "What are you doing later?",
    "Hey, just checking in.",
    "You wanna meet later?"
]

sent_messages = send_messages(text_messages.copy())

print("Remaining Messages:", text_messages)
print("Sent Messages:", sent_messages)
