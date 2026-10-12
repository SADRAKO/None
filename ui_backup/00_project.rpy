define config.name = "地址已失效"
define config.version = "0.1.0"
define config.main_menu = False
define config.check_conflicting_properties = True

define gui.text_font = "fonts/msyh.ttc"
define gui.name_text_font = "fonts/simhei.ttf"
define gui.interface_text_font = "fonts/msyh.ttc"
define gui.text_size = 28
define gui.name_text_size = 30

define narrator = Character(None, what_font="fonts/msyh.ttc", what_size=28, what_color="#F2F4F8")
define me = Character("我", who_font="fonts/simhei.ttf", what_font="fonts/msyh.ttc", who_color="#B9D6FF")
define xi = Character("希", who_font="fonts/simhei.ttf", what_font="fonts/msyh.ttc", who_color="#FFD76B")
define operator = Character("值班员", who_font="fonts/simhei.ttf", what_font="fonts/msyh.ttc", who_color="#C5C8CE")
define colleague = Character("同事", who_font="fonts/simhei.ttf", what_font="fonts/msyh.ttc", who_color="#B8E6CE")
define young_xi = Character("年轻的希", who_font="fonts/simhei.ttf", what_font="fonts/msyh.ttc", who_color="#FFD76B")
define b = Character("B", who_font="fonts/simhei.ttf", what_font="fonts/msyh.ttc", who_color="#D0B4FF")

define system_text = Character("系统", who_font="fonts/simhei.ttf", what_font="fonts/msyh.ttc", who_color="#75E4B5")

image bg street = Solid("#11192B")
image bg relay = Solid("#26323B")
image bg tunnel = Solid("#18242A")
image bg office = Solid("#2A303D")
image bg archive = Solid("#343038")
image bg memory = Solid("#4B3D42")
image bg terminal = Solid("#18352F")
image bg drainage = Solid("#25313A")
image bg rooftop = Solid("#273044")
image bg ending = Solid("#35434B")

# All story data remains in script.rpy. Visual assets can replace these image tags later.
default xi_trust = 0
default solved_01 = False
default solved_02 = False
default solved_03 = False
default hint_stage = 0
