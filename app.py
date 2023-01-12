import os
from rich import print; from rich.console import Console; cn = Console();
from rich.traceback import install
import requests
from PIL import Image
from tkinter import filedialog

R = '[bold red]'     # 🔴| Красный
Q = '[bold #E32636]' # 🔴| Ярко красный
G = '[bold green]'   # 🟢| Зелёный
B = '[bold blue]'    # 🔵| Синий
D = '[bold #00FF7F]' # 🔵| Голубой
W = '[bold white]'   # ⚪| Белый
Y = '[bold #FFFF00]' # 🟡| Жёлтый
I = '[bold yellow]'  # 🟡| Светло жёлтый
E = '[bold #808080]' # ⚙️| Сервый
O = '   '
A = '───'

IA = '                         '
TAB ='    '
TAG1 = ['0+','6+','12+','16+','18+']
TAG2 = ['0', '6', '12', '16', '18']

print('   ')
cn.print(f'{R}─── AledCreatik ───', justify="center")

num = 0
Файлов = 1
for dirpath, dirnames, filenames in os.walk("./page"):
    for dirname in dirnames:
        num += 1
        Файлов += 1
nun = f'{num}      '

DIR = f'page/{Файлов}'
FILE = 'image.png'

class app:
    _1_Print  = f'{R}┌────────────────────────────────────{A*3}{E} Панель разработчка {R}─{R}┐'
    _2_Print  = f'{R}│{W} Папок: {Y}{nun}                                           {O*2}{R}│'
    _3_Print  = f'{R}└───────────────────────────────────────────────────────────────{A*1}{R}┘'
    _4_Print  = f'{B} Для начала настройки сайта                          {Y}Нажмите: {D}Enter'
    _0_Input  = f''

    _11_Print = f'{R}┌────────────────────────────────────────────{A*3}{E} Коментарий {R}─{R}┐'
    _12_Print = f'{R}│{I} Значения: {G}Любой текст                                   {O*3}{R}│'
    _13_Print = f'{R}│{E} └{Q} Требуется обязательно!                                {O*3}{R}│'
    _14_Print = f'{R}└───────────────────────────────────────────────────────────────{A*1}{R}┘'
    _1_Name   = f'{IA}{B} Название'
    _1_Input  = f'{IA}{E} └ {I}Значение: '

    _21_Print = f'{R}┌────────────────────────────────────────────{A*3}{E} Коментарий {R}─{R}┐'
    _22_Print = f'{R}│{I} значения: {G}0+, 6+, 12+, 16+, 18+                         {O*3}{R}│'
    _23_Print = f'{R}│{E} └{Y} По умолчанию: {G}0+                                   {O*4}{R}│'
    _24_Print = f'{R}└───────────────────────────────────────────────────────────────{A*1}{R}┘'
    _2_Name   = f'{IA}{B} Возрастное ограничение'
    _2_Input  = f'{IA}{E} └ {I}Значение: '

    _31_Print = f'{R}┌────────────────────────────────────────────{A*3}{E} Коментарий {R}─{R}┐'
    _32_Print = f'{R}│{I} Значения: {G}Команда {Q}file {W}или {G}https://example.com {O*6}{R}│'
    _33_Print = f'{R}│{E} └{Y} По умолчанию: {G}Нет                                  {O*4}{R}│'
    _34_Print = f'{R}└───────────────────────────────────────────────────────────────{A*1}{R}┘'
    _3_Name   = f'{IA}{B} Изображение'
    _3_Input  = f'{IA}{E} └ {I}Значение: '
    _33_Input = f'{IA}{E}   └ {I}URL Изображения: '

    _41_Print = f'{R}┌────────────────────────────────────────────{A*3}{E} Коментарий {R}─{R}┐'
    _42_Print = f'{R}│{I} Значения: {G}https://example.com                           {O*3}{R}│'
    _43_Print = f'{R}│{E} └{Y} По умолчанию: {G}Нет                                  {O*4}{R}│'
    _44_Print = f'{R}└───────────────────────────────────────────────────────────────{A*1}{R}┘'
    _4_Name   = f'{IA}{B} URL Информация'
    _4_Input  = f'{IA}{E} └ {I}Значение: '

    _51_Print = f'{R}┌────────────────────────────────────────────{A*3}{E} Коментарий {R}─{R}┐'
    _52_Print = f'{R}│{I} Значения: {G}https://example.com                           {O*3}{R}│'
    _53_Print = f'{R}│{E} └{Q} Требуется обязательно!                                {O*3}{R}│'
    _54_Print = f'{R}└───────────────────────────────────────────────────────────────{A*1}{R}┘'
    _5_Name   = f'{IA}{B} URL Видео'
    _5_Input  = f'{IA}{E} └ {I}Значение: '

Формат_App = (app._1_Print  + '\n' + app._2_Print  + '\n' + app._3_Print  + '\n' + app._4_Print)
Формат_1   = (app._11_Print + '\n' + app._12_Print + '\n' + app._13_Print + '\n' + app._14_Print); Имя = ''; Имя1 = f'{B}-'
Формат_2   = (app._21_Print + '\n' + app._22_Print + '\n' + app._23_Print + '\n' + app._24_Print); Возраст = ''; Возраст1 = f'{B}-'
Формат_3   = (app._31_Print + '\n' + app._32_Print + '\n' + app._33_Print + '\n' + app._34_Print); Изображение = ''; Изображение1 = f'{B}-'
Формат_4   = (app._41_Print + '\n' + app._42_Print + '\n' + app._43_Print + '\n' + app._44_Print); Кнопка = ''; Кнопка1 = f'{B}-'; Button = ''
Формат_5   = (app._51_Print + '\n' + app._52_Print + '\n' + app._53_Print + '\n' + app._54_Print); Видео = ''; Видео1 = f'{B}-'

cn.print(Формат_App, justify="center")
cn.input(app._0_Input, password=True)
os.system('cls')
cn.print()
cn.print(f'{R}─── Настройка сайта ───', justify="center")
cn.print()
cn.print(f'{E}   Название фильма: {Имя1}')
cn.print(f'{E}   Возрастное ограничение: {Возраст1}')
cn.print()
cn.print(f'{E}   URL Изображения: {Изображение1}')
cn.print(f'{E}   URL Информация: {Кнопка1}')
cn.print(f'{E}   URL Видео: {Видео1}')
cn.print()
cn.print()
cn.print(Формат_1, justify="center")
while Имя in '':
    cn.print(app._1_Name)
    Имя = cn.input(app._1_Input)
    if Имя == '':
        cn.print(f'{IA}   {E}└ {R}Это поле обязательно\n')
        pass
    else:
        Имя1 = Y + Имя
        break

os.system('cls')
cn.print()
cn.print(f'{R}─── Настройка сайта ───', justify="center")
cn.print()
cn.print(f'{E}   Название фильма: {Имя1}')
cn.print(f'{E}   Возрастное ограничение: {Возраст1}')
cn.print()
cn.print(f'{E}   URL Изображения: {Изображение1}')
cn.print(f'{E}   URL Информация: {Кнопка1}')
cn.print(f'{E}   URL Видео: {Видео1}')
cn.print()
cn.print()
cn.print(Формат_2, justify="center")
while Возраст in '':
    cn.print(app._2_Name)
    Возраст = cn.input(app._2_Input)
    if Возраст == '':
        Возраст = '0+'
        Возраст1 = f'{R}{Возраст} {B}По умолчанию'
        break
    elif Возраст in TAG1:
        Возраст = f'{Возраст}'
        Возраст1 = f'{R}{Возраст} {B}'
        break
    elif Возраст in TAG2:
        Возраст = f'{Возраст}+'
        Возраст1 = f'{R}{Возраст} {B}'
        break
    else:
        Возраст = '0+'
        Возраст1 = f'{R}{Возраст} {B}По умолчанию'
        break

os.system('cls')
cn.print()
cn.print(f'{R}─── Настройка сайта ───', justify="center")
cn.print()
cn.print(f'{E}   Название фильма: {Имя1}')
cn.print(f'{E}   Возрастное ограничение: {Возраст1}')
cn.print()
cn.print(f'{E}   URL Изображения: {Изображение1}')
cn.print(f'{E}   URL Информация: {Кнопка1}')
cn.print(f'{E}   URL Видео: {Видео1}')
cn.print()
cn.print()
cn.print(Формат_3, justify="center")
while True:
    cn.print(app._3_Name)
    Изображение = cn.input(app._3_Input)
    if Изображение in '':
        Изображение = 'Нет'
        Изображение1 = f'{D}Файл {B}По умолчанию'
        imgLOG = '1'
        break
    if Изображение in ['1', 'file', 'File', 'FILE', 'файл', 'Файл', 'ФАЙЛ']:
        try:
            Изображение = filedialog.askopenfilename()
            FILE = Image.open(Изображение)  
            Изображение1 = f'{D}Файл'
            imgLOG = '2'
            break
        except:
            cn.print(f'{IA}   {E}└ {R}Файл не поддерживается\n')
    else:
        try:
            Данные = requests.get(Изображение).content
            Изображение1 = f'{D}Ссылка'
            imgLOG = '3'
            break
        except:
            cn.print(f'{IA}   {E}└ {R}Ссылка указана некоректно\n')

os.system('cls')
cn.print()
cn.print(f'{R}─── Настройка сайта ───', justify="center")
cn.print()
cn.print(f'{E}   Название фильма: {Имя1}')
cn.print(f'{E}   Возрастное ограничение: {Возраст1}')
cn.print()
cn.print(f'{E}   URL Изображения: {Изображение1}')
cn.print(f'{E}   URL Информация: {Кнопка1}')
cn.print(f'{E}   URL Видео: {Видео1}')
cn.print()
cn.print()
cn.print(Формат_4, justify="center")
while Кнопка in '':
    cn.print(app._4_Name)
    Кнопка = cn.input(app._4_Input)
    if Кнопка == '':
        button = ''
        Кнопка = 'Нет'
        Кнопка1 = f'{Y}{Кнопка} {B}'
    else:
        Кнопка1 = f'{Y}{Кнопка} {B}'
        Button = f'<a class="buttonn" href="{Кнопка}" target="0">Информация</a>'

os.system('cls')
cn.print()
cn.print(f'{R}─── Настройка сайта ───', justify="center")
cn.print()
cn.print(f'{E}   Название фильма: {Имя1}')
cn.print(f'{E}   Возрастное ограничение: {Возраст1}')
cn.print()
cn.print(f'{E}   URL Изображения: {Изображение1}')
cn.print(f'{E}   URL Информация: {Кнопка1}')
cn.print(f'{E}   URL Видео: {Видео1}')
cn.print()
cn.print()
cn.print(Формат_5, justify="center")
while Видео in '':
    cn.print(app._5_Name)
    Видео = cn.input(app._5_Input)
    if Видео == '':
        cn.print(f'{IA}   {E}└ {R}Это поле обязательно\n')
    else:
        Видео1 = f'{Y}{Видео} {B}'

#    <style>:root{
#            --VName: 'Удача';
#            --VAge:  '6+';
#        }
#    </style> 

Страница = (   
f"""<!-- Форматирование -->
<!DOCTYPE html>
<html lang="ru" class="no-js">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <head>
        <meta charset="utf-8">
        <meta name="yandex-verification" content="2d8c1dcb18ad48b7"/>
        
<!-- Интеграция Embed -->
<meta property="og:site_name" content="AledGG">
<link rel="shortcut icon" href="https://i.imgur.com/tPQs4ZD.png">
<meta property="og:image:width" content="170">
<meta property="og:image:height" content="250">
<meta name="theme-color" content="#26ade9">

<!-- CSS -->
<link rel="stylesheet" href="../../css/Page.css">        <!-- Дизайн фона сайта --> 
<link rel="stylesheet" href="../../css/Header.css">      <!-- Дизайн шапки сайта --> 
<link rel="stylesheet" href="../../css/ScrollBar.css">   <!-- Полоса прокрутки -->
<link rel="stylesheet" href="../../css/SectionBox.css">  <!-- Секции блоков -->
<link rel="stylesheet" href="../../css/VideoPlayer.css"> <!-- Видео блок -->
<link rel="stylesheet" href="../../css/Animation.css">   <!-- Анимации -->

<link rel="stylesheet" href="../../css/Root.css">        <!-- Конфигурация -->

<!-- JavasCript -->
<script src="../../index.js"></script>

<!-- Шапка страницы -->
<div class="body-wrap">
    <header class="site-header">
        <div class="container">
            <div class="site-header-inner">
                <div class="brand header-brand">
                    <ul class="footer-links list-reset">
                        <h4 class="hero-title mt-0">
                            <a href="../../">
                                <span class="LogoBox"><ui class="LogoName"></span></a><ui class="LogoPage"><ui class="LogoVersion"></ui></h4>
                            </head>
                        </header>

<!-- каталог фильмов -->
<section class="hero2"></section>

<section class="hero1"><div class="container"><div class="hero-inner"><div class="hero-copy"><div class="film">
    <div class="name">{Имя}<p class="number">{Возраст}</p></div></div><div class="im">
    <img src="image.png" class="image" onerror="this.style.visibility = 'hidden'" width="170px" height = "250px"><div class="hero-cta">
    {Button}</section><section class="hero1"><div class="container"><p class="buttonns"><p>
    <iframe class="fonv" src="{Видео}" frameborder="0" allowfullscreen></iframe></div></div></div>       
    <meta property="og:title" content="{Имя}">
    <title>ALED | {Имя}</title>
</section>

</html>""")

os.system('cls')
print('   ')
cn.print(f'{R}─── AledCreatik ───', justify="center")
num = 0
for dirpath, dirnames, filenames in os.walk("./page"):
    for dirname in dirnames:
        num += 1
        pass
nun = f'{num}      '
num += 1
cn.print(Формат_App, justify="center")

____________________Имя = F'{Имя}                                                       '
________________Возраст = F'{Возраст}                                                   '
cn.print(f'{G}─── Фильм сгенерирован ───', justify="center")
cn.print(f'{E}┌─────────────────────────────────────────────────────────{E}{E}{E}{E}{E}┐', justify="center")
cn.print(f'{E}│{W} Название: {R}{R}{R}{R}{R}{____________________Имя[:45]} {Y}{Y}{Y}{E}│', justify="center")
cn.print(f'{E}│{W} Возрасное ограниение: {R}{________________Возраст[:33]} {Y}{Y}{Y}{E}│', justify="center")
cn.print(f'{E}└───────────────────────────────────────────────{Y} ID: {num} {E}─{E}{E}┘', justify="center")
cn.print()
cn.print(f'{W}   URL Информация: {B}{Кнопка}')
cn.print(f'{W}   URL Видео: {B}{Видео}')
cn.print()
cn.print()

# Создать папку для фильма
if not os.path.exists(f'./{DIR}'): 
    os.makedirs(f'./{DIR}')

# Изменение каталога
Строка = 50
with open('./index.html', 'r', encoding='utf8') as Файл:
    lines = Файл.readlines()
lines.insert(Строка-2, f'''
<section class="hero1"><div class="container"><div class="hero-inner"><div class="hero-copy"><div class="film">
    <h1 class="name">{Имя}
    <p class="number">{Возраст}</p></h1></div>
    <div class="im"><img src="page/{num}/image.png" class="image" onerror="this.style.visibility = 'hidden'" width="170px" height = "250px"><div class="hero-cta">
    <a class="buttonn"  href="page/{num}/">Смотреть</a>
</section>
''')
Файл = open('./index.html', 'w+', encoding='utf8')
Файл.writelines(lines)

# Создание изображения
if imgLOG in '1':
    FILE = Image.open('icon/image.png')
    FILE = FILE.save(f'./{DIR}/image.png')
if imgLOG in '2':
    FILE = Image.open(Изображение)  
    FILE = FILE.save(F'./{DIR}/image.png')
if imgLOG in '3':
    FILE = open(f'./{DIR}/{FILE}', 'wb')
    FILE.write(Данные)
    FILE.close()

# Страница фильма
Фильм = open(F"./{DIR}/index.html", "w+", encoding='utf8')
Фильм.write(Страница)
Фильм.close()