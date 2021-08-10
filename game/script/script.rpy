define a = Character("Alice ")
define pressure_value = 0
define friendly_value = 0

define config.say_attribute_transition = dissolve

image purple:
    "#281438"
image logo2:
    contains:
        "images/others/logo.jpeg"
        truecenter

label start:
    # play music "music/bgm/clean morning.mp3"
    scene city day
    with dissolve
    "Hi! How are you? Welcome to {b} WonderWhy {\b}"
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
    define finn_look = 0
    define f = Character("[p_name]")
    "Hi, {b}[p_name]{/b} I'm so glad to see you here! "
    menu:
        "Please generate the look you prefer."
        "Boy":
            $ finn_look = 0
            call screen create_male
            $ quick_menu = True
            show finn_m:
                pos(350,30)
                zoom 0.5
            "Nice look!"
        "Girl":
            $ finn_look = 1
            call screen create_female
            $ quick_menu = True
            show finn_f:
                pos(350, 30)
                zoom 0.5
            "Nice look!"
        "Skip":
            $ finn_look = 2
            "No worries."
    "Now try to go to these places to learn about your life."
    define mt = 3
    define company_done = False
    define home_done = False
    jump scene_choices

    return

label scene_choices:

    if mt == 3:
        scene city day
    elif mt == 2:
        scene city dusk
    else:
        scene city light
    menu:
        "Try to go to these places to learn about your life."
        "Company" if company_done == False:
            "Going to the company. . . "
            $ company_done = True
            jump company
        "Home" if home_done == False:
            "Going back home. . . "
            $ home_done = True
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
