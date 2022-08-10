import speech_recognition as sr, pyttsx3;  # Подключение необходимых библиотек
import webbrowser as web, wikipedia, requests, datetime, smtplib
import sys, os, re, time, psutil
from colorama import Fore, init
from time import sleep

version = ver = 1.0
voice_man_woman = 0
hi = 'Zontax'

engine = pyttsx3.init()  # Microsoft (SAPI5) – технология распознавания и синтеза речи
voice = engine.getProperty('voices')  # даёт подробности о текущем установленном голосе
engine.setProperty('voice', voice[voice_man_woman].id)  # 0-мужской , 1-женский


def main_command():
    r = sr.Recognizer()  # Создаем объект на основе speech_recognition и вызываем метод для определения данных
    with sr.Microphone() as source:  # Прослущиваем микрофон и записываем звук в source
        print('Говорите: ')
        r.pause_threshold = 0.5  # Устанавливаем паузу на прослушивание, n min = 5
        r.adjust_for_ambient_noise(source, duration=1)  # удалениt шумов
        audio = r.listen(source)  # Полученные данные записываем в audio в .mp3
    try:
        zadanie = r.recognize_google(audio, language="ru-RU").lower()
        print('Вы сказали: ' + zadanie)
    except sr.UnknownValueError:
        init()  # Запуск COLORAMA
        print(Fore.RED + '[НЕ РАСПОЗНАНО]' + Fore.RESET)
        zadanie = main_command()  # Снова слушаем микрофон
    return zadanie


def talk(word):
    print(word)  # Принт слов
    engine.say(word)  # Озвучка слов
    engine.runAndWait()  # Без этой команды мы не услышим речь


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk(f"Good Morning! {hi}")
    elif hour >= 12 and hour < 18:
        talk(f"Good Afternoon! {hi}")
    else:
        talk(f"Good Evening! {hi}")


def ExamIf(zadanie):  # Функция для проверки текста

    l_hi = ['hi friday', 'здравствуй пятница', 'привет пятница', 'привет пятницу']
    l_info = ['версия', 'информация', 'версия']
    l_exit = ['close', 'отключись']
    l_time = ['time', 'время', 'бремя']

    l_replacements = ['открой замены', 'відкрий заміни', 'замена', 'заміни', 'замены', 'open replacements',
                      'открой replacements']

    l_search_in_google = ['найди ', 'найти ', 'поиск ']

    l_url_google = ['open google', 'открой google', 'открыть google', 'запусти google', 'запустить google',
                    'запуск google']
    l_url_youtube = ['open youtube', 'открой youtube', 'открыть youtube', 'запусти youtube', 'запустить youtube',
                     'запуск youtube', 'березюк youtube']
    l_sinoptik = ['погода', 'открой погоду', 'open sinoptik', 'открой sinoptik']

    l_run_youmusic = ['open music', 'открой музыку', 'открыть музыку', 'запуск музыка',
                      'запусти музыку' 'запустить музыку']
    l_run_steam = ['open steam', 'открой steam', 'открыть steam', 'запуск steam', 'запусти steam']
    l_del_steam = ['close steam', 'закрой steam', 'закрыть steam', 'закройся steam', 'закрой стих', 'закрыть стих',
                   'закройся стих', 'простим', 'выйти из стима', 'выйти из steam']

    l_run_teams = ['open teams', 'открой teams', 'открыть teams', 'запуск teams', 'запусти teams' 'запустить teams',
                   'открой тимс', 'открыть тимс', 'запуск тимс', 'запусти тимс' 'запустить тимс', 'откройте мтс']
    l_del_teams = ['close teams', 'закрой teams', 'закрыть teams', 'закройся teams', 'close тимс', 'закрой тимс',
                   'закрыть тимс', 'закройся тимс', 'закройте мтс', 'зактой timss']

    l_run_notepad = ['open notepad', 'открой блокнот', 'открыть блокнот', 'запуск блокнот', 'запусти блокнот',
                     'запустить блокнот', 'открой букву']
    l_del_notepad = ['close notepad', 'закрой блокнот', 'закрыть блокнот', 'закройся блокнот', 'закрой букву']

    def open_browser(name_site, site):
        talk(name_site)
        web.open(site)

    def run_programs(name_program, path):
        # l_run = ['открой ', 'открыть ', 'запуск ', 'запусти ', 'запустить ', 'open']
        os.startfile(f'{path}')
        talk(f'Start {name_program}')

    def close_programs(name_program, name_task):
        # l_del = ['close ', 'закрой ', 'закрыть ', 'закройся ']
        talk(f'Close {name_program}')
        os.system(f"taskkill /f /im {name_task}")

    # Hi
    if zadanie in l_hi:
        wishme()
    # Info
    elif zadanie in l_info:
        talk(f"Friday {ver}, I'm a voice acistent in Python")
    # Exit
    elif zadanie in l_exit:
        talk("Exit")
        exit()
    # Time
    elif zadanie in l_time:
        talk(time.asctime()[-13:-8])

    # Search in Google
    elif 'найди ' in zadanie or 'найти ' in zadanie or 'поиск ' in zadanie:
        key_search = (zadanie[6:])
        talk(f'''Search {key_search}''')
        web.open(f"https://www.google.com/search?q={key_search}")

    # Open replacements hpfk
    elif zadanie in l_replacements:
        open_browser('Replacements', 'https://hpk.edu.ua/replacements')
    # Open YouTube
    elif zadanie in l_url_youtube:
        open_browser('YouTube', 'https://www.youtube.com')
    # Open Google
    elif zadanie in l_url_google:
        open_browser('Google', 'https://www.google.com')
    # Sinoptic
    elif zadanie in l_sinoptik:
        web.open('https://ua.sinoptik.ua/погода-ярмолинці-303030218/10-днів')
    # Virustotal
    elif 'open virus total' in zadanie:
        web.open('https://www.virustotal.com/gui/home/upload')
    # Music
    elif 'play music' in zadanie:
        music_dir = 'C:/Users/Zontax/Music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    # Steam
    elif zadanie in l_run_steam:
        run_programs('Steam', 'f:/Programs/Steam/steam.exe')

    elif zadanie in l_del_steam:
        talk("Close Steam")
        os.system("taskkill /f /im steam.exe")
        os.system("taskkill /f /im steamwebhelper.exe")

    # Блокнот
    elif zadanie in l_run_notepad:
        run_programs('Notepad', 'c:/Windows/system32/notepad.exe')

    elif zadanie in l_del_notepad:
        close_programs('Notepad', 'notepad.exe')

    # Teams
    elif zadanie in l_run_teams:
        talk("Start Teams")
        os.startfile(r'C:/Users/Zontax/AppData/Local/Microsoft/Teams/Update.exe')
    elif zadanie in l_del_teams:
        talk("Close Teams")
        os.system("taskkill /f /im Teams.exe")
    # Wikipedia
    elif 'wikipedia' in zadanie:  # если wikipedia встречается в запросе, выполнится блок:
        talk('Searching Wikipedia...')
        zadanie = zadanie.replace("wikipedia", "")
        results = wikipedia.summary(zadanie, sentences=5)
        talk("According to Wikipedia")
        print(results)
        talk(results)


print(Fore.GREEN + f'Friday {ver} sucsessfull started!' + Fore.RESET)
wishme()

while True:  # While проверка команд
    ExamIf(main_command())
