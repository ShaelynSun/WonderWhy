init:
    default expression = 1
    default hairstyle = 1
    default hair_color = 1
    default costume = 1
    default acc = 1

image finn_f  = Composite(
    (300, 600),
    (0, 0), "Create_Character1/Expression/expression[expression].png",
    (0, 0), "Create_character1/Costume/costume[costume].png",
    (0, 0), "Create_character1/Hair/hair[hairstyle]_[hair_color].png",
    (0, 0), "Create_character1/Accessories/acc[acc].png",
)

screen create_female():
    modal True

    imagemap:
        ground "Dressup_Screen/background.png"
        idle "Dressup_Screen/idle.png"
        hover "Dressup_Screen/hover.png"
        selected_idle "Dressup_Screen/selected.png"
        selected_hover "Dressup_Screen/selected.png"

        ##Expression##
        hotspot(178, 74, 53, 53) action SetVariable("expression", 1)
        hotspot(242, 74, 53, 53) action SetVariable("expression", 2)
        hotspot(307, 74, 53, 53) action SetVariable("expression", 3)
        hotspot(372, 74, 53, 53) action SetVariable("expression", 4)
        hotspot(436, 74, 53, 53) action SetVariable("expression", 5)

        ##Hairstyle##
        hotspot(178, 155, 53, 53) action SetVariable("hairstyle", 1)
        hotspot(242, 155, 53, 53) action SetVariable("hairstyle", 2)
        hotspot(307, 155, 53, 53) action SetVariable("hairstyle", 3)
        hotspot(372, 155, 53, 53) action SetVariable("hairstyle", 4)
        hotspot(436, 155, 53, 53) action SetVariable("hairstyle", 5)

        ##Hair Color##
        hotspot(178, 234, 53, 53) action SetVariable("hair_color", 1)
        hotspot(242, 234, 53, 53) action SetVariable("hair_color", 2)
        hotspot(307, 234, 53, 53) action SetVariable("hair_color", 3)
        hotspot(372, 234, 53, 53) action SetVariable("hair_color", 4)
        hotspot(436, 234, 53, 53) action SetVariable("hair_color", 5)

        ##Accessori##
        hotspot(178, 296, 53, 53) action SetVariable("costume", 1)
        hotspot(242, 296, 53, 53) action SetVariable("costume", 2)
        hotspot(307, 296, 53, 53) action SetVariable("costume", 3)
        hotspot(372, 296, 53, 53) action SetVariable("costume", 4)
        hotspot(436, 296, 53, 53) action SetVariable("costume", 5)

        ##Accessori##
        hotspot(178, 358, 53, 53) action SetVariable("acc", 1)
        hotspot(242, 358, 53, 53) action SetVariable("acc", 2)
        hotspot(307, 358, 53, 53) action SetVariable("acc", 3)
        hotspot(372, 358, 53, 53) action SetVariable("acc", 4)
        hotspot(436, 358, 53, 53) action SetVariable("acc", 5)

        ##Continue##
        hotspot(1107, 9, 157, 53) action Return()

    add "finn_f":
        pos(600, 80)
        zoom 0.5

image finn_m  = Composite(
    (300, 600),
    (0, 0), "Create_character2/Hair/hair[hairstyle]_[hair_color].png",
    (0, 0), "Create_Character2/Expression/expression[expression].png",
    (0, 0), "Create_character2/Costume/costume[costume].png",
    (0, 0), "Create_character2/Accessories/acc[acc].png",
)

screen create_male():
    modal True

    imagemap:
        ground "Dressup_Screen/background.png"
        idle "Dressup_Screen/idle.png"
        hover "Dressup_Screen/hover.png"
        selected_idle "Dressup_Screen/selected.png"
        selected_hover "Dressup_Screen/selected.png"

        ##Expression##
        hotspot(178, 74, 53, 53) action SetVariable("expression", 1)
        hotspot(242, 74, 53, 53) action SetVariable("expression", 2)
        hotspot(307, 74, 53, 53) action SetVariable("expression", 3)
        hotspot(372, 74, 53, 53) action SetVariable("expression", 4)
        hotspot(436, 74, 53, 53) action SetVariable("expression", 5)

        ##Hairstyle##
        hotspot(178, 155, 53, 53) action SetVariable("hairstyle", 1)
        hotspot(242, 155, 53, 53) action SetVariable("hairstyle", 2)
        hotspot(307, 155, 53, 53) action SetVariable("hairstyle", 3)
        hotspot(372, 155, 53, 53) action SetVariable("hairstyle", 4)
        hotspot(436, 155, 53, 53) action SetVariable("hairstyle", 5)

        ##Hair Color##
        hotspot(178, 234, 53, 53) action SetVariable("hair_color", 1)
        hotspot(242, 234, 53, 53) action SetVariable("hair_color", 2)
        hotspot(307, 234, 53, 53) action SetVariable("hair_color", 3)
        hotspot(372, 234, 53, 53) action SetVariable("hair_color", 4)
        hotspot(436, 234, 53, 53) action SetVariable("hair_color", 5)

        ##Costume##
        hotspot(178, 296, 53, 53) action SetVariable("costume", 1)
        hotspot(242, 296, 53, 53) action SetVariable("costume", 2)
        hotspot(307, 296, 53, 53) action SetVariable("costume", 3)
        hotspot(372, 296, 53, 53) action SetVariable("costume", 4)
        hotspot(436, 296, 53, 53) action SetVariable("costume", 5)

        ##Accessori##
        hotspot(178, 358, 53, 53) action SetVariable("acc", 1)
        hotspot(242, 358, 53, 53) action SetVariable("acc", 2)
        hotspot(307, 358, 53, 53) action SetVariable("acc", 3)
        hotspot(372, 358, 53, 53) action SetVariable("acc", 4)
        hotspot(436, 358, 53, 53) action SetVariable("acc", 5)

        ##Continue##
        hotspot(1107, 9, 157, 53) action Return()

    add "finn_m":
        pos(600, 80)
        zoom 0.5
