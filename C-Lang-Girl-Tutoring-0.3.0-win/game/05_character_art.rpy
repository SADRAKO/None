# 立绘由 tools/install_sprites.py 从 image/去掉背景/ 装进来（作者已经抠好的原图）。
image c happy = "images/c/happy.png"
image c normal = "images/c/normal.png"
image c thinking = "images/c/thinking.png"
image c angry = "images/c/angry.png"
image c sad = "images/c/sad.png"
# 害羞（shy）的原图已经不在了，暂时沿用「平静」的画面：shy.png 与 normal.png
# 完全相同，表情名保留，剧情脚本无需改动。拿到真正的害羞立绘后换掉这个文件即可。
image c shy = "images/c/shy.png"

transform c_story:
    xalign 0.67
    yalign 1.0
    zoom 0.68

default c_expression = "normal"
