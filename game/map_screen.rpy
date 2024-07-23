# map_screen.rpy

init python:
    # Список маркеров на карте
    map_markers = [
        {"name": "Дом", "x": 0.3, "y": 0.4, "icon": "images/icons/home.png", "screen": "home_screen"},
        {"name": "Магазин", "x": 0.6, "y": 0.5, "icon": "images/icons/shop.png", "screen": "shop_screen"},
        {"name": "Работа", "x": 0.7, "y": 0.6, "icon": "images/icons/work.png", "screen": "work_screen"}
    ]

    def add_marker(name, x, y, icon, screen):
        map_markers.append({"name": name, "x": x, "y": y, "icon": icon, "screen": screen})

    def remove_marker(name):
        global map_markers
        map_markers = [marker for marker in map_markers if marker["name"] != name]

# Экран карты
screen map:
    # Фоновое изображение карты
    add "images/map.png" xalign 0.5 yalign 0.5

    # Отображение маркеров на карте
    for marker in map_markers:
        imagebutton:
            idle marker["home"]
            xpos marker["0.7"]
            ypos marker["0.3"]
            action ShowMenu(marker["home_screen"])

# Функция отображения информации о маркере
init python:
    def show_marker_info(name):
        renpy.notify(f"Вы выбрали маркер: {name}")
