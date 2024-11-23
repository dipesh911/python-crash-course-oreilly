from pathlib import Path

path = Path(r'C:\Users\Dipesh\Documents\my\python\orielly-py-crash-course\learning_python.txt')
content = path.read_text()
print(content)

lines = content.splitlines()
for line in lines:
    print(line)