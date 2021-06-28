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
    define f = Character("[p_name]")
    show me shy2
    s "Hi [p_name], I'm so glad to see you here! "
    show me normal
    s "Now try to go to these places to learn about your life."
    hide me normal
    with fade

    define mt = 3
    menu:
        "Company":
            jump company
            "Going to the company. . . "
        "Home":
            jump home
            "Going back home. . . "
        "Supermarket":
            jump supermaket

    return

label before_main_menu:
    scene purple
    show logo2
    with dissolve
    # pause
    hide logo2
    with dissolve

    return
