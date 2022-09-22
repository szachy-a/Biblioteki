import chatbot
import time

chatbot.start(80)
with chatbot.withRedirectIO():
    imie = input('Jak masz na imię?')
    print('Witaj ' + imie + '!', flush=False)
    time.sleep(5)
    print('To już koniec konwersacji!!!', flush=True)
raise SystemExit
