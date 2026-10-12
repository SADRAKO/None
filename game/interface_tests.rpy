testsuite interface:
    setup:
        $ _test.transition_timeout = 0.05
        $ _test.timeout = 5.0
        pause until screen "main_menu"
    teardown:
        $ renpy.unlink_save("99-1")
        $ renpy.unlink_save("99-2")
        exit
    testcase menu_and_progress:
        click "设置"
        assert screen "preferences"
        run Preference("skip", "toggle")
        run Preference("skip", "toggle")
        run Preference("all mute", "toggle")
        run Preference("all mute", "toggle")
        click "操作说明"
        assert screen "help"
        click "返回标题页"
        click "开始游戏"
        advance
        advance
        click "历史"
        assert screen "history"
        assert eval (len(_history_list) > 0)
        click "返回游戏"
        click "存档"
        run FilePage(99)
        click "存档位 1"
        pause 0.3
        assert eval renpy.can_load("99-1")
        click "存档位 1"
        assert screen "confirm"
        click "确定"
        click "读取存档"
        click "读取位 1"
        assert screen "confirm"
        click "取消"
        click "读取位 1"
        click "确定"
        pause until screen "say"
        click "设置"
        click "返回标题"
        assert screen "confirm"
        click "确定"
        pause until screen "main_menu"
        click "继续游戏"
        pause until screen "say"
        run Jump("question_01")
        pause until screen "algorithm_question"
        click "问希（提示 1 / 3）"
        assert eval (hint_stage == 1)
        keysym "K_ESCAPE"
        assert screen "save"
        run FilePage(99)
        click "存档位 2"
        pause 0.3
        assert eval renpy.can_load("99-2")
        click "返回游戏"
        assert screen "algorithm_question"
        click "问希（提示 2 / 3）"
        assert eval (hint_stage == 2)
        keysym "K_ESCAPE"
        click "读取存档"
        click "读取位 2"
        click "确定"
        pause until screen "algorithm_question"
        assert eval (hint_stage == 1)
        keysym "K_ESCAPE"
        click "退出游戏"
        assert screen "confirm"
        click "取消"
        assert screen "save"
