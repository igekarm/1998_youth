# health_status.rpy

init python:
    health = 100
    hunger = "Не голоден"
    thirst = "Не хочет пить"
    hygiene = "Чистый"
    fatigue = "Выспался"
    arousal = 0

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
