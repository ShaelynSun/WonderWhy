image black:
    "#000000"
menu end_choice:
    "You've finished this part. Do you choose to end the game next or go through Alice's perspective?"
    "Review the answers":
        scene q1
        "All social platforms are regulated for speech. They are not allowed to smear Alice with rumours, so reporting it is the right thing to do. You can keep an eye on the 'Report' function on social media platforms."
        scene q2
        "According to the Code of Civilized Internet Use, you may choose to post something positive to say against them. But the best option is to simply report them."
        scene q3
        "This is the migration of bullying. We should stop this behaviour from the start. Instead, we should continue to uncover personal information about this person."
        scene q4
        "You need to be clear that this is {a=https://en.wikipedia.org/wiki/Human_flesh_search_engine}{b}human flesh search engine.{/b}{/a} It is also not good to expose your private information on the internet. You can hardly guarantee that they won't be used by the bad guys. You need to remind Hazel to delete this information to protect herself."
        scene q5
        "He stole your identity in order to spread gossip about Alice. For you, it's an impersonation. That's why you need to be vigilant in your life about passwords not being stolen by phishing sites."
        scene q6
        "You need to quickly clarify your identity and remove the inaccurate statements. And explain your position and your attitude. Oh yes, and don't give an eye for an eye. {a=https://en.wikipedia.org/wiki/Human_flesh_search_engine}{b}HUMAN FLESH SEARCH ENGINE{/b}{/a} is illegal and unethical."
        jump end_choice
    "Go through Alice":
        jump alice_view
    "End":
        return
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
                hc5 = "(Scroll down)\n{b}Anonymous:{/b}I've onece seen Alice steal food from the supermarket donation cart and throw it away :( bad girl.\n{b}qwert:{/b}OMG Is it true? Amazing.\n{b}poiuy:{/b}Interesting. Where's her agency? Does someone like that deserve to be a celebrity?\n{b}lkjhg:{/b}Doesn't she have money to buy food? Why doesn't she go and eat the food in the rubbish."
                hc6 = "(Scroll down)\n{b}Anonymous:{/b}I've onece seen Alice steal food from the supermarket donation cart and throw it away :( bad girl.\n{b}qwert:{/b}OMG Is it true? Amazing.\n{b}poiuy:{/b}Interesting. Where's her agency? Does someone like that deserve to be a celebrity?\n{b}lkjhg:{/b}Doesn't she have money to buy food? Why doesn't she go and eat the food in the rubbish.\n{b}mnbv:{/b}Gross, I don't want to see her face on any screen anymore. Disgusting."
                hc7 = "(Scroll down)\n{b}Anonymous:{/b}I've onece seen Alice steal food from the supermarket donation cart and throw it away :( bad girl.\n{b}qwert:{/b}OMG Is it true? Amazing.\n{b}poiuy:{/b}Interesting. Where's her agency? Does someone like that deserve to be a celebrity?\n{b}lkjhg:{/b}Doesn't she have money to buy food? Why doesn't she go and eat the food in the rubbish.\n{b}mnbv:{/b}Gross, I don't want to see her face on any screen anymore. Disgusting.\n{b}zxcv:{/b}FLORIST wake up. If you don't change the spokesperson your perfume will stink.\n{b}asdfg:{/b}It's like a rotten piece of an apple. Lame"
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
            "Perhaps this is indeed a choice to follow your heart. You choose to release all your stress here, on Alice. Because you trust your own eyes."
            "You believe what you see is a talentless star who is rude and mean."
            "You believe she will pay for this. And you, you are the one who will bring justice."
            "Congratulations on your achievement. {b}Scales of Justice.{/b}"
        "No, feel regret":
            "That doesn't seem to be the outcome you want."
            "You want everyone to know who Alice really is. But she doesn't deserve to be treated so aggressively and harshly."
            "Those who insult Alice must be perfect people without any mistakes? Do they ever consider the damage these mean words can do?"
            "You feel a bit of regret. Maybe, maybe there is another solution to things. Does hurting like that definitely make Alice understand her faults?"
            "Congratulations on your achievement. {b}Witnesses to Cyberbullying.{/b}"
    jump end_choice
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
    call assessment_quiz from _call_assessment_quiz
    # define beh = 0
    # $ beh = 10
    if beh < 1:
        "You're not making a good choice. I don't know if you're serious about completing these questions. So do you want to do them again?"
        menu:
            "Yes":
                call assessment_quiz from _call_assessment_quiz_1
            "No":
                "Fine, let's go on."
    elif 0 < beh < 7:
        "You have a good finish on the quiz, do you plan to redo it to make it perfect?"
        menu:
            "Yes":
                call assessment_quiz from _call_assessment_quiz_2
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
        if beh < 1:
            "As a veritable bystander, you don't want to be the most special person."
            "You just want to be in the corner to see how things are going to be. It's not your responsibility. You don't need to take it on."
            "But things may have different outcomes."
            "You shouldn't ignore the responsibility. It's a shared responsibility of the community and the individual."
            "I understand your concerns. Alice is not your friend. She may have done the wrong thing. You're just an ordinary person and can't do anything for her."
            "But there would have been some interventions here that you could have done."
            "Congratulations on your achievement. {a=https://en.wikipedia.org/wiki/Bystander_effect}{b}Bystander effect.{/b}{/a}"
        elif 0 < beh < 5:
            "Don't be discouraged, at least you attempted to try to change."
            "Don't be too radical, don't be too cowardly. You need to understand the sensible choice."
            "Congratulations on your achievement. {b}The spirit is willing, but the flesh is weak.{/b}"
        else:
            "You think your role is tiny. But I want you to know that it isn't."
            "You've done a great job. Your choices were mostly successful."
            "So don't be afraid. You can stand up for yourself."
            "Congratulations on your achievement. {b}Sword of Justice.{/b}"

    else:
        "As someone who is {b}on her side{/b}."
        "You help Alice as much as you can."
        "Perhaps your help is weakly effective. Perhaps Alice didn't even know you did."
        "But you didn't choose to be a bystander."
        "Sometimes an indifferent bystander is worse than a heartless bully. Isn't it?"
        "It is the presence of bystanders that allows the bullies to hurt others with impunity."
        "It's a challenge to the law and a challenge to human nature."
        if beh < 1:
            "Don't be discouraged, you did attempt to stand up for those who were being bullied."
            "But it is about getting the right approach and behaviour."
            "Congratulations on your achievement. {b}The spirit is willing, but the flesh is weak.{/b}"
        elif 0 < beh < 5:
            "You've tried your options. Even though they're not all the best. But you've helped Alice in a big way."
            "So don't be afraid, you just have to be brave and stand up for yourself. The outcome will be different."
            "Congratulations on your achievement. {b}Sword of Justice.{/b}"
        else:
            "You tried the best choices. That's good."
            "Would you consider your help to be feeble? No, it won't. Never underestimate the power of words."
            "It will be the shooting star that cuts through the night. It will be a burning match in the darkness of the night. It will be the darkness before the dawn. It will bring a different ending for Alice."
            "Congratulations on your achievement. {b}Brave meteors.{/b}"
    jump end_choice
    return
label assessment_quiz:
    define beh = 0
    menu q1:
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
    menu q2:
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
    menu q3:
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
    menu q4:
        "You happen to find out that Hazel has some information on her Facebook page that reveals her personal information such as her {b}workplace, home address, mobile phone number, etc{/b}. What would you do?"
        "Find out if she is related to Alice based on this information.":
            $ beh -= 2
            "This is {a=https://en.wikipedia.org/wiki/Human_flesh_search_engine}{b}human flesh search engine{/b}{/a}. this is a breach of law and humanitarianism. This should be banned. You shouldn't be doing this."
        "Record this information and tell everyone about it.":
            $ beh -= 2
            "Sometimes {b}spreading the word{/b} is a form of bullying."
        "Contacted Hazel to ask her to hide this information.":
            $ beh += 2
            "You remind Hazel not to give out private information on the internet. It's for her own protection. Well done. Remember not to be leaking information."
    menu q5:
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
            $ beh = beh
            "Well, his comments didn't threaten you. Note the question was TO YOU."
    menu q6:
        "How would you handle this tweet?"
        "Delete it without explanation.":
            $ beh += 1
            "You deleted the words but did not explain them. Your fans still think you're right. More people think Alice is really bad."
        "Delete it and post anouther tweet to explain.":
            $ beh += 2
            "You deleted it and gave an explanation for this message. You made your position clear i.e. to protect Alice from bullying. Your fans believed you."
        "You ask for help to find this hacker and attack him.":
            $ beh -= 2
            "Another form of {a=https://en.wikipedia.org/wiki/Human_flesh_search_engine}{b}HUMAN FLESH SEARCH ENGINE{/b}{/a}. Fighting violence with violence is never the best solution."
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
    scene black
    a "My name is Alice. yes. Alice from <Alice in Wonderland>. One of my favorite movies.  I've been very fond of beautiful people since I was a child including actors, models. I really liked being photographed by the flash."
    a "So I started learning various instruments at a young age and went on to study acting at university."
    a "Fortunately, I did it. Despite coming into the industry from modelling first. I never forgot my dream - to be an actress."
    a "I've already done it haven't I? I've just passed the audition for the film [m_name]. I'm about to be an actress!!!!"
    a "I'm going to tell Hazel, my best friend from childhood. She must be so happy for me!!!"
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
    if finn_look == 0:
        show finn_m:
            pos(350, 30)
            zoom 0.5
            xalign 1.0
            linear 1.0 xalign -0.5
        "A shadow flashes from your eyes."
    elif finn_look == 1:
        show finn_f:
            pos(350,30)
            zoom 0.5
            xalign 1.0
            linear 1.0 xalign -0.5
        "A shadow flashes from your eyes."
    else:
        "A shadow flashes from your eyes."
    "Someone is walking past you and towards the donation cart."
    "This catched your attention. So you go over and look at the donation cart too."
    show alice spm
    "You don't really notice whether the guy donated something before. But because of Hazel's words you start noticing the food in the cart."
    "Sure enough, one of the sandwiches has started to get mouldy. You picked it up and looked at it close. Some tiny bits of mould have appeared. You frowned and decided to get rid of it."
    "You take the sandwich and leave the supermarket. Then you throw it in the trash."
    hide alice spm
    scene alice bd night
    "Back home."
    "Everything is normal, everything is ordinary."
    "You're going to tell Hazel that you passed the audition for the film [m_name]. They all say you're very talented."
    "You're happy and you feel grateful for the life."
    "That's the way things were supposed to be. You remember that today you will be announced for the role you are going to play."
    "So you open your computer......"
    a "Dear gosh. What are these?"
    "Alice has seen a lot of rumours about her on the internet. It was as if a lot of people who hated her had suddenly appeared overnight."
    a "Why? What did I do wrong?"
    "Many days have passed. Alice tried to ignore them, but they wanted to flood her life."
    show m2 angry
    ag "Are you okay? Honey. Have you been affected by what those people said?"
    hide m2 angry
    a "I'm fine, I'm good, really. I haven't looked at my computer or my phone or anything lately. I'm reading a book and going for a run. Oh yeah I also went and gave my dog a bath. You know, it's a pain in the ass to give it a bath. It took me a long time. I don't even have time to go online. Really."
    show m2 angry
    ag "You're anxious baby. I'm worried about you."
    hide m2 angry
    a "No. You're worrying too much, Teresa. I'm fine really. By the way, is there something wrong today? What do I need to do?"
    show m2 angry
    ag "No honey. Listen to me. Don't pay attention to what those people are saying. I'll deal with them for you. Let's rest for a while, shall we?"
    hide m2 angry
    a "It's okay, Teresa. you can just tell me. Was my endorsement disqualified? I don't have a job anymore do I?"
    "(Silence)"
    a "Contact a lawyer. I need to protect myself."
    show black
    "Alice is quick to use the law to protect herself. Report malicious comments and clarify inaccurate statements."
    "Alice has tried a lot to get her life on track. She had a hard time, she had anxiety, she had depression. She has regained a new life on her own."
    "Things didn't go in the worst possible direction. This is thanks to Alice herself, but not the bullies. The bullies should thank Alice's powerful mindset to not to cause a bad outcome because of what they said."
    "Broken glass does not revert. All we can do is protect it from harm."
    "The End......"
    jump end_choice
