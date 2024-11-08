msg=['Hey','Hi']
new_msg=[]

def send_messages(msg,new_msg):
    while msg:
        amsg = msg.pop()
        new_msg.append(amsg)

def show_message(msg):
    print(f"{msg}")

print("msg is : ")
show_message(msg)
print("new_msg is : ")
show_message(new_msg)
print("calling send mesg")
send_messages(msg,new_msg)
print("msg is now : ")
show_message(msg)
print("new_msg is now : ")
show_message(new_msg)