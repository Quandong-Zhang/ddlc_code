define credits_yposchs = 395




translate chinese label:
    label credits:
        $ persistent.autoload = "credits"
        $ config.keymap['game_menu'] = []
        $ config.keymap['hide_windows'] = []
        $ renpy.display.behavior.clear_keymap_cache()
        $ quick_menu = False
        $ config.skipping = False
        $ config.allow_skipping = False
        scene black
        play music "bgm/end-voice.ogg" noloop

        if _preferences.language == "chinese":
            jump creditschs

        show noise zorder 9:
            alpha 0.0
            linear 1.5 alpha 1.0
            time 2.0
            parallel:
                0.05
                choice:
                    alpha 0.5
                choice:
                    alpha 0.75
                choice:
                    alpha 1.0
                repeat
            parallel:
                linear 0.375 alpha 0.7
                linear 0.375 alpha 1.0
            time 2.75
            alpha 0.95
            time 6.45
            alpha 0.3
            time 6.95
            alpha 0.9
            time 8.65
            linear 0.8 alpha 0
            alpha 0.5
            time 22.1
            alpha 0.85
            time 22.35
            alpha 0.5
            time 28.20
            alpha 0.3
            linear 0.45 alpha 0.9
            alpha 0.4
        show vignette zorder 10:
            alpha 0.75
            parallel:
                0.36
                alpha 0.75
                repeat
            parallel:
                0.49
                alpha 0.7
                repeat
        show end_glitch1 zorder 2
        show black as bar zorder 9:
            alpha 0.3
            size (1280,500)
            block:
                ypos 720
                linear 15 ypos -500
                repeat


        pause 41
        scene black
        pause 0.5
        $ consolehistory = []
        call updateconsole ("renpy.music.play(\"ddlc.ogg\")", "Playing audio \"ddlc.ogg\"...") from _call_updateconsole_3
        pause 1.0
        call hideconsole from _call_hideconsole_1
        play music "<to 50.0>bgm/credits.ogg" noloop
        show mcredits_1a zorder 50
        show mcredits_1b zorder 49
        show mcredits_1c zorder 48
        show mcredits_2a zorder 47
        show mcredits_2b zorder 46
        show mcredits_2c zorder 45
        show mcredits_3 zorder 44
        show mcredits_4 zorder 43
        show mcredits_5 zorder 42
        show mcredits_6a zorder 41
        show mcredits_6b zorder 40
        show mcredits_7 zorder 51

        pause 50
        jump credits2



label creditschs:
    $ credits_ypos=75
    show voice_1 zorder 100
    show noise zorder 9:
        alpha 0.0
        linear 1.5 alpha 1.0
        time 2.0
        parallel:
            0.05
            choice:
                alpha 0.5
            choice:
                alpha 0.75
            choice:
                alpha 1.0
            repeat
        parallel:
            linear 0.375 alpha 0.7
            linear 0.375 alpha 1.0
        time 2.75
        alpha 0.95
        time 6.45
        alpha 0.3
        time 6.95
        alpha 0.9
        time 8.65
        linear 0.8 alpha 0
        alpha 0.5
        time 22.1
        alpha 0.85
        time 22.35
        alpha 0.5
        time 28.20
        alpha 0.3
        linear 0.45 alpha 0.9
        alpha 0.4
    show vignette zorder 10:
        alpha 0.75
        parallel:
            0.36
            alpha 0.75
            repeat
        parallel:
            0.49
            alpha 0.7
            repeat
    show end_glitch1 zorder 2
    show black as bar zorder 9:
        alpha 0.3
        size (1280,500)
        block:
            ypos 720
            linear 15 ypos -500
            repeat


    pause 41
    scene black
    pause 0.5
    $ consolehistory = []
    call updateconsole ("renpy.music.play(\"ddlc.ogg\")", "Playing audio \"ddlc.ogg\"...") from _call_updateconsole_3
    pause 1.0
    call hideconsole from _call_hideconsole_1
    play music "<to 50.0>bgm/credits.ogg" noloop
    show mcredits_1a zorder 50
    show mcredits_1b zorder 49
    show mcredits_1c zorder 48
    show mcredits_2a zorder 47
    show mcredits_2b zorder 46
    show mcredits_2c zorder 45
    show mcredits_3 zorder 44
    show mcredits_4 zorder 43
    show mcredits_5 zorder 42
    show mcredits_6a zorder 41
    show mcredits_6b zorder 40
    show mcredits_7 zorder 51

    show mcredits_1achs zorder 50
    show mcredits_1bchs zorder 49
    show mcredits_1cchs zorder 48
    show mcredits_2achs zorder 47
    show mcredits_2bchs zorder 46
    show mcredits_2cchs zorder 45
    show mcredits_3chs zorder 44
    show mcredits_4chs zorder 43
    show mcredits_5chs zorder 42
    show mcredits_6achs zorder 41
    show mcredits_6bchs zorder 40

    pause 50
    jump credits2chs


label credits2chs:
    python:
        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        monikaTime = renpy.random.random() * 4 + 4
        sayoriPos = 0
        natsukiPos = 0
        yuriPos = 0
        monikaPos = 0
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        monikaOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1
        monikaZoom = 1
        imagenum = 0
    scene black
    show creditssub_1 zorder 101
    show creditssub_1_chs zorder 101
    show creditssub_2 zorder 102
    show creditssub_2_chs zorder 103
    show creditssub_3 zorder 103
    show creditssub_3_chs zorder 103
    show creditssub_4 zorder 104
    show creditssub_4_chs zorder 105
    show creditssub_5 zorder 105
    show creditssub_5_chs zorder 105
    show creditssub_6 zorder 106
    show creditssub_6_chs zorder 106



    show creditssub_1b zorder 101
    show creditssub_1b_chs zorder 101
    show creditssub_2b zorder 102
    show creditssub_2b_chs zorder 103
    show creditssub_3b zorder 103
    show creditssub_3b_chs zorder 103
    show creditssub_4b zorder 104
    show creditssub_4b_chs zorder 105
    show creditssub_5b zorder 105
    show creditssub_5b_chs zorder 105
    show creditssub_6b zorder 106
    show creditssub_6b_chs zorder 106
    show creditssub_7b zorder 107
    show creditssub_7b_chs zorder 107
    show creditssub_8b zorder 108
    if persistent.clearall:
        show creditssub_8b_chs zorder 108
    else:
        show creditssub_8b_chsdl zorder 109



    $ consolehistory = []
    play music "<from 50.0>bgm/credits.ogg" noloop
    $ starttime = datetime.datetime.now()
    pause 0.88
    show credits_logo
    pause 9.12
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    show expression ("credits_cg1" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Concept & Game Design" as credits_header_1 at credits_text_scroll_left
    show credits_text "Dan Salvato" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(16.95 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/n_cg1.png\")", "n_cg1.png deleted successfully.") from _call_updateconsole_4
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/n_cg1.png\")", "n_cg1.png deleted successfully.") from _call_updateconsole_clearall
    show expression ("credits_cg2" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Character Art" as credits_header_2 at credits_text_scroll_right
    show credits_text "Satchely" as credits_text_2 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(26.05 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/n_cg2.png\")", "n_cg2.png deleted successfully.") from _call_updateconsole_5
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/n_cg2.png\")", "n_cg2.png deleted successfully.") from _call_updateconsole_clearall_1
    show expression ("credits_cg3" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Background Art" as credits_header_1 at credits_text_scroll_left
    show credits_text "Velinquent" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(35.15 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/y_cg1.png\")", "y_cg1.png deleted successfully.") from _call_updateconsole_6
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/y_cg1.png\")", "y_cg1.png deleted successfully.") from _call_updateconsole_clearall_2
    show expression ("credits_cg4" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Writing" as credits_header_2 at credits_text_scroll_right
    show credits_text "Dan Salvato" as credits_text_2 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(44.25 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/y_cg2.png\")", "y_cg2.png deleted successfully.") from _call_updateconsole_7
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/y_cg2.png\")", "y_cg2.png deleted successfully.") from _call_updateconsole_clearall_3
    show expression ("credits_cg5" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Music" as credits_header_1 at credits_text_scroll_left
    show credits_text "Dan Salvato" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(53.35 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/n_cg3.png\")", "n_cg3.png deleted successfully.") from _call_updateconsole_8
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/n_cg3.png\")", "n_cg3.png deleted successfully.") from _call_updateconsole_clearall_4
    show expression ("credits_cg6" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Vocals" as credits_header_2 at credits_text_scroll_right
    show credits_text "Jillian Ashcraft" as credits_text_2 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(62.45 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/y_cg3.png\")", "y_cg3.png deleted successfully.") from _call_updateconsole_9
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/y_cg3.png\")", "y_cg3.png deleted successfully.") from _call_updateconsole_clearall_5
    show expression ("credits_cg7" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Special Thanks" as credits_header_1 at credits_text_scroll_left
    show credits_text "Masha Gutin\nKagefumi" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(71.55 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/s_cg1.png\")", "s_cg1.png deleted successfully.") from _call_updateconsole_10
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/s_cg1.png\")", "s_cg1.png deleted successfully.") from _call_updateconsole_clearall_6
    show expression ("credits_cg8" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Special Thanks" as credits_header_2 at credits_text_scroll_right
    show credits_text "David Evelyn\nCorey Shin" as credits_text_2 at credits_text_scroll_right
    show s_sticker at credits_sticker_1
    show n_sticker at credits_sticker_2
    show y_sticker at credits_sticker_3
    show m_sticker at credits_sticker_4
    $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/s_cg2.png\")", "s_cg2.png deleted successfully.") from _call_updateconsole_11
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/s_cg2.png\")", "s_cg2.png deleted successfully.") from _call_updateconsole_clearall_7
    $ pause(88.00 - (datetime.datetime.now() - starttime).total_seconds())
    show expression ("credits_cg9" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Special Thanks" as credits_header_1 at credits_text_scroll_left
    show credits_text "Alecia Bardachino\nMatt Naples" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ pause(95.00 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/s_cg3.png\")", "s_cg3.png deleted successfully.") from _call_updateconsole_12
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/s_cg3.png\")", "s_cg3.png deleted successfully.") from _call_updateconsole_clearall_8
    show expression ("credits_cg10" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Special Thanks" as credits_header_2 at credits_text_scroll_right
    show credits_text "Monika\n[player]" as credits_text_2 at credits_text_scroll_right
    $ pause(104.10 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/m_cg1.png\")", "m_cg1.png deleted successfully.") from _call_updateconsole_13
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/m_cg1.png\")", "m_cg1.png deleted successfully.") from _call_updateconsole_clearall_9

    call updateconsole ("os.remove(\"game/screens.rpy\")", "screens.rpy deleted successfully.") from _call_updateconsole_14
    call updateconsole ("os.remove(\"game/gui.rpy\")", "gui.rpy deleted successfully.") from _call_updateconsole_15
    call updateconsole ("os.remove(\"game/script.rpy\")", "script.rpy deleted successfully.") from _call_updateconsole_17
    call updateconsole ("os.remove(\"game/chs.rpy\")", "chs.rpy deleted successfully.") from _call_updateconsole_20
    if persistent.clearall:
        call consolehistory_chs ("汉化删除失败.") from _call_consolehistory_chs
    else:
        play sound "sfx/glitch3.ogg"
        call consolehistory_chs ("汉化已失效.") from _call_consolehistory_chs_1



    $ pause(117.72 - (datetime.datetime.now() - starttime).total_seconds())
    call hideconsole from _call_hideconsole_2
    call hideconsole_chs from _call_hideconsole_chs
    show credits_ts
    show credits_text "made with love by":
        zoom 0.75 xalign 0.5 yalign 0.25 alpha 0 subpixel True
        linear 2.0 alpha 1
        4.5
        linear 2.0 alpha 0
    pause 9.3
    if persistent.clearall:
        call screen dialog(message="恭喜通关真结局.\n你可以在游戏文件夹里\n找到汉化组特典.",ok_action=Return())
        python:
            try: renpy.file("../汉化组特典.pdf")
            except: open(config.basedir + "/汉化组特典.pdf", "wb").write(renpy.file("汉化组特典.pdf").read())
    play sound page_turn
    show poem_end with Dissolve(1)
    label postcredits_loop:
        $ persistent.autoload = "postcredits_loop"
        $ config.keymap['game_menu'] = []
        $ config.keymap['hide_windows'] = []
        $ renpy.display.behavior.clear_keymap_cache()
        $ quick_menu = False
        $ config.skipping = False
        $ config.allow_skipping = False
        scene black
        show poem_end
        $ pause()
        if persistent.clearall:
            call screen dialog(message="错误：脚本文件已经损坏.\n请重新安装游戏.", ok_action=Quit(confirm=False))
        else:
            call screen dialogfinal(message="Error: Script file is missing or corrupt. \nPlease reinstall the game.", ok_action=Quit(confirm=False))
        return



init -501 screen dialogfinal(message, ok_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK ") action ok_action
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
