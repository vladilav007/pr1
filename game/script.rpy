﻿default book = False
default slo = Dissolve(1.0)
define i = Character(_("Я"), color="#19070B")
define ni = Character(_("Морозиха"), color="#19070B")
define gg  = Character(_("Гопари"), color="#04B404")
define bom = Character(_("Бродяга"), color="#3B240B")
define dan = Character(_("Даня"), color="#3B240B")
define mav = Character(_("Мавка"), color="#FF00FF")
define vod = Character(_("Водяной"), color="#3B240B")
define ed = Character(_("Эдик"), color="#808000")

label start:
    $ test = 0
    with slo
    play music "music/anime.mp3" fadeout 1
    scene room
    show muxa
    i  "Сил учиться нет."
    i  "Скоро экзамены."
    i  "Но я действительно чувствую, что время до поступления трачу в никуда."
    i  "Нужно встать и сделать сегодня действительно что-то великое.."
    i  "На счет три!"
    i  "Oдин!"
    i  "Два!"
    i  "Три!"
    scene street
    "*Сейчас 15:00.*"
    "*Первый экзамен послезавтра.*"
    show ali:
        xalign 0.0
        yalign 1.0
    with slo
    i  "Cхожу в магаз и куплю книжку для подготовки, авось выучу.."
    with slo
    "Незнакомец" "Виталик!"
    "Незнакомец" "Виталя!   "
    "Незнакомец" " Погоди!  "
    "*Голос был до боли знакомым..*"
    stop music
    "*Hа ступеньках заброшеного клуба сидели Сашка и Даня.*"
    show sasha2:
        xalign 1.0
        yalign 1.0
    show martun2:
        xalign 0.7
        yalign 1.0
    dan "Пошли бухлишка купим и затусим. "
    menu:
        "Го бухнем хули.":
            
            $ test = 1
        "А почему бы и нет, собстенно говоря.":
            $ test = 2
    if test == 1 or test == 2:
        "Сашка" "О, мужик, уважаю. "
    jump glava1

label glava1:  
    with slo
    
    play music "music/draka.mp3" fadeout 1
    scene bg ttt
    with slo
    show ali
    show sasha2:
        xalign 0.0
        yalign 1.0
    "Сашка" "Скидуемся, ребята."
    i  "Йомайо." 
    "*Подумал я тихо*"
    i  "А по сколько?" 
    show martun2:
        xalign 1.0
        yalign 1.0
    dan"Пошли зайдем, там и решим по сколько.."
    i  "Ок." 
    
    scene inshop
    i  "Дороговато" 
    show martun2:
        xalign 1.0
        yalign 1.0
    with slo 
    "А ты как хотел?"
    dan" Две чекушки и черниговское.."
    i  "На книжку так точно не хватит." 
    dan"C тебя полтос."
    menu:
        "Сказать, что нету, оставить на книжку.":
            $ test = 1
        "Отдать полтос и весело провести время.":
            $ test = 2
    if test == 1:
        "*Пацаны розстроились* "
        jump glava2
    else:
        i"Да, водяра нынче дорогая, моего полтоса на литру максимум хватит."
        jump glava3
        
        
        
label glava2:
    
     i"Я трезвый, как свинья. Нужно исправить."
     "Только ты выходишь из АТБ как к тебе подходит пожилой мужчина с модельной внешностью и шикарной щетиной."
     with slo
     scene bg ttt
     show ali at left
     with slo
     show brod at right
     bom "Разрешите обратиться."
     hide ali
     show ali2 at left
     with slo
     i"Обратись."
     bom "Дайте 10 рублей."
     i"Зачем тебе эти деньги? На бухло потратишь?"
     bom "Доехать до Черкас."
     "*Ты глядел в его глаза и делал свой выбор*"
     menu:
        "Дать мужчине 10 гривен.":
            $ test = 1
        "Сказать, что нету.":
            $ test = 2
     if test == 1:
         jump glava2_1
    
     else:
         jump glava2_2
label glava2_1:
    play music "music/padal.mp3" fadeout 1
    with slo
    "*Ты впервые увидел такого щастливого человека*"
    "*В его глазах наворачивались слезы*"
    bom "Hаконец-то смогу нажр... {w} до Черкас доехать."
    "*И тихо добавил*"
    bom "В долгу не останусь парнишка."
    with slo
    scene dk
    "*Ты пошёл домой осозновая, что зная дорогу к тёте Нине, ты и сам за эти деньги мог нажр...  {p} до Черкас доехать.*"
    show ali
    with slo
    "*Ты также осознал, что Мартын с Сашкой пытались тебя наебать*"
    hide ali
    show ali2 at left
    with slo
    "*По пути домой ты встретил быдло*"
    stop music fadeout 1
    with slo
    show gop at right
    gg"Слышь маджахерт, денюжкой не подсабишь?"
    i"Пацаны, нету, отвечаю."
    gg"Ты нас за долбоёбов держишь? {w}Мы только что видели как ты бомжу чирик отдал."
    i"Бля..."
    menu:
        "Отдать им все деньги, целое ебало важнее.":
            $ test = 1
        "Дать по ебалу главарю, а остальные сами убегут.":
            $ test = 2
    if test == 1:
        
         jump glava2_1_1
    
    else:
         jump glava2_1_2
         
label glava2_1_1:
    hide ali2
    show ali at left
    with slo
    "*Только ты полез в карман за баблом, как случаеться невероятное. {p}Появляеться тот самый бомж. *"
    hide ali
    with slo
    hide gg
    with slo
    show gop at left
    with slo
    show brod at right    
    with slo
    "*Бомж молвит*"
    bom "Коровка говорит мууу."
    bom "Курочка говорит ко-ко-ко."
    bom "Свинка говорит хрю-хрю." 
    hide brod
    show bom2 at right
    with slo
    bom "А я говорю, что вы допизделись."
    "*И тут же розпечатывает быдланам пачку пиздюлей*"
    "*...*"
    hide bom2
    hide gop
    show brod at left
    show gopbeg at right
    with slo
    gg"Помогите!!!"
    gg"Он монстр!"
    hide brod
    hide gopbeg
    "*Неловкое молчание...*"
    return

label glava2_1_2:
    hide ali2
    show ali at left
    with slo
    gg"Так что упырь?"
    "*И тут ты наносишь сильнейший удар главарю*"
    "*Выбиваешь два пальца *"
    play music "music/run.mp3"
    
    hide ali
    hide gop 
    play music "music/run.mp3"
    
    "*Ты начинаешь бежать.*"
    scene home 
    with fade 
    gg"Cтоять мразота!"
    gg"Мы тебя найдем и уроем!"
    "*Забегаешь в дом и прячешься.*"
    stop music
    scene room
    play music "music/anime.mp3" fadeout 1
    i"Подготовился называеться. "
    i"Сколько там дней до ЗНО.. "
    "*Смотришь на календарь*"
    i"йоооомаайооо. Сегодня же днюха Томы!  {p}Нужно срочно написать ей письмо. "
    play music "music/zona.mp3" fadeout 1
    scene pis1
    with fade
    "..."
    scene pis2
    with fade
    "..."
    stop music
    play music "music/anime.mp3" fadeout 1
    scene room
    i"Хотя бы одно дело готово. {p}
    Зайду к брату в комнату, может он купил книги и готовиться."
    scene dark
    "*Cтучишь и заходишь*"
    stop music
    play music "music/gay.mp3" fadeout 1
    i"Где тут свет врубить?"
    i"Темно как в ж..."
    i"А вот!"
    scene spalna
    with fade
    i"Чево!?"
    i"Ах вы пи... проклятые!"
    ed  "Это не то что ты думаешь!"
    ed  "Паша просто показывал мне новый прием."
    i"Знаю я ваши гомозахваты!"
    i"Эдик, через минуту зайди ко мне, нужно обсудить поступление"
    ed  "Ok"
    scene zalhome
    with fade
    show ali2 at left
    with slo
    show edik at right
    with slo
    ed  "Что ты хотел?"
    ed  "Мне с Пашкой еще еб...{w} тренить."
    i"Успеете."
    ed  "Так что!?"
    hide ali2
    show ali at left
    with slo
    menu:
        "Я хочу бухнуть.":
            $ test = 1
        "Мне нужна твоя помощь.":
            $ test = 2
    if test == 1:
        
        ed  "А есть моменты, когда ты не хочешь бухнуть?"
        i"Мне сейчас нужно."
    
    else:
         ed  "Хочешь бухнуть?"
         i"Да."
    ed"А я тут каким боком?"
    hide ali
    show ali2 at left
    with slo
    i"Думаешь я не видел как ты две чекушки в шкаф спрятал?{p}
    Но никто не узнает, если ты мне одну так сказать..."
    stop music
    "*Эдик полез в шкаф*"
    play sound "music/bottle.mp3"
    "*Ты олизываешь губы в предвкушении*"
    play music "music/padal.mp3" fadeout 1
    i"Спасибо тебе, брат, во век не забуду."
    ed"Та ну тебя."
    hide edik
    with slo
    hide ali2
    "*Ты наконец-то понял, что семья самое главное в жизни*"
    stop music
    menu:
        "Выпить все сразу.":
            $ test = 1
        "Пойти выпить во дворе.":
            $ test = 2
    if test == 1:
        
        play sound "music/drinking-water.mp3"
        i"Чет мне не хорошо....{p} Паленка галимая...."
        scene dark
        i"брррєуєє бббьрррєууу"
        "   ---ПОЛУЧЕНО ЗВАНИЕ: *ОБРЫГАЛ КОВРИК В ЗАЛЕ*  ---"
        "*GAME OVER*"  
        return
    else:
         jump narko
 
  

    
label glava2_2:
    scene bg ttt
    show ali at left
    with slo
    show brod at right
    with slo
    bom"Чтож, тогда ничего не поделаешь..."
    "*Бомж розстроился(*"
    "*Ты прошел три шага и заметил под ногами 10 гривен.*"
    "*Когда ты поднимал чирик ты встретился глазами с бомжом.*"
    "*Неудобно получилось.*"
    "*Он наверняка неправильно понял.*"
    "*Он развернулся, начал уходить и тихо сказал*"
    bom"Вот пидор."
    "   ---ПОЛУЧЕНО ЗВАНИЕ: *НУ ТЫ И СКОТИНА КОНЕЧНО*  ---"
    "*GAME OVER*"  
    return
label glava3:
    stop music
    scene besedka11
    play sound "music/Sound_birds.mp3"
    "*17:00. Вы подошли на беседку.*"
    show ali at left
    with slo
    "*Там нас уже ждали Гребенюк и Горенок.*"
    show dangol at right
    with dissolve
    dan"Ну всё, пацаны, сегодня нажрёмся."
    play sound "music/Sound_birds.mp3"
    dan"Сегодня у нас целая литра!"
    "*Тебя по царски наебали и скинулся только ты.*"
    "*Но полтос уже было не вернуть.*"
    "*Ты решил неотвлекаться от важных дел и взялся за свой пластиковый стаканчик.*"
    hide dangol
    "*Только ты было хотел хлебнуть горючки как подошел Мося.*"
    show mosa at right
    with dissolve
    play sound "music/Sound_birds.mp3"
    "Мося""А я от тёти Нины."
    play sound "music/Sound_birds.mp3"
    "*Достал ещё две литры из сумки*"
    play sound "music/bottle.mp3"
    "*Ладно, живём ещё.*"
    scene podyom_fin
    show ali at left
    with slo
    "*За несколько минут вы уже ужрались как надо.*"
    show sasha2 at right
    with slo
    "*И тут Сашка достал 250 милилитров какого-то шмурдяка.*"
    play sound "music/bottle.mp3"
    "*Пацаны разлили его себе по чаркам.*"
    "*Перед тобой стоит выбор*"
    menu:
        "Бахнуть шмурдяка.":
            $ test = 1
        "Обойтись двумя литрами водяры.":
            $ test = 2
    if test == 1:
        "*Ты взял чарку и опустошил её..*"
        play sound "music/svist_tolpu.mp3"
        "..."
        stop sound
        scene dark
        "..."
        jump glava3_1
    else:
        " *хвыр-чив-крю*  "
        "Это было последнее, что услышала твоя больная голова перед погружением в глубокий сон.  "
        
        jump glava3_2

label glava3_1:
    scene dark
    with slo
    "*Ты просыпаешься на пляже слепой на один глаз в коровьем говне.*"
    scene beach_fin
    with slo
    "*Не стоило всё таки пить шмурдяк.*"
    "Ты пришёл домой."
    scene home
    with slo
    scene room
    with slo
    "*Книгу ты не купил, да и готовиться к экзамену времени уже не было.Книгу ты не купил, да и готовиться к экзамену времени уже не было.*"
    scene komp
    with slo
    "*Ты начал смотреть видосы из розряда 'как сдать ЗНО на 200'.*"
    "*Не помогло.*"
    "*Но сдаваться было рано.*"
    "*Ты начал разробатывать хитрые планы списывания и к утру ты был готов.*"
    "..."
    scene home
    with slo
    "*На следующий день. 7:00*"
    "*Ты сел в автобус.*"
    scene aut
    with slo
    show ali at left
    with slo
    "*Ты настроен.*"
    "*Ты решителен.*"
    show sasha2 at right
    with slo
    "Сашка""Ну что ты, готов?"
    i"Да не, уже немного протрезвел..."
    "*Хотя всё ещё слеп на один глаз.*"
    "*Проклятый шмурдяк.*"
    hide sasha2
    with slo
    hide ali
    with slo
    scene clas
    with slo
    "*Вот и начался экзамен.*"
    "*Первое задание: {w}Решите систему уравнений пяти переменных методом Кракера  "
    show ali at right
    with slo
    "*Ты начал плакать.*"
    "*Тебя попросили заткнуться.*"
    "*Давить на жалость не прокатило.*"
    "*Ты осмотрел аудиторию.*"
    "*За столом позади тебя сидел чувак в очках.*"
    "*Он умный, инфа сотка.*"
    "*Только ты обернулся чтобы списать у него, как он встал и сдал работу.*"
    "*Бля.*"
    "*Оставался только один вариант.*"
    menu:
        "Использовать идеально продуманный план списывания не обращая внимания на риски":
            $ test = 1
        "Надеяться на удачу.":
            $ test = 2
    if test == 1:
         jump glava3_1_1
    
    else:
        jump glava3_1_2
    return
label glava3_1_1:
    hide ali
    show ali2 at right
    with slo
    "*Ты обоссался чтобы тебя выпустили из аудитории и ты смог списать.*"
    "*Только ты закончил своё дело как очкарик поднял руку и попросился выйти.*"
    "*Ему разрешили.*"
    "*Бля...*"
    "*В аудиторию зашёл полицейский и попросил всех встань для проверки металодетектором.*"
    show kop
    with slo
    "*Ты отказался.*"
    "*Полицейский подошёл к тебе и вступил в лужу.*"
    "Полицейский""Что это?"
    i"Воду пролил."
    "*Полицейский поверил.*"
    "Полицейский""~Ничего страшного, у меня с собой платочек."
    "*Он наклонился и начал, вытерать.*"
    "*Спустя пару секунд до него дошло.*"
    "Полицейский""Ты что, долбоёб?"
    "Полицейский""Это же пробный экзамен."
    i"Бляяя..."
    "*Он вышел в коридор и крикнул:*"
    "Полицейский""Танюша, неси штанишки, тут ещё один переволновался!!!"
    "Танюша""Из того же класса?!!"
    "Полицейский""Да!!"
    "*Этот день навсегда отпечатался в твоей памяти...*"
    i"Зато экзамен хорошо сдал..."
    "			---ПОЛУЧЕНО ЗВАНИЕ: *АДМИРАЛ МОРСКОГО ФЛОТА*  ---"
    "HAPPY END"
    return
label glava3_1_2:
    "*Удача тебя не подвела.*"
    hide ali
    with slo
    scene bridge
    "*Ты набрал 125 балов по всем предметам.*"
    "*Это на 25 балов больше чем ты планировал.*"
    "*Тебе пришла в голову гениальная мысль.*"
    "*Поступить в Полтаву.*"
    "*Через некоторое время на посланную тобой заявку пришёл ответ*"
    scene e-mail
    with slo
    "..."
    scene dark
    with slo
    "..."                                       
    scene politeh
    with slo
    "Чтобы оправдать ожидания декана, ты учился всё время."
    "*Особенно хорошо тебе давалась высшая математика.*"
    "*В особинности метод Кракера.*"
    "*Ещё неплохо шёл ЭС+*"
    "*Вобщем всё было заебись.*"
    "*Но в какой-то момент ты осознал, что тебе нужно больше.*"
    "*Ты решил искать работу.*"
    "*Ты нашел одно неплохое заведение, где смог бы накосить немного бабла.*"
    "..."
    scene bar
    with slo
    "*Это был бар.*"
    "*Назывался он ''Голубой жеребец''*"
    "*Тогда ты ещё не понимал почему так...*"
    show boss at right
    with slo
    "Босс""Чтож, я думаю ты неплохо подходишь на роль коче... кххм, на роль главного менеджера."
    hide boss
    "*Обед прилогался.*"
    "*Кстати, во время одного из таких обедов ты понял почему бар называеться так.*"
    "*И использованные гандоны хорошим перекусом не назовёшь...*"
    "*Тогда то ты и решил, что пора завязывать с этим местом работы.*"
    scene cab
    show ali2 at left
    show boss at right
    with slo
    i "Я увольняюсь."
    "Босс""Если уйдёшь сейчас, я расскажу Томе как ты прошёл комиссию и не поехал на соревнования."
    hide ali2
    show ali at left
    with slo
    "*Это был верх подлости.*"
    "*Но дальше было хуже.*"
    "Босс""А ещё я могу рассказать, как ты в параше на фотки бабок дрочил."
    "Босс""И вообще, забыл с чьей ширинки кормишься."
    "*Это была последняя капля.*"
    scene mers
    with slo    
    "*После работы ты насрал на водительское сиденье его мерседеса.*"
    "*Только ты закончил свои дела, как из бара вышел шеф.*"
    show boss at right
    with slo
    "Босс"" Прости за тот раз, я немного погарячился."
    "Босс""В качестве извенения и в благодарность за твою работу :);):) я дарю тебе свою машину."
    "*Бля...*"
    "Босс""Садись и подкинь меня домой."
    "*Тебе пришлось сесть.*"
    "*Неприятно.*"
    "			---ПОЛУЧЕНО ЗВАНИЕ: *НЕ НАСОСАЛ, А ПОДАРИЛИ*  ---"
    "честно говоря ГОВНЯНЫЙ ФИНАЛ"
    return
label glava3_2:
    scene dark
    with slo
    "3:30."
    "*Ты проснулся от того что какой-то нежный женский голос тебя звал.* "
    "Женский голос""Витаалик..."
    "Женский голос""Витааааалик..."
    scene beach_fin
    with slo
    show ali at left
    with slo
    "*Встав и отряхнув свою одежду от блювотины ты взял фонарик чтобы найти своих друзей.* "
    i"ПАЦЫКИ,ВЫ ГДЕЕ? АУУУ "
    menu:
        "Поискать пацанов за старой беседкой.":
            $ test = 1
        "Пойти к берегу умыться.":
            $ test = 2
    if test == 1:
         jump glava3_2_1
    
    else:
        jump glava3_2_2

label glava3_2_1:
    "*Поиски долго не продлились.*"
    "*Ты заметил их как только беседка рухнула от их перегара.*"
    "*Даня и Сашка спали валетиком.*"
    "*Ты занимался мине..., не суть.*"
    "*Ты разбудил пацыков.*"
    "*Гульня продолжаеться*"

    
label glava3_2_2:
    play sound "music/Sound_mavka.mp3"
    i"Умоюсь и можно пойти похмеляться."
    hide ali
    with slo
    scene mif_fin
    with slo
    show ali at left
    with slo
    play sound "music/Sound_mavka.mp3"
    "*вдруг вода забурлила ..... месяц осветил прекрасный стан молодой девы*"
    show mavka at right
    with slo
    "*волосы девушки были ярко зеленого цвета а верх ничем не прикрыт* "
    play sound "music/Sound_mavka.mp3"
    "*как только Виталик подумал, что это удача*"
    play sound "music/Sound_mavka.mp3"
    "*и его ждет доступная шкура, как увидел, что девушка русалка*"
    i"йооообаааанааааа!!!"
    play sound "music/Sound_mavka.mp3"
    i"Что ты такое?"
    mav"Мене звати Сирена. Не бiйся, хлопець молодий."
    mav"Я давно тебе чекала..."
    play sound "music/Sound_mavka.mp3"
    mav"За прородством саме сьогоднi, в повний мiсяць, я зустрiну свого нареченого."
    i"Извини, но мне еще в высшее учебное заведение поступать."
    mav"не мий ноги об ногу,"
    play sound "music/Sound_mavka.mp3"
    mav"не сiй муки на дiжу"
    mav"ух, ух, дух, дух!"
    play sound "music/Sound_mavka.mp3"
    i"Что с тобой случилось? Как ты стала такой?"
    mav"Це дуже довга iсторiя."
    play music "music/tili-tili-bom.mp3" fadeout 1
    mav"Я гуляла на вечорницях з хлопцями та дiвчатами."
    mav"Ось сидiли ми i я перднула."
    mav"Усiм весело, регочуть, рвуть животи."
    play sound "music/Sound_mavka.mp3"
    mav"А я пiшла й повiсилась"
    mav"Як казав потiм татко Водяник 'остались люди для которых слово честь не пустой звук'  "
    mav"То чи залишишся ти зі мною, юначе молодий?"
    menu:
        "Остаться с мавкой.":
            $ test = 1
        "Отказать":
            $ test = 2
    if test == 1:
         jump glava3_2_1_1
    
    else:
        jump glava3_2_2_2
        
        
label glava3_2_1_1:
    scene dark
    with fade
    stop music
    play music "music/love.mp3"
    "Нам вольно, нам больно{p}
    Нам сладко вдвоем.{p}
    Нам в темные ночи{p}"

    "Легко умереть{p}
    И в мертвые очи{p}
    Друг другу глядеть."
    "*...*"
    "*Мавка схватила Виталика и потощила в глубь болота.*"
    scene boloto
    with fade
    play sound "music/Sound_mavka.mp3"
    show mavka at left
    mav"Татку!"
    mav"Таточку, ти де?"
    mav"Скоріш іди сюди."
    show vod at right
    vod"Я тут, доченька, что случилось?"
    mav"Я виходжу заміж!"
    vod"Какая только радость!{p}И где этот красавец?"
    mav"Он він!"
    show vitgol1
    "*Водяной посмотрел на него.*"
    mav"Красень мій."
    vod"Он то?"
    vod"Радость моя, одумайся.{w} На какой позор ты обрекаешь нашу реку!"
    mav"Не кажи дурниць, татку."
    mav"Коханий, ходи до нас."
    hide vitgol1
    with slo
    show vitgol2
    with slo
    i"Здравствуйте."
    play sound "music/Sound_mavka.mp3"
    vod"Ну привет, зять."
    vod"Чем занимаешься?"
    i"Cобираюсь поступить в высшее учебное заведение."
    vod"Теперь тебе оно не понадобиться. "
    "*Ты видел, что водяной смотрел на тебя, как на дерьмо.*"
    vod"Какой-то ты хилый. "
    hide vitgol2
    with slo
    show vitgol3
    with slo
    i"Вы ошибаетесь."
    
    menu:
        "Вскочить и выпить 6 чарок водяры подряд.":
            $ test = 1
        "Поступить по умному":
            $ test = 1
    if test == 1:
        play sound "music/bottle.mp3"
        hide vitgol3
        with slo
        show vitgol1
        with slo
        "*Ты бегишь и начинаешь пить одну чарку за другой*"
        play sound "music/bottle.mp3"
        play sound "music/svist_tolpu.mp3"
        "*Водяной и Мавка пристально за этим наблюдают*"
        vod"Дочка, он же придурок еще и алкаш. "
        mav"Головне, що я його кохаю."
        vod"Ладно...{p} Пьяни...   {w}зять, поди сюда. "
        hide vitgol1
        with slo
        show vitgol3
        with slo
        "*Полон гордости за себя ты подошел.*"
        vod"Удивил, удивил... "
        vod"Но главный вопрос после которого я узнаю готов ли ты стать властелином всех морей и повести войско на битву с соседней рекой. "
        vod"Любишь мою дочку? "
        menu:
           "Люблю всем сердцем.":
               $ test = 1
           "Думаю, я не готов к серьезным отношениям.":
               $ test = 2
        if test == 1:
            jump mavkagood
        else:
            jump mavkabad
    return


label glava3_2_2_2:                                                                                        
    hide ali 
    with slo
    show ali2 at right
    with slo
    i"Грустно, но все равно вместе нам не быть.."                                                                    
    mav"Помри ж тодi й будь один навiки!"
    "*и в тот же момент исчезла*"
    hide mavka
    with slo
    i"Курка драная."
    "*не послушал ее слова Виталик, споткнулся и упал в реку*"
    hide ali2
    with slo
    "*Нашли его тело пацаны утром.*"
    "*Они еще долго пытались оживить его водкой...*"
    "*но уже ничего нельзя было изменить...*"
    "*На могиле написали 'погиб от белки' и только река знает всю правду*"
    "			---ПОЛУЧЕНО ЗВАНИЕ: *ВОЛОДАР ЗЕЛЕНИХ СВЯТ*  ---"
    " ... то, что называют 'на худой КОНЕЦ'"
    return
label mavkagood:
    
    vod"Это для меня главное."
    mav"А я казала, таточку."
    vod"Тогда не вижу смысла терять время."
    vod"Свадьба будет сегодня же!"
    hide mavka
    hide vod
    hide vitgol3
    scene svadba
    with fade
    "*Ты так нервничал*"
    show vitgol2 at left
    with slo
    i"Вдруг что-то пойдет не так."
    "*Гости собрались*"
    "*На болото даже притянули твоих друзей*"
    show mosa 
    with slo
    hide mosa
    show sasha2 at right
    with slo
    hide sasha2
    show dangol
    with slo
    hide dangol
    "Пацаны" "Удачи братан!"
    i"Ну все, началось.."
    hide vitgol2
    show vitgol3 at left
    with slo
    "*Водяной выводит к арке Мавку*"
    play music "music/nevesta.mp3"
    show vod
    with slo
    show nevesta at right
    with slo
    vod "Удачи дети мои."
    "*И сел на место.*"
    hide vod
    hide nevesta
    show nevesta
    with slo
    hide vitgol3
    show vitgol1 at left
    with slo
    "Церемонимейстер""Две одинокие души сошлись в гавани любви..."
    "Церемонимейстер""бла бла бла..." 
    "Церемонимейстер""Согласны ли вы..." 
    "Церемонимейстер""бла бла бла..." 
    "Церемонимейстер""Можете поцеловать невесту" 
    "Пацаны и морские твари" "горько горько горько"
    stop music
    play sound "music/gorko.mp3"
    hide nevesta
    hide vitgol1
    scene dark
    scene dark
    with fade
    "..."
    vod"А теперь все в ресторан!"
    play music "music/svadba.mp3"
    scene zal 
    with fade
    show sasha2 at left
    "Сашка""Ох нахреначемся сегодня"
    play sound "music/bottle.mp3"
    "*Не осторожно наливая водяру Сашка облил одного из жителей реки*"
    show mon at right
    with slo
    "Чудище" "Ты офигел?"
    show dangol 
    dan"Наших бьют!!!"
    "*Тем временем на другом краю зала*"
    hide mon
    hide dangol
    hide sasha2
    show vitgol3 at left
    with slo
    show vod at right
    with slo
    vod"Вот тебе приданое, зять, три бочки золота и дом из алмазов"
    "*Тебя подкосило, ты стал сказочно богат*"
    "*Вдруг вы услышали шум*"
    hide vod
    hide vitgol3
    show mon at right
    with slo
    show dangol at left
    dan"Я тя щас уебу!"
    "Чудище" "Fuck you!"
    hide dangol
    show dangol 
    with slo
    dan"Ты допизделся! Пацаны бей их!"
    hide dangol
    hide mon
    stop music
    play sound "music/draka2.mp3"
    scene dark
    dan"На те падла"
    "получи!"
    "а от так, гнида!"
    vod"Довольно!!!"
    scene zal
    play music "music/love.mp3"
    show vod at right
    with slo
    show vitgol3 at left
    vod"За то, что сделали твои друзья.{w} Я навсегда изгоняю тебя!"
    vod"А еще ты оплатишь всю свадьбу!"
    "			---ПОЛУЧЕНО ЗВАНИЕ: *Брат за брата, так за основу взято*  ---"
    "скажи спасибо пацанам, за такой КОНЕЦ"
    return
label mavkabad:
    vod"Чтож, тогда ничего не поделаешь..."
    i"Я рад что вы всё поняли."
    vod"Садись на моего покемона, подкину тебя."
    hide mavka
    with slo
    hide vod
    with slo
    hide vitgol3
    with slo
    scene pokemon
    with slo
    show vitgol3 at left
    show vod at right
    i"Где вы взяли такую тварь?"
    vod"Мне бы тоже хотелось встретиться с тем чуваком, который мне на базаре таксу продал..."
    hide vod
    hide vitgol3
    scene forest
    with slo
    show vitgol2 at left
    with slo
    show vod at right
    with slo
    "*Что-то тебе подсказывало, что вы не к тебе домой прибыли.*"
    play music "music/dorime.mp3"
    vod"Копай."
    hide vitgol2
    show vitgol3 at left
    with slo
    "..."
    i"Простите я.."
    vod"Я сказал копай."
    stop music
    play music "music/diatel.mp3"
    i "Я, наверное, всё же люблю вашу дочь."
    vod"Раньше зятьок думать надо было.{w} Теперь копай."
    vod"Ты же пониманшь, как упадёт авторитет такого уважаемого человека как я, если кто узнает, что моя доця суженого выбрала, а он съебался."
    i"Я, никому не скажу, честно. "
    vod"Конечно не скажешь.{w} А теперь копай.."
    i"Может как-то договоримся?. "
    vod"Да ты уже как надо допизделся."
    vod"Что ты вообще можешь мне предложить?"
    vod"Я владелец шикарного болота на 1000 гектаров, велеколепной животины и дочери мои - красотки.{w} А ты алкаш из мухосранска."
    i"Ладно, я всё понял...{w} Тогда можно последнее желание?"
    vod"Валяй."
    hide vitgol3
    show vitgol2 at left
    with slo
    i"Можно мне литру пивка на последок бахнуть?"
    vod"Можно конечно, но ты же понимаешь, что просто мог попросить не убивать тебя?"
    i"Бля..."
    play music "music/run.mp3"
    "*Ты начинаешь бежать.*"
    hide vitgol2
    hide vod
    scene forest2
    show vitgol1 at left
    with slo
    show vod at right
    with slo
    vod"Стоять, сука"
    "*Он со своей тварью быстро тебя нагонял...*"
    hide vitgol1
    hide vod
    scene forest3
    with slo
    vod"Доганю, яица отор...ааай блять, сука, капкан!!"
    vod"Теперь тебе точно пизда."
    scene forest
    show vitgol2 at left
    with slo
    show vod at right
    with slo
    hide vitgol2
    show vitgol3 at left
    with slo
    stop music
    play music "music/diatel.mp3"
    vod"Попался петух?"
    i"Видимо...."
    i"Разрешите загадать последнее желание?"
    vod"Ты, блять, издеваешься?"
    show mavka
    with slo
    mav"Зупинись таточку, я ж кохаю його!"
    vod"Не вмешивайся дочь."
    vod"Он не заслуживает твоей любви."
    mav"Невже в тебе таке холодне серце, що ти не можеш навіть одного юнака пробачити."
    mav"Він же нікого не вбив, нічого не вкрав, чи ти не можеш над ним змилуватись? "
    "*В этот момент у тебя из кармана выпало два алмаза.*"
    stop music
    play music "music/dorime.mp3"
    mav"Бля..."
    vod"Так ты, блять, ещё и алмазы у меня спиздил?!"
    i"Простите."
    stop music
    play music "music/diatel.mp3"
    vod"Это уже даже не серьёзно, напомни, почему ты ещё жив?"
    i"Потому что ваша дочь меня любит, а вы меня безмерно уважаете?"
    vod "*Передёрнул затвор.*"
    mav"О ні, я не можу на це дивитись."
    "*Мавка убежала в слезах.*"
    hide mavka
    "*Вдруг раздался крик*"
    "Крик" "Остановитесь!!!"
    "*Голос всем покозался до боли знакомым.*"
    show frek1
    with slo
    "Все" "Тётя Нина?!!!"
    ni "Что вы здесь устроили?"
    "**"
label narko:
    play music "music/anime.mp3" fadeout 1
    with fade
    scene pod
    "*Ты радосно бегишь пить водяру*"
    "*Это лучший день в двоей жизни*"
    "*Вдруг...*"
    stop music
    play sound "music/broken_cup.mp3" 
    i"аааа..стекло....."
    i"А это что?"
    i"Шприц в ноге!?"
    "*....*"
    play music "music/rados.mp3"
    i"Гыыыы"
    i"Далой футболку!{w}ГЫЫЫ..."
    show vitgol2 at center 

    with slo 
    scene jel
    with slo 
    scene dark
    with slo 
    scene jel
    with slo 
    scene dark
    with slo 
    scene jel
    with slo 
    scene dark
    with slo 
    scene jel
    i"Гыыыы"
    hide vitgol2
    show vitgol1
    with fade
    i"А на чем я полечу?{w}Гыыыы"
    scene home
    stop music
    play sound "music/shmel.mp3"
    i"..."
    i"Дааа, то что нужно! {w} ГЫЫЫ)))"
    hide vitgol1
    with slo 
    show muxa
    with fade
    i"ПОЛЕТЕЛИ!!!"
    play music "music/rados.mp3"
    hide muha
    show muxa:
      xalign 1.0 yalign 0.0
      linear 3.0 xalign 0.0
      pause 1.0
      repeat
    i"..."
    scene bg ttt
    show muxa:
      xalign 1.0 yalign 0.0
      linear 3.0 xalign 0.0
      pause 1.0
      repeat
    i"ЭГЭГЭЭЭЭЙ!!!"
    scene forest2
    show muxa:
      xalign 1.0 yalign 0.0
      linear 3.0 xalign 0.0
      pause 1.0
      repeat
    with slo
    i"..."
    scene street
    show muxa:
      xalign 1.0 yalign 0.0
      linear 3.0 xalign 0.0
      pause 1.0
      repeat
   
    i"Я король ящериц!!! "
    scene dk
    hide muxa
    stop music
    show gop at right 
    "Гопник1" "Не парься найдем этого придурка!"
    play sound "music/shmel.mp3"
    "Гопник2"  "Ты слышишь этот звук?"
    play sound "music/shmel.mp3"
    i"look up!!!"
    show muxa:
        rotate_pad False
        xalign 0.0 yalign 0.0
        rotate 0
        linear 4.0 rotate 360
        repeat
    play music "music/rados.mp3"
    "Гопник2"  "йооомааайооо!!!!???"
    i"Пиф Пиф!"
    "Гопники"  "аааааа!!!Помогите!"
    hide gop 
    with slo
    hide muxa
    scene jel
    
    show muxa:
        xzoom .75 yzoom 1.25
        linear 1.0 xzoom 1.25 yzoom .75
        linear 1.0 xzoom .75 yzoom 1.25
        repeat
    i"А теперь и мне пора!{p}В теплые края!"
    "---ПОЛУЧЕНО ЗВАНИЕ: *Властелин иглы*  ---"
   
    
    
 
    
         
    
    
    
    
