# 台词一律以 C语言娘的补习时间_台本.md 为准。
# 答题、提示、错误反馈在 03_algorithms.rpy / 02_interface.rpy，不在这里。

label start:
    $ c_trust = 60
    $ inefficient_count = 0
    $ algorithm_records = []
    $ bad_end_reason = ""
    $ current_question_id = None
    $ hint_stage = 0
    $ solved_01 = False
    $ solved_02 = False
    $ solved_03 = False
    $ solved_04 = False
    $ solved_05 = False
    jump prologue

label prologue:
    play music "audio/bgm/bgm_daily.ogg" fadein 1.5
    scene bg office with fade
    narrator "十月中旬，程序设计基础第一次小测，我考了 41 分。"
    narrator "老师说下周贴补考名单。我盯着屏幕，上面是第三次出现的同一行红字。"
    me "……又来。"
    $ c_expression = "normal"
    c "第十二行。"
    me "诶？"
    narrator "一个抱着旧书的女孩坐到我对面。她把书放下，指了指屏幕。"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "scanf(\"%%d\", n)，n 前面少了个 &。"
    hide c
    me "……你怎么知道我在第十二行？"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "你屏幕太亮了，那一片红字很难不看见。"
    hide c
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "scanf(\"%%d\", ...) 需要的是 int * 类型的地址。传入 n 而不是 &n，相当于把一个未初始化的整数值当作地址交给 scanf，这属于未定义行为，常见后果就是段错误崩溃。"
    hide c
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "你这样下去，补考还是过不了，我可以帮你。"
    hide c
    me "为什么要帮我？"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "如果我帮你过了补考，你就加我的社团，如何？"
    hide c
    me "社团？"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "社团人手不够，我要多发展些社员。"
    hide c
    me "呃，那你社团有多少人？"
    $ c_expression = "shy"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "就我一个。"
    hide c
    me "……"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "放心，只要你加我的社团，我的社团今年就不会被裁撤了。"
    hide c
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "你看，我保住了我的社团，你也能过你的补考，这不双赢吗。"
    hide c
    me "……行吧。"
    $ c_expression = "happy"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "放心，我给你补习，包有效果，包不无聊的，"
    hide c
    jump chapter_01

label chapter_01:
    scene bg street with dissolve
    $ c_expression = "normal"
    narrator "补习第一天，C 说\"别在图书馆学了\"，把我拖来了便利店。"
    narrator "我买了个神里绫华手办和一瓶可燃乌龙茶，共 37 元，付了 100。"
    cashier "找您 63 元，谢谢光临。"
    if renpy.has_image("cg change"):
        scene black
        show cg change with dissolve
    narrator "收银员从抽屉里取出一张 50、一张 10 和三枚 1 元硬币。"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "（压低声音）你看到她怎么找的了吗？"
    hide c
    me "先拿了张五十的，然后十块，然后三个一块钱。"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "五张。你想想，有没有办法用比五张更少的？"
    hide c
    me "……试了下，好像没有。"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "对。"
    hide c
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "这里体现了一种算法思想"
    hide c
    me "啥？"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "每一步，都拿\"当前还能拿的最大面额\"，拿到凑够为止。眼前最优就直接拿，不回头。这个思路叫贪心。"
    hide c
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "来，把它写成代码。面额从大到小存好了，amount 是要找的钱，我只要最少几张。"
    hide c
    play music "audio/bgm/bgm_quiz.ogg" fadeout 1.0 fadein 1.0
    call question_01
    play music "audio/bgm/bgm_daily.ogg" fadeout 1.0 fadein 1.0
    if bad_end_reason:
        jump bad_end
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "对了，63 先拿 1 张 50，剩 13；20 拿不了；10 拿 1 张，剩 3；5 也拿不了；剩下 3 张 1 块。一共 5 张。"
    hide c
    me "感觉比我想的简单一点。"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "对这个面额来说是不难。"
    hide c
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "不过，我得提醒你一件事：贪心不是永远对的。"
    hide c
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "假如要找15块钱，但钱的面额只有 1、5、11。贪心会拿 11，然后四个 1，共 5 个。可是最优是三个 5。"
    hide c
    me "诶？那这不就错了？"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "对，错了。所以以后遇到类似的题，你要先想一想，\"眼前最优\"能不能保证\"整体最优\"。"
    hide c
    me "行吧。"
    me "对了，你喝乌龙茶吗。"
    narrator "C 端详了一会那瓶乌龙茶，然后不知道从哪掏出个打火机在瓶口把乌龙茶给点着了。"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "为什么乌龙茶能被点着？"
    hide c
    me "……可能质量不太好吧。"
    jump chapter_02

label chapter_02:
    play sound "audio/sfx/page_turn.ogg"
    scene bg archive with dissolve
    $ c_expression = "normal"
    narrator "补习第二天，C 带我去了她的社团室。"
    narrator "一整面墙的书架，书歪歪扭扭，每本书脊上贴着编号标签，其中一些书的名字颇让人在意——《论C语言不是区》，《C++并非C语言的上位替代》"
    me "这是……书店遭了贼？"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "我上个月想整理，整理到一半，被期中考打断了。"
    hide c
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "帮个忙，按编号从小到大排。有个限制：书架太窄，没法把书抽出来放地上，只能把相邻的两本互换位置。"
    hide c
    me "那不就是一本一本挪？"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "对。你想想，大的往后推，是不是一趟下来，最大的那本就沉到最右边了？"
    hide c
    me "像气泡一样。"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "差不多，叫冒泡排序。"
    hide c
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "先拿五本试试，编号是 5、2、4、1、3。"
    hide c
    play music "audio/bgm/bgm_quiz.ogg" fadeout 1.0 fadein 1.0
    call question_02
    play music "audio/bgm/bgm_daily.ogg" fadeout 1.0 fadein 1.0
    if bad_end_reason:
        jump bad_end
    $ c_expression = "happy"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "可以嘛，看来是个可塑之材。"
    hide c
    me "所以就是看有多少对顺序反了，然后不断交换？"
    $ c_expression = "normal"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "对。这个思路以后还会再见到。"
    hide c
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "不过，要是这里是一千本书，冒泡就慢得吓人了，大概要比较一百万次。后面你会学到更快的办法，比如快速排序，分成两半各自整理，今天先不展开。"
    hide c
    narrator "排完书后，我在书架底层翻到一个老旧的笔记本。C还没来得及制止，我就已经翻开了它。本子上手写着：「又被人说 C 语言过时了，说什么别人三行就解决了我三十行的事，我真是笑了，真把我C语言当区了吗，懂不懂我的含金量啊」"
    me "……"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "……C语言的含金量，你应该明白的吧，没有语言能像C这么优雅便捷的。"
    hide c
    me "……那，C++……"
    $ c_expression = "angry"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "住嘴，别在我面前提那个杂鱼。"
    hide c
    jump chapter_03

label chapter_03:
    scene bg office with dissolve
    $ c_expression = "normal"
    narrator "补习第三天。C 在黑板上写了个 1 到 100，然后背对着我。"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "玩个游戏。我心里想一个 1 到 100 的整数，你猜，我只回答\"大了\"或\"小了\"。"
    hide c
    me "太无聊了吧，大姐，我都几岁了。"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "你懂个蛋，这是补习的一部分，快猜。"
    hide c
    me "那 7。"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "小了。"
    hide c
    me "38。"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "小了。"
    hide c
    me "……你是想让我一个个猜到下课吗？"
    $ c_expression = "thinking"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "我在等你自己发现，这个猜法太笨了。"
    hide c
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "更聪明一点的叫做二分查找。"
    hide c
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "就是这个函数，你试试。"
    hide c
    play music "audio/bgm/bgm_quiz.ogg" fadeout 1.0 fadein 1.0
    call question_03
    if bad_end_reason:
        jump bad_end
    $ c_expression = "normal"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "好了，回到游戏。我真的想了个数，你来猜。"
    hide c
    me "所以你之前根本没有想数字吗"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "别在意这么多细节，来猜。"
    hide c
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "100以内，只给你7次机会哦。"
    hide c
    $ guess_count = 0
    $ guess_low = 1
    $ guess_high = 100
    while guess_count < 7:
        $ guess = renpy.input("输入 1 到 100 的猜测：", length=3)
        $ guess = int(guess) if guess.isdigit() else 0
        $ guess_count += 1
        if guess == 72:
            $ c_expression = "happy"
            if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
                $ renpy.show("c " + c_expression, at_list=[c_story])
            c "可以啊，我教你的是不是一下就懂了。"
            hide c
            $ guess_count = 7
        elif guess < 72:
            if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
                $ renpy.show("c " + c_expression, at_list=[c_story])
            c "小了。"
            hide c
            $ guess_low = guess + 1
        elif guess > 72:
            if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
                $ renpy.show("c " + c_expression, at_list=[c_story])
            c "大了。"
            hide c
            $ guess_high = guess - 1
        else:
            if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
                $ renpy.show("c " + c_expression, at_list=[c_story])
            c "请输入范围内的整数。"
            hide c
    if guess != 72:
        $ c_expression = "thinking"
        if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
            $ renpy.show("c " + c_expression, at_list=[c_story])
        c "还是没懂二分查找吗，7次是百分百能查出来的，再去消化消化吧，zako"
        hide c
    play music "audio/bgm/bgm_daily.ogg" fadeout 1.0 fadein 1.0
    jump chapter_04

label chapter_04:
    scene bg drainage with dissolve
    $ c_expression = "normal"
    narrator "补习第四天。C 说今天要去爬楼梯。"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "这段台阶，一共十级。我习惯一次迈一级，或者一次迈两级。你猜，从最下面走到顶，一共有多少种走法？"
    hide c
    me "又是算法吗？"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "对。"
    hide c
    me "那……先从简单的想？"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    me "如果只有一级台阶的话，就只有一种走法。"
    hide c
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "对。两级呢？"
    hide c
    me "一步两级，或者一步一级再一步一级。两种。"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "三级呢？"
    hide c
    me "1+1+1、1+2、2+1……三种。"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "很好。现在我们不去数十级，换个角度：你站在第十级，上一步是从哪儿过来的？"
    hide c
    me "第九级，或者第八级。"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "对。所以走到第十级的方法数，等于走到第九级的方法数，加上走到第八级的方法数。"
    hide c
    me "这不就是……斐波那契？"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "对。这种\"大问题拆成同类的小问题\"的斐波那契，就叫递归。"
    hide c
    play music "audio/bgm/bgm_quiz.ogg" fadeout 1.0 fadein 1.0
    call question_04
    play music "audio/bgm/bgm_daily.ogg" fadeout 1.0 fadein 1.0
    if bad_end_reason:
        jump bad_end
    $ c_expression = "happy"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "哎哟，不错哟，这都会。"
    hide c
    me "小菜一碟。"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "不错不错，就以这样的势头继续下去吧。"
    hide c
    jump chapter_05

label chapter_05:
    play music "audio/bgm/bgm_festival.ogg" fadeout 1.0 fadein 1.0
    scene bg terminal with dissolve
    $ c_expression = "normal"
    narrator "补习第五天，也是校园祭当晚。C 还是穿着平时那件外套，只是别了一朵小小的纸花。"
    me "你难得没抱书。"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "今天……还有最后一道题。"
    hide c
    narrator "一个摊位，招牌写着「代币兑换处」，里面摆着一整排奶茶和章鱼烧。"
    stallkeeper "代币有 1 点、5 点、11 点三种面额。奶茶要 15 点，请用最少的代币兑换！"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "还记得第一章便利店吗？我当时说，\"贪心并不总是对的\"。"
    hide c
    me "面额 1、5、11，凑 15……"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "先用贪心想一想，你会怎么拿？"
    hide c
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "贪心给的是 5个，但实际最少是 3个。所以这一题，贪心不行了。"
    hide c
    me "那该怎么办？"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "回想一下上一次爬楼梯。第十级的走法，是第九级和第八级的走法相加。你换个角度想：要凑 15，最后一个代币拿的是 1、5 还是 11？"
    hide c
    me "如果最后拿 11，那前面要凑的是 4+1=5。如果最后拿 5，前面要凑 10+1=11。拿 1 的话，前面要凑 14+1=15。"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "对。所以凑 15 最少的个数，就是 凑4、凑10、凑14 这三个里最小的那个再加 1。"
    hide c
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "而且这些小问题，你只要从小到大算一遍，把答案记在表里，就不用重复算了。这就是动态规划。"
    hide c
    play music "audio/bgm/bgm_quiz.ogg" fadeout 1.0 fadein 1.0
    call question_05
    play music "audio/bgm/bgm_festival.ogg" fadeout 1.0 fadein 1.0
    if bad_end_reason:
        jump bad_end
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "你看，dp[[10] 是 2，因为 10 正好是两枚 5 点；dp[[4] 是 4，四枚 1 点；dp[[14] 是 4，一枚 11 点加三枚 1 点。凑 15 时最后拿的那个代币可以是 1、5 或 11：拿 1 就要先凑出 14，dp[[14]+1 = 5；拿 5 就要先凑出 10，dp[[10]+1 = 3；拿 11 就要先凑出 4，dp[[4]+1 = 5。三种取最小，答案是 3。"
    hide c
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "从小到大，把每个小问题算清楚，记下来，再一步一步推到大问题。这是一种非常\"老实\"的做法，一般也是最可靠的。"
    hide c
    jump good_end

label good_end:
    play music "audio/bgm/bgm_ending.ogg" fadeout 2.0 fadein 2.0
    play sound "audio/sfx/fireworks.ogg"
    scene bg ending with fade
    $ c_expression = "happy"
    narrator "终章｜烟花"
    narrator "烟花升起来的时候，所有摊位的灯都暗了一下。"
    narrator "我们并排坐在湖边的长椅上，谁也没说话。"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "补习，就到这里了。"
    hide c
    me "嗯。"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "你的补考，应该没问题了。"
    hide c
    me "是啊，多亏了你。"
    $ c_expression = "shy"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "所以，社团……"
    hide c
    narrator "C拿出了一份早已准备好的入部申请书"
    me "给我吧。"
    if renpy.has_image("cg invitation"):
        scene black
        show cg invitation with dissolve
    narrator "我把名字签在那张入部申请书上，C 用指尖碰了碰那几个字。"
    if renpy.has_image("cg invitation"):
        scene bg ending with dissolve
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "你字真该好好练练了。"
    hide c
    me "喂，都补习完了，就不能夸夸我吗。"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "这才哪到哪，算法这条路还远着呢。"
    hide c
    me "确实，算法的路还长，一直用C的话还是太麻烦了，得考虑换个方便点的语言了。"
    $ c_expression = "angry"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "你敢！！！"
    hide c
    system_text "return 0;"
    call screen ending_report(True)
    return

label bad_end:
    play music "audio/bgm/bgm_bad_end.ogg" fadeout 2.0 fadein 2.0
    scene bg street with fade
    $ c_expression = "sad"
    narrator "坏结局｜补习结束"
    narrator "那件事之后，我和 C 没有再像以前那样一起学习。"
    narrator "消息从当天回复，变成隔天，再后来只剩社团群里的已读。"
    narrator "我们逐渐渐行渐远。没有谁正式说再见，只是那份入部申请书，再也没有递出去。"
    if not renpy.showing("cg invitation") and not renpy.showing("cg change"):
        $ renpy.show("c " + c_expression, at_list=[c_story])
    c "算法题不会因为你绕开它就消失。"
    hide c
    system_text "error: 'together' undeclared (first use in this function)"
    call screen ending_report(False)
    return
