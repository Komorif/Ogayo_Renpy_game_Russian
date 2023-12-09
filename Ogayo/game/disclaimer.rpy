# Дисклеймер 1
screen disclaimer:
    modal True
    zorder 100

    fixed:
        xsize 1920 ysize 1080
        add "images/splash_screen/disclaimer1.png" align (.5,.5)

    fixed:
        xsize 1920 ysize 1080

        button:
            xpos 780 ypos 852
            xsize 380 ysize 86
            idle_background "images/sprites/arrow_hover.png"
            hover_foreground "images/sprites/arrow_idle.png"
            action Hide("disclaimer"), Show("disclaimer2")

# Дисклеймер 1 подтверждение
screen disclaimer2:
    modal True
    zorder 100

    fixed:
        xsize 1920 ysize 1080
        add "images/splash_screen/disclaimer1.png" align (.5,.5)
        add "images/sprites/iphone.png" align (.5,.5)

    fixed:
        xsize 1920 ysize 1080

        button:
            xpos 890 ypos 650
            xsize 173 ysize 165
            idle_background "images/sprites/arrow1_hover.png"
            hover_foreground "images/sprites/arrow1_idle.png"
            action Hide("disclaimer2"), Show("disclaimer3")

# Дисклеймер 2
screen disclaimer3:
    modal True
    zorder 100

    fixed:
        xsize 1920 ysize 1080
        add "images/splash_screen/disclaimer2.png" align (.5,.5)

    button:
            xpos 890 ypos 700
            xsize 173 ysize 165
            idle_background "images/sprites/arrow1_hover.png"
            hover_foreground "images/sprites/arrow1_idle.png"
            action Hide("disclaimer3"), Jump("continue_history")