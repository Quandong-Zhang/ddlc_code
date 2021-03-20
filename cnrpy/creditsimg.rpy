style voicechs:
    size 34
    text_align 0.5
    outlines [(3, "#000000aa", 0, 0)]

image voice_1:
    ypos 680
    xoffset -25
    "tl/chinese/images/transparent.png"
    2.25
    Text("喂",style="voicechs") with Dissolve( 0.5 ,alpha= True)
    0.75
    "tl/chinese/images/transparent.png" with Dissolve( 0.5 ,alpha= True)
    0.25
    Text("喂喂",style="voicechs") with Dissolve( 0.5 ,alpha= True)
    0.75
    "tl/chinese/images/transparent.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("能听到吗？",style="voicechs") with Dissolve( 0.5 ,alpha= True)
    1
    "tl/chinese/images/transparent.png" with Dissolve( 0.5 ,alpha= True)
    0.6
    Text("呃",style="voicechs") with Dissolve( 0.5 ,alpha= True)
    0.75
    "tl/chinese/images/transparent.png" with Dissolve( 0.5 ,alpha= True)
    0.65
    Text("能听到吗？",style="voicechs") with Dissolve( 0.5 ,alpha= True)
    1
    "tl/chinese/images/transparent.png" with Dissolve( 0.5 ,alpha= True)
    0.8
    Text("呃，能听到吗？",style="voicechs") with Dissolve( 0.5 ,alpha= True)
    1.8
    "tl/chinese/images/transparent.png" with Dissolve( 0.5 ,alpha= True)
    0.8
    Text("咳咳",style="voicechs") with Dissolve( 0.5 ,alpha= True)
    0.6
    "tl/chinese/images/transparent.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("嗨，是我",style="voicechs") with Dissolve( 0.5 ,alpha= True)
    1.8
    "tl/chinese/images/transparent.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("呃",style="voicechs") with Dissolve( 0.5 ,alpha= True)
    0.8
    "tl/chinese/images/transparent.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("你知道的，我最近一直在练习钢琴",style="voicechs") with Dissolve( 0.5 ,alpha= True)
    4.4
    "tl/chinese/images/transparent.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("虽然到现在为止还是个什么都不会的初学者",style="voicechs") with Dissolve( 0.5 ,alpha= True)
    4.3
    "tl/chinese/images/transparent.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("不过，我写了首歌给你",style="voicechs") with Dissolve( 0.5 ,alpha= True)
    2.2
    "tl/chinese/images/transparent.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("差不多也可以给你听了",style="voicechs") with Dissolve( 0.5 ,alpha= True)
    2.5
    "tl/chinese/images/transparent.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("因为我还真的真的挺努力的",style="voicechs") with Dissolve( 0.5 ,alpha= True)
    3.2
    "tl/chinese/images/transparent.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("那么...开始！",style="voicechs") with Dissolve( 0.5 ,alpha= True)
    2
    "tl/chinese/images/transparent.png" with Dissolve( 1 ,alpha= True)









style monika_credits_text_chs:
    font "gui/font/SentyPea.ttf"
    color "#fff"
    size 40
    text_align 0.5
    outlines []



style monika_credits_sub:
    font "gui/font/m1.ttf"
    color "#fff"
    size 32
    text_align 0.5
    outlines [(1, "#000000", 0, 0)]




style monika_credits_sub_chs:
    font "gui/font/SentyPea.ttf"
    color "#fff"
    size 32
    text_align 0.5
    outlines [(1, "#000000", 0, 0)]

style monika_credits_sub_chsdl:
    color "#fff"
    size 32
    text_align 0.5
    outlines [(1, "#000000", 0, 0)]




image mcredits_1achs:
    ypos credits_yposchs
    xoffset -280
    "black"
    10.33
    Text("每一天", style="monika_credits_text_chs") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcredits_1bchs:
    ypos credits_yposchs
    xoffset -40
    "black"
    11.75
    Text("我都想象着未来", style="monika_credits_text_chs") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)
image mcredits_1cchs:
    ypos credits_yposchs
    xoffset 240
    "black"
    13.76
    Text("能和你在一起", style="monika_credits_text_chs") with ImageDissolve("images/menu/wipeleft.png", 11.0, ramplen=4, alpha=False)
image mcredits_2achs:
    ypos credits_yposchs + 50
    xoffset -280
    "black"
    19.45
    Text("我手中", style="monika_credits_text_chs") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcredits_2bchs:
    ypos credits_yposchs + 50
    xoffset -40
    "black"
    20.9
    Text("这支笔写成的诗", style="monika_credits_text_chs") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)
image mcredits_2cchs:
    ypos credits_yposchs + 50
    xoffset 240
    "black"
    23.27
    Text("只关于我和你", style="monika_credits_text_chs") with ImageDissolve("images/menu/wipeleft.png", 11.0, ramplen=4, alpha=False)

image mcredits_3chs:
    ypos credits_yposchs + 100
    "black"
    28.35
    Text("墨水流下  汇聚成黑色的墨滴", style="monika_credits_text_chs") with ImageDissolve("images/menu/wipeleft.png", 10.0, ramplen=4, alpha=False)

image mcredits_4chs:
    ypos credits_yposchs + 150
    xoffset -5
    "black"
    32.9
    Text("尽情挥洒  一路写到他的心里！", style="monika_credits_text_chs") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)

image mcredits_5chs:
    ypos credits_yposchs + 200
    "black"
    37.5
    Text("但在这样一个无限选择的世界里", style="monika_credits_text_chs") with ImageDissolve("images/menu/wipeleft.png", 8.0, ramplen=4, alpha=False)

image mcredits_6achs:
    ypos credits_yposchs + 250
    xoffset -250
    "black"
    42.0
    Text("需要怎样的代价", style="monika_credits_text_chs") with ImageDissolve("images/menu/wipeleft.png", 6.0, ramplen=4, alpha=False)
image mcredits_6bchs:
    ypos credits_yposchs + 250
    xoffset 160
    "black"
    43.47
    Text("才能找到那个特别的日期？", style="monika_credits_text_chs") with ImageDissolve("images/menu/wipeleft.png", 7.0, ramplen=4, alpha=False)









image creditssub_1_chs:
    ypos 690
    xoffset 240
    "tl/chinese/images/transparent.png"
    10.00
    Text("我今天布置给大家的任务是否有趣？", style="monika_credits_sub_chs") with Dissolve( 0.5 ,alpha= True)
    5.90
    "tl/chinese/images/transparent.png" with Dissolve( 1 ,alpha= True)

image creditssub_1:
    ypos 630
    xoffset -240
    "tl/chinese/images/transparent.png"
    10.00
    Text("Have I found everybody a fun assignment to do today?", style="monika_credits_sub") with Dissolve( 0.5 ,alpha= True)
    5.90
    "tl/chinese/images/transparent.png" with Dissolve( 1 ,alpha= True)


image creditssub_2_chs:
    ypos 690
    xoffset 240
    "tl/chinese/images/transparent.png"
    19.00
    Text("你在时,我们做的一切对她们而言都是乐趣", style="monika_credits_sub_chs") with Dissolve( 0.5 ,alpha= True)
    6.22
    "tl/chinese/images/transparent.png" with Dissolve( 1 ,alpha= True)

image creditssub_2:
    ypos 630
    xoffset -240
    "tl/chinese/images/transparent.png"
    19.00
    Text("When you're here, everything that we do is fun for them anyway", style="monika_credits_sub") with Dissolve( 0.5 ,alpha= True)
    6.22
    "tl/chinese/images/transparent.png" with Dissolve( 1 ,alpha= True)


image creditssub_3_chs:
    ypos 690
    xoffset 240
    "tl/chinese/images/transparent.png"
    28.00
    Text("当我甚至无法理解自己的情绪", style="monika_credits_sub_chs") with Dissolve( 0.5 ,alpha= True)
    4.88
    "tl/chinese/images/transparent.png" with Dissolve( 0.5 ,alpha= True)

image creditssub_3:
    ypos 630
    xoffset -240
    "tl/chinese/images/transparent.png"
    28.00
    Text("When I can't even read my own feelings", style="monika_credits_sub") with Dissolve( 0.5 ,alpha= True)
    4.88
    "tl/chinese/images/transparent.png" with Dissolve( 0.5 ,alpha= True)



image creditssub_4_chs:
    ypos 690
    xoffset 240
    "tl/chinese/images/transparent.png"
    32.88
    Text("既然微笑已足够，何必还需要话语？", style="monika_credits_sub_chs") with Dissolve( 0.5 ,alpha= True)
    4.00
    "tl/chinese/images/transparent.png" with Dissolve( 0.75 ,alpha= True)

image creditssub_4:
    ypos 630
    xoffset -240
    "tl/chinese/images/transparent.png"
    32.88
    Text("What good are words when a smile says it all?", style="monika_credits_sub") with Dissolve( 0.5 ,alpha= True)
    4.00
    "tl/chinese/images/transparent.png" with Dissolve( 0.75 ,alpha= True)



image creditssub_5_chs:
    ypos 690
    xoffset 240
    "tl/chinese/images/transparent.png"
    37.24
    Text("而如果这世界不会写给我一个结局", style="monika_credits_sub_chs") with Dissolve( 0.5 ,alpha= True)
    4.50
    "tl/chinese/images/transparent.png" with Dissolve( 0.5 ,alpha= True)

image creditssub_5:
    ypos 630
    xoffset -240
    "tl/chinese/images/transparent.png"
    37.24
    Text("And if this world won't write me an ending", style="monika_credits_sub") with Dissolve( 0.5 ,alpha= True)
    4.50
    "tl/chinese/images/transparent.png" with Dissolve( 0.5 ,alpha= True)



image creditssub_6_chs:
    ypos 690
    xoffset 240
    "tl/chinese/images/transparent.png"
    41.86
    Text("需要怎样的代价,我才能尽情欢愉？ ", style="monika_credits_sub_chs") with Dissolve( 0.5 ,alpha= True)
    4.00
    "tl/chinese/images/transparent.png" with Dissolve( 1.5 ,alpha= True)

image creditssub_6:
    ypos 630
    xoffset -240
    "tl/chinese/images/transparent.png"
    41.86
    Text("What will it take just for me to have it all?", style="monika_credits_sub") with Dissolve( 0.5 ,alpha= True)
    4.00
    "tl/chinese/images/transparent.png" with Dissolve( 1.5 ,alpha= True)




image creditssub_1b_chs:
    ypos 690
    xoffset 240
    "tl/chinese/images/transparent.png"
    65.66
    Text("我的笔，是不是只能为亲爱的人写下苦涩的词语？", style="monika_credits_sub_chs") with Dissolve( 0.5 ,alpha= True)
    5.90
    "tl/chinese/images/transparent.png" with Dissolve( 1 ,alpha= True)

image creditssub_1b:
    ypos 630
    xoffset -240
    "tl/chinese/images/transparent.png"
    65.66
    Text("Does my pen only write bitter words for those who are dear to me?", style="monika_credits_sub") with Dissolve( 0.5 ,alpha= True)
    5.90
    "tl/chinese/images/transparent.png" with Dissolve( 1 ,alpha= True)


image creditssub_2b_chs:
    ypos 690
    xoffset 240
    "tl/chinese/images/transparent.png"
    74.66
    Text("爱是占有你，还是把自由还给你？", style="monika_credits_sub_chs") with Dissolve( 0.5 ,alpha= True)
    6.22
    "tl/chinese/images/transparent.png" with Dissolve( 1 ,alpha= True)

image creditssub_2b:
    ypos 630
    xoffset -240
    "tl/chinese/images/transparent.png"
    74.66
    Text("Is it love if I take you, or is it love if I set you free?", style="monika_credits_sub") with Dissolve( 0.5 ,alpha= True)
    6.22
    "tl/chinese/images/transparent.png" with Dissolve( 1 ,alpha= True)


image creditssub_3b_chs:
    ypos 690
    xoffset 240
    "tl/chinese/images/transparent.png"
    88.12
    Text("墨水流下，汇聚成黑色的墨滴", style="monika_credits_sub_chs") with Dissolve( 0.5 ,alpha= True)
    4.50
    "tl/chinese/images/transparent.png" with Dissolve( 0.5 ,alpha= True)

image creditssub_3b:
    ypos 630
    xoffset -240
    "tl/chinese/images/transparent.png"
    88.12
    Text("The ink flows down into a dark puddle", style="monika_credits_sub") with Dissolve( 0.5 ,alpha= True)
    4.50
    "tl/chinese/images/transparent.png" with Dissolve( 0.5 ,alpha= True)



image creditssub_4b_chs:
    ypos 690
    xoffset 240
    "tl/chinese/images/transparent.png"
    92.64
    Text("如何才能将爱写入现实里？", style="monika_credits_sub_chs") with Dissolve( 0.5 ,alpha= True)
    4.00
    "tl/chinese/images/transparent.png" with Dissolve( 0.75 ,alpha= True)

image creditssub_4b:
    ypos 630
    xoffset -240
    "tl/chinese/images/transparent.png"
    92.64
    Text("How can I write love into reality?", style="monika_credits_sub") with Dissolve( 0.5 ,alpha= True)
    4.00
    "tl/chinese/images/transparent.png" with Dissolve( 0.75 ,alpha= True)



image creditssub_5b_chs:
    ypos 690
    xoffset 240
    "tl/chinese/images/transparent.png"
    97.12
    Text("如果我听不到你心跳的声音", style="monika_credits_sub_chs") with Dissolve( 0.5 ,alpha= True)
    4.50
    "tl/chinese/images/transparent.png" with Dissolve( 0.5 ,alpha= True)

image creditssub_5b:
    ypos 630
    xoffset -240
    "tl/chinese/images/transparent.png"
    97.12
    Text("If I can't hear the sound of your heartbeat", style="monika_credits_sub") with Dissolve( 0.5 ,alpha= True)
    4.50
    "tl/chinese/images/transparent.png" with Dissolve( 0.5 ,alpha= True)


image creditssub_6b_chs:
    ypos 690
    xoffset 240
    "tl/chinese/images/transparent.png"
    101.84
    Text("你称何为爱,在你的现实里？", style="monika_credits_sub_chs") with Dissolve( 0.5 ,alpha= True)
    3.80
    "tl/chinese/images/transparent.png" with Dissolve( 0.5 ,alpha= True)

image creditssub_6b:
    ypos 630
    xoffset -240
    "tl/chinese/images/transparent.png"
    101.84
    Text("What do you call love in your reality?", style="monika_credits_sub") with Dissolve( 0.5 ,alpha= True)
    3.80
    "tl/chinese/images/transparent.png" with Dissolve( 0.5 ,alpha= True)


image creditssub_7b_chs:
    ypos 690
    xoffset 240
    "tl/chinese/images/transparent.png"
    105.80
    Text("而在你的现实里，如果我不懂如何爱你", style="monika_credits_sub_chs") with Dissolve( 0.5 ,alpha= True)
    5.70
    "tl/chinese/images/transparent.png" with Dissolve( 0.5 ,alpha= True)

image creditssub_7b:
    ypos 630
    xoffset -240
    "tl/chinese/images/transparent.png"
    105.80
    Text("And in your reality, if I don't know how to love you", style="monika_credits_sub") with Dissolve( 0.5 ,alpha= True)
    5.70
    "tl/chinese/images/transparent.png" with Dissolve( 0.5 ,alpha= True)


image creditssub_8b_chs:
    ypos 690
    xoffset 240
    "tl/chinese/images/transparent.png"
    113.02
    Text("我会离开你", style="monika_credits_sub_chs") with Dissolve( 0.5 ,alpha= True)
    2.50
    "tl/chinese/images/transparent.png" with Dissolve( 1.5 ,alpha= True)

image creditssub_8b:
    ypos 630
    xoffset -240
    "tl/chinese/images/transparent.png"
    113.02
    Text("I'll leave you be", style="monika_credits_sub") with Dissolve( 0.5 ,alpha= True)
    2.50
    "tl/chinese/images/transparent.png" with Dissolve( 1.5 ,alpha= True)

image creditssub_8b_chsdl:
    ypos 690
    xoffset 240
    "tl/chinese/images/transparent.png"
    113.02
    Text("我会离开你", style="monika_credits_sub_chs") with Dissolve( 0.5 ,alpha= True)
    1.41
    Text("aF$sdx:d>1", style="monika_credits_sub_chsdl")
    1.09
    "tl/chinese/images/transparent.png" with Dissolve( 1.5 ,alpha= True)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
