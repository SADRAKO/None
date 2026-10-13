screen algorithm_question(question):
    modal True
    zorder 90
    key "game_menu" action ShowMenu("save")
    add Solid("#0D1420F2")
    frame:
        xpos 90 ypos 105 xsize 1740 ysize 865
        background Solid("#172235") padding (35, 25)
        vbox:
            spacing 16
            text question["title"] size 38 color "#FFD76B"
            text question["source"] size 20 color "#9CB6D5" substitute False
            hbox:
                spacing 35
                viewport:
                    xsize 755 ysize 570
                    scrollbars "vertical" mousewheel True draggable True
                    vbox:
                        spacing 20
                        text question["text"] size 27 line_spacing 10 xsize 720 substitute False
                        frame:
                            background Solid("#0A1019") padding (20, 18)
                            text question["sample"] size 25 line_spacing 8 xsize 680 substitute False
                        for hint in question["hints"][:hint_stage]:
                            text ("C：" + hint) size 25 color "#FFD76B" xsize 720 line_spacing 8 substitute False
                vbox:
                    xsize 860 spacing 14
                    text "你会怎样实现？" size 28 color "#F2F4F8"
                    for index, option in enumerate(question["options"]):
                        button:
                            id ("solution_%d" % index)
                            action Return(index)
                            xsize 850 ysize 94
                            text option[0] size 24 xalign 0.0 yalign 0.5 substitute False
            hbox:
                spacing 25
                textbutton ("问C（提示 %d / 3）" % (hint_stage + 1) if hint_stage < 3 else "提示已全部显示"):
                    action Return("hint") sensitive hint_stage < 3 xsize 330
                text "提示不扣信任。错误解法会结束故事；累计 3 次低效解法也会结束故事。" size 21 color "#AAB9CE" yalign 0.5

screen trust_hud():
    zorder 95
    if not main_menu and not renpy.get_screen("ending_report"):
        frame:
            xpos 1295 ypos 18 xsize 535
            background Solid("#0D1526E8") padding (20, 12)
            vbox:
                spacing 5
                hbox:
                    spacing 28
                    text "C的信任  [c_trust] / 100" size 21 color "#E8C77E"
                    text "低效方案 [inefficient_count] / 3" size 21 color "#B9C8DE"
                bar:
                    value c_trust range 100 xsize 490 ysize 9
                    left_bar Solid("#E8C77E") right_bar Solid("#304054") thumb None

init python:
    config.overlay_screens.append("trust_hud")

screen algorithm_feedback(record, question):
    modal True
    zorder 110
    key "game_menu" action ShowMenu("save")
    add Solid("#080F1EF2")
    frame:
        xalign 0.5 yalign 0.5 xsize 1400
        background Solid("#19273B") padding (45, 35)
        vbox:
            spacing 24
            text ({"correct": "正确解法 · 信任 +8", "inferior": "低效解法 · 信任 -20", "wrong": "错误解法 · 连接中断"}[record["kind"]]) size 38 color "#E8C77E"
            text record["caption"] size 27 xsize 1300 substitute False
            text record["explanation"] size 28 xsize 1300 line_spacing 10 substitute False
            text record["cost"] size 26 color "#9CB6D5"
            text ("参考思路：" + question["reference"]) size 26 xsize 1300 substitute False
            text "当前信任 [c_trust] / 100    累计低效方案 [inefficient_count] / 3" size 24
            textbutton ("查看结局" if bad_end_reason else "继续剧情") action Return() xalign 1.0

screen learning_records():
    tag menu
    use game_menu("解题记录", scroll="viewport", spacing=20):
        for record in algorithm_records:
            frame:
                background Solid("#19273B") padding (24, 20)
                vbox:
                    spacing 12
                    text record["title"] size 28 color "#E8C77E"
                    text record["caption"] size 24 xsize 1270 substitute False
                    text ({"correct": "正确", "wrong": "错误", "inferior": "低效"}[record["kind"]] + "｜" + record["cost"]) size 23 color "#9CB6D5"
                    text record["explanation"] size 25 xsize 1270 line_spacing 8 substitute False
        if not algorithm_records:
            text "完成一次选择后，这里会留下解法与分析。" size 26

screen ending_report(good):
    modal True
    zorder 110
    add Solid("#0D1526F5")
    frame:
        xpos 280 ypos 140 xsize 1360 ysize 790
        background Solid("#19273B") padding (40, 32)
        vbox:
            spacing 22
            text ("地址已更新" if good else "未收到回应") size 48 color "#E8C77E"
            text "信任 [c_trust] / 100    低效方案 [inefficient_count] / 3" size 26
            if not good:
                text bad_end_reason size 27 color "#EDB2A0"
            viewport:
                ysize 460 xfill True scrollbars "vertical" mousewheel True draggable True
                vbox:
                    spacing 20
                    for record in algorithm_records:
                        text record["title"] size 28 color "#E8C77E"
                        text record["caption"] size 24 xsize 1230 substitute False
                        text record["explanation"] size 25 xsize 1230 line_spacing 6 substitute False
                        text ("参考：" + ALGORITHM_QUESTIONS[record["question_id"]]["reference"]) size 23 color "#9CB6D5" xsize 1230 substitute False
            hbox:
                spacing 30
                textbutton "读取存档" action ShowMenu("load")
                textbutton "返回标题" action MainMenu(confirm=False)
