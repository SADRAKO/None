# 发行（打包分享）配置。
#
# 用法：用 Ren'Py SDK 的 launcher 运行
#     renpy.exe <SDK>/launcher distribute <本项目目录>
# 产物在项目目录旁边：C-Lang-Girl-Tutoring-<版本>-dists/
# 只发其中的 -win.zip：解压后双击里面的 exe 即可，对方不需要装 Ren'Py。
#
# 两个坑，都已在下面对付掉：
#
# 1. build.package 的签名是 (name, format, file_lists, description=None, ...)，
#    第三个参数必须是文件列表（windows / linux / mac / renpy / all），不是给用户看的
#    描述文字，写反了会得到一个内容为空的包。
#
# 2. Ren'Py 在 common/00build.rpy 里**预置了** pc / win / linux / mac / market 五个包。
#    只写 build.package("pc", "zip", "windows", ...) 的话，覆盖掉的只是 "pc" 自己的
#    定义，其余四个照旧生成——于是 "pc.zip" 里只有运行时没有 game/，得和别的 zip
#    拼起来才能跑；而 "win.zip" 会把项目根目录下的 tools/、art_source/ 一并打进去。
#    所以这里先把预置包清空，只声明要发的那个。

define build.name = "C-Lang-Girl-Tutoring"

init python:

    build.packages = []
    build.package("win", "zip", "windows renpy all", "Windows，解压即玩")

    # ---- 以下内容属于本机或开发过程，不进分发包 ----

    # game/ 里
    build.classify("game/saves/**", None)       # 本机存档，含个人进度
    build.classify("game/cache/**", None)       # 可自动重建的缓存
    build.classify("game/images/bg/**", None)   # 未被脚本引用的旧素材（中文名，ZIP 不可靠）
    build.classify("game/images/test_bg.jpg", None)
    build.classify("game/**.rpy.txt", None)     # 备份脚本
    build.classify("game/*_tests.rpy", None)    # 开发自测脚本
    build.classify("game/*_tests.rpyc", None)

    # 项目根目录下
    build.classify("tools/**", None)            # 素材处理脚本与中间产物
    build.classify("art_source/**", None)       # 已被 image/去掉背景 取代的旧 JPG
    build.classify("ui_backup/**", None)
    build.classify("renpy/**", None)            # 误跑 renpy.exe 生成的官方模板副本
    build.classify("dist/**", None)
    build.classify("*.txt", None)               # errors.txt / traceback.txt / log.txt
    build.classify("README.md", None)
    build.classify(".gitignore", None)
