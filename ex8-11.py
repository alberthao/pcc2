#Author: Alberthao
#Topic: Function

# start from here
def send_messages(messages):
    sent_messages=[]
    while messages:
        current_msg=messages.pop()
        print(current_msg)
        sent_messages.append(current_msg)
    return sent_messages


msgs=['Lost years are worse than lost dolars.','Every little helps.','Pride hurts,modesty benefits.','Rome was not built in a day.']
sent_messages=send_messages(msgs[:])  #这里传递进入的参数为列表副本，下一行的输出结果原有列表不受影响
print(msgs)
print(sent_messages)