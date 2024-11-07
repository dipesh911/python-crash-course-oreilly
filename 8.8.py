def make_album(name,title,no=None):
    info = {}
    info[name]=title
    if no:
        info['Number']=no
    return info

while True:
    prompt = ("Input q to quit")
    name = input("Name: ").strip()
    title = input("Title: ").strip()
    # q = input(prompt)
    if name == "q" or title == "q":
        break

    info = make_album(name,title)
    print(info)
