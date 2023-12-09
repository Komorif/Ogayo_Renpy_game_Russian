# Кнопки для изменения фона меню
screen change_menu_background:

    imagebutton:
            yalign 0.99
            xalign 0.99
    
            idle "images/sprites/idle gallery button.png"
            hover "images/sprites/hover gallery button.png"
            action ShowMenu("gallery")
    
    if persistent.twoChapter:


        imagebutton:
            yalign 0.75
            xalign 0.01
    
            idle "images/sprites/1 menu button idle.png"
            hover "images/sprites/1 menu button hover.png"
            action Jump("main_menu_one")

        imagebutton:
            yalign 0.87
            xalign 0.01
    
            idle "images/sprites/2 menu button idle.png"
            hover "images/sprites/2 menu button hover.png"
            action Jump("main_menu_two")

    if persistent.threeChapter:
        imagebutton:
            yalign 0.99
            xalign 0.01
    
            idle "images/sprites/3 menu button idle.png"
            hover "images/sprites/3 menu button hover.png"
            action Jump("main_menu_three")

# Видео в меню
label main_menu:
    play music menu_music
    show abyss
    show name_game

    show screen change_menu_background

    if persistent.menuOneChapter:
        show subaru_two_animation:
            xalign 0.1
        show subaru_three_animation:
            xalign 0.9

    elif persistent.menuTwoChapter:
        show warrior:
            xalign 0.01
        show nasa_animation:
            xalign 1.0

    elif persistent.menuThreeChapter:
        show subaru_four_animation:
            xalign 0.01
        show neerwox_animation:
            xalign 0.9
    jump main_menu_screen

# 1 меню
label main_menu_one:
    show subaru_two_animation with moveinleft:
        xalign 0.1
    show subaru_three_animation with moveinright:
        xalign 0.9

    hide warrior with moveoutleft
    hide nasa_animation with moveoutright

    hide subaru_four_animation with moveoutleft
    hide neerwox_animation with moveoutright

    jump main_menu_screen

# 2 меню
label main_menu_two:
    show warrior with moveinleft:
        xalign 0.01
    show nasa_animation with moveinright:
        xalign 1.0

    hide subaru_two_animation with moveoutleft
    hide subaru_three_animation with moveoutright

    hide subaru_four_animation with moveoutleft
    hide neerwox_animation with moveoutright

    jump main_menu_screen

# 3 меню
label main_menu_three:
    show subaru_four_animation with moveinleft:
        xalign 0.01
    show neerwox_animation with moveinright:
        xalign 0.9

    hide subaru_two_animation with moveoutleft
    hide subaru_three_animation with moveoutright

    hide warrior with moveoutleft
    hide nasa_animation with moveoutright

    jump main_menu_screen    