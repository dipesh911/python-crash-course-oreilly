from pathlib import Path
import json

def fav_no():
    try:
        no = int(input('input your fav no : '))
        path = Path('no.json')
        content = json.dumps(no)
        path.write_text(content)
    except ValueError:
        print('Enter only integers')

def read_fav_no():
        path = Path('no.json')
        if path.exists():
             content = path.read_text()
             no = json.loads(content)
             return no

fav_no()
fav_no1 = read_fav_no()
if fav_no1 == '':
    print(f"You do not have favorite number!")
else:
    print(f"I know your favorite number! It’s {fav_no1}.")


no= ''
path = Path('no.json')
content = json.dumps(no)
path.write_text(content)

