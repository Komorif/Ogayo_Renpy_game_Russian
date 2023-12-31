# 2 Глава: Нужно больше чем три?
label chapterTwo:
    scene black with dissolve
    $ renpy.movie_cutscene("videos/2chapter.avi")

    play music forest
    scene forest_meadow with dissolve
    show subaru_one_animation with dissolve:
        xalign 0.1
    show subaru_two_animation with dissolve
    show subaru_three_animation with dissolve:
        xalign 0.9
    show leaves with dissolve
    s2 two "— Неужто. {w}последний?"
    s3 three "— Нет, ещё рано судить."
    s3 three "— Пусть он и назвался новеньким, он может быть шпионом от Макаки или КПфагов, не стоит ослаблять бдительность."
    "Субару начали переговариваться между собой."
    play sound leaves
    hide leaves with dissolve
    "Я в этот момент вышел из кустов, в которых сидел всё это время."
    "Только сейчас я вспомнил о том, что порезался по пути к месту битвы и осмотрел свою рану."
    rezo "— Извините, у вас не найдётся воды?"
    "Трое Субару посмотрели на меня и быстро приблизились, окружив со всех сторон."
    s3 three "— Кто ты?"
    "Я был слегка удивлён и напуган, однако по ним было видно, что они не собирались атаковать, и скорее всего не будут."
    rezo "— Я же сказал, я новичок здесь и прошу чтобы мне объяснили что к чему."

    show rezotable with dissolve:
        xalign 0.5 yalign 0.4
    "Вдруг надо мной появилась какая-то таблица."
    "'Способность: закрыта'"
    "'Время до открытия: 23.29.14-13-12'"

    s1 one "— Он. действительно последний!"
    s1 one "— Но, если у кого-то есть способность изменять информацию, подаренную Ирисом?"
    s3 three "— Нет, это невозможно изменить."
    s1 one "— Ребята! Вы видели?! Его ник!"
    "Двое Субару по просьбе третьего посмотрели на таблицу, которая показывала всем: 'Резо'."
    s1 one "— Тот самый Резо, которого хотят заполучить все три королевства?"
    s1 one "— Ура! Мы нашли его первыми!"
    s3 three "— Тише ты! Вокруг нас может кто быть и подслушивать."
    "~ Ирисом? Это он просил меня ввести ник? ~"
    "~ И похоже, что так же как в телеграмме, если я спрошу у кого-то кто ты, то мне покажут информацию о нём. ~"
    rezo "— 'Кто ты?'"
    hide rezotable with dissolve
    show subarotable with dissolve:
        xalign 0.5 yalign 0.1
    "Над вторым Субару появилась такая же таблица, как и надо мной."
    "Это пользователь под ником: Малайзия."
    "Способность: закрыто."

    rezo "— Малайзия?"
    malaysia two "— Да, у меня такой ник. Сама я кпфаг родом оттуда же решила такой ник сделать."
    rezo "— А почему способность закрыта?"
    hide subarotable with dissolve
    malaysia two "— Это можно настроить в Ирисе, чтобы твои способности не видели, но мы позже покажем."
    rezo "— Почему?"
    s1 one "— Сейчас намного важнее доставить тебя к нам - Френдсоло!"
    s3 three "— Вот, выпей."

    hide subaru_one_animation with moveoutleft
    hide subaru_three_animation with moveoutright

    scene waterbag with dissolve
    "Один из Субару протянул ко мне кожаную сумку для воды, в которой, скорее всего, находилась какая-нибудь жидкость."
    rezo "— Что это?"
    s3 three "— Неважно, пей быстрее. {w}Мы не можем терять времени на болтовню."

    "Я решил подчинится и выпить предоставленный мне напиток."
    "После питья я ощутил странное чувство по всему телу."
    "Словно меня переполняла сила, что по ощущениям, выходила за рамки человеческих возможностей."

    scene forest_meadow with dissolve
    show subaru_one_animation with dissolve:
        xalign 0.1
    show subaru_two_animation with dissolve
    show subaru_three_animation with dissolve:
        xalign 0.9


    s3 three "— Чувствуешь что-то?"
    rezo "— Да."
    s3 three "— Отлично. Тогда следуй за нами."
    s3 three "— Как выйдем на дорогу можешь бежать со всех ног."

    hide subaru_one_animation with moveoutleft
    hide subaru_two_animation with moveoutleft
    hide subaru_three_animation with moveoutleft

    scene forest_path with dissolve
    "Трое Субару и я начали путь на восток, чтобы выйти из леса и попасть на дорогу."
    "В процессе передвижения я заметил, что эти Субару двигались очень ловко между деревьями и кустами."
    "Они во время перепрыгивали ямы и с лёгкостью взбирались на горбы."
    "Я сделал вывод о том, что они не первый раз здесь находятся."

    malaysia two "— Не отставай."

    "~ А ведь я так и не промыл свою рану, придётся забыть на время о ней. ~"

    scene forest_road with dissolve
    show warrior with dissolve
    show leaves with dissolve

    "Спустя ещё 5 минут передвижений мы вышли на широкую дорогу."
    "Однако с левой стороны этой дороги находились воины КПфагов."

    s1 one "— Твари. Это наша часть леса, какого лешего они здесь ходят?"
    malaysia two "— Неважно. На открытой местности мы будем достаточно быстры чтобы от них убежать."
    malaysia two "— Самое главное - чтобы Резо смог бежать также быстро как и мы."
    malaysia two "— Справишься?"

    "~ Забавно видеть, как двое Субару разговаривают друг с другом. ~"

    "Я не знал наверняка, получиться ли у меня бежать также быстро как Субару, но другого пути не было, поэтому я ответил."
    rezo "— Да."

    "Мы вышли из кустов и начали бежать по дороге в правую сторону."

    "Воины КПфагов заметили нас и уже хотели начать бежать за нами, но остановились, поняв, что это было бесполезно."

    KpPhageSquad "— Где ещё один наш отряд?"
    KpPhageSquad "— Они не выходили на связь примерно 15 минут."
    KpPhageSquad "— Скорее потерпели поражение от этих чудиков."
    KpPhageSquad "— Между прочим, среди них был один 'не Субару' и при этом он не похож на кого-то из элиты Френдсоло."
    KpPhageSquad "— Что думаете?"
    coePhages "— Может, тот самый последний?"
    coePhages "— Такое совпадение. Тяжело верится."

    hide warrior with moveoutleft

    scene forest_road_two with dissolve
    "Тем временем, я и трое Нацуки бежали по пыльной дороге, чтобы как можно скорее попасть в Френдсоло."
    "Я отставал от них, однако всё равно бежал довольно быстро, как для обычного человека."
    "Субару были удивлены тем, что я не врезался в дерево при первой же попытке бега, и это вызвало в них уважение ко мне."
    "Они понемногу начали понимать, почему меня хотят заполучить все три королевства."
    "Через примерно 5 минут бега я попросил перерыв."

    show subaru_one_animation with dissolve:
        xalign 0.1
    show subaru_two_animation with dissolve
    show subaru_three_animation with dissolve:
        xalign 0.9

    s3 three "— Хорошо, передохнём немного."
    rezo "— Сколько нам ещё бежать?"
    s3 three "— Минут 10."
    malaysia two "— Ещё выпьешь?"

    rezo "— Пожалуй не откажусь."

    s3 three "Малазия кинул мне тот же мешок для воды."

    malaysia two "— Можешь всю выпить."
    rezo "— А как же вы?"
    s3 three "— Мы и без этого справимся."
    s3 three "— И не такие расстояния бежали без воды."
    rezo "— Кстати, я пока всё это время был с вами заметил, что пусть вы и выглядите прямо как Субару Натцуки."
    rezo "— Но если присмотреться, то у каждого есть особенность, что отличает его от другого Субару."
    rezo "— К примеру цвет глаз, рост, форма носа и так далее."
    s3 three "— Ага. Просто наш король сказал всем переодеться как этот Субару, а иначе он нас выселит."
    rezo "— И вы согласились на это?"
    s3 three "— Если бы это было просто ради его прихоти, то конечно же нет."
    s3 three "— Но от этого есть несколько практичных плюсов."
    rezo "— Каких?"
    s3 three "— Мы пока не так сильно тебе доверяем, чтобы рассказывать обо всём."
    rezo "— Понимаю."

    "~ А ещё я заметил, что несмотря на то, что король у них Френд они довольно хорошо мыслят и при этом организованы. ~"
    "~ Наверное это Свит постарался, так как его имя я тоже слышал от них. ~"
    "~ Но почему он с Френдом? ~"
    "~ Самое логичное, что приходит на ум, это то, что он выглядит как Юмеко. ~"
    "~ По этой причине КПфаги могут ненавидеть его даже сильнее чем Френда, который, скорее всего, выглядит как Ягами. ~"
    "~ Тоже самое может относиться к Сузаку и Шашлыку. ~"
    "~ Это лишь мои догадки, но думаю в итоге я прав. ~"

    s3 three "— Побежали?"
    rezo "— Ага."

    hide subaru_one_animation with moveoutleft
    hide subaru_two_animation with moveoutleft
    hide subaru_three_animation with moveoutleft

    scene forest_man with dissolve
    show nasa_animation with dissolve
    s1 one "— Смотрите! Прячемся!"
    "Вдруг в небе не пойми откуда появился человек, который осматривал территорию леса."
    hide nasa_animation with moveoutleft
    "Через несколько секунд он улетел на восток, в то время как королевство Френдсоло находилось на юго-востоке."

    scene forest_continue with dissolve
    show subaru_one_animation with dissolve:
        xalign 0.1
    show subaru_two_animation with dissolve
    show subaru_three_animation with dissolve:
        xalign 0.9

    rezo "— Скорость помогла нам скрыться."
    rezo "~ Тут даже полёты есть? ~"
    rezo "— Кто это был?"

    s3 three "— Сильнейший воин из КПфагов."
    s1 one "— Мы сами не знаем как его зовут, но он очень проблемный."
    s3 three "— В особенности из-за его полётов."

    rezo "— Будем через лес пробираться?"

    s3 three "— Нет времени."
    malaysia two "— Эффект от напитка скоро спадёт и мы не сможем добежать так быстро."
    malaysia two "— Нужно рискнуть."

    rezo "— Окей."

    rezo "~ Если они боятся того летающего воина, значит ли это, что сейчас я на стороне слабых? ~"
    rezo "~ Стоит ли мне, как он опять появится, сказать, что меня на самом деле захватили Субару и я из королевства КПфагов? ~"
    rezo "~ Так я смогу стать на сторону сильных ~"
    rezo "~ И увеличить свои шансы на выживание. ~"
    rezo "~ Хотя не факт, что тот человек поверит мне. ~"
    rezo "~ Пока останусь вместе с Субару, а если ситуация ухудшиться, то стану на сторону КПфага и выставлю Субару в плохом свете. ~"

    malaysia two "— Готовы? Вперёд!"

    hide subaru_one_animation with moveoutleft
    hide subaru_two_animation with moveoutleft
    hide subaru_three_animation with moveoutleft

    scene forest_continue_two with dissolve

    "В этот момент, мы продолжили бег от начальной позиции в королевство Френдсоло."

    show nasa_animation with dissolve

    "Однако, через 6-7 минут их обнаружил летающий воин."
    "Точнее не нас самих, а большой след от поднятой нами, на дороге, пыли."

    nasaQuestion "~ Кто-то бегал по дороге? ~"
    nasaQuestion "~ А в той стороне у нас. Френдсоло. ~"
    nasaQuestion "~ Пока я летал, я пересекал эту дорогу дважды. ~"
    nasaQuestion "~ Наверное, они заметили меня первый раз, а после выждали момент и начали убегать. ~"
    nasaQuestion "~ Что ж, посмотрим как далеко они убежали. ~"

    hide nasa_animation with moveoutleft

    scene forest_fly with dissolve
    show nasa_animation with dissolve

    "Воин, всё также находясь в воздухе и летая при помощи силы мысли направился в сторону королевства Френдсоло."
    "Погода была не очень ясной, но дождя ожидать явно не стоило."
    "В этот момент кто-то попытался связаться с этим воином при помощи телепатии."
    
    nasaQuestion "— Первый отряд?"
    coePhages "— Мы вас потеряли, где вы находитесь?"
    coePhages "— Господин Наса, мы встретили чудиков из королевства Френдсоло и они напали на нас, а после где-то укрылись."

    nasa "— Будь они прокляты."
    nasa "— Я сейчас преследую их и скоро настигну. Меньше минуты лететь."

    coePhages "— Отлично! Вы как всегда неподражаем."

    nasa "— Займитесь своими делами. До связи."
    
    "Наса отключил телепатическую связь и продолжил лететь в сторону королевства Френдсоло."

    hide nasa_animation with moveoutleft

    scene friend_solo with dissolve
    show nasa_animation with dissolve

    "С его положения уже можно было видеть само очертание королевства."
    "Его стены высотой до 5 метров из семена и камня выглядели довольно уродливо и ненадёжно."
    "Где-то посередине из видимого обзора находились небольшие ворота."
    hide nasa_animation with moveoutleft

    show subaru_four_shadow with dissolve:
        xalign 0.01
    show subaru_five_shadow with dissolve
    show subaru_six_shadow with dissolve:
        xalign 1.02

    "А прямо над ними стояли несколько Субару и осматривали округу."
    hide subaru_four_shadow with moveoutleft
    hide subaru_five_shadow with moveoutleft
    hide subaru_six_shadow with moveoutleft

    show nasa_animation with dissolve
    "Наса оценил расстояние от своей позиции до ворот Френдсоло примерно в два километра."

    nasa "— Придётся потратить две минуты чтобы догнать бездарей."
    hide nasa_animation with moveoutleft

    "В ту же секунду Наса ускорился и начал догонять нас."
    "Однако мы не заметили угрозы, поскольку бежали со всех сил и не оборачивались."
    "Даже если бы мы обернулись, то поднятая нами пыль мешала бы обзору."
    "Поэтому мы решили бежать со всех сил к стенам королевства."
    "Однако Наса был более чем в два раза быстрее."
    "Он уже оказался на одном уровне с Субару, а после, полетел вперёд и приземлился прямо перед ними."

    show subaru_one_bed_animation with dissolve:
        xalign 0.1
    show subaru_two_bed_animation with dissolve
    show subaru_three_bed_animation with dissolve:
        xalign 0.9

    "Субару и я остановились где-то в 10 метрах от Насы."
    "Их лица изменились смесью гнева и волнения."
    "Находясь возле них я заметил трясущиеся колени, а также стекавший из них пот."
    
    nasa "— Куда бежим?"
    s3 three bed "— Тебя это не должно волновать, КПфаг."
    hide subaru_one_bed_animation with moveoutleft
    hide subaru_two_bed_animation with moveoutleft
    hide subaru_three_bed_animation with moveoutleft
    show nasa_animation with dissolve
    "Наса только пожал плечами и сказал."
    
    nasa "— Мы все тут кпфаги по факту, так что вы не гении."
    nasa "— Лучше скажите, Френд разрешил кому-то из вас не быть как Субару?"
    
    "Наса намекал на меня, потому что своим видом я отличался от остальных Субару."
    "Прямо сейчас надо мной навис тяжелый выбор."
    "Попытаться пройти сквозь эту девушку, что всем своим внешним видом напоминала одну из тех, что стояли на аватарке у Насы."
    "Или признатся в том, что я и есть Резо и стать на её сторону?"
    "Сейчас я был глубоко уверен в том, что передо мной стоял Наса."
    "Пока я раздумывал над ответом, Третий субару сказал."
    
    s3 three "— И что, если да?"
    nasa "— Ничего. {w}Ничего хорошего для вас."
    
    rezo "— Это я, Резо."

    "На лице Насы появилось удивление."
    "Он встал в обычную позу, однако сознательно был более напряжён."

    nasa "— Докажи."
    "Мои товарищи посмотрели на меня тем же взглядом, что и на Насу."
    "Однако я не испытывал волнения, поскольку знал наверняка, кто передо мной."
    "Неспешно идя по пыльной дороге я приблизился к Насе на расстояние менее двух метров."
    
    rezo "— Кто я."
    show rezotable_two with dissolve:
        xalign 0.5 yalign 0.4
    
    "Наса посмотрел на нависший экран надо мной и его глаза стали квадратными от увиденного, а челюсть почти полностью отвалилась."
    "Даже казалось, что на некоторое время он перестал дышать."
    hide rezotable_two with dissolve
    nasa "— Вот это совпадение, не так ли?"
    nasa "— Ахахахах, я уже подумал что Свит настолько отчаялся в поисках победы над нами."
    nasa "— Что переодел одного из Субару в обычного человека и выдал за Резо."
    rezo "— Ну, я посчитал что мне лучше сказать о том, что я это я, а не то ты бы меня избил."
    nasa "— А где Субару?"
    
    "Наса и я осмотрели всё вокруг и не увидели ни одного Субару."
    "Только следы пыли от бега по краям дороги."
    
    nasa "— Вот же крысы."
    nasa "— Ладно, не важно. Я так понимаю, ты уже выбрал нашу сторону?"
    rezo "— Да."
    rezo "— Даже если бы они сопротивлялись и я остался последним, я бы всё равно рассказал о себе и присоединился."
    nasa "— И сейчас у тебя много вопросов, да?"
    rezo "— Угу."
    nasa "— Прости, но придётся подождать ещё немного."
    nasa "— Не хочешь, побыть шпионом в Френдсоло?"
    nasa "— Потом мы тебя заберём."
    rezo "— Ты не боишься, что я могу передумать?"
    nasa "— Будет очень жаль если так. Но я уверен, что ты вряд ли так сделаешь."
    nasa "— Как минимум ты мог заметить, что мои воины одеты в латы и обладают неплохим оружием."
    nasa "— В то время как те Субару его не имели."
    nasa "— Этого достаточно, чтобы сделать вывод о том, что наша экономика и развитие лучше, чем у этих бездарей."
    rezo "~ А ещё количество КПфагов было больше, чем Френдсоло. ~"
    rezo "~ Это не показатель, но возможно, между этими странами есть также большая разница в численности. ~"
    
    nasa "— Что такое?"
    coePhages "— Господин Наса, нам нужна ваша помощь!"
    nasa "— Сразу как попадёшь в Френдсоло попытайся найти Ичиносе, что продаёт эдиты в прозрачных упаковках."
    nasa "— До скорого, Резо."

    hide nasa_animation with moveoutleft
    
    "После этих слов, Наса поднялся в воздух и улетел на север."
    "Только облако пыли осталось после него."
    nasa "— Говорите, где вы?"
    
    rezo "— Меня оставили один на один с этой дорогой."
    rezo "— Думаю, она ведёт прямо в Френдсоло и не разделяется на право и лево."
    
    "~ А сейчас, можно всё обдумать. ~"
    "~ И самое первое, во Френдсоло мне нужно найти Нирвокса, верно? ~"
    "~ Никто другой, из знакомых, не приходит на ум. ~"
    $ persistent.twoChapter = True
    
    $ persistent.menuTwoChapter = True
    $ persistent.menuOneChapter = False
    "— А ещё. Я так и не продезинфицировал свою рану."


    jump chapterThree
    return