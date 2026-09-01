import webbrowser
import speech_recognition as sr
import subprocess

r = sr.Recognizer()

TELEGRAM_PATH = r"D:\Users\Andrey\AppData\Roaming\Telegram Desktop\Telegram.exe"

print("Джавис запущен...")

try:
    while True:
        with sr.Microphone() as src:
            try:
                print("Слушаю...")
                audio = r.listen(src)

                cmd = r.recognize_google(
                    audio,
                    language="ru-RU"
                ).lower()

                print(f"Вы: {cmd}")

                if "браузер" in cmd:
                    webbrowser.open("https://www.google.com")

                elif "telegram" in cmd or "телеграм" in cmd:
                    
                    subprocess.run([
                        "cmd",
                        "/c",
                        "start",
                        "",
                        TELEGRAM_PATH
                    ])

                elif "стоп" in cmd:
                    break

            except sr.UnknownValueError:
                pass

            except sr.RequestError as error:
                print(f"Ошибка сервиса распознавания: {error}")

except KeyboardInterrupt:
    print("\nДжавис остановлен.")