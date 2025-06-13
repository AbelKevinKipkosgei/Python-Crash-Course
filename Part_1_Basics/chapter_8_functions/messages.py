def show_messages(messages):
    print(f"\nRead the following messages:")
    for message in messages:
        print(f"\t{message}")


def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Printing message: {current_message}")
        sent_messages.append(current_message)


messages = [
    "Keep going!",
    "You're doing great!",
    "Stay focused.",
    "Never give up.",
    "Believe in yourself.",
    "Progress, not perfection.",
    "Trust the process.",
    "You've got this!",
    "Stay consistent.",
]
sent_messages = []

show_messages(messages)
send_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)
