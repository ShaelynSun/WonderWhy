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
                $ mt -= 1
                jump scene_choices
    elif mt == 2:
        scene sodu
        "It's still a bit early, why don't you come back later?"
        menu:
            "It's daytime, there are no discounts on food in the supermarket now,
            why don't you go to other places first?"
            "Return":
                $ mt -= 1
                jump scene_choices
    elif mt == 1:
        scene son
        "Goooood! Now supermarkets must have discounts on many foods!"
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
    define m = 1 # define the price of Milk
    define b = 1
    define j = 1
    define c = 1
    define price = 0
    define shopping_times = 0
    jump goshopping

    return

label goshopping:
    if shopping_times < 5:
        menu:
            "Milk":
                $ price = price + m
                $ shopping_times += 1
                jump Milk
            "Bread":
                $ price = price + b
                $ shopping_times += 1
                jump Bread
            "Juice":
                $ price = price + j
                $ shopping_times += 1
                jump Juice
            "Chocolate":
                $ price = price + c
                $ shopping_times += 1
                jump Chocolate
            "Qiut":
                jump quitshopping
    else:
        "You bought so many things, are you still going to buy?"
        menu:
            "Quit":
                jump quitshopping

    return

label Milk:
    if shopping_times < 4:
        menu:
            "Bread":
                $ shopping_times += 1
                $ price = price + b
                jump Bread
            "Juice":
                $ price = price + j
                $ shopping_times += 1
                jump Juice
            "Chocolate":
                $ price = price + c
                $ shopping_times += 1
                jump Chocolate
            "Qiut":
                jump quitshopping
    else:
        "You bought so many things, are you still going to buy?"
        menu:
            "Quit":
                jump quitshopping
    return

label Bread:
    if shopping_times < 4:
        menu:
            "Milk":
                $ price = price + m
                $ shopping_times += 1
                jump Milk
            "Juice":
                $ price = price + j
                $ shopping_times += 1
                jump Juice
            "Chocolate":
                $ price = price + c
                $ shopping_times += 1
                jump Chocolate
            "Qiut":
                jump quitshopping
    else:
        "You bought so many things, are you still going to buy?"
        menu:
            "Quit":
                jump quitshopping
    return

label Juice:
    if shopping_times < 4:
        menu:
            "Milk":
                $ price = price + m
                $ shopping_times += 1
                jump Milk
            "Bread":
                $ price = price + b
                $ shopping_times += 1
                jump Bread
            "Chocolate":
                $ price = price + c
                $ shopping_times += 1
                jump Chocolate
            "Qiut":
                jump quitshopping
    else:
        "You bought so many things, are you still going to buy?"
        menu:
            "Quit":
                jump quitshopping
    return

label Chocolate:
    if shopping_times < 4:
        menu:
            "Milk":
                $ price = price + m
                $ shopping_times += 1
                jump Milk
            "Bread":
                $ price = price + b
                $ shopping_times += 1
                jump Bread
            "Juice":
                $ price = price + j
                $ shopping_times += 1
                jump Juice
            "Qiut":
                jump quitshopping
    else:
        "You bought so many things, are you still going to buy?"
        menu:
            "Quit":
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
    show alice home
    return
