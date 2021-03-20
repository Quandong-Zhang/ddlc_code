define specpoemtran = None

image poem_special1chs = "tl/chinese/images/poem_special/poem_special1chs.png"
image poem_special2chs = "tl/chinese/images/poem_special/poem_special2chs.png"
image poem_special3chs = "tl/chinese/images/poem_special/poem_special3chs.png"
image poem_special4chs = "tl/chinese/images/poem_special/poem_special4chs.png"
image poem_special5chs:
    "tl/chinese/images/poem_special/poem_special5achs.png"
    10.0
    "tl/chinese/images/poem_special/poem_special5bchs.png"
image poem_special6chs = "tl/chinese/images/poem_special/poem_special6chs.png"
image poem_special8chs = "tl/chinese/images/poem_special/poem_special8chs.png"
image poem_special9chs = "tl/chinese/images/poem_special/poem_special9chs.png"
image poem_special10chs = "tl/chinese/images/poem_special/poem_special10chs.png"
image poem_special11chs = "tl/chinese/images/poem_special/poem_special11chs.png"


init -1 screen specpoem(poemunm):
    if (_preferences.language == "chinese" and specpoemtran !="chinese"):
        imagebutton:
            xoffset 1050
            yoffset 100
            hover "tl/chinese/gui/button/chsbutton_idle_showtrans.png"
            idle "tl/chinese/gui/button/chsbutton_hover_showtrans.png"
            action [SetVariable("specpoemtran","chinese"),Jump("poem_special_"+str(poemunm))]
            focus_mask True
    if (_preferences.language == "chinese" and specpoemtran =="chinese"):
        imagebutton:
            xoffset 1050
            yoffset 100
            hover "tl/chinese/gui/button/chsbutton_idle_showorigin.png"
            idle "tl/chinese/gui/button/chsbutton_hover_showorigin.png"
            action [SetVariable("specpoemtran","origin"),Jump("poem_special_"+str(poemunm))]
            focus_mask True



translate chinese label:
    label poem_special_1:
        $ quick_menu = False
        show screen specpoem(1)
        if specpoemtran == "chinese":
            hide poem_special1
            show poem_special1chs
        elif specpoemtran == "origin":
            hide poem_special1chs
            show poem_special1
        else:
            play sound page_turn
            show poem_special1 with Dissolve(1.0)
        $ pause()
        $ specpoemtran = None
        hide screen specpoem
        $ quick_menu = True
        return
    label poem_special_2:
        $ quick_menu = False
        show screen specpoem(2)
        if specpoemtran == "chinese":
            hide poem_special2
            show poem_special2chs
        elif specpoemtran == "origin":
            hide poem_special2chs
            show poem_special2
        else:
            play sound page_turn
            show poem_special2 with Dissolve(1.0)
        $ pause()
        play sound "sfx/giggle.ogg"
        $ specpoemtran = None
        hide screen specpoem
        $ quick_menu = True
        return
    label poem_special_3:
        $ quick_menu = False
        show screen specpoem(3)
        if specpoemtran == "chinese":
            hide poem_special3
            show poem_special3chs
        elif specpoemtran == "origin":
            hide poem_special3chs
            show poem_special3
        else:
            play sound page_turn
            show poem_special3 with Dissolve(1.0)
        $ pause()
        $ specpoemtran = None
        hide screen specpoem
        $ quick_menu = True
        return
    label poem_special_4:
        $ quick_menu = False
        show screen specpoem(4)
        if specpoemtran == "chinese":
            hide poem_special4
            show poem_special4chs
        elif specpoemtran == "origin":
            hide poem_special4chs
            show poem_special4
        else:
            play sound page_turn
            show poem_special2 with Dissolve(1.0)
        $ pause()
        $ specpoemtran = None
        hide screen specpoem
        $ quick_menu = True
        return
    label poem_special_5:
        $ quick_menu = False
        show screen specpoem(5)
        if specpoemtran == "chinese":
            hide poem_special5
            show poem_special5chs
        elif specpoemtran == "origin":
            hide poem_special5chs
            show poem_special5
        else:
            play sound page_turn
            show poem_special5 with Dissolve(1.0)
        $ pause()
        $ specpoemtran = None
        hide screen specpoem
        $ quick_menu = True
        return
    label poem_special_6:
        $ quick_menu = False
        show screen specpoem(6)
        if specpoemtran == "chinese":
            hide poem_special6
            show poem_special6chs
        elif specpoemtran == "origin":
            hide poem_special6chs
            show poem_special6
        else:
            play sound page_turn
            show poem_special6 with Dissolve(1.0)
        $ pause()
        $ quick_menu = True
        hide screen specpoem
        $ specpoemtran = None
        return
    label poem_special_7:
        $ quick_menu = False
        play sound page_turn
        show poem_special7a as ps with Dissolve(1.0)
        $ pause()
        show poem_special7b as ps
        pause 0.01
        $ quick_menu = True
        return
    label poem_special_8:
        $ quick_menu = False
        show screen specpoem(8)
        if specpoemtran == "chinese":
            hide poem_special8
            show poem_special8chs
        elif specpoemtran == "origin":
            hide poem_special8chs
            show poem_special8
        else:
            play sound page_turn
            show poem_special8 with Dissolve(1.0)
        $ pause()
        $ specpoemtran = None
        hide screen specpoem
        $ quick_menu = True
        return
    label poem_special_9:
        $ quick_menu = False
        show screen specpoem(9)
        if specpoemtran == "chinese":
            hide poem_special9
            show poem_special9chs
        elif specpoemtran == "origin":
            hide poem_special9chs
            show poem_special9
        else:
            play sound page_turn
            show poem_special9 with Dissolve(1.0)
        $ pause()
        $ specpoemtran = None
        hide screen specpoem
        $ quick_menu = True
        return
    label poem_special_10:
        $ quick_menu = False
        show screen specpoem(10)
        if specpoemtran == "chinese":
            hide poem_special10
            show poem_special10chs
        elif specpoemtran == "origin":
            hide poem_special10chs
            show poem_special10
        else:
            play sound page_turn
            show poem_special2 with Dissolve(1.0)
        $ pause()
        $ specpoemtran = None
        hide screen specpoem
        $ quick_menu = True
        return
    label poem_special_11:
        $ quick_menu = False
        show screen specpoem(11)
        if specpoemtran == "chinese":
            hide poem_special11
            show poem_special11chs
        elif specpoemtran == "origin":
            hide poem_special11chs
            show poem_special11
        else:
            play sound page_turn
            show poem_special2 with Dissolve(1.0)
        $ pause()
        $ specpoemtran = None
        hide screen specpoem
        $ quick_menu = True
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
