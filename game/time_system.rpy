# time_system.rpy

init python:
    time_of_day = "Утро"
    hours = 6  # Начальное время: 06:00 утра
    minutes = 0
    time_speed = 15  # Скорость времени: 1 минута каждые 15 секунд реального времени

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

    def auto_update_state():
        import time
        while True:
            time.sleep(120)
            if thirst != "Сушняк":
                update_thirst(3)
            else:
                update_thirst(2)
            renpy.restart_interaction()
