label home:
    if mt == 3:
        $ mt -= 1
        scene bedroom day
        with fade
    elif mt == 2:
        $ mt -= 1
        scene bedroom dusk
        with fade
    elif mt == 1:
        $ mt -= 1
        scene bedroom night
        with fade
    else:
        "You have wasted all your chances."
        menu:
            "How about......"
            "Re-choose those places":
                $ mt = 3
                jump scene_choices
            "Skip these pressure test":
                jump meet_alice # not yet
    "You have returned your house."
    "Choose some details to learn about your life."
    define choose_movie = False
    define m_name = "WonderWhy"
    define check_alice_on_phone = False
    menu home_main:
        f "I wanna check......"
        "The whole room":
            "This is a small shared room because the rent will be lower. Fortunately, your landlord has not found another one."
            "So you can enjoy a whole room by yourself temporarily."
            "You have a family that is not rich. You applied to a university in this city, but your family can't help you pay for your tuition."
            "You also don't want to apply for those grants. Because you have seen {b}some people who are discriminated against for applying for grants."
            "So you decide to work first and go to university when you have enough money."
            "Life is a bit tough, but you still insist on it, don't you?"
            jump home_main
        "Your computer":
            "You sold the laptop that you didn't know how long you used, and used your first month salary to buy this new computer."
            "In addition to using it for work, you also use it for studying and watching movies."
            "Oh wait! Your favorite movie is now available on MeTube!"
            if choose_movie:
                "Yup. The name of your favorite movie is [m_name]!"
            else:
                call choose_fav_movie
                "Yup. The name of your favorite movie is [m_name]!"
            "In fact, you often write comments for your favorite movies, music, and books."
            define init_comment_style = 0
            menu:
                "And those comments are very......"
                "Sharp":
                    $ init_comment_style = 1
                    "Those comments are very sharp. They can always catch some pain points very accurately."
                "Friendly":
                    $ init_comment_style = 2
                    "Those comments are very friendly, and you can always have a good impression among the fans of every artist."
                "Fair":
                    $ init_comment_style = 3
                    "Those comments are fair. You can always summarize their strengths and weaknesses in some works. This makes everyone feel that you are very objective and professional."
                "Personal":
                    $ init_comment_style = 4
                    "Those comments are personal opinions. You will evaluate the works of those artists according to your own preferences. Your comments are humorous. This is very popular among people who have the same likes and dislikes as you."
            "So, you actually have a lot of fans on some social platforms. About a few hundred."
            "It seems that there are still many people who are very friendly to you and support you."
            jump home_main
        "You phone":
            $ check_alice_on_phone = True
            "You checked your bank balance, it is very close to your dream!"
            "Perhaps, you can save a little bit more. Like food?"
            "Whatever you want. Let's browse some news first. Your favorite movie seems to have something new."
            if choose_movie:
                "Yup. The name of your favorite movie is [m_name]!"
            else:
                call choose_fav_movie
                "Yup. The name of your favorite movie is [m_name]!"
            "Oh wait, [m_name] is currently available, and......the shooting of [m_name]2 will start next month?"
            "And.....and your favorite character actually chose the model Alice?"
            "You can't believe it."
            jump home_main
        "Check Alice right now" if check_alice_on_phone == True:
            show cpt alice
            with fade
            show alice normal:
                xalign 0.5
                linear 0.5 xalign 1.0
            "(Open the Metube channel of Alice. And learn about her)"
            "She is a model and usually shoots print ads for some luxury goods."
            "And she will also record some vlogs and post them on her social platform. She has a REALLY large number of fans."
            f "But why is it her? That character is called Jessica, she was a blonde white girl. She looks like a bad girl, her language is very mean, but she has a very good heart. But this Alice and Jessica are nothing like. especially......"
            menu:
                "But this Alice and Jessica are nothing like. especially......"
                "The skin color":
                    f "Especially the skin color. She is not a white girl at all."
                "The appearance":
                    f "Especially the appearance. She looks so innocent. Jessica ought to look like a fox."
                "Nothing":
                    "It seems like there's nothing about Alice that doesn't fit the role. Because the character is all up to the actor."
            f "Except they are all rich. Goodness. This may be the only similarity. Anyway, I have recognized many luxury brands that I haven't seen in her MeTube."
            "(A video of Alice looking frightened after seeing a bug)"
            f "Mmmm, yes. Jessica is also afraid of bugs. Is this why the director thinks she is suitable for Jessica? Can't believe it."
            f "Forget it."
            jump scene_choices
    return

label choose_fav_movie:
    python:
        choose_movie = True
        while True:
            input_name = renpy.input("The name of the movie is...... ")
            input_name = input_name.replace(" ", "")
            len_name = int(len(input_name))
            if len_name != 0:
                m_name = input_name
                break
    return
