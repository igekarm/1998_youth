# Инициализация переменных и настроек
init python:
    # Переменные для времени суток
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

    # Левый верхний угол - время суток, кнопки перемотки времени
    add icon_time_of_day[time_of_day] xalign 0.0 yalign 0.0
    imagebutton idle icon_forward_1h action Function(set_time, 1) xalign 0.0 yalign 0.1
    imagebutton idle icon_forward_2h action Function(set_time, 2) xalign 0.0 yalign 0.2

    # Правый верхний угол - навыки, карта, инвентарь, телефон
#     frame:
#         align (1.0, 0.0)
#         has vbox
#
#         textbutton "Навыки" action ShowMenu("skills_menu")

    hbox:
        xalign 1.0
        yalign 0.07
        spacing 0

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
    def set_time(hours):
        global time_of_day
        if time_of_day == "Утро":
            if hours == 1:
                time_of_day = "День"
            elif hours == 2:
                time_of_day = "Вечер"
        elif time_of_day == "День":
            if hours == 1:
                time_of_day = "Вечер"
            elif hours == 2:
                time_of_day = "Ночь"
        elif time_of_day == "Вечер":
            if hours == 1:
                time_of_day = "Ночь"
            elif hours == 2:
                time_of_day = "Утро"
        elif time_of_day == "Ночь":
            if hours == 1:
                time_of_day = "Утро"
            elif hours == 2:
                time_of_day = "День"

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
            thirst = "Легкая жажда"
        elif level == 2:
            thirst = "Жажда"
        elif level == 3:
            thirst = "Сильная жажда"

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
            time.sleep(10)
            # Логика обновления состояния
            # Пример: понижение уровня жажды
            if thirst != "Сильная жажда":
                update_thirst(3)
            else:
                update_thirst(2)
            renpy.restart_interaction()
