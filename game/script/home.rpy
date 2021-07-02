label home:
    if mt == 3:
        $ mt -= 1
        scene flat day
        with Fade(1.0, 0.0, 1.0)
        scene bedroom day
        with fade
        menu:
            "test, mt = [mt]"
            "Return":
                jump scene_choices
    elif mt == 2:
        $ mt -= 1
        scene flat dusk
        with Fade(1.0, 0.0, 1.0)
        scene bedroom dusk
        with fade
        menu:
            "test, mt = [mt]"
            "Return":
                jump scene_choices
    elif mt == 1:
        $ mt -= 1
        scene flat night
        with Fade(1.0, 0.0, 1.0)
        scene bedroom night
        with fade
        menu:
            "test, mt = [mt]"
            "Return":
                jump scene_choices
    else:
        "You have wasted all your chances."
        menu:
            "How about......"
            "Re-choose those places":
                $ mt = 3
                jump scene_choices
            "Skip these pressure test":
                jump meet_alice # not yet
    return
