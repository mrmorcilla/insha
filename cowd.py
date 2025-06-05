import os
ruta = r"C:\mzci\funciono.txt"
os.makedirs(os.path.dirname(ruta), exist_ok=True)
codigo = '''el verdadero enderpell
'''
with open(ruta, "w", encoding="utf-8") as f:
    f.write(codigo)
