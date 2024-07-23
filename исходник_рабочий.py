# Инициализация переменных и настроек
init python:
    # Переменные для времени суток и часов
    time_of_day = "Утро"

    # Переменные для навыков
    skills = {
        "charisma": 0,
        "influence": 0,
        "manipulation": 0,
        "oratory": 0,
        "strength": 0,
        "dexterity": 0
    }

    # Переменные для состояния здоровья и нужд
    health = 100
    hunger = "Не голоден"
    thirst = "Не хочет пить"
    hygiene = "Чистый"
    fatigue = "Выспался"
    arousal = 0

    # Переменные для часов
    hours = 6  # Начальное время: 06:00 утра
    minutes = 0
    time_speed = 15  # Скорость времени: 1 минута каждые 15 секунд реального времени

# Пути к иконкам
define icon_map = "images/icons/map.png"
define icon_inventory = "images/icons/inventory.png"
define icon_phone = "images/icons/phone.png"
define icon_time_of_day = {
    "Утро": "images/icons/morning.png",
    "День": "images/icons/afternoon.png",
    "Вечер": "images/icons/evening.png",
    "Ночь": "images/icons/night.png"
}
define icon_forward_1h = "images/icons/forward_1h.png"
define icon_forward_2h = "images/icons/forward_2h.png"

# Пути к иконкам состояния
define icon_health = "images/icons/health.png"
define icon_hunger = "images/icons/hunger.png"
define icon_thirst = "images/icons/thirst.png"
define icon_hygiene = "images/icons/hygiene.png"
define icon_fatigue = "images/icons/fatigue.png"
define icon_arousal = "images/icons/arousal.png"

# Основной экран новеллы с кнопками карты, инвентаря, телефона, индикацией времени и кнопками перемотки времени
screen hud:

    # Индикаторы состояния в центре экрана в самом верху
    hbox:
        xalign 0.5
        yalign 0.0
        spacing 5
        style_prefix "indicator"

        vbox:
            add icon_health
            text "[health]"

        vbox:
            add icon_hunger
            text "[hunger]"

        vbox:
            add icon_thirst
            text "[thirst]"

        vbox:
            add icon_hygiene
            text "[hygiene]"

        vbox:
            add icon_fatigue
            text "[fatigue]"

        vbox:
            add icon_arousal
            text "[arousal]"

    # Левый верхний угол - время суток, кнопки перемотки времени, часы
    hbox:
        xalign 0.0
        yalign 0.0
        spacing 10

        # Индикатор времени суток
        add icon_time_of_day[time_of_day]

        # Часы
        text "[hours:02d]:[minutes:02d]" color "#FFFFFF" size 24

        # Кнопки перемотки времени
        imagebutton idle icon_forward_1h action Function(set_time, 1) xalign 0.04 yalign 0.0
        imagebutton idle icon_forward_2h action Function(set_time, 2) xalign 0.07 yalign 0.0

    # Правый верхний угол - навыки, карта, инвентарь, телефон
    frame:
        align (1.0, 0.0)
        has vbox

        textbutton "Навыки" action ShowMenu("skills_menu")

        hbox:
            imagebutton idle icon_map action ShowMenu("map")
            imagebutton idle icon_inventory action ShowMenu("inventory")
            imagebutton idle icon_phone action ShowMenu("phone")

style indicator_text:
    size 12
    color "#FFFFFF"

# Экран для отображения навыков в виде выпадающего списка
screen skills_menu:
    modal True
    tag menu

    frame:
        align (0.5, 0.5)
        has vbox

        text "Навыки" size 24

        for skill, value in skills.items():
            hbox:
                text skill.capitalize() + ": "
                text str(value)

        textbutton "Закрыть" action Hide("skills_menu")

# Логика для обновления времени
init python:
    def set_time(hours_increment):
        global time_of_day
        global hours

        hours += hours_increment
        if hours >= 24:
            hours -= 24

        if 6 <= hours < 12:
            time_of_day = "Утро"
        elif 12 <= hours < 18:
            time_of_day = "День"
        elif 18 <= hours < 24:
            time_of_day = "Вечер"
        else:
            time_of_day = "Ночь"

    def update_time():
        global hours, minutes, time_speed

        while True:
            renpy.pause(time_speed)  # Ждать реальное время
            minutes += 1
            if minutes >= 60:
                minutes = 0
                hours += 1
                if hours >= 24:
                    hours = 0
            renpy.restart_interaction()

# Логика для обновления состояния персонажа
init python:
    def update_hunger(level):
        global hunger
        if level == 0:
            hunger = "Не голоден"
        elif level == 1:
            hunger = "Легкий голод"
        elif level == 2:
            hunger = "Голоден"
        elif level == 3:
            hunger = "Очень голоден"

    def update_thirst(level):
        global thirst
        if level == 0:
            thirst = "Не хочет пить"
        elif level == 1:
            thirst = "Пить"
        elif level == 2:
            thirst = "Жажда"
        elif level == 3:
            thirst = "Сушняк"

    def update_hygiene(level):
        global hygiene
        if level == 0:
            hygiene = "Чистый"
        elif level == 1:
            hygiene = "Не мытый"
        elif level == 2:
            hygiene = "Воняет"

    def update_fatigue(level):
        global fatigue
        if level == 0:
            fatigue = "Выспался"
        elif level == 1:
            fatigue = "Сонливость"
        elif level == 2:
            fatigue = "Усталость"
        elif level == 3:
            fatigue = "Очень устал"

    def update_arousal(level):
        global arousal
        arousal = level

# Функция для обновления состояния персонажа с интервалом
init python:
    import time

    def auto_update_state():
        while True:
            time.sleep(120)
            # Логика обновления состояния
            # Пример: понижение уровня жажды
            if thirst != "Сушняк":
                update_thirst(3)
            else:
                update_thirst(2)
            renpy.restart_interaction()

# Пример игрового экрана
label start:

    # Фоновое изображение для экрана
    scene hud_background

    $ renpy.invoke_in_thread(auto_update_state)
    show screen hud
    #"Добро пожаловать в игру!"
    "Здесь будет сюжет вашей визуальной новеллы."
    return

# Экраны для карты, инвентаря и телефона с изображениями

screen map:
    # Путь к изображению карты
    add "images/map.png" xalign 0.5 yalign 0.5

screen inventory:
    # Путь к изображению инвентаря
    add "images/screens/inventory_screen.png" xalign 0.5 yalign 0.5

screen phone:
    # Путь к изображению телефона
    add "images/phone.png" xalign 0.5 yalign 0.5
