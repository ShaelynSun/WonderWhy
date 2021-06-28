image sod = "images/bg/spm out day.jpg"
image sodu = "images/bg/spm out dusk.jpg"
image son = "images/bg/spm out night.jpg"
label supermaket:
    if mt == 3:
        scene sod
        with fade
        scene spm day
        with fade
        "It's daytime, there are no discounts on food in the supermarket now,
        why don't you go to other places first?"
        menu:
            "Company":
                jump company
            "Home":
                jump home
            "Supermarket":
                jump supermaket
    elif mt == 2:
        scene sodu
        "It's still a bit early, why don't you come back later?"
        menu:
            "Company":
                jump company
            "Home":
                jump home
            "Supermarket":
                jump supermaket
    else:
        scene son
        "Goooood! Now supermarkets must have discounts on many foods!"
        menu:
            "Enter":
                jump spmin
return

label spmin:
    return
