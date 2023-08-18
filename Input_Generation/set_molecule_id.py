import sys

arguments = sys.argv
data_path = arguments[1]
creation_path = arguments[2]

with open(data_path, "r") as file:
    for i, line in enumerate(file):
         if "Atoms" in line:
                n = i
    
with open(data_path, "r") as file:
    pre_lines = file.readlines()[:n+2]
    
    
with open(data_path, "r") as file:
    atom_lines = file.readlines()[n+2:]
    new_lines = []
    j=0
    for i, line in enumerate(atom_lines):
        if i%5 == 0:
            j+=1
        values = line.split(" ")
        values[1] = str(j)
        line = " ".join(values)
        new_lines.append(line)
        

with open (creation_path, "w") as file:
    file.writelines(pre_lines)
    file.writelines(new_lines)
