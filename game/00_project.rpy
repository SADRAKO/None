define config.name = "C 语言娘的补习时间"
define config.version = "0.3.0"
define config.main_menu = True

define narrator = Character(None, what_font="fonts/msyh.ttc", what_size=28, what_color="#F2F4F8")
define me = Character("我", who_font="fonts/simhei.ttf", what_font="fonts/msyh.ttc", who_color="#B9D6FF")
define c = Character("C", who_font="fonts/simhei.ttf", what_font="fonts/msyh.ttc", who_color="#FFD76B")
define cashier = Character("收银员", who_font="fonts/simhei.ttf", what_font="fonts/msyh.ttc", who_color="#E8C7A0")
define stallkeeper = Character("摊主", who_font="fonts/simhei.ttf", what_font="fonts/msyh.ttc", who_color="#D9B8E8")
define operator = Character("值班员", who_font="fonts/simhei.ttf", what_font="fonts/msyh.ttc", who_color="#C5C8CE")
define colleague = Character("同事", who_font="fonts/simhei.ttf", what_font="fonts/msyh.ttc", who_color="#B8E6CE")
define xi = c
define young_xi = c
define b = Character("B", who_font="fonts/simhei.ttf", what_font="fonts/msyh.ttc", who_color="#D0B4FF")

define system_text = Character("系统", who_font="fonts/simhei.ttf", what_font="fonts/msyh.ttc", who_color="#75E4B5")

image bg street = Transform("images/backgrounds/street.jpg", xysize=(1920, 1080), fit="cover")
image bg relay = Solid("#26323B")
image bg tunnel = Solid("#18242A")
image bg office = Transform("images/backgrounds/office.jpg", xysize=(1920, 1080), fit="cover")
image bg archive = Transform("images/backgrounds/archive.jpg", xysize=(1920, 1080), fit="cover")
image bg memory = Solid("#4B3D42")
image bg terminal = Transform("images/backgrounds/terminal.jpg", xysize=(1920, 1080), fit="cover")
image bg drainage = Transform("images/backgrounds/drainage.jpg", xysize=(1920, 1080), fit="cover")
image bg rooftop = Solid("#273044")
image bg ending = Transform("images/backgrounds/ending.jpg", xysize=(1920, 1080), fit="cover")

# Backgrounds use local user-provided artwork.
default c_trust = 60
default solved_01 = False
default solved_02 = False
default solved_03 = False
default solved_04 = False
default solved_05 = False
default hint_stage = 0

default inefficient_count = 0
default algorithm_records = []
default bad_end_reason = ""
default current_question_id = None
default selected_solution = None
