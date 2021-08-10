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
                jump meet_alice
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
        m = 1.5 # define the price of buy_milk
        b = 1
        j = 2.0
        c = 0.75
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
                "Success to pay"
                jump meet_alice
    return

screen hate_comments(hc):
    style_prefix "hate_comments"
    frame:
        area (320, 200, 450, 210)
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            vbox:
                text "[hc]"
default hc = 0

label meet_alice:
    scene son
    with Fade(1.0, 0.0, 1.0)
    "This city is experiencing typhoon weather recently."
    "The weather doesn't look good outside."
    define stay_outside = True
    menu:
        "You decide to......"
        "Stay outside":
            "You decide to stay outside and watch the changes in the weather."
            scene son
            with Fade(1.0, 0.0, 1.0)
            "(Broadcast on TV) A typhoon has landed in our city two days ago. We sincerely hope the public could pay attention to changes in the weather."
            "(Broadcast on TV) The government plans temporary shelters for the homeless. If you hear the news, please go to the nearest refuge immediately."
        "Go inside":
            $ stay_outside = False
            "You decide to go back to the supermarket and check the weather on your phone."
            scene sin
            with Fade(1.0, 0.0, 1.0)
            "Take out your phone and read the latest news."
            "(News on phone) A typhoon has landed in our city two days ago. We sincerely hope the public could pay attention to changes in the weather."
            "(News on phone) The government plans temporary shelters for the homeless. If you hear the news, please go to the nearest refuge immediately."
    f "Alas, the suffering of the afflicted one, has no right to pessimism."
    "You feel sad, but you can do nothing."
    if buy_water:
        "Have you decided to donate the water you just bought to the donation cart to help the homeless?"
    elif buy_juice:
        "Have you decided to donate the juice you just bought to the donation cart to help the homeless?"
    else:
        "Have you decided to buy a bottle of water and donate it to the donation cart to help the homeless?"
    menu:
        "Yes":
            $ friendly_value += 1
            "You decide to donate it. You need money, but someone may need it more to stay alive."
        "No":
            $ friendly_value -= 1
            "You decided not to donate it. That's okay. Everyone is experiencing a tough time."
    "You are passing by the donation cart. But one person has caught your attention."
    show cart
    show alice spm:
        xalign 0.5
        linear 0.5 xalign 0.0
    "She looks different from your impression. But you still recognize her, she is {b}Alice{b}"
    "She is looking for something in the donation cart, and she still has a bottle of water in her hand."
    show sandwich:
        xalign 0.5
        linear 0.5 xalign 1.0
    "At this time, you notice that Alice take out a {b}sandwich{/b} from the cart.
        She is watching the {b}ingredients list{/b} of the sandwich carefully and {b}feels disgust just like she saw a bug."
    "You are a little surprised, but you don't do anything. However, what happened next is beyond your imagination."
    show sandwich:
        xalign 1.0
        linear 0.5 xalign -0.5
    show alice spm:
        xalign 0.5
        linear 0.5 xalign -0.5
    "{b}She smells the sandwich and throw it into the trash can by the supermarket door."
    menu:
        "You feel very ...... about this."
        "nothing":
            $ friendly_value += 1
            "You feel very speechless about this. But she must have some reasons, right?"
        "angry":
            $ friendly_value -= 1
            "You feel very angry about this. You feel an imbalance between the rich and ordinary people."
    "You look at the weather that is about to rain. You still decide to {b}buy another sandwich and put it in the donate cart."
    "The hard life will be passed. Everything will get better."

    scene bedroom night
    with Fade(1.0, 0.0, 1.0)
    "You return your home."
    "But, still feel a little bit aggrieved at the computer desk."
    "So you decide to look up some information about Alice."
    show cpt alice
    "You specifically look at her comment area."
    python:
        hc = "(Scroll down)\n{b}unknown:{/b} You are really really bad.\n{b}qwert:{/b} Overrated...I think.\n{b}bubu:{/b} HOW dare she?\n{b}ltleFrog{/b} Hw..so disgusting about her look.\n{b}asdf:{/b} I dnt understand the hype.\n{b}zxcv:{/b}How much did she pay for the job?\n{b}poiuy:{/b}Does anyone know she is also the brand spokesman of FLORIST perfume in 2020?\n{b}lkjh:{/b}OMG, is FLORIST crazy? Their perfume won't give me any good impression then.\n{b}Hahahazel:{/b}Serious? She is just a model. She is a very kind person in her life. Why so mean?\n{b}unknown2:{/b}You know what. The light bulb in my house broke down today. It must be done by Alice;)\n{b}mnbv:{/b}hhhahah copy that. covid-19 in China was also made by Alice. Leave the earth."
    show screen hate_comments(hc)
    "There are really many malicious comments about Alice on the Internet. Many comments criticized her appearance and skin color,"
    "But you noticed one thing: everyone attacked Alice {b}without evidence{/b}. Someone explained that Alice is a kind person in life."
    "This caught your attention. Because her actions in the supermarket prove that she is not a nice person."
    hide cpt alice
    hide screen hate_comments
    menu:
        "So you decide to......({color=#f00}You can save your progress here. And come back later to re-select another option.{/color})"
        "Expose her":
            jump main1
        "Give up exposure":
            jump main2
    return
