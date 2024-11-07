def make_album(name,title,no=None):
    info = {}
    info['name']=title
    if no:
        info['Number']=no
    return info

album = make_album("Sonu","Deewana")

print(album)