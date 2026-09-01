import webbrowser
import speech_recognition as sr
import subprocess

r = sr.Recognizer()

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

                elif "начать" in cmd:
                    webbrowser.open("https://rt.pornhub.com")

                elif "калькулятор" in cmd:
                    subprocess.Popen("calc.exe")

                elif "стоп" in cmd:
                    break

            except sr.UnknownValueError:
                pass

            except sr.RequestError as error:
                print(f"Ошибка сервиса распознавания: {error}")

except KeyboardInterrupt:
    print("\nДжавис остановлен.")