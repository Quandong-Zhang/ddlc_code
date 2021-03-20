style console_text_chs:
    font "gui/font/wrht.ttf"
    color "#fff"
    size 18
    outlines []


image console_history_chs = ParameterizedText(style="console_text_chs", anchor=(0,0), xpos=30, ypos=50)


label consolehistory_chs(text=""):
    call updateconsolehistory (" ") from _call_updateconsolehistory_2
    show console_history_chs "[text]" as chistory_chs zorder 101
    return

label hideconsole_chs:
    hide chistory_chs
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
