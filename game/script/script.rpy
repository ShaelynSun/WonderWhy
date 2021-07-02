define a = Character("Alice ")
define c = Character("Charles")
define s = Character ("Shaelyn")

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
    show me normal
    s "Hi! How are you? Welcome to {b} WonderWhy {b}"
    s "The name of WonderWhy is inspired by ‘Wonderland’.
        This is like a virtual world. But......"
    show me shy1
    s "But who knows? Can we really clarify the boundary between virtual and reality?"
    s "Now, may I get your name?"
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
    show me shy2
    s "Hi [p_name], I'm so glad to see you here! "
    show me normal
    s "Now try to go to these places to learn about your life."
    hide me normal
    with fade

    image side finn n = "images/main/finn daily normal.png"
    f n "I decide to go to......"
    define mt = 3
    jump scene_choices

    return

label scene_choices:
    if mt == 3:
        scene city day
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
