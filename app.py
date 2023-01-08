import os
import time
from rich import print; from rich.console import Console; cn = Console();
from rich.traceback import install
import easygui
import requests

R = '[bold red]'     # 🔴| Красный
Q = '[bold #E32636]' # 🔴| Ярко красный
G = '[bold green]'   # 🟢| Зелёный
B = '[bold blue]'    # 🔵| Синий
D = '[bold #00FF7F]' # 🔵| Голубой
W = '[bold white]'   # ⚪| Белый
Y = '[bold #FFFF00]' # 🟡| Жёлтый
I = '[bold yellow]'  # 🟡| Светло жёлтый
E = '[bold #808080]' # ⚙️| Сервый

IA = '                              '
TAG1 = ['0+','6+','12+','16+','18+']
TAG2 = ['0', '6', '12', '16', '18']

print('   ')
cn.print(f'{R}─── AledCreatik ───', justify="center")

num = 0
for dirpath, dirnames, filenames in os.walk("./page"):
    for dirname in dirnames:
        num += 1
nun = f'{num}      '
num += 1

class app:
    _1_Print  = f'{R}┌────────────────────────────────────{E} Панель разработчка {R}─{R}{R}┐'
    _2_Print  = f'{R}│{W} Папок: {Y}{nun}                                         {W}{R}{R}│'
    _3_Print  = f'{R}└─────────────────────────────────────────────────────────{R}{R}{R}{R}┘'
    _0_Input  = f'{IA} Нажмите Enter что-бы начать настройку                    '

    _11_Print = f'{R}┌────────────────────────────────────────────{E} Коментарий {R}─{R}{R}┐'
    _12_Print = f'{R}│{I} Доступные значения: {G}Любой текст                         {R}{R}│'
    _13_Print = f'{R}│{E} └{Q} Требуется обязательно!                                {R}{R}│'
    _14_Print = f'{R}└─────────────────────────────────────────────────────────{R}{R}{R}{R}┘'
    _1_Name   = f'{IA}{B} Название фильма'
    _1_Input  = f'{IA}{E} └ {I}Значение: '

    _21_Print = f'{R}┌────────────────────────────────────────────{E} Коментарий {R}─{R}{R}┐'
    _22_Print = f'{R}│{I} Доступные значения: {G}0+, 6+, 12+, 16+, 18+               {R}{R}│'
    _23_Print = f'{R}│{E} └{Y} По умолчанию: {G}0+                                      {R}│'
    _24_Print = f'{R}└─────────────────────────────────────────────────────────{R}{R}{R}{R}┘'
    _2_Name   = f'{IA}{B} Возрастное ограничение'
    _2_Input  = f'{IA}{E} └ {I}Значение: '

    _31_Print = f'{R}┌────────────────────────────────────────────{E} Коментарий {R}─{R}{R}┐'
    _32_Print = f'{R}│{I} Доступные значения: {G}1.Файл, 2.Ссылка                    {R}{R}│'
    _33_Print = f'{R}│{E} └{Q} Требуется обязательно!                                {R}{R}│'
    _34_Print = f'{R}└─────────────────────────────────────────────────────────{R}{R}{R}{R}┘'
    _3_Name   = f'{IA}{B} Изображение'
    _3_Input  = f'{IA}{E} └ {I}Значение: '
    _33_Input = f'{IA}{E}   └ {I}URL Изображения: '

    _41_Print = f'{R}┌────────────────────────────────────────────{E} Коментарий {R}─{R}{R}┐'
    _42_Print = f'{R}│{I} Доступные значения: {G}https://example.com                 {R}{R}│'
    _43_Print = f'{R}│{E} └{Y} По умолчанию: {G}Нет                                     {R}│'
    _44_Print = f'{R}└─────────────────────────────────────────────────────────{R}{R}{R}{R}┘'
    _4_Name   = f'{IA}{B} URL Информация'
    _4_Input  = f'{IA}{E} └ {I}Значение: '

    _51_Print = f'{R}┌────────────────────────────────────────────{E} Коментарий {R}─{R}{R}┐'
    _52_Print = f'{R}│{I} Доступные значения: {G}https://example.com                 {R}{R}│'
    _53_Print = f'{R}│{E} └{Q} Требуется обязательно!                                {R}{R}│'
    _54_Print = f'{R}└─────────────────────────────────────────────────────────{R}{R}{R}{R}┘'
    _5_Name   = f'{IA}{B} URL Видео'
    _5_Input  = f'{IA}{E} └ {I}Значение: '


Pr_App = (
    app._1_Print + '\n' +
    app._2_Print + '\n' +
    app._3_Print
    )
Pr_1   = (
    app._11_Print + '\n' +
    app._12_Print + '\n' +
    app._13_Print + '\n' +
    app._14_Print
    )
Pr_2   = (
    app._21_Print + '\n' +
    app._22_Print + '\n' +
    app._23_Print + '\n' +
    app._24_Print
    )
Pr_3   = (
    app._31_Print + '\n' +
    app._32_Print + '\n' +
    app._33_Print + '\n' +
    app._34_Print
    )
Pr_4   = (
    app._41_Print + '\n' +
    app._42_Print + '\n' +
    app._43_Print + '\n' +
    app._44_Print
    )
Pr_5   = (
    app._51_Print + '\n' +
    app._52_Print + '\n' +
    app._53_Print + '\n' +
    app._54_Print
    )

    
cn.print(Pr_App, justify="center")
cn.input(app._0_Input, password=True)
cn.print()


Имя = ''
while Имя in '':
    cn.print(Pr_1, justify="center")
    cn.print(app._1_Name)
    Имя = cn.input(app._1_Input)
    if Имя == '':
        cn.print(f'{IA}   {E}└ {R}Это поле обязательно\n')
    else:
        cn.print(f"{IA}   {E}└ {D}Установлено значение: {Y}{Имя}\n")
Возраст = ''
while Возраст in '':
    cn.print(Pr_2, justify="center")
    cn.print(app._2_Name)
    Возраст = cn.input(app._2_Input)
    if Возраст == '':
        Возраст = '0+'
        cn.print(f"{IA}   {E}└ {D}Установлено значение: {Y}По умолчанию\n")
        break
    elif Возраст in TAG1:
        Возраст = f'{Возраст}'
        cn.print(f"{IA}   {E}└ {D}Установлено значение: {Y}{Возраст}\n")
        break
    elif Возраст in TAG2:
        Возраст = f'{Возраст}+'
        cn.print(f"{IA}   {E}└ {D}Установлено значение: {Y}{Возраст}\n")
        break
    else:
        Возраст = '0+'
        cn.print(f"{IA}   {E}└ {R}Ошибка автомачический выбор: {Y}По умолчанию\n")
Изображение = ''
while Изображение in '':
    cn.print(Pr_3, justify="center")
    cn.print(app._3_Name)
    Изображение = cn.input(app._3_Input)
    if Изображение == '':
        cn.print(f'{IA}   {E}└ {R}Это поле обязательно\n')
    else:
        if Изображение == '1':
            cn.print(f"{IA}   {E}└ {D}Открытие проводника...")
            Изображение =  easygui.fileopenbox()
            cn.print(f"{IA}     {E}└ {D}Установлено значение: {Y}{Изображение}\n")
            break   
        if Изображение == '2':
            Изображение = cn.input(app._33_Input)
            cn.print(f"{IA}     {E}└ {D}Установлено значение: {Y}{Изображение}\n")
            break        
Кнопка = ''; Button = ''
while Кнопка in '':
    cn.print(Pr_4, justify="center")
    cn.print(app._4_Name)
    Кнопка = cn.input(app._4_Input)
    if Кнопка == '':
        Кнопка = 'Нет'
        cn.print(f"{IA}   {E}└ {D}Установлено значение: {Y}По умолчанию\n")
        Кнопка = 'Нет информации'
        break
    else:
        Button = f'<a class="buttonn" href="{Кнопка}" target="0">Информация</a>'
        cn.print(f"{IA}   {E}└ {D}Установлено значение: {Y}{Кнопка}\n")
        break
Видео = ''

while Видео in '':
    cn.print(Pr_5, justify="center")
    cn.print(app._5_Name)
    Видео = cn.input(app._5_Input)
    if Видео == '':
        cn.print(f'{IA} {E}└ {R}Это поле обязательно\n')
    else:
        cn.print(f"{IA}   {E}└ {D}Установлено значение: {Y}{Видео}\n")

# '            '


#    <style>:root{
#            --VName: 'Удача';
#            --VAge:  '6+';
#        }
#    </style> 

tt    = '    '

class Format:
    Content = (
f'{tt}' + '<style>:root{' + '\n' +
f'{tt}{tt}{tt}' + '--VName: '+ "'" + Имя + "'" + ';' + '\n' +
f'{tt}{tt}{tt}' + '--VAge:  '+ "'" + Возраст + "'"+ ';' + '\n' +
f'{tt}{tt}' + '}' + '\n' +
f'' + '</style>'
)

code = (   
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

<section class="hero1"><div class="container"><div class="hero-inner"><div class="hero-copy"><div class="film"><div class="name"><p class="number"></p></div></div><div class="im">
    <img src="image.png" class="image" onerror="this.style.visibility = 'hidden'" width="170px" height = "250px"><div class="hero-cta">
    {Button}</section><section class="hero1"><div class="container"><p class="buttonns"><p>
    <iframe class="fonv" src="{Видео}" frameborder="0" allowfullscreen></iframe></div></div></div>       

    <meta property="og:title" content="{Имя}">
    <title>ALED | {Имя}</title>
{Format.Content}
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
cn.print(f'{R}┌─{E} Панель разработчка {R}────────────────────────────────────{R}{R}{R}┐', justify="center")
cn.print(f'{R}│{W} Папок: {Y}{nun}                                         {W}{R}{R}{R}│', justify="center")
cn.print(f'{R}└─────────────────────────────────────────────────────────{R}{R}{R}{R}{R}┘', justify="center")
print()

____________________Имя = F'{Имя}                                                       '
________________Возраст = F'{Возраст}                                                   '
cn.print(f'{G}─── Фильм сгенерирован ───', justify="center")
cn.print(f'{E}┌─────────────────────────────────────────────────────────{E}{E}{E}{E}{E}┐', justify="center")
cn.print(f'{E}│{W} Название: {R}{R}{R}{R}{R}{____________________Имя[:45]} {Y}{Y}{Y}{E}│', justify="center")
cn.print(f'{E}│{W} Возрасное ограниение: {R}{________________Возраст[:33]} {Y}{Y}{Y}{E}│', justify="center")
cn.print(f'{E}└────────────────────────────────────────────────{Y} ID: {num} {E}─{E}{E}┘', justify="center")

cn.print(f'{W}   URL Информация: {R}{R}{B}{Кнопка}')
cn.print(f'{W}   URL Видео: {R}{R}{B}{Видео}')
cn.print()
cn.print()

newpath = f'./page/{num}' 

if not os.path.exists(newpath):
    os.makedirs(newpath)

my_file = open(F"./page/{num}/index.html", "w+", encoding='utf8')
my_file.write(code)
my_file.close()

img_data = requests.get(Изображение).content
with open(f'page/{num}/image.png', 'wb') as handler:
    handler.write(img_data)

with open('./index.html', 'r', encoding='utf8') as file:
    data = file.readlines()
    code = (f'''
<section class="hero1"><div class="container"><div class="hero-inner"><div class="hero-copy"><div class="film">
    <h1 class="name">{Имя}
    <p class="number">{Возраст}</p></h1></div>
    <div class="im"><img src="page/{num}/image.png" class="image" onerror="this.style.visibility = 'hidden'" width="170px" height = "250px"><div class="hero-cta">
    <a class="buttonn"  href="page/{num}/">Смотреть</a>
</section>
''')
data[50] = code + '\n'
with open('index.html', 'w', encoding='utf8') as file:
    file.writelines(data)