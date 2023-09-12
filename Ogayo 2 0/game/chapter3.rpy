# 3 Глава: Старый новенький
label chapterThree:
    scene black with dissolve
    $ renpy.movie_cutscene("videos/3chapter.ogv")

    scene forest_trail with dissolve

    show subaru_one_bed_animation with dissolve:
        xalign 0.1
    show subaru_two_bed_animation with dissolve
    show subaru_three_bed_animation with dissolve:
        xalign 0.9

    s3 three bed "— Мы уже оторвались от него."
    s2 two bed "— Аааа, как же обидно что пришлось оставить Резо."
    s2 three bed "— А так могли бы повышение заслужить."
    s1 one bed "— Вы дебилы. Куда важнее, что мы остались целыми и смогли прибежать обратно."

    scene friend_solo_left with dissolve
    show subaru_one_bed_animation with dissolve:
        xalign 0.1
    show subaru_two_bed_animation with dissolve
    show subaru_three_bed_animation with dissolve:
        xalign 0.9

    s1 bed one "— Ворота открытые."
    nameQuestion "— Похоже, они увидели то летающее чучело и посчитали, что оно гонится за нами."
    nameQuestion "— Но всё же рискованно открывать ворота когда он здесь!"
    nameQuestion "— А какая ему разница как к нам залетать."
    nameQuestion "—..."

    scene friend_solo_inside with dissolve
    play sound door_opening

    show subaru_one_bed_animation with dissolve:
        xalign 0.1
    show subaru_two_bed_animation with dissolve
    show subaru_three_bed_animation with dissolve:
        xalign 0.9

    "Первый Субару наклонился, и держал руками колени, таким образом успокаивая свой организм."

    #show

    "Несколько Субару, что стояли сверху, подошли к ним для ознакомления с ситуацией."
    #show

    show screen back_butt
    scene end with dissolve
    "Чтобы закончить игру нажмите на стрелочку."
    return