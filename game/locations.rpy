# locations.rpy
# Основные локации

# Экран для Дома
screen home_screen:
    # Фоновое изображение для Дома
    add "images/home/1.jpg"

    # Иконка для перехода в мини-локацию "Гараж"
    imagebutton:
        idle "images/icons/home/13.png"  # Иконка гаража в обычном состоянии
        hover "images/icons/home/13_1.png"  # Иконка гаража при наведении
        action Jump("garage_scene")
        xalign 0.01
        yalign 0.98

    # Иконка для перехода в мини-локацию "Кухня"
    imagebutton:
        idle "images/icons/home/4.png"  # Иконка кухни в обычном состоянии
        hover "images/icons/home/4_1.png"  # Иконка кухни при наведении
        action Jump("kitchen_scene")
        xalign 0.09
        yalign 0.98

#     # Иконка дома для возврата назад
#     imagebutton:
#         idle "images/icons/home/1.png"  # Иконка дома в обычном состоянии
#         hover "images/icons/home/1_1.png"  # Иконка дома при наведении
#         action Return()
#         xalign 0.9
#         yalign 0.9

# Экран для Магазина
screen shop_screen:
    # Фоновое изображение для Магазина
    add "images/shop.webp" xalign 0.5 yalign 0.5

    # Иконка для перехода в мини-локацию "Отдел одежды"
    imagebutton:
        idle "images/icons/clothes_section_icon_idle.png"  # Иконка отдела одежды в обычном состоянии
        hover "images/icons/clothes_section_icon_hover.png"  # Иконка отдела одежды при наведении
        action Jump("clothes_section_scene")
        xalign 0.2
        yalign 0.7

    # Иконка для перехода в мини-локацию "Касса"
    imagebutton:
        idle "images/icons/cash_register_icon_idle.png"  # Иконка кассы в обычном состоянии
        hover "images/icons/cash_register_icon_hover.png"  # Иконка кассы при наведении
        action Jump("cash_register_scene")
        xalign 0.4
        yalign 0.7

    # Иконка дома для возврата назад
    imagebutton:
        idle "images/icons/home_icon_idle.png"
        hover "images/icons/home_icon_hover.png"
        action Return()
        xalign 0.9
        yalign 0.9

# Экран для Работы
screen work_screen:
    # Фоновое изображение для Работы
    add "images/backgrounds/work.png" xalign 0.6 yalign 0.55

    # Иконка для перехода в мини-локацию "Офис"
    imagebutton:
        idle "images/icons/office_icon_idle.png"  # Иконка офиса в обычном состоянии
        hover "images/icons/office_icon_hover.png"  # Иконка офиса при наведении
        action Jump("office_scene")
        xalign 0.1
        yalign 0.7

    # Иконка для перехода в мини-локацию "Склад"
    imagebutton:
        idle "images/icons/warehouse_icon_idle.png"  # Иконка склада в обычном состоянии
        hover "images/icons/warehouse_icon_hover.png"  # Иконка склада при наведении
        action Jump("warehouse_scene")
        xalign 0.3
        yalign 0.7

    # Иконка дома для возврата назад
    imagebutton:
        idle "images/icons/home_icon_idle.png"
        hover "images/icons/home_icon_hover.png"
        action Return()
        xalign 0.9
        yalign 0.9


# Мини-локации

# Экран для мини-локации Гараж
screen garage_scene:
    # Фоновое изображение для Гаража
    add "images/home/13.jpg"

    # Иконка дома для возврата назад
    imagebutton:
        idle "images/icons/home/1.png"
        hover "images/icons/home/1_1.png"
        action Return()
        xalign 0.9
        yalign 0.9

# Экран для мини-локации Кухня
screen kitchen_scene:
    # Фоновое изображение для Кухни
    add "images/home/4.jpg"

    # Иконка дома для возврата назад
    imagebutton:
        idle "images/icons/home/1.png"
        hover "images/icons/home/1_1.png"
        action Return()
        xalign 0.9
        yalign 0.9

# Экран для мини-локации Отдел одежды
screen clothes_section_scene:
    # Фоновое изображение для отдела одежды
    add "images/backgrounds/clothes_section.png"

    # Иконка дома для возврата назад
    imagebutton:
        idle "images/icons/home_icon_idle.png"
        hover "images/icons/home_icon_hover.png"
        action Return()
        xalign 0.9
        yalign 0.9

# Экран для мини-локации Касса
screen cash_register_scene:
    # Фоновое изображение для кассы
    add "images/backgrounds/cash_register.png"

    # Иконка дома для возврата назад
    imagebutton:
        idle "images/icons/home_icon_idle.png"
        hover "images/icons/home_icon_hover.png"
        action Return()
        xalign 0.9
        yalign 0.9

# Экран для мини-локации Офис
screen office_scene:
    # Фоновое изображение для офиса
    add "images/backgrounds/office.png"

    # Иконка дома для возврата назад
    imagebutton:
        idle "images/icons/home_icon_idle.png"
        hover "images/icons/home_icon_hover.png"
        action Return()
        xalign 0.9
        yalign 0.9

# Экран для мини-локации Склад
screen warehouse_scene:
    # Фоновое изображение для склада
    add "images/backgrounds/warehouse.png"

    # Иконка дома для возврата назад
    imagebutton:
        idle "images/icons/home_icon_idle.png"
        hover "images/icons/home_icon_hover.png"
        action Return()
        xalign 0.9
        yalign 0.9




# # Экран для Дома старая версия
# screen home_screen:
#     # Фоновое изображение для Дома
#     add "images/backgrounds/conteiner.webp"
#     # Опционально, можно добавить кнопки или элементы для взаимодействия
#     textbutton "Назад" action Return()
#
# # Экран для Магазина
# screen shop_screen:
#     # Фоновое изображение для Магазина
#     add "images/shop.webp" xalign 0.5 yalign 0.5
#     # Опционально, можно добавить кнопки или элементы для взаимодействия
#     textbutton "Назад" action Return()
#
# # Экран для Работа
# screen work_screen:
#     # Фоновое изображение для Работы
#     add "images/backgrounds/work.png" xalign 0.6 yalign 0.55
#     # Опционально, можно добавить кнопки или элементы для взаимодействия
#     textbutton "Назад" action Return()
