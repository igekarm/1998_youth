# skills.rpy

init python:
    skills = {
        "charisma": 0,
        "influence": 0,
        "manipulation": 0,
        "oratory": 0,
        "strength": 0,
        "dexterity": 0
    }

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

        textbutton "Назад" action Return() xalign 0.5 yalign 1.0
