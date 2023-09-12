# 2 Глава: Нужно больше чем три?
label chapterTwo:
    scene black with dissolve
    $ renpy.movie_cutscene("videos/2chapter.ogv")

    play music forest
    scene forest_meadow with dissolve
    show subaru_one_animation with dissolve:
        xalign 0.1
    show subaru_two_animation with dissolve
    show subaru_three_animation with dissolve:
        xalign 0.9
    show leaves with dissolve
    s3 three "— Неужто. {w}последний?"
    s2 two "— Нет, ещё рано судить."
    s2 two "— Пусть он и назвался новеньким, он может быть шпионом от Макаки или КПфагов, не стоит ослаблять бдительность."
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
    "'Это пользователь под ником: Резо'"
    "'Способность: закрыта'"
    "'Время до открытия: 23.29.14-13-12'"

    s3 three "— Он. действительно последний!"
    s3 three "— Но, если у кого-то есть способность изменять информацию, подаренную Ирисом?"
    s3 three "— Нет, это невозможно изменить."
    s3 three "— Ребята! Вы видели?! Его ник!"
    "Двое Субару по просьбе третьего посмотрели на таблицу, которая показывала всем: 'Резо'."
    s1 one "— Тот самый Резо, которого хотят заполучить все три королевства?"
    s1 one "— Ура! Мы нашли его первыми!"
    s2 two "— Тише ты! Вокруг нас может кто быть и подслушивать."
    "~ Ирисом? Это он просил меня ввести ник? ~"
    "~ И похоже, что так же как в телеграмме если я спрошу у кого-то кто ты, то мне покажут информацию о нём. ~"
    rezo "— Кто ты?"
    hide rezotable with dissolve
    show subarotable with dissolve:
        xalign 0.5 yalign 0.1
    "Над вторым Субару появилась такая же таблица, как и надо мной:"
    "Это пользователь под ником: Малайзия"
    "Способность: закрыто."

    rezo "— Малайзия?"
    s2 two "— Да, у меня такой ник. Сам я кпфаг родом оттуда же решил такой ник сделать."
    rezo "— А почему способность закрыта?"
    hide subarotable with dissolve
    s2 two "— Это можно настроить в Ирисе, что бы твои способности не видели, но мы позже покажем."
    rezo "— Почему?"
    s2 two "— Сейчас намного важнее доставить тебя к нам - Френдсоло!"
    s2 two "— Вот, выпей."

    scene waterbag with dissolve
    "Один из Субару протянул ко мне кожаную сумку для воды, в которой, скорее всего, находилась какая-нибудь жидкость."
    rezo "— Что это?"
    s2 two "— Неважно, пей быстрее. {w}Мы не можем терять времени на болтовню."

    "Я решил подчинится и выпить предоставленный мне напиток."
    "После питья я ощутил странное чувство по всему телу."
    "Словно меня переполняла сила, что по ощущениям, выходила за рамки человеческих возможностей."

    scene forest_meadow with dissolve
    show subaru_one_animation with dissolve:
        xalign 0.1
    show subaru_two_animation with dissolve
    show subaru_three_animation with dissolve:
        xalign 0.9


    s2 two "— Чувствуешь что-то?"
    rezo "— Да."
    s2 two "— Отлично. Тогда следуй за нами. {w}Как выйдем на дорогу можешь бежать со всех ног."

    scene forest_path with dissolve
    "Трое Субару и я начали путь на восток, чтобы выйти из леса и попасть на дорогу."
    "В процессе передвижения я заметил, что эти Субару двигались очень ловко между деревьями и кустами."
    "Они во время перепрыгивали ямы и с лёгкостью взбирались на горбы."
    "Я сделал вывод о том, что они не первый раз здесь находятся."

    s2 two "— Не отставай."

    "~ А ведь я так и не промыл свою рану, придётся забыть на время о ней. ~"

    scene forest_road with dissolve
    show nasa_animation with dissolve:
        xalign 0.9 yalign 1.1
    show warrior with dissolve:
        xalign 0.1 yalign 1.1
    show leaves with dissolve

    "Спустя ещё 5 минут передвижений мы вышли на широкую дорогу."
    "Однако с левой стороны этой дороги находились воины КПфагов."

    s2 two "— Вот твари. Это наша часть леса, какого лешего они здесь ходят?"
    s1 one "— Неважно. На открытой местности мы будем достаточно быстры чтобы от них убежать."
    s1 one "— Самое главное чтобы Резо смог бежать так же быстро как и мы."
    s1 one "— Справишься?"

    "~ Забавно видеть, как двое Субару разговаривают друг с другом. ~"

    "Я не знал наверняка, получиться ли у меня бежать так же быстро как Субару, но другого пути не было, поэтому я ответил."
    rezo "— Да."

    "Мы вышли из кустов и начали бежать по дороге в правую сторону."

    "Воины КПфагов заметили нас и уже хотели начать бежать за нами, но остановились, поняв, что это было бесполезно."

    coePhagesLeader "— Где ещё один наш отряд?"
    coePhagesLeader "— Они не выходили на связь примерно 20 минут."
    coePhagesLeader "— Скорее потерпели поражение от этих чудиков."
    coePhagesLeader "— Между прочим, среди них был один 'не Субару' и при этом он не похож на кого-то из элиты Френдсоло."
    coePhagesLeader "— Что думаете?"
    coePhages "— Может, тот самый последний?"
    coePhages "— Такое совпадение. тяжело верится."

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

    s1 one "— Хорошо, передохнём немного."
    rezo "— Сколько нам ещё бежать?"
    s2 two "— Минут 10."
    s2 two "— Ещё выпьешь?"

    rezo "— Пожалуй не откажусь."

    "Один из Субару кинул мне тот же мешок для воды."

    s2 two "— Можешь всю выпить."
    rezo "— А как же вы?"
    s2 two "— Мы и без этого справимся. И не такие расстояния бежали без воды."
    rezo "— Кстати, я пока всё это время был с вами заметил, что пусть вы и выглядите прямо как Субару Натсуки."
    rezo "— Но если присмотреться, то у каждого есть особенность, что отличает его от другого Субару."
    rezo "— К примеру цвет глаз, рост, форма носа и так далее."
    s3 three "— Ага. Просто наш король сказал всем переодеться как этот Субару, а не то он нас выселит."
    rezo "— И вы согласились на это?"
    s3 three "— Если бы это было просто ради его прихоти, то конечно же нет."
    s3 three "— Но от этого есть несколько практичных плюсов."
    rezo "— Каких?"
    s2 two "— Мы пока не так сильно тебе доверяем, чтобы рассказывать обо всём."
    rezo "— Понимаю."

    "~ А ещё я заметил, что несмотря на то, что король у них Френд они довольно хорошо мыслят и при этом организованы. ~"
    "~ Наверное это Свит постарался, так как его имя я тоже слышал от них. ~"
    "~ Но почему он с Френдом? ~"
    "~ Самое логичное, что приходит на ум, так это то, что он выглядит как Юмеко. ~"
    "~ По этой причине КПфаги могут ненавидеть его даже сильнее чем Френда, который, скорее всего, выглядит как Ягами. ~"
    "~ То же самое может относиться к Сузаку и Шашлыку. ~"
    "~ Это лишь мои догадки, но думаю в итоге я прав. ~"

    s1 one "— Побежали?"
    rezo "— Ага."

    scene forest_man with dissolve
    show nasa_animation with dissolve
    s3 three "— Смотрите! Прячемся!"
    "Вдруг в небе не пойми откуда появился человек, который осматривал территорию леса."
    hide nasa_animation with dissolve
    "Через несколько секунд он улетел на восток, в то время как королевство Френдсоло находилось на юго-востоке."

    scene forest_continue with dissolve
    show subaru_one_animation with dissolve:
        xalign 0.1
    show subaru_two_animation with dissolve
    show subaru_three_animation with dissolve:
        xalign 0.9

    s1 one "— Скорость помогла нам скрыться."
    "~ Тут даже полёты есть? ~"
    rezo "— Кто это был?"

    s3 three "— Сильнейший воин из КПфагов."
    s3 three "— Мы сами не знаем как его зовут, но он очень проблемный."
    s3 three "— В особенности из-за его полётов."

    rezo "— Будем через лес пробираться?"

    s2 two "— Нет времени."
    s2 two "— Эффект от напитка скоро спадёт и мы не сможем добежать так быстро."
    s2 two "— Нужно рискнуть."

    rezo "— Окей."

    "~ Если они боятся того летающего воина, значит ли это, что сейчас я на стороне слабых? ~"
    "~ Стоит ли мне, как он опять появится, сказать, что меня на самом деле захватили Субару и я из королевства КПфагов? ~"
    "~ Так я смогу стать на сторону сильных и увеличить свои шансы на выживание. ~"
    "~ Хотя не факт, что тот человек поверит мне. ~"
    "~ Пока останусь вместе с Субару, а если ситуация ухудшиться, то стану на их сторону и выставлю Субару с плохой стороны. ~"

    s2 two "— Готовы? Вперёд!"

    scene forest_continue_two with dissolve

    "В этот момент мы продолжили бег от начальной позиции в королевство Френдсоло."

    show nasa_animation with dissolve

    "Однако, через 6-7 минут нас обнаружил летающий воин."
    "Точнее не нас самих, а большой след от поднятой ими, на дороге, пыли."

    nasaQuestion "~ Кто то бегал по дороге? ~"
    nasaQuestion "~ А в той стороне у нас. Френдсоло. ~"
    nasaQuestion "~ Пока я летал, я пересекал эту дорогу дважды. ~"
    nasaQuestion "~ Наверное, они заметили меня первый раз, а после выждали момент и начали убегать. ~"
    nasaQuestion "~ Что ж, посмотрим как далеко они убежали. ~"

    scene forest_fly with dissolve
    show nasa_animation with dissolve

    "Воин, всё также находясь в воздухе и летая при помощи силы мысли направился в сторону королевства Френдсоло."
    "Погода была не очень ясной, но дождя ожидать явно не стоило."
    "В этот момент кто-то попытался связаться с этим воином при помощи телепатии."
    
    nasaQuestion "— Первый отряд?"
    nasaQuestion "— Мы вас потеряли, где вы находитесь?"

    coePhages "— Господин Наса, мы встретили чудиков из королевства Френдсоло и они напали на нас, а после где-то укрылись."
    coePhages "— Будь они прокляты."

    nasa "— Я сейчас преследую их и скоро настигну. Меньше минуты лететь."

    coePhages "— Отлично! Вы как всегда неподражаем."

    nasa "— Займитесь своими делами. До связи."
    
    "Наса отключил телепатическую связь и продолжил лететь в сторону королевства Френдсоло."

    scene friend_solo with dissolve
    show nasa_animation with dissolve

    "С его положения уже можно было видеть само очертание королевства."
    "Его стены высотой до 5 метров из семена и камня выглядели довольно уродливо и ненадёжно."
    "Где-то посередине из видимого обзора находились небольшие ворота."
    hide nasa_animation with dissolve
    show subaru_one_animation with dissolve:
        xalign 0.1
    show subaru_two_animation with dissolve
    show subaru_three_animation with dissolve:
        xalign 0.9

    "А прямо над ними стояли несколько Субару и осматривали округу."
    hide subaru_one_animation with dissolve
    hide subaru_two_animation with dissolve
    hide subaru_three_animation with dissolve
    show nasa_animation with dissolve
    "Наса оценил расстояние от своей позиции до ворот Френда примерно в два километра."

    nasa "— Придётся потратить две минуты чтобы догнать бездарей."
    hide nasa_animation with dissolve

    "В ту же секунду Наса ускорился и начал догонять бегущих Субару."
    "Однако последние не заметили угрозы, поскольку бежали со всех сил и не оборачивались."
    "Даже если бы они обернулись, то поднятая ими пыль мешала бы обзору"
    "Поэтому они решили бежать со всех сил к стенам королевства."
    "Однако Наса был более чем в два раза быстрее бегунов."
    "Она уже оказалась на одном уровне с Субару, а после, полетела вперёд и приземлилась прямо перед ними."

    show subaru_one_bed_animation with dissolve:
        xalign 0.1
    show subaru_two_bed_animation with dissolve
    show subaru_three_bed_animation with dissolve:
        xalign 0.9

    "Бегущие Субару и я остановились где то в 10 метрах от Насы."
    "Их лица изменились смесью гнева и волнения."
    "Находясь возле них я заметил трясущиеся колени, а также стекавший из них пот."
    
    coePhages "— Куда бежим?"
    s2 two bed "— Тебя это не должно волновать, КПфаг."
    hide subaru_one_bed_animation with dissolve
    hide subaru_two_bed_animation with dissolve
    hide subaru_three_bed_animation with dissolve
    show nasa_animation with dissolve
    "Наса только пожал плечами и сказал:"
    
    nasa "— Мы все тут кпфаги по факту, так что вы не гении."
    nasa "— Лучше скажите, Френд разрешил кому-то из вас не быть как Субару?"
    
    "Наса намекал на меня, которая своим видом отличалась от остальных трёх."
    "Прямо сейчас надо мной навис тяжелый выбор."
    "Попытаться пройти сквозь эту девушку, что всем своим внешним видом напоминала одну из тех, что стояли на аватарке у Насы."
    "Или признатся в том, что я и есть Резо и стать на её сторону?"
    "Сейчас я был глубоко уверен в том, что передо мной стоял Наса."
    "Пока я раздумывал над ответом, один из его новых товарищей сказал."

    hide nasa_animation with dissolve
    show warrior with dissolve
    
    coePhages "— И что если да?"
    coePhages "— Ничего. {w}Ничего хорошего для вас."

    hide warrior with dissolve
    show nasa_animation with dissolve
    
    rezo "— Это я, Резо."

    "На лице Насы появилось удивление."
    "Он встал в обычную позу, однако сознательно был более напряжён."

    nasa "— Докажи."
    show rezotable with dissolve:
        xalign 0.5 yalign 0.4
    "Мои товарищи посмотрели на меня тем же взглядом, что и на Насу."
    "Однако я не испытывал волнения, поскольку знал наверняка, кто передо мной."
    "Неспешно идя по пыльной дороге я приблизился к Насе на расстояние менее двух метров."
    
    rezo "— Кто я."
    
    "Наса посмотрел на нависший экран надо мной и его глаза стали квадратными от увиденного, а челюсть почти полностью отвалилась."
    "Даже казалось, что на некоторое время он перестал дышать."
    hide rezotable with dissolve
    nasa "— Вот это совпадение, не так ли?"
    nasa "— Ахахахах, я уже подумал что Свит настолько отчаялся в поисках победы над нами."
    nasa "— Что переодел одного из Субару в обычного человека и выдал за Резо."
    rezo "— Ну, я посчитал что мне лучше сказать о том, что я это я, а не то ты бы меня избил."
    nasa "— А где они?"
    
    "Наса и я осмотрели всё вокруг и не увидели ни одного Субару."
    "Только следы пыли от бега по краям дороги."
    
    nasa "— Вот же крысы."
    nasa "— Ладно, не важно. Я так понимаю, ты уже выбрал нашу сторону?"
    rezo "— Да."
    rezo "— Даже если бы они сопротивлялись и я остался последним, я бы всё равно рассказал о себе и присоединился."
    nasa "— И сейчас у тебя много вопросов, да?"
    rezo "— Угу."
    nasa "— Прости, но придётся подождать ещё немного."
    nasa "— Не хочешь, побыть шпионом в Френдсоло? Потом мы тебя заберём."
    rezo "— Ты не боишься, что я могу передумать?"
    nasa "— Будет очень жаль если так. Но я уверена что ты вряд ли так сделаешь."
    nasa "— Как минимум ты мог заметить, что мои воины одеты в латы и обладают неплохим оружием."
    nasa "— В то время как те Субару его не имели."
    nasa "— Этого достаточно, чтобы сделать вывод о том, что наша экономика и развитие лучше, чем у этих бездарей."
    rezo "~ А ещё количество КПфагов было больше, чем Френдсоло. ~"
    rezo "~ Это не показатель, но возможно, между этими странами есть также большая разница в численности. ~"
    
    nasa "— Что такое?"
    coePhages "— Господин Наса, нам нужна ваша помощь!"
    nasa "— Сразу как попадёшь в Френдсоло попытайся найти Ичиносе, что продаёт эдиты в прозрачных упаковках."
    nasa "— До скорого, Резо."

    hide nasa_animation with dissolve
    
    "После этих слов, Наса поднялся в воздух и улетел на север."
    "Только облако пыли осталось после него."
    nasa "— Говорите, где вы?"
    
    rezo "— Меня оставили один на один с этой дорогой."
    rezo "— Думаю, она ведёт прямо в Френдсоло и не разделяется на право и лево."
    
    "~ А сейчас, можно всё обдумать. ~"
    "~ И самое первое, во Френдсоло мне нужно найти Нирвокса, верно? ~"
    "~ Никто другой, из знакомых, не приходит на ум. ~"
    
    "— А ещё. Я так и не продезинфицировал свою рану."

    jump chapterThree
    return