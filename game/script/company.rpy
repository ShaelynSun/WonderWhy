label company:
    define m1 = Character("Marian")
    define uk = Character("???")

    if mt == 3:
        $ mt -= 1
        scene company day
        with Fade(1.0, 0.0, 1.0)
        scene work day
        with fade
    elif mt == 2:
        $ mt -= 1
        scene company dusk
        with Fade(1.0, 0.0, 1.0)
        scene work dusk
        with fade
    elif mt == 1:
        $ mt -= 1
        scene company night
        with Fade(1.0, 0.0, 1.0)
        scene work night
        with fade
    else:
        "You have wasted all your chances."
        menu:
            "Re-choose those places":
                $ mt = 3
                jump scene_choices
            "Skip these pressure test":
                jump meet_alice

    show m1 normal:
        linear 0.5 center
    uk "Finally, you are late again! Why don't you remember the time by your heart?"
    define forget_name = False
    define wrong_name = ""
    menu:
        f "I'm sorry......"
        "Daisy":
            $ forget_name = True
            $ wrong_name = "Daisy"

            python:
                original_name = list(p_name)
                reversed_name = original_name.reverse()
                reversed_name = ''.join(original_name)

            f "I'm sorry.....[wrong_name], I won't be late next time. I promice."
            show m1 calm
            m1 "Fine. Oh wait. What? Don't you even forget my name?"
            m1 "[wrong_name]? Have you entered a parallel universe or something?"
            show m1 ssmile
            m1 "Are you [p_name]? Aha, I see. You are [reversed_name] right?"
            menu:
                "Sorry Marian......":
                    show m1 calm
                    f "Sorry Marian, I just...I just need coffee to keep me sober! Is there anything I can do for you?"
        "Marian":
            $ forget_name = False
            f "I'm sorry Marian, I won't be late next time. I promice."
            show m1 ssmile
            m1 "Thanks god, you are alive. You ought to be sober up a bit."
        "Carol":
            $ forget_name = True
            $ wrong_name = "Carol"

            python:
                original_name = list(p_name)
                reversed_name = original_name.reverse()
                reversed_name = ''.join(original_name)

            f "I'm sorry.....[wrong_name], I won't be late next time. I promice."
            show m1 calm
            m1 "Fine. Oh wait. What? Don't you even forget my name?"
            m1 "[wrong_name]? Have you entered a parallel universe or something?"
            show m1 ssmile
            m1 "Are you [p_name]? Aha, I see. You are [reversed_name] right?"
            menu:
                "Sorry Marian......":
                    show m1 calm
                    f "Sorry Marian, I just...I just need coffee to keep me sober! Is there anything I can do for you?"
    show m1 calm
    m1 "Whatever, scan these documents, you DON'T need me to teach you again, right? "
    m1 "GO GO GO"
    hide m1 calm
    show printer
    "Working......"
    menu:
        "OOPS, it looks like the printer is stuck, you need help."
        "Ask for help":
            f "I need help please......"
            if forget_name:
                show m1 calm
                m1 "Really, [p_name]? why don't you call [wrong_name] for help?"
                m1 "Listen, we are willing to pay an intern who has never attended college because he ought to put in enough effort."
                show m1 ssmile
                m1 "Isn't it enough to use one hand to operate the printer?"
                show m1 calm
                m1 "5 minutes, I wish I could see the printed documents appear on my desk."
                hide m1 calm
            else:
                show m1 normal
                m1 "What's up, [p_name]? Dear gosh, trust me please. This machine is more expensive than you."
                show m1 smile
                m1 "If it doesn’t work in your hands, I believe the boss will change a new printer and replace you by the way."
                hide m1 smile
                f "I didn't mean to destroy it......I......"
                show m1 normal
                m1 "Okay, stand back."
                hide m1 normal
                "Give the printer a few taps......"
                show m1 normal
                m1 "Seems good. Go on your job and finish in time."
                m1 "Not really hard huhh?"
                hide m1 normal
        "I can do it by myself":
            "Try to give the printer a few taps......"
            if forget_name:
                show m1 calm
                m1 "Hmmmmm, hi, this is [wrong_name], who is knocking the door?"
                show m1 ssmile
                m1 "Trust me please. This machine is more expensive than you."
                m1 "If it doesn’t work in your hands, I believe the boss will change a new printer and replace you by the way."
                menu:
                    "......":
                        f "Sorry......"
                        show m1 calm
                        m1 "Wake up ok? Where is my documents?"
                    "Check the printer":
                        f "I will check it right now!"
                        m1 "(Looked at the printer and then at you) Good! God bless me I can see my files within 5 minutes."
                f "I am scanning the stuff. Wait 5 minute, no, 3 minutes."
                hide m1 ssmile
            else:
                show m1 smile
                m1 "What's wrong again? [p_name], you can't complete even one job by yourself right?"
                menu:
                    "I just...checking the printer......":
                        f "I am just checking the printer. It seems stuck."
                        show m1 calm
                        m1 "No explanation. God bless me I can see my files within 5 minutes."
                    "Right now":
                        f "I'm doing right now. No worries."
                        show m1 calm
                        m1 "(Thinking) Not bad. Go ahead."
                hide m1 ssmile
    hide printer
    "You finish the scanning work. But Marian doesn't seem happy."
    "So you decide to continue your other work."
    "......"
    show m1 calm:
        xalign 1.0
        linear 0.5 xalign 0.5
    if mt == 2:
        m1 "Ok, fine. it's almost 12 o'clock. Let's have something for lunch."
    elif mt == 1:
        m1 "Ok, fine. it's almost 18 o'clock. Let's have something for dinner."
    else:
        m1 "Ok, fine. it's almost 20 o'clock. Let's have something for midnight snack."
    show m1 smile
    m1 "Except......you, [p_name]."
    show m1 calm
    m1 "Because of your inefficiency, I need you to finish your work first instead of getting together with us."
    show m1 calm:
        yanchor 0.0
        linear 1.0 yanchor -0.05
    m1 "Calm down. This is also an opportunity for you to exercise and grow in your abilities."
    m1 "Lack of ability requires more effort than others, doesn't it?"
    show m1 smile:
        yanchor -0.05
        linear 1.0 yanchor 0.0
    m1 "Go for it."
    show m1 smile:
        xalign 0.5
        linear 1.0 xalign 2.0
    "You are the only one left in the office."
    "In fact, this is not the first time you have been treated like this."
    "I need you to know this is one of the more common types of stress in the workplace."
    "From bosses or colleagues. Their main concern is that the benefits include the company's and their own."
    "It's reasonable that these people won't treat you with 100 percent friendliness."
    "It's important that you need to get used to it and stay in a good frame of mind."
    "They're just minding that you haven't been to university but are missing out on getting this internship."
    "But you're saving up for tuition. Maybe you can go to college within two years. Or maybe one year."
    "After a while......"
    show m1 calm:
        xalign 2.0
        linear 1.0 xalign 0.5
    m1 "How's it going?"
    f "Pretty good. I got most of it done. But I still have a few professional questions I'd like to ask you."
    f "May I, Marian?"
    m1 "No......."
    show m1 smile
    m1 "(Laugh) Not now. We accidentally bought an extra salad. Your current task is to eat it first. I need you to finish it as soon as possible before you come back to me with your questions. Understand?"
    show m1 ssmile
    f "Get it! Thank you Marian."
    m1 "Come on. Eat up."
    hide m1 ssmile
    "Malice in life is everywhere. But we should always believe that there is no 100 percent friendliness and no 100 percent malice."
    menu:
        "How do you feel about your experience with the company?"
        "I don't care":
            $ pressure_value -= 1
            f "I don't care. I will cut down some more unnecessary expenses."
            f "When I get enough money, I will leave this place."
        "Still feel unfair":
            $ pressure_value += 1
            f "I get this internship opportunity by my own efforts. I take a salary that matches my efforts."
            f "Why can't everyone be more friendly?"
    jump scene_choices
    return
