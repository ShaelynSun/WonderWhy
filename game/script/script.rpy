define a = Character("Alice ")
define c = Character("Charles")

define config.say_attribute_transition = dissolve

image purple:
    "#281438"
image logo2:
    contains:
        "images/others/logo.jpeg"
        truecenter

label start:
    play music "music/bgm/clean morning.mp3"
    scene city day
    with dissolve
    "Hi! How are you? Welcome to {b} WonderWhy {b}"
    "The name of WonderWhy is inspired by ‘Wonderland’.
        This is like a virtual world. But......"
    "But who knows? Can we really clarify the boundary between virtual and reality?"
    "Now, may I have your name?"
    python:
        p_name = "Finn"
        while True:
            input_name = renpy.input("Please enter your name here: ")
            input_name = input_name.replace(" ", "")
            len_name = int(len(input_name))
            if len_name != 0:
                p_name = input_name
                break
    define f = Character("[p_name]", image="finn")
    "Hi [p_name], I'm so glad to see you here! "
    menu:
        "Please confirm your gender to generate your look."
        "Male (not yet)":
            $ define sex = 1
            call screen create_male
        "Female":
            $ define sex = 0
            call screen create_female
    $ quick_menu = True
    show finn:
        pos(400, 50)
        zoom 0.5
    "You've created your look!"
    "Now try to go to these places to learn about your life."
    define mt = 3
    jump scene_choices

    return

label scene_choices:
    if mt == 3:
        scene city day
        menu:
            "I decide to go to......"
            "Company":
                "Going to the company. . . "
                jump company
            "Home":
                "Going back home. . . "
                jump home
            "Supermarket":
                "Going to the supermarket. . . "
                jump supermaket
    elif mt == 2:
        scene city dusk
        menu:
            "Try to go to these places to learn about your life."
            "Company":
                "Going to the company. . . "
                jump company
            "Home":
                "Going back home. . . "
                jump home
            "Supermarket":
                "Going to the supermarket. . . "
                jump supermaket
    else:
        scene city light
        menu:
            "Try to go to these places to learn about your life."
            "Company":
                "Going to the company. . . "
                jump company
            "Home":
                "Going back home. . . "
                jump home
            "Supermarket":
                "Going to the supermarket. . . "
                jump supermaket
    return



label before_main_menu:
    scene purple
    show logo2
    with dissolve
#    pause
    hide logo2
    with dissolve

    return
