from pathlib import Path

path = Path(r'C:\Users\Dipesh\Documents\my\python\orielly-py-crash-course\guestbook.txt')

q= True
name_group = ''
while q:
    name=input("Enter your name or q to quit : ")
    if name == "q":
       q = False
       break
    # name = print(name)
    name_group += name+'\n'
content = path.write_text(name_group)
