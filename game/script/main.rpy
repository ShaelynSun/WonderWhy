image black:
    "#000000"

label  main1:
    "You decided to expose Alice's affair about her sneaking food from the supermarket donation cart."
    "So you started exaggerating about it on the internet."
    menu:
        "I've onece seen Alice steal food from the supermarket donation cart and throw it away :( bad girl.":
            show cpt alice
            python:
                hc2 = "{b}Anonymous:{/b}I've onece seen Alice steal food from the supermarket donation cart and throw it away :( bad girl."
                hc3 = "{b}Anonymous:{/b}I've onece seen Alice steal food from the supermarket donation cart and throw it away :( bad girl.\n{b}qwert:{/b}OMG Is it true? Amazing."
                hc4 = "{b}Anonymous:{/b}I've onece seen Alice steal food from the supermarket donation cart and throw it away :( bad girl.\n{b}qwert:{/b}OMG Is it true? Amazing.\n{b}poiuy:{/b}Interesting. Where's her agency? Does someone like that deserve to be a celebrity?"
                hc5 = "(Page down)\n{b}Anonymous:{/b}I've onece seen Alice steal food from the supermarket donation cart and throw it away :( bad girl.\n{b}qwert:{/b}OMG Is it true? Amazing.\n{b}poiuy:{/b}Interesting. Where's her agency? Does someone like that deserve to be a celebrity?\n{b}lkjhg:{/b}Doesn't she have money to buy food? Why doesn't she go and eat the food in the rubbish."
                hc6 = "(Page down)\n{b}Anonymous:{/b}I've onece seen Alice steal food from the supermarket donation cart and throw it away :( bad girl.\n{b}qwert:{/b}OMG Is it true? Amazing.\n{b}poiuy:{/b}Interesting. Where's her agency? Does someone like that deserve to be a celebrity?\n{b}lkjhg:{/b}Doesn't she have money to buy food? Why doesn't she go and eat the food in the rubbish.\n{b}mnbv:{/b}Gross, I don't want to see her face on any screen anymore. Disgusting."
                hc7 = "(Page down)\n{b}Anonymous:{/b}I've onece seen Alice steal food from the supermarket donation cart and throw it away :( bad girl.\n{b}qwert:{/b}OMG Is it true? Amazing.\n{b}poiuy:{/b}Interesting. Where's her agency? Does someone like that deserve to be a celebrity?\n{b}lkjhg:{/b}Doesn't she have money to buy food? Why doesn't she go and eat the food in the rubbish.\n{b}mnbv:{/b}Gross, I don't want to see her face on any screen anymore. Disgusting.\n{b}zxcv:{/b}FLORIST wake up. If you don't change the spokesperson your perfume will stink.\n{b}asdfg:{/b}It's like a rotten piece of an apple. Lame"
            show screen hate_comments(hc2)
    "Very quickly, your comments got a lot of replies."
    show screen hate_comments(hc3)
    "All of them believed you."
    show screen hate_comments(hc4)
    "They believe Alice is essentially a bad girl."
    show screen hate_comments(hc5)
    "Although only a small group of people attacked her appearance at first. The unsubstantiated malicious comments did not do much harm."
    show screen hate_comments(hc6)
    "But now more and more are joining in."
    show screen hate_comments(hc7)
    "hings are getting out of control. {b}'AliceQuitEarth'{/b} has turned out to be the new trend in Twitter."
    "Some people have even called FLORIST to ask them to change their spokesperson."
    "More and more people are starting to start rumours about the new gossip about Alice."
    "People are only willing to assume what they see as the truth, even though it may not be true at all."
    hide screen hate_comments
    hide cpt alice
    menu:
        "Are you sure that this is the result you want? Are you sure that Alice deserves to be treated like this?"
        "Yes":
            "Congratulations on your achievement. {b}Stubborn bully{/b}"
        "No, feel regret":
            "Congratulations on your achievement. {b}Apologetic bully{/b}"
    menu:
        "You've finished this part. Do you choose to end the game next or go through Alice's perspective?"
        "End":
            return
        "Go through Alice":
            jump alice_view
    return
label main2:
    "You decide not to expose her affairs."
    "Because you don't think you have sufficient evidence to prove that she is a mean person."
    "You see people's comments about Alice on the screen. They are very {b}sharp and mean{/b}."
    "You don't think Alice is that good. But she is always innocent."
    "In the face of these hate comments, you decide to be ......"
    define id_is_bystander = True
    menu:
        "Please choose seriously."
        "a bystander":
            $ id_is_bystander = True
            "You decide to be a bystander. she is an innocent person but her previous behaviour you always remembered."
        "on her side":
            $ id_is_bystander = False
            "You decide to take her side, even though you don't know about her. But bullying a girl with words on the internet like that is always wrong."
    "You open up some bad reviews about her."
    call assessment_quiz
    # define beh = 0
    # $ beh = 10
    if beh < 3:
        "You're not making a good choice. I don't know if you're serious about completing these questions. So do you want to do them again?"
        menu:
            "Yes":
                call assessment_quiz
            "No":
                "Fine, let's go on."
    elif 2 < beh < 9:
        "You have a good finish on the quiz, do you plan to redo it to make it perfect?"
        menu:
            "Yes":
                call assessment_quiz
            "No":
                "Fine, let's go on."
    else:
        "Let's move on to the next process."
    "There are consistently a lot of bad comments about Alice on the internet, many of which hurt her without REASON or EVIDENCE."
    if id_is_bystander:
        "As a {b}bystander{/b}."
        "You didn't do anything about it, you just indifferently saw the rumours and gossip that those people were spreading about her."
        "You could have done something. But you didn't."
        "Although your voice of support may be faint. It's always helpful for Alice."
        "Never underestimate the power of words."
        if beh < 3:
            "Congratulations on your achievement. {b}The indifferent bystander{/b}"
        elif beh > 2 and beh < 9:
            "Congratulations on your achievement. {b}The spirit is willing, but the flesh is weak.{/b}"
        else:
            "Congratulations on your achievement. {b}Active bystanders.{/b}"
    else:
        "As someone who is {b}on her side{/b}."
        "You help Alice as much as you can."
        "Perhaps your help is weakly effective. Perhaps Alice didn't even know you did."
        "But you didn't choose to be a bystander."
        "Sometimes an indifferent bystander is worse than a heartless bully. Isn't it?"
        "It is the presence of bystanders that allows the bullies to hurt others with impunity."
        "It's a challenge to the law and a challenge to human nature."
        if beh < 3:
            "Congratulations on your achievement. {b}The spirit is willing, but the flesh is weak.{/b}"
        elif beh > 2 and beh < 9:
            "Congratulations on your achievement. {b}Tried to do your best.{/b}"
        else:
            "Congratulations on your achievement. {b}Actions speak louder than words.{/b}"
    menu:
        "You've finished this part. Do you choose to end the game next or go through Alice's perspective?"
        "End":
            return
        "Go through Alice":
            jump alice_view
    return
label assessment_quiz:
    define beh = 0
    menu:
        "You see some screenshots about a conversation between Alice and her girlfriend. The conversations in them are very explicit and dirty. But you notice that the {b}edges of the pictures are rough{/b}, which means that the pictures are probably {b}fake{/b}. So......"
        "This is hilarious. Share it with your friends.":
            $ beh -= 2
            "You shared this content with your friends. They all start laughing at Alice. it's not a good start. Sometimes {b}spreading the word{/b} is a form of bullying."
        "It's boring. Ignore it.":
            $ beh -= 1
            "You ignore the content and, unfortunately, you become a complete bystander."
        "Refute in the comments section that this is a false picture.":
            $ beh += 1
            "You try to rebut those comments, it has some effect but minimal."
        "Find out the first person who posts these and report him.":
            $ beh += 2
            "You found some of the people who spoke the meanest language. Recorded their account names and reported them. Without the incitement of these people, the number of vicious comments about Alice became less."
    menu:
        "Many people say hurtful words about {b}Alice's body{/b} under her selfies. Because she is too thin. It doesn't match what people expect of her. Especially for your favourite character 'Jessica'. So......"
        "Join them.":
            $ beh -= 2
            "You also think Alice's body doesn't fit the role, so you join in the bashing of her figure. You went from being a bystander to being a bully."
        "Ignore it.":
            $ beh -= 1
            "You ignore the content and, unfortunately, you become a complete bystander."
        "Post some positive comments.":
            $ beh += 1
            "You try to post somet positive word. Although there is some refutation, it still bodes well."
        "Report it.":
            $ beh += 2
            "Instead of choosing to argue with them, you just report them. It is very effective."
    menu:
        "An account called 'Hazel' is defending Alice. She is always rebutting malicious comments. As a result she has received some harassment. The person called 'Hazel' is considered to be as Alice herself or someone else who supports Alice. What can you do about this?"
        "Post comments asking the bully to stop.":
            $ beh += 2
            "Very few people have made bad comments about Hazel and none of them have any evidence or are sure that they should do so. Because of your intervention, they quickly stopped hurting Hazel."
        "Arguing with bullies about their faults.":
            $ beh += 1
            "Your argument led to more anger from them, but some supporters still appeared in the masses of the bullying Hazel."
        "Ignore it.":
            $ beh -= 1
            "You ignore the content and, unfortunately, you become a complete bystander."
        "Without judging the malicious remarks, try to uncover Hazel's message in detail.":
            $ beh -= 2
            "You ignored the malicious comments as a bystander and scoured her social accounts for her personal information."
    menu:
        "You happen to find out that Hazel has some information on her Facebook page that reveals her personal information such as her {b}workplace, home address, mobile phone number, etc{/b}. What would you do?"
        "Find out if she is related to Alice based on this information.":
            $ beh -= 2
            "This is a {b}human flesh search{/b}. this is a breach of law and humanitarianism. This should be banned. You shouldn't be doing this."
        "Record this information and tell everyone about it.":
            $ beh -= 2
            "Sometimes {b}spreading the word{/b} is a form of bullying."
        "Contacted Hazel to ask her to hide this information.":
            $ beh += 2
            "You remind Hazel not to give out private information on the internet. It's for her own protection. Well done. Remember not to be leaking information."
    menu:
        "As a critic with hundreds of followers. One day you log on to Twitter and find that you have posted a hate comment about Alice. It's obvious that your account has been {b}stolen{/b}. What kind of bullying is this?"
        "Gossip":
            $ beh = beh
            "He's not gossiping about you. Note the question was TO YOU."
        "Impersonation":
            $ beh += 2
            "That's right. He impersonated you to make his own statements."
        "Exclusion":
            $ beh = beh
            "He didn't repel you did he? He merely stole your {b}identity{/b}."
        "Threats":
            $ beh += 2
            "Well, his comments didn't threaten you. Note the question was TO YOU."
    menu:
        "How would you handle this tweet?"
        "Delete it without explanation.":
            $ beh += 1
            "You deleted the words but did not explain them. Your fans still think you're right. More people think Alice is really bad."
        "Delete it and post anouther tweet to explain.":
            $ beh += 2
            "You deleted it and gave an explanation for this message. You made your position clear i.e. to protect Alice from bullying. Your fans believed you."
        "You ask for help to find this hacker and attack him.":
            $ beh -= 2
            "Another form of {b}HUMAN FLEESH SEARCH{/b}. fighting violence with violence is never the best solution."
    return

label alice_view:
    define ag = Character("Agent Teresa")
    define h = Character("Hazel")
    scene alice bd day
    show m2 angry
    ag "How many times have I told you? Don't buy pizza and burgers for takeout. You just didn't remember did you?"
    a "Sorry Teresa, I won't next time."
    show m2 scorn
    ag "...uh-huh Don't let me catch you next time. You'd better......"
    ag "Where are you going? Ain't you listening to me?"
    hide m2 scorn
    a "Supermarket, supermarket, Teresa. I'm gonna buy salad. See you!"
    show m2 scorn
    ag "Childish. huh. Whatever."
    hide m2 scorn
    with fade
    scene sin
    show hazel smile
    h "Hiiiii luv luv Alice! Do you come to see me specifically?"
    show hazel smile:
        xalign 0.75
    show alice spm pre:
        xalign 0.25
        yanchor 0.0
        linear 0.25 yanchor -0.05
    a "Let me think ......  For you, but also for the salad."
    show alice spm pre:
        xalign 0.25
        yanchor -0.05
        linear 0.25 yanchor 0.0
    show hazel smile:
        xalign 0.75
        linear 0.25 yanchor 0.95
    h "I knew it! I kept one of the best salads of the day for you as your best friend."
    h "Happy with it?"
    show alice spm pre:
        xalign 0.25
        yanchor 0.0
        linear 0.25 yanchor -0.05
    show hazel smile:
        xalign 0.75
        linear 0.25 yanchor 1.0
    a "Yes!"
    show alice spm pre:
        xalign 0.25
        yanchor -0.05
        linear 0.25 yanchor 0.0
    show hazel smile:
        xalign 0.75
        linear 0.25 yanchor 0.95
    h "And a bottle of water, take it."
    show hazel smile:
        xalign 0.75
        linear 0.25 yanchor 1.0
    show alice spm:
        xalign 0.25
    a "Hhhahah Thank you so much Hazel."
    show hazel normal:
        xalign 0.75
        linear 0.25 yanchor 0.95
    h "That's great. But honey. A lot of our food has gone mouldy because of the wet weather from the typhoon. I still need some time to sort them out."
    show hazel smile:
        xalign 0.75
        yanchor 0.95
    h "Just go home and try not to go out. Okay?"
    show hazel smile:
        xalign 0.75
        linear 0.25 yanchor 1.0
    show alice spm:
        xalign 0.25
        yanchor 0.0
        linear 0.25 yanchor -0.05
    a "Sounds good. stay safe Hazel. love you. I'll go home and we can talk later."
    show alice spm:
        xalign 0.25
        yanchor -0.05
        linear 0.25 yanchor 0.0
    show hazel smile:
        xalign 0.75
        linear 0.25 yanchor 0.95
    h "Great, great. Bye-bye."
    show hazel smile:
        xalign 0.75
        linear 0.25 yanchor 1.0
    hide hazel smile
    with fade
    if stay_outside:
        scene son
    else:
        scene sin
    if finn_is_f:
        show finn_f:
            pos(350, 30)
            zoom 0.5
            xalign 1.0
            linear 1.0 xalign -0.5
    else:
        show finn_m:
            pos(350,30)
            zoom 0.5
            xalign 1.0
            linear 1.0 xalign -0.5
    "Someone is walking past you and towards the donation cart."
    "This catched your attention. So you go over and look at the donation cart too."
    show alice spm
    "You don't really notice whether the guy donated something before. But because of Hazel's words you start noticing the food in the cart."
    "Sure enough, one of the sandwiches has started to get mouldy. You picked it up and looked at it close. Some tiny bits of mould have appeared. You frowned and decided to get rid of it."
    "You take the sandwich and leave the supermarket. Then you throw it in the trash."
    hide alice spm
    scene alice bd night
    "You are back home."
    "Everything is normal, everything is ordinary."
    "You're going to tell Hazel that you passed the audition for the film [m_name]. They all say you're very talented."
    "You're happy and you feel grateful for the life."
    "That's the way things were supposed to be. You remember that today you will be announced for the role you are going to play."
    "So you open your computer......"
    scene black
    "Alice never expected what would happen next."
    "However, a white war on the internet has already begun."
    "You can continue on from your saved progress and explore other endings."
    "The End......"
    return
