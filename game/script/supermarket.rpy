image sod = "images/bg/spm out day.jpg"
image sodu = "images/bg/spm out dusk.jpg"
image son = "images/bg/spm out night.jpg"
image sin = "images/bg/spm night.jpg"

label supermaket:
    if mt == 3:
        scene sod
        menu:
            "It's daytime, there are no discounts on food in the supermarket now,
            why don't you go to other places first?"
            "Return":
                jump scene_choices
    elif mt == 2:
        scene sodu
        menu:
            "It's still a bit early, why don't you come back later?"
            "Return":
                jump scene_choices
    elif mt == 1:
        scene son
        "Goooood! Now the supermarket must have discounts on many foods!"
        menu:
            "Let's go!!":
                jump spmin
    else:
        scene sod
        "You have wasted all your chances."
        menu:
            "How about......"
            "Re-choose those places":
                $ mt = 3
                jump scene_choices
            "Skip these pressure test":
                jump meet_alice # not yet
    return

image black:
    "#000000"

label spmin:
    scene sin
    with Fade(1.0, 0.0, 1.0)
    scene black
    show spm shelf
    with fade
    "Buy the food you want!"
    init python:
        m = 1 # define the price of buy_milk
        b = 1
        j = 1
        c = 1
        w = 1
        price = 0
        buy_milk = False
        buy_bread = False
        buy_juice = False
        buy_cho = False
        buy_water = False
    jump goshopping

    return

label goshopping:
    menu:
        "Milk" if buy_milk == False:
            $ price = price + m
            $ buy_milk = True
            jump goshopping
        "Bread" if buy_bread == False:
            $ price = price + b
            $ buy_bread = True
            jump goshopping
        "Juice" if buy_juice == False:
            $ price = price + j
            $ buy_juice = True
            jump goshopping
        "Chocolate" if buy_cho == False:
            $ price = price + c
            $ buy_cho = True
            jump goshopping
        "Water" if buy_water== False:
            $ price = price + w
            $ buy_water = True
            jump goshopping
        "Qiut":
            jump quitshopping
    return

label quitshopping:
    if price == 0:
        "You didn't but anything!! why?? Ain't you houngry?"
        menu:
            "Go back shopping":
                jump goshopping
    else:
        menu:
            "You have to pay [price] pounds."
            "Pay":
                "Sccess to pay"
                jump meet_alice
    return

label meet_alice:
    scene son
    with Fade(1.0, 0.0, 1.0)
    
    return
