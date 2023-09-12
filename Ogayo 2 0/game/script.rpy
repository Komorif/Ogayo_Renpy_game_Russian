# Персонажи
define nameQuestion = Character('???', color="#ffffff")
define loudspeaker = Character('Громкоговоритель', color="#00cfff")
define memories = Character('Воспоминания', color="#ffffff")
define rezo = Character('Rezo', color="#ffffff")
define s1 = Character('Первый Субару', color="#ffae00", image='subaru')
define s2 = Character('Второй Субару', color="#ffae00", image='subaru')
define s3 = Character('Третий Субару', color="#ffae00", image='subaru')
define coePhages = Character('КП фаги', color="#ff0000")
define coePhagesLeader = Character('Лидер КП фагов', color="#ffafc1")
define nasaQuestion = Character('Летающий воин', color="#ffafc1", image='nasa')
define nasa = Character('Nasa', color="#ffafc1", image='nasa')


# Спрайты
image menAbyss = "sprites/men.png"
image name_game = "images/name_game.png"
image logo = "images/logo.png"

image splash_screen_new_vison = "images/splash_screen/splash_screen_New_Vison.png"
image splash_screen_rezo = "images/splash_screen/splash_screen_Rezo.png"
image splash_screen_meme = "images/splash_screen/splash_screen_meme.png"

define config.mouse = {}

define config.mouse["default"] = [("gui/cursors/black_cursor.png", 0, 0)]

# Переменные
init:
    # Расположение спрайта
    $ left = Position(xalign=0.1, yalign=1.1)
    $ chapterOneMenu = True
    $ chapterTwoMenu = False

# Кнопка для выхода из игры
screen back_butt:
    imagebutton:
        xalign 5.1
        yalign 5.3
        idle "sprites/white_hover.png"
        hover "sprites/white_idle.png"
        action Quit(confirm=True)

screen menu_panel:
    modal True
    frame:
        padding(10, 10)
        xsize 170
        ysize 500

        vbox:
            text "Выбрать главу"
            textbutton "1\nглава" action Jump("chapterOne")
            null height 15
            textbutton "2\nглава" action Jump("chapterTwo")
            null height 15
            textbutton "закрыть" action Hide("menu_panel")


# Лейблы
label splashscreen:
    scene black with dissolve
    show splash_screen_new_vison with dissolve
    pause 1
    hide splash_screen_new_vison
    show splash_screen_rezo with dissolve
    pause 2
    show splash_screen_meme with dissolve
    pause 2
    scene black with dissolve
    pause 1
    return

# Видео в меню
label main_menu:
    play music menu_music
    show abyss
    show name_game

    show subaru_two_animation:
        xalign 0.1
    show subaru_three_animation:
        xalign 0.9

    jump main_menu_screen

label start:
    stop music
    scene room_day
    play music lite
    nameQuestion "— Очередной жаркий летний день."
    nameQuestion "— Я уже два часа занимаюсь домашними делами, зайду-ка в чат Понаценко."
    show phone with dissolve:
        xalign 0.1 yalign 0.2
    nameQuestion "— В чате как всегда споры. {w}Просто понаблюдаю за этим, а после займусь своими делами."
    show vzlom1 with dissolve:
        xalign 0.1 yalign 0.2
    stop music fadeout 1
    nameQuestion "— Что это?"
    nameQuestion "— Неужели мой телефон взломали?"
    nameQuestion "— Хотя нет."
    nameQuestion "— Скорее ивенты от Понаценко вышли на новый уровень."
    show vzlom2 with dissolve:
        xalign 0.1 yalign 0.2
    nameQuestion "— Я напрягся."
    nameQuestion "— От Понаценко обычно многого не жду, но это действительно выглядит интересно."
    show vzlom3 with dissolve:
        xalign 0.1 yalign 0.2
    nameQuestion "— Эта надпись слишком долго держится на экране."
    play sound off
    nameQuestion "— ..."
    stop sound fadeout 1
    nameQuestion "— Неужели меня всё-таки взломали?"
    play sound vzdoh
    "фф-хх"
    stop sound fadeout 1
    show abyss with dissolve
    show menAbyss with dissolve
    nameQuestion "— Меня.. меня засасывает!"
    nameQuestion "— Нужно бежать."
    play sound krik
    nameQuestion "— ААААААА!!"
    stop sound fadeout 1
    scene room_phone with dissolve
    "Комната опустела."
    "Только телефон лежал на кровати, с навсегда потухшим экраном."
    jump chapterOne
    return