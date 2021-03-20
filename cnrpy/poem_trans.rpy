translate chinese screen:
    screen poem(currentpoem, paper="paper"):
        style_prefix "poem"
        vbox:
            add paper
        viewport id "vp":
            child_size (710, None)
            mousewheel True
            draggable True
            has vbox
            null height 40
            if currentpoem.author == "yuri":
                if currentpoem.yuri_2:
                    text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text"
                elif currentpoem.yuri_3:
                    text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text_3"
                else:
                    text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text"
            elif currentpoem.author == "sayori":
                text "[currentpoem.title]\n\n[currentpoem.text]" style "sayori_texten"
            elif currentpoem.author == "natsuki":
                text "[currentpoem.title]\n\n[currentpoem.text]" style "natsuki_text"
            elif currentpoem.author == "monika":
                text "[currentpoem.title]\n\n[currentpoem.text]" style "monika_text"
            null height 100
        vbar value YScrollValue(viewport="vp") style "poem_vbar"
        if (_preferences.language == "chinese" and currentpoem.title != "mdpnfbo,jrfp"):
            imagebutton:
                xoffset 1050
                yoffset 100
                hover "tl/chinese/gui/button/chsbutton_idle_showtrans.png"
                idle "tl/chinese/gui/button/chsbutton_hover_showtrans.png"
                action [ShowTransient("poemchs",currentpoem=currentpoem, paper=paper),Hide("poem")]
                focus_mask True





screen poemchs(currentpoem, paper="paper"):
    if currentpoem.author == "sayori":
        if currentpoem.title == "Dear Sunshine":
            $ poemchs = poem_s1_chs
        elif currentpoem.title == "Bottles":
            $ poemchs = poem_s2_chs
        elif currentpoem.title == "%":
            $ poemchs = poem_s3_chs
    elif currentpoem.author == "monika":
        if currentpoem.title == "Hole in Wall":
            if persistent.playthrough == 0:
                $ poemchs = poem_m1_chs
            elif persistent.playthrough ==2:
                $ poemchs = poem_m21_chs
        elif currentpoem.title == "Save Me":
            if persistent.playthrough ==0:
                $ poemchs = poem_m2_chs
            elif persistent.playthrough ==2:
                $ poemchs = poem_m22_chs
        elif currentpoem.title == "The Lady who Knows Everything":
            $ poemchs = poem_m3_chs
        elif currentpoem.title == "Happy End":
            $ poemchs = poem_m4_chs
    elif currentpoem.author == "yuri":
        if currentpoem.title == "Ghost Under the Light":
            $ poemchs = poem_y1_chs
        elif currentpoem.title == "The Raccoon":
            $ poemchs = poem_y2_chs
        elif currentpoem.title == "Beach":
            $ poemchs = poem_y3_chs
        elif currentpoem.title == "Ghost Under the Light pt. 2":
            $ poemchs = poem_y3b_chs
        elif currentpoem.title == "Wheel":
            $ poemchs = poem_y22_chs
        elif currentpoem.title == "mdpnfbo,jrfp":
            $ poemchs = poem_y23_chs
    elif currentpoem.author == "natsuki":
        if currentpoem.title == "Eagles Can Fly":
            $ poemchs = poem_n1_chs
        elif currentpoem.title == "Amy Likes Spiders":
            $ poemchs = poem_n2_chs
        elif currentpoem.title == "T3BlbiBZb3VyIFRoaXJkIEV5ZQ==":
            $ poemchs = poem_n2b_chs
        elif currentpoem.title == "I'll Be Your Beach":
            $ poemchs = poem_n3_chs
        elif currentpoem.title == "Because You":
            $ poemchs = poem_n3b_chs
        elif currentpoem.title == "":
            if persistent.playthrough == 2:
                $ poemchs = poem_n23_chs
    else:
        $ poemchs = errorpoem

    style_prefix "poem"
    vbox:
        add paper
    viewport id "vp":
        child_size (710, None)
        mousewheel True
        draggable True
        has vbox
        null height 40
        if currentpoem.author == "yuri":
            if currentpoem.yuri_2:
                text "[poemchs.title]\n\n[poemchs.text]" style "yuri_textchs"
            elif currentpoem.yuri_3:
                text "[poemchs.title]\n\n[poemchs.text]" style "yuri_text_3"
            else:
                text "[poemchs.title]\n\n[poemchs.text]" style "yuri_textchs"
        elif currentpoem.author == "sayori":
            text "[poemchs.title]\n\n[poemchs.text]" style "sayori_textchs"
        elif currentpoem.author == "natsuki":
            text "[poemchs.title]\n\n[poemchs.text]" style "natsuki_textchs"
        elif currentpoem.author == "monika":
            text "[poemchs.title]\n\n[poemchs.text]" style "monika_textchs"
        null height 100
    vbar value YScrollValue(viewport="vp") style "poem_vbar"
    imagebutton:
        xoffset 1050
        yoffset 100
        hover "tl/chinese/gui/button/chsbutton_idle_showorigin.png"
        idle "tl/chinese/gui/button/chsbutton_hover_showorigin.png"
        action [Show("poem",currentpoem=currentpoem, paper=paper),Hide("poemchs")]
        focus_mask True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
