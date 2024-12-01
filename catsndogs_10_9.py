from pathlib import Path

try:
    path = Path(r"C:\Users\Dipesh\Documents\my\python\orielly-py-crash-course\cats.txt")
    cat = path.read_text()
    print(cat)

    path = Path(r"orielly-py-crash-course\dogs.txt")
    dog = path.read_text()
    print(dog)
except FileNotFoundError:
    pass
