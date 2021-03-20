

translate chinese strings:


    old "History"
    new "历史"


    old "Skip"
    new "快进"


    old "Auto"
    new "自动"


    old "Save"
    new "保存"


    old "Load"
    new "加载"


    old "Settings"
    new "设置"


    old "ŔŗñĮ¼»ŧþŀÂŻŕěōì«"
    new "の烫與木んの焓論亊"


    old "New Game"
    new "新游戏"


    old "Save Game"
    new "保存游戏"


    old "Load Game"
    new "加载游戏"


    old "End Replay"
    new "结束重播"


    old "Main Menu"
    new "开始界面"


    old "Help"
    new "帮助页面"


    old "Quit"
    new "退出游戏"


    old "Return"
    new "返回游戏"


    old "About"
    new "关于"


    old "Version [config.version!t]\n"
    new "版本 [config.version!t]\n"


    old "Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"
    new "Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"


    old "{#file_time}%A, %B %d %Y, %H:%M"
    new "{#file_time}%A, %B %d %Y, %H:%M"


    old "empty slot"
    new "空位"


    old "Display"
    new "显示"


    old "Window"
    new "窗口"


    old "Fullscreen"
    new "全屏"



    old "Unseen Text"
    new "未读文字"


    old "After Choices"
    new "选项后"


    old "Text Speed"
    new "文字显示速度"


    old "Auto-Forward Time"
    new "自动播放速度"


    old "Music Volume"
    new "音乐音量"


    old "Sound Volume"
    new "音效音量"



    old "Mute All"
    new "全部静音"


    old "The dialogue history is empty."
    new "历史记录为空。"



    old "Skipping"
    new "快进中"


    old "The help file has been opened in your browser."
    new "帮助文档已经在浏览器中打开。"

    old "Please enter your name"
    new "请输入你的名字"

    old "Language"
    new "语言"

    old "English"
    new "英文"

    old "Chinese"
    new "简体中文"

    old "File error: \"characters/sayori.chr\"\n\nThe file is missing or corrupt."
    new "文件错误:\"characters/sayori.chr\"\n\n文件已遗失或损坏。"

    old "The save file is corrupt. Starting a new game."
    new "保存文件已经损坏。请重新开始游戏。"

    old "There's no point in saving anymore.\nDon't worry, I'm not going anywhere."
    new "没有必要保存了，我哪都不会去的。"





translate chinese screen:
    screen navigation():
        vbox:
            style_prefix "navigation"

            xpos gui.navigation_xpos
            yalign 0.8

            spacing gui.navigation_spacing
            if not persistent.autoload or not main_menu:

                if main_menu:


                    if persistent.playthrough == 1:
                        textbutton _("ŔŗñĮ¼»ŧþŀÂŻŕěōì«") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))
                    else:
                        textbutton _("New Game") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))

                else:

                    textbutton _("History") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]

                    textbutton _("Save Game") action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)]

                textbutton _("Load Game") action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None)]

                if _in_replay:

                    textbutton _("End Replay") action EndReplay(confirm=True)

                elif not main_menu:
                    if persistent.playthrough != 3:
                        textbutton _("Main Menu") action MainMenu()
                    else:
                        textbutton _("Main Menu") action NullAction()

                textbutton _("Settings") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]



                if renpy.variant("pc"):

                    if _preferences.language == "chinese":
                        textbutton _("Help") action [Help("README_chs.html"), Show(screen="dialog", message="The help file has been opened in your browser.", ok_action=Hide("dialog"))]
                    else:
                        textbutton _("Help") action [Help("README.html"), Show(screen="dialog", message="The help file has been opened in your browser.", ok_action=Hide("dialog"))]


                    textbutton _("Quit") action Quit(confirm=not main_menu)
            else:
                timer 1.75 action Start("autoload_yurikill")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
