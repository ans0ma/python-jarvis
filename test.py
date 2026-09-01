import subprocess

telegram = r"D:\Users\Andrey\AppData\Roaming\Telegram Desktop\Telegram.exe"

subprocess.run([
    "cmd",
    "/c",
    "start",
    "",
    telegram
])

print("Telegram запущен")