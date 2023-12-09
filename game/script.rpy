# Персонажи
define nameQuestion = Character('???', color="#ffffff", image='question')

define loudspeaker = Character('Громкоговоритель', color="#00cfff", image='loudspeaker')
define memories = Character('Воспоминания', color="#ffffff", image='memories')
define rezo = Character('Rezo', color="#ffffff", image='rezo')

# КП Фаги
define coePhages = Character('КП фаги', color="#ff0000", image='coe_phages')
define KpPhageSquad = Character('Отряд КПфагов', color="#f5e4ab", image='kpphagesquad')

# Наса
define nasaQuestion = Character('Летающий воин', color="#f5e4ab", image='nasa')
define nasa = Character('Nasa', color="#f5e4ab", image='nasa')

# Субару
# Троица Серполле
define s1 = Character('Первый Субару', color="#ffae00", image='subaru')
define s2 = Character('Второй Субару', color="#ffae00", image='subaru')
define s3 = Character('Третий Субару', color="#ffae00", image='subaru')

define s4 = Character('Обычный Субару', color="#ffae00", image='subaru')
define s5 = Character('Обычный Субару', color="#ffae00", image='subaru')
define s6 = Character('Обычный Субару', color="#ffae00", image='subaru')

define malaysia = Character('Малайзия', color="#ffae00", image='subaru')
define martin = Character('Мартин', color="#ffae00", image='subaru')


define subaru_from_the_crowd = Character('Субару из толпы', color="#ffae00", image='subaru_from_the_crowd')
define subaru_from_the_crowd_two = Character('Субару из толпы', color="#6a386c", image='subaru_from_the_crowd_two')

define guests = Character('Гости', color="#0048ff", image='guests')

define ayanokouji_black_sprite = Character('???', color="#ffffff", image='ayanokouji')

define neerwox = Character('NeerwoX', color="#ffb8c6", image='neerwox')


define serpolle_question = Character('Серполле', color="#dc3a35", image='question_serpolle')
define serpolle = Character('Серполле', color="#dc3a35", image='serpolle')





# Спрайты
image menAbyss = "sprites/men.png"
image name_game = "images/name_game.png"
image logo = "images/logo.png"

image subaru_seven = "sprites/subaru seven.png"

image subaru_four_shadow = "sprites/subaru four shadow.png"
image subaru_five_shadow = "sprites/subaru five shadow.png"
image subaru_six_shadow = "sprites/subaru six shadow.png"


image splash_screen_new_vison = "images/splash_screen/splash_screen_New_Vison.png"
image splash_screen_rezo = "images/splash_screen/splash_screen_Rezo.png"

image disclaimer_one = "images/splash_screen/disclaimer1.png"
image disclaimer_two = "images/splash_screen/disclaimer2.png"


# Курсор
define config.mouse = {}
define config.mouse["default"] = [("gui/cursors/black_cursor.png", 0, 0)]



init python:
    g = Gallery()

    g.locked_button = "images/posters/lock.png"

    g.button("room_phone")
    g.condition("persistent.room_phone")
    g.image("poster1")

    g.button("forest")
    g.condition("persistent.forest")
    g.image("poster2")

    g.button("three_subaru")
    g.condition("persistent.three_subaru")
    g.image("poster3")



# Заставка
label splashscreen:
    show disclaimer_one with dissolve
    pause 4
    hide disclaimer_one with dissolve
    show disclaimer_two with dissolve
    pause 4
    hide disclaimer_two with dissolve
    scene black with dissolve
    show splash_screen_new_vison with dissolve
    pause 1
    hide splash_screen_new_vison
    show splash_screen_rezo with dissolve
    pause 2
    hide splash_screen_rezo
    pause 2
    scene black with dissolve
    pause 0.5
    return


# Начало (дисклеймер)
label start:
    play music menu_music
    show screen disclaimer
    scene black
    ""

# Продолжение истории после дисклеймера
label continue_history:
    stop music
    scene black with dissolve
    scene room_day with dissolve
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

    $ renpy.notify("В галерее появился новый постер.")
    $ persistent.room_phone = True
    scene poster1 with dissolve

    "Комната опустела."
    "Только телефон лежал на кровати, с навсегда потухшим экраном."
    jump chapterOne
    return