# 3 Глава: Старый новенький
label chapterThree:
    scene black with dissolve
    $ renpy.movie_cutscene("videos/3chapter.avi")

    scene forest_trail with dissolve

    show subaru_one_bed_animation with dissolve:
        xalign 0.1
    show subaru_two_bed_animation with dissolve
    show subaru_three_bed_animation with dissolve:
        xalign 0.9

    malaysia two bed "— Мы уже оторвались от него."
    s1 one bed "— Аааа, как же обидно что пришлось оставить Резо."
    s1 one bed "— А так могли бы повышение заслужить."
    s3 three bed "— Вы дебилы. Куда важнее, что мы остались целыми и смогли прибежать обратно."

    hide subaru_one_bed_animation with moveoutleft
    hide subaru_two_bed_animation with moveoutleft
    hide subaru_three_bed_animation with moveoutleft

    scene friend_solo_left with dissolve
    show subaru_one_bed_animation with dissolve:
        xalign 0.1
    show subaru_two_bed_animation with dissolve
    show subaru_three_bed_animation with dissolve:
        xalign 0.9

    s1 one bed "— Ворота открытые."
    nameQuestion "— Похоже, они увидели то летающее чучело и посчитали, что оно гонится за нами."
    nameQuestion "— Но всё же рискованно открывать ворота когда он здесь!"
    nameQuestion "— А какая ему разница как к нам залетать."
    nameQuestion "—..."

    hide subaru_one_bed_animation with moveoutleft
    hide subaru_two_bed_animation with moveoutleft
    hide subaru_three_bed_animation with moveoutleft

    scene friend_solo_inside with dissolve
    play sound door_opening
    play music friend_solo_inside
    
    show subaru_one_bed_animation with dissolve:
        xalign 0.1
    show subaru_two_bed_animation with dissolve
    show subaru_three_bed_animation with dissolve:
        xalign 0.9

    hide subaru_one_bed_animation with moveoutleft
    hide subaru_two_bed_animation with moveoutleft
    hide subaru_three_bed_animation with moveoutleft

    "Все три Субару благополучно добрались внутрь королевства. Сразу после закрытия ворот они решили перевести дух."
    "Первый Субару наклонился, и держал руками колени, таким образом успокаивая свой организм."

    show subaru_four_animation with dissolve:
        xalign 0.01
    show subaru_five_animation with dissolve
    show subaru_six_animation with dissolve:
        xalign 1.02
    
    "Несколько Субару, что стояли сверху, подошли к ним для ознакомления с ситуацией."

    hide subaru_four_animation with moveoutleft
    hide subaru_five_animation with moveoutleft
    hide subaru_six_animation with moveoutleft

    show subaru_seven_animation with dissolve:
        xalign 0.55

    "Этим же действиям подверглись и соседние Субару, что переносили оружие и бочки с напитками."

    hide subaru_seven_animation with moveoutleft
    show subaru_one_bed_animation with dissolve:
        xalign 0.1
    show subaru_two_bed_animation with dissolve
    show subaru_three_bed_animation with dissolve:
        xalign 0.9
    "Оценив краем глаза обстановку, бегуны поняли, что все волновались о них и уже начали подготавливать отряд, чтобы дать отпор Насе."

    s4 four "— Он вас отпустил? Как вам удалось остаться в живых?"
    s5 five "— Может, они через лес бежали, чтобы этот самолёт из сала не достал их."
    s6 six "— Много напитков потратили, а узнали что нибудь?"

    "Бегунов окружили и телами и вопросами, взглядами и дыханием, интересом и жалостью."

    s1 one bed "— Серполле…"
    "Все сразу поняли суть этих слов."

    s3 three bed "— Нам нужно доложить ему полученную информацию."

    malaysia two bed "— Я направлюсь в башню на юге, к капитану."

    s1 one bed "— Я пойду в центр королевства и скажу о случившемся Серполле."
    "Третий Субару утвердительно кивнул."
    s3 three bed "~ Я понял, что моя задача - рассказать о случившемся капитану Северо-Западной башни. ~"

    hide subaru_one_bed_animation with moveoutleft
    hide subaru_two_bed_animation with moveoutleft
    hide subaru_three_bed_animation with moveoutleft

    show subaru_four_animation with dissolve:
        xalign 0.01
    show subaru_five_animation with dissolve
    show subaru_six_animation with dissolve:
        xalign 1.02

    "Другие Субару, что окружали их, были немного в недоумении от того, что же они собирались передать."

    s5 five "— Может, нам позвать тех кто вам нужен."

    malaysia two bed "— Нет."
    malaysia two bed "— Будет быстрее, если мы сами придём и доложим."
    s1 one bed "— Только нужно напиток выпить, а то мы все свои уже истратили."

    subaru_from_the_crowd "— Сейчас!"

    "Один Субару из толпы, что стоял возле бочек с напитком."
    "Взял несколько кожаных мешочков, что находились неподалёку, и наполнил их содержимым."
    "Однако, он выполнял эту процедуру слишком долго."
    "В итоге Малайзия и двое Субару одолжили напитки у других Нацуки."
    "Преимущественно тех, чьи напитки обладали эффектом ускорения."

    play sound door_opening
    "А после убежали, выпив содержимое одолженных мешочков."

    subaru_from_the_crowd "— Вот ваши напитки…"
    "Это огорчило его."

    "Но вскоре, он вернулся в обычное состояние и передал набранные кожаные мешочки тем Субару."
    "Те одолжили свои мешочки трём прибывшим бегунам."
    "Однако, уже зародившуюся грусть этим не убрать."
    "Малайзия и остальные двое Субару рассредоточились, и бежали по разным прямым дорогам, что вели к центру, и краям королевства."
    "Однако путь, ведущий в центр, отличается от остальных."
    "Перед тем, как попасть в центральную зону, они должны пройти ворота второй стены."
    "К счастью, у них есть на это разрешение."
    "Тем не менее, во вторые ворота всегда забегал только один Субару из всей троицы, пусть разрешение и имел каждый из них."

    scene friend_solo with dissolve
    play music forest
    "Взгляни на карту Фреднсоло."
    play music menu_music

    show screen map
    ""