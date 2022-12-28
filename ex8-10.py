#Author: Alberthao
#Topic: Function

# this part not use in this file
def show_messages(messages):
    for message in messages:
        print(message)
    return

# start from here
def send_messages(messages):
    sent_messages=[]
    while messages:
        current_msg=messages.pop()
        print(current_msg)
        sent_messages.append(current_msg)
    return sent_messages


msgs=['Lost years are worse than lost dolars.','Every little helps.','Pride hurts,modesty benefits.','Rome was not built in a day.']
sent_messages=send_messages(msgs)
print(msgs)
print(sent_messages)