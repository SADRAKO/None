screen algorithm_question(question_title, source, question_text, sample_text, hints, answers, hint_stage):
    modal True
    zorder 100

    add Solid("#0D1420DD")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1500
        ysize 900
        background Solid("#172235")
        padding (42, 32)

        vbox:
            spacing 18

            text question_title size 38 font "fonts/simhei.ttf" color "#FFD76B"
            text source size 19 color "#9CB6D5"
            null height 4

            viewport:
                xfill True
                ysize 460
                mousewheel True
                draggable True
                scrollbars "vertical"

                vbox:
                    spacing 16
                    text question_text size 25 color "#F2F4F8" line_spacing 8
                    frame:
                        background Solid("#0A1019")
                        padding (20, 16)
                        text sample_text size 23 font "fonts/simhei.ttf" color "#CBE1FF" line_spacing 7
                    if hint_stage > 0:
                        text "希的提示" size 26 font "fonts/simhei.ttf" color "#FFD76B"
                        for hint in hints[:hint_stage]:
                            frame:
                                background Solid("#223044")
                                padding (16, 12)
                                text "希：" + hint size 23 color "#E7EDF5" line_spacing 6

            hbox:
                spacing 16
                if hint_stage < 3:
                    textbutton "问希（提示 %d / 3）" % (hint_stage + 1):
                        action Return("hint")
                        xsize 300
                else:
                    textbutton "她已经把话说到最直白了":
                        action NullAction()
                        sensitive False
                        xsize 360
                text "提示不影响信任，也没有次数限制。" size 18 color "#90A0B8" yalign 0.5

            text "你的回答" size 25 font "fonts/simhei.ttf" color "#F2F4F8"
            hbox:
                spacing 14
                for answer in answers:
                    textbutton answer[0]:
                        action Return(answer[1])
                        xsize 450
                        ysize 90
                        text_size 22
                        text_xalign 0.0
                        text_yalign 0.5

style button:
    background Solid("#273A55")
    hover_background Solid("#3D5A7D")
    insensitive_background Solid("#26313E")
    padding (16, 10)

style button_text:
    font "fonts/msyh.ttc"
    size 23
    color "#F2F4F8"
    hover_color "#FFFFFF"
