# locations.rpy

# Экран для Дома
screen home_screen:
    # Фоновое изображение для Дома
    add "images/backgrounds/conteiner.webp"
    # Опционально, можно добавить кнопки или элементы для взаимодействия
    textbutton "Назад" action Return()

# Экран для Магазина
screen shop_screen:
    # Фоновое изображение для Магазина
    add "images/shop.webp" xalign 0.5 yalign 0.5
    # Опционально, можно добавить кнопки или элементы для взаимодействия
    textbutton "Назад" action Return()

# Экран для Работа
screen work_screen:
    # Фоновое изображение для Работы
    add "images/backgrounds/work.png" xalign 0.6 yalign 0.55
    # Опционально, можно добавить кнопки или элементы для взаимодействия
    textbutton "Назад" action Return()
