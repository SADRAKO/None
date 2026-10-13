# Interface layer: story labels and dialogue can change independently.
init offset = 1













define config.save_directory = "address-expired"
define config.has_voice = False
define config.autosave_on_choice = True
define config.autosave_on_quit = True
define config.game_menu_action = ShowMenu("save")
define gui.show_name = True
define gui.about = ""
default preferences.text_cps = 35
default preferences.afm_time = 12
define config.has_sync = False

style default:
    font "fonts/msyh.ttc"
    color "#E7EDF5"
style button:
    background Solid("#1C2A40")
    hover_background Solid("#31435B")
    selected_background Solid("#3E3C35")
    padding (20, 12)
style button_text:
    font "fonts/msyh.ttc"
    color "#BDC9DB"
    hover_color "#FFE3A0"
    selected_color "#FFE3A0"
    insensitive_color "#647187"
    size 26
style window:
    background Solid("#0B1222EF")
    ysize 285
style say_dialogue:
    xpos 230
    ypos 76
    xsize 1460
style namebox:
    xpos 230
    ypos 20
    background None
style quick_button:
    background None
    hover_background Solid("#25334B")
    padding (16, 10)
style quick_button_text:
    size 21
    color "#AAB9CE"
    selected_color "#E8C77E"
style slider_slider:
    xsize 510
style gui_vscrollbar:
    unscrollable "hide"

transform title_reveal:
    alpha 0.0
    yoffset 15
    ease 0.6 alpha 1.0 yoffset 0

screen title_art():
    add Solid("#0D1526")
    add Solid("#142237") xpos 920 ypos 0 xsize 1000 ysize 1080
    for x, y, width in [(900, 210, 820), (1040, 350, 730), (850, 730, 900), (1260, 870, 580)]:
        add Solid("#304054") xpos x ypos y xsize width ysize 2
        add Solid("#E8C77E") xpos x ypos (y-4) xsize 10 ysize 10
    add Solid("#304054") xpos 1260 ypos 210 xsize 2 ysize 660
    add Solid("#304054") xpos 1530 ypos 350 xsize 2 ysize 520

screen main_menu():
    tag menu
    on "show" action Play("music", "audio/bgm/bgm_title.ogg", fadein=1.5, if_changed=True)
    use title_art
    vbox at title_reveal:
        xpos 145 ypos 185 spacing 18
        text "C 语言娘的补习时间" font "fonts/simhei.ttf" size 60 color "#F4E8CF"
        text "五天补习，一场补考，还有她的社团邀请。" size 24 color "#A6B6CA"
        null height 48
        textbutton "开始游戏" action Start() xsize 390
        textbutton "继续游戏" action Continue() xsize 390
        textbutton "读取存档" action ShowMenu("load") xsize 390
        textbutton "设置" action ShowMenu("preferences") xsize 390
        textbutton "操作说明" action ShowMenu("help") xsize 390
        textbutton "退出游戏" action Quit(confirm=True) xsize 390
    text "C 语言娘的补习时间  /  [config.version]" xpos 145 ypos 990 size 20 color "#75859B"

screen navigation():
    vbox:
        xpos 70 ypos 205 spacing 10
        if not main_menu:
            textbutton "继续游戏" action Return() xsize 265
            textbutton "存档" action ShowMenu("save") xsize 265
            textbutton "历史记录" action ShowMenu("history") xsize 265
            textbutton "解题记录" action ShowMenu("learning_records") xsize 265
        textbutton "读取存档" action ShowMenu("load") xsize 265
        textbutton "设置" action ShowMenu("preferences") xsize 265
        textbutton "操作说明" action ShowMenu("help") xsize 265
        if not main_menu:
            textbutton "返回标题" action MainMenu(confirm=True) xsize 265
        textbutton "退出游戏" action Quit(confirm=True) xsize 265

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):
    add Solid("#0D1526F5")
    add Solid("#142237") xsize 370 ysize 1080
    text "C 语言娘的补习时间" xpos 45 ypos 75 size 26 color "#E8C77E"
    text title xpos 430 ypos 80 size 48 color "#F4E8CF"
    add Solid("#304054") xpos 430 ypos 158 xsize 1410 ysize 2
    use navigation
    frame:
        xpos 430 ypos 195 xsize 1410 ysize 760
        background None padding (0, 0)
        if scroll:
            viewport:
                xfill True
                yfill True
                yinitial yinitial
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True
                side_yfill True
                vbox:
                    spacing spacing
                    transclude
        else:
            transclude
    textbutton ("返回标题页" if main_menu else "返回游戏"):
        xpos 70 ypos 960 xsize 265
        action (ShowMenu("main_menu") if main_menu else Return())
    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

screen file_slots(title):
    use game_menu(title):
        vbox:
            spacing 24
            text ("自动存档" if FileCurrentPage() == "auto" else "快速存档" if FileCurrentPage() == "quick" else "第 %s 页" % FileCurrentPage()) size 26 color "#E8C77E"
            grid 3 2:
                spacing 22
                for i in range(1, 7):
                    frame:
                        background Solid("#19273B") padding (10, 10)
                        vbox:
                            spacing 5
                            button:
                                action FileAction(i)
                                alt (("存档位 %d" if CurrentScreenName() == "save" else "读取位 %d") % i)
                                padding (0, 0)
                                has vbox
                                add FileScreenshot(i) xsize 384 ysize 216
                                text FileTime(i, format="%Y-%m-%d  %H:%M", empty="空存档位") size 20 xalign 0.5
                                text FileSaveName(i) size 18 xalign 0.5
                                key "save_delete" action FileDelete(i)
                            textbutton "删除" action FileDelete(i) text_size 18 xalign 1.0 padding (12, 3)
            hbox:
                spacing 10
                textbutton "上一页" action FilePagePrevious()
                textbutton "自动" action FilePage("auto")
                textbutton "快速" action FilePage("quick")
                for n in range(1, 10):
                    textbutton str(n) action FilePage(n)
                textbutton "下一页" action FilePageNext()
            text "点击存档位保存或读取；覆盖、删除和读取会先询问确认。" size 20 color "#8294AE"

screen say(who, what):
    window:
        id "window"
        if who:
            window:
                id "namebox"
                style "namebox"
                text who id "who"
        text what id "what"
    add SideImage() xalign 0.0 yalign 1.0

screen choice(items):
    vbox:
        xalign 0.5 yalign 0.42 spacing 22
        for item in items:
            textbutton item.caption action item.action xsize 1320 text_xalign 0.5 padding (35, 22)

screen quick_menu():
    zorder 100
    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5 yalign 1.0
            textbutton "回退" action Rollback()
            textbutton "历史" action ShowMenu("history")
            textbutton "快进" action Skip()
            textbutton "自动" action Preference("auto-forward", "toggle")
            textbutton "存档" action ShowMenu("save")
            textbutton "读取" action ShowMenu("load")
            textbutton "解题" action ShowMenu("learning_records")
            textbutton "快存" action QuickSave()
            textbutton "快读" action QuickLoad()
            textbutton "设置" action ShowMenu("preferences")

screen preferences():
    tag menu
    use game_menu("设置", scroll="viewport"):
        vbox:
            spacing 32
            hbox:
                spacing 90
                vbox:
                    xsize 590 spacing 16
                    text "显示与阅读" size 32 color "#E8C77E"
                    hbox:
                        spacing 16
                        textbutton "窗口" action Preference("display", "window")
                        textbutton "全屏" action Preference("display", "fullscreen")
                    text "文字速度" size 25
                    bar value Preference("text speed") style "slider_slider"
                    text "自动播放等待时间" size 25
                    bar value Preference("auto-forward time") style "slider_slider"
                    text "快进选项" size 25 color "#E8C77E"
                    textbutton "跳过未读文字" action Preference("skip", "toggle")
                    textbutton "选项后继续快进" action Preference("after choices", "toggle")
                    textbutton "跳过转场" action InvertSelected(Preference("transitions", "toggle"))
                vbox:
                    xsize 590 spacing 16
                    text "声音" size 32 color "#E8C77E"
                    text "音乐音量" size 25
                    bar value Preference("music volume") style "slider_slider"
                    text "音效音量" size 25
                    bar value Preference("sound volume") style "slider_slider"
                    textbutton "全部静音" action Preference("all mute", "toggle")
                    null height 30
                    text "设置会自动保存。" size 21 color "#8294AE"

screen history():
    tag menu
    predict False
    use game_menu("历史记录", scroll="viewport", yinitial=1.0, spacing=16):
        for h in _history_list:
            frame:
                background Solid("#19273B") padding (24, 18) xfill True
                vbox:
                    spacing 10
                    if h.who:
                        text h.who substitute False size 25 color h.who_args.get("color", "#E8C77E")
                    text renpy.filter_text_tags(h.what, allow=gui.history_allow_tags) substitute False size 25 xsize 1270 line_spacing 8
        if not _history_list:
            text "还没有对话记录。" color "#8294AE"

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    add Solid("#050912CC")
    frame:
        xalign 0.5 yalign 0.5 xsize 900
        background Solid("#1B293D") padding (50, 45)
        vbox:
            spacing 36
            text "请确认" size 32 color "#E8C77E"
            text _(message) size 28 xsize 800 textalign 0.5
            hbox:
                xalign 0.5 spacing 40
                textbutton "确定" action yes_action xsize 220 text_xalign 0.5
                textbutton "取消" action no_action xsize 220 text_xalign 0.5
    key "game_menu" action no_action

screen help():
    tag menu
    use game_menu("操作说明", scroll="viewport"):
        vbox:
            spacing 24
            text "阅读与选择" size 32 color "#E8C77E"
            text "左键 / 回车 / 空格：推进对白\n方向键：移动界面焦点\nEsc / 鼠标右键：打开游戏菜单\n滚轮向上 / Page Up：回退对白\nCtrl：按住快进；Tab：切换快进\nH / 鼠标中键：隐藏界面\nAlt + Enter：切换全屏" size 27 line_spacing 16
            text "保存进度" size 32 color "#E8C77E"
            text "底部「存档」保存当前进度，「读取」恢复进度。\n「快存 / 快读」用于临时保存和恢复。\n信任、低效计数、解题记录与提示阶段会随存档保留。" size 27 line_spacing 16
            text "题目界面" size 32 color "#E8C77E"
            text "每题提供 5 种解法，选择后显示正确性、复杂度和参考思路。\n正确解法增加 8 点信任；低效解法扣除 20 点信任。\n错误解法立即进入坏结局，累计 3 次低效解法也进入坏结局。\n提示不扣信任，题目中可使用 Esc 存档。" size 27 line_spacing 16

screen about():
    tag menu
    use game_menu("关于"):
        vbox:
            spacing 25
            text "C 语言娘的补习时间" size 45 color "#E8C77E"
            text "版本 [config.version]\n使用 Ren'Py [renpy.version_only] 制作。" size 26
