import glob2
from datetime import datetime

filenames = glob2.glob('file*.txt')
with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%s-%f")+".txt", "w") as file:
    for filename in filenames:
        with open(filename, "r") as f:
            file.write(f.read() + "\n")