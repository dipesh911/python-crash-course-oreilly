from pathlib import Path

name = input("Enter your name : ")

path = Path(r'C:\Users\Dipesh\Documents\my\python\orielly-py-crash-course\name.txt')
content = path.write_text(name)

