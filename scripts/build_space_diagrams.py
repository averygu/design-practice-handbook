"""Build three original spatial illustrations; no network or third-party media."""
from html import escape
from pathlib import Path

DEST = Path(__file__).resolve().parents[1] / "assets" / "diagrams"
INK, MUTED, GREEN = "#203c3b", "#526a65", "#315e54"
BG, PALE, LINE = "#f6f7f3", "#e9f0ea", "#c8d4cb"
AMBER = "#956337"
P = []


def text(x, y, value, size=22, weight=400, fill=INK, anchor="start"):
    P.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" '
             f'fill="{fill}" text-anchor="{anchor}">{escape(value)}</text>')


def rect(x, y, w, h, fill="white", stroke=LINE, r=12):
    P.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" '
             f'fill="{fill}" stroke="{stroke}"/>')


def line(x, y, xx, yy, color=LINE, width=1):
    P.append(f'<line x1="{x}" y1="{y}" x2="{xx}" y2="{yy}" stroke="{color}" stroke-width="{width}"/>')


def bracket(x, y, xx, yy, color=GREEN):
    line(x, y, xx, yy, color, 2)
    if x == xx:
        line(x-5, y, x+5, y, color, 2)
        line(xx-5, yy, xx+5, yy, color, 2)
    else:
        line(x, y-5, x, y+5, color, 2)
        line(xx, yy-5, xx, yy+5, color, 2)


def marker(x, y, number):
    P.append(f'<circle cx="{x}" cy="{y}" r="16" fill="{GREEN}"/>')
    text(x, y+6, str(number), 18, 700, "white", "middle")


def begin(height, number, title, subtitle, desc):
    P.clear()
    P.extend([f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{height}" '
              f'viewBox="0 0 1200 {height}" role="img" aria-labelledby="title desc">',
              f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>',
              '<style>text{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC",'
              '"Noto Sans CJK SC",sans-serif}</style>',
              f'<rect width="1200" height="{height}" fill="{BG}"/>'])
    text(48, 52, f"图 {number:02d} · 原创示意 / 布局与密度", 17, 700, GREEN)
    text(48, 106, title, 36, 700)
    text(48, 148, subtitle, 21, 400, MUTED)


def finish(name, height):
    line(48, height-72, 1152, height-72)
    text(48, height-36, "原创场景与构图 · 尺寸只用于说明关系 · 不是已测产品或学习效果证据", 17, 400, MUTED)
    P.append('</svg>')
    (DEST / name).write_text("\n".join(P) + "\n", encoding="utf-8")


def grouping():
    h = 1020
    begin(h, 7, "让距离说明：哪些文字属于同一组", "示例正文、字号、行距与面板宽度一致；注释说明改变的距离。",
          "左右均有观察和改写两个标题及对应说明。左侧标题与说明之间、两组之间距离接近；右侧标题靠近自己的说明，两组拉开。图下说明组内收紧与组间分开可以同时进行。")
    for x, title in [(48, "每处都留相近的距离"), (624, "把空间分给不同关系")]:
        text(x, 206, title, 25, 700)
        rect(x, 236, 528, 488)
    # Same text and line spacing. Only title-to-body and inter-group gaps vary.
    for x, ys in [(78, (292, 368, 404, 480, 556, 592)),
                  (654, (292, 332, 368, 480, 520, 556))]:
        for y, s, bold in zip(ys,
                             ["观察", "读原句，找出没有说清的原因。", "先想一想，再打开下一步。", "改写", "补出具体原因，写成一个完整句。", "保留原意，不增加未经提供的事实。"],
                             [True, False, False, True, False, False]):
            text(x, y, s, 25 if bold else 22, 700 if bold else 400)
    bracket(548, 304, 548, 344, AMBER)
    bracket(548, 416, 548, 456, AMBER)
    bracket(548, 492, 548, 532, AMBER)
    bracket(1124, 304, 1124, 308)
    bracket(1124, 380, 1124, 456)
    bracket(1124, 492, 1124, 496)
    text(78, 677, "标题与相邻说明的归属需要再判断", 19, 400, MUTED)
    text(654, 677, "标题贴近自己的说明，两组有分隔", 19, 400, MUTED)
    rect(48, 772, 1104, 128, PALE, PALE)
    text(72, 814, "看关系，不看空白总量", 25, 700)
    text(72, 854, "组内可以更紧，组间可以更松；还要检查多行内容和真实读者的理解。", 22, 400, MUTED)
    finish("03-grouping-by-relationship.svg", h)


def roles():
    h = 1180
    begin(h, 8, "五类空间，各自承担不同工作", "以教师比较两条练习答案为例；编号是空间角色，不是像素数值。",
          "练习导航位于左侧，主区域包含待比较的两条答案和下方共同问题。五个标注分别指向导航宽度、主内容内边距、区块间距、同组答案间距及答案内部内边距。")
    rect(48, 218, 1104, 586)
    rect(48, 218, 220, 586, PALE, PALE)
    line(268, 218, 268, 804)
    text(72, 266, "练习列表", 24, 700)
    text(72, 326, "1  找出主张", 21)
    rect(64, 350, 188, 53, "white", GREEN, 8)
    text(80, 384, "2  补出原因", 21, 650)
    text(72, 444, "3  检查例证", 21)
    text(72, 504, "4  完成改写", 21)
    bracket(48, 740, 268, 740)
    marker(158, 773, 1)
    text(316, 267, "比较两条答案", 28, 700)
    text(316, 307, "当前练习：补出原因", 20, 400, MUTED)
    bracket(268, 345, 316, 345)
    marker(292, 381, 2)
    rect(316, 350, 376, 230)
    rect(716, 350, 376, 230)
    for x, title, rows in [(316, "回答 A", ["它展示了人物作出", "决定的过程。"]),
                           (716, "回答 B", ["它让读者看到选择", "带来的后果。"])]:
        text(x+28, 399, title, 22, 700)
        text(x+28, 452, rows[0], 24)
        text(x+28, 490, rows[1], 24)
        text(x+28, 550, "查看原题", 19, 500, GREEN)
    bracket(694, 466, 714, 466)
    marker(704, 503, 4)
    bracket(716, 374, 744, 374)
    line(744, 374, 756, 354, GREEN)
    marker(767, 340, 5)
    bracket(1118, 582, 1118, 628)
    marker(1118, 606, 3)
    rect(316, 630, 776, 142, PALE, PALE)
    text(344, 676, "共同问题", 23, 700)
    text(344, 719, "两条回答是否都把原因说具体了？", 23)
    text(48, 866, "分别调整，才知道改变了什么", 26, 700)
    for x, y, n, title, detail in [
        (66, 918, 1, "导航宽度", "需要持续切换时才保留"),
        (436, 918, 2, "主区内边距", "给内容稳定的起始边界"),
        (806, 918, 3, "区块间距", "比较区与讲评区分开"),
        (66, 1012, 4, "同组间距", "两条答案仍属于同一组"),
        (436, 1012, 5, "组件内边距", "让文字与边框保持距离")]:
        marker(x, y, n)
        text(x+28, y+6, title, 23, 700)
        text(x+28, y+42, detail, 19, 400, MUTED)
    finish("03-five-spatial-roles.svg", h)


def reflow():
    h = 1220
    begin(h, 9, "窗口变窄时，重排任务而非缩小整页", "任务内容相同，说明标注不同；宽屏并排参照与作答，窄屏上下排列。",
          "宽窗口中任务区域有限宽，左栏原句和要求，右栏答案与提交。窄窗口保留练习进度，以相同正文大小上下排列原句、要求、答案和提交。标题换行，必要内容没有删除。")
    text(48, 208, "宽窗口：分栏比较", 25, 700)
    rect(48, 234, 704, 624)
    text(80, 282, "练习 2 / 4", 19, 500, MUTED)
    text(80, 329, "把原因写成具体的解释句", 30, 700)
    # Margins remain unused; each column has its own content role.
    rect(80, 366, 312, 412, PALE, PALE)
    text(104, 409, "原句", 23, 700)
    text(104, 455, "我选择这个例子，", 22)
    text(104, 491, "因为它比较好。", 22)
    text(104, 573, "要求", 23, 700)
    text(104, 619, "补出具体原因。", 22)
    text(424, 409, "你的改写", 23, 700)
    rect(424, 435, 296, 198)
    text(446, 480, "它展示了人物作出", 22)
    text(446, 516, "决定的过程。", 22)
    rect(424, 677, 296, 60, GREEN, GREEN, 8)
    text(572, 716, "提交改写", 23, 650, "white", "middle")
    text(80, 824, "剩余空间不必再塞入新模块", 19, 400, MUTED)
    text(804, 208, "窄窗口：上下排列", 24, 700)
    rect(804, 234, 348, 756)
    text(828, 282, "练习 2 / 4", 19, 500, MUTED)
    text(828, 329, "把原因写成", 30, 700)
    text(828, 369, "具体的解释句", 30, 700)
    rect(828, 396, 300, 234, PALE, PALE)
    text(850, 435, "原句", 23, 700)
    text(850, 477, "我选择这个例子，", 22)
    text(850, 513, "因为它比较好。", 22)
    text(850, 565, "要求", 23, 700)
    text(850, 605, "补出具体原因。", 22)
    text(828, 683, "你的改写", 23, 700)
    rect(828, 708, 300, 150)
    text(850, 752, "它展示了人物作出", 22)
    text(850, 788, "决定的过程。", 22)
    rect(828, 898, 300, 60, GREEN, GREEN, 8)
    text(978, 937, "提交改写", 23, 650, "white", "middle")
    rect(48, 892, 704, 98, PALE, PALE)
    text(72, 931, "可以伸缩：正文区域", 22, 700)
    text(72, 966, "需要另查：长标题、文字放大、焦点与输入法", 20, 400, MUTED)
    text(48, 1051, "保留任务，改变排列", 26, 700)
    text(48, 1093, "示意不是响应式实现；真实滚动、输入、保存与触控仍需单独检查。", 21, 400, MUTED)
    finish("03-reflow-by-task.svg", h)


if __name__ == "__main__":
    DEST.mkdir(parents=True, exist_ok=True)
    grouping()
    roles()
    reflow()
