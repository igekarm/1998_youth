# Определение переменных для хранения текущей локации
default current_location = "living_room"

# Функция для отображения мини-карты
screen minimap:
    # Фон мини-карты (замените 'minimap.png' на изображение вашей карты)
    add "images/map.png"

    # Кнопки для перехода по локациям
    imagemap:
        ground "minimap.png"  # Изображение мини-карты
        idle "minimap.png"
        hover "minimap.png"

        # Координаты кнопок для каждой локации
        hotspot (50, 50, 100, 100) action Jump("living_room")  # Координаты и переход для гостиной
        hotspot (200, 50, 100, 100) action Jump("kitchen")    # Координаты и переход для кухни
        hotspot (350, 50, 100, 100) action Jump("bedroom")    # Координаты и переход для спальни

# Определение локаций
label show_minimap:
    # Показ мини-карты
    call screen minimap
    return

label living_room:
    # Изображение гостиной
    scene bg living_room
    "Вы находитесь в гостиной."

    # Кнопка для вызова мини-карты
    show screen minimap_button
    return

label kitchen:
    # Изображение кухни
    scene bg kitchen
    "Вы находитесь на кухне."

    # Кнопка для вызова мини-карты
    show screen minimap_button
    return

label bedroom:
    # Изображение спальни
    scene bg bedroom
    "Вы находитесь в спальне."

    # Кнопка для вызова мини-карты
    show screen minimap_button
    return

# Кнопка для вызова мини-карты в любой локации
screen minimap_button:
    # Кнопка вызова мини-карты в нижнем углу экрана
    textbutton "Карта" action Jump("show_minimap") xpos 10 ypos 560
