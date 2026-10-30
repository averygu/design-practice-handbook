"""Build the handbook's three original hierarchy illustrations, without assets or network."""
from html import escape
from pathlib import Path

DEST = Path(__file__).resolve().parents[1] / "assets" / "diagrams"
INK = "#203c3b"
MUTED = "#526a65"
GREEN = "#315e54"
PALE = "#e9f0ea"
BG = "#f6f7f3"
LINE = "#c8d4cb"
RED = "#943c31"
PARTS = []


def text(x, y, value, size=22, weight=400, fill=INK, anchor="start"):
    PARTS.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" '
                 f'fill="{fill}" text-anchor="{anchor}">{escape(value)}</text>')


def rect(x, y, w, h, fill="white", stroke=LINE, radius=16):
    PARTS.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" '
                 f'fill="{fill}" stroke="{stroke}"/>')


def rule(x, y, x2, y2, color=LINE, width=1):
    PARTS.append(f'<line x1="{x}" y1="{y}" x2="{x2}" y2="{y2}" '
                 f'stroke="{color}" stroke-width="{width}"/>')


def button(x, y, w, label, kind="main", size=21):
    if kind == "main":
        rect(x, y, w, 52, GREEN, GREEN, 9)
        color = "white"
    elif kind == "danger":
        rect(x, y, w, 52, RED, RED, 9)
        color = "white"
    elif kind == "secondary":
        rect(x, y, w, 52, "white", MUTED, 9)
        color = INK
    else:
        color = RED if kind == "danger-text" else INK
    text(x + w / 2, y + 34, label, size, 600, color, "middle")


def begin(height, title, desc, kicker, headline, subtitle):
    PARTS.clear()
    PARTS.extend([
        f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{height}" '
        f'viewBox="0 0 1200 {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>',
        '<style>text{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC",'
        '"Noto Sans CJK SC",sans-serif}</style>',
        f'<rect width="1200" height="{height}" fill="{BG}"/>',
    ])
    text(48, 52, kicker, 17, 700, GREEN)
    text(48, 106, headline, 36, 700)
    text(48, 148, subtitle, 21, 400, MUTED)


def finish(filename, height, footer):
    rule(48, height - 74, 1152, height - 74)
    text(48, height - 38, footer, 17, 400, MUTED)
    PARTS.append('</svg>')
    (DEST / filename).write_text("\n".join(PARTS) + "\n", encoding="utf-8")


def current_task():
    height = 1090
    begin(height, "当前任务与视觉竞争", "相同核心信息与操作的两种原创方案：左侧每项都强调，右侧按准备讲评这一任务安排注意顺序，并增加方法说明与设计要求批注。",
          "图 04 · 原创示意 / 教学工作台", "先确定当前任务，再分配视觉强调", "比较的是完整组合方案；不是证明某个字号、颜色或分组单独有效的实验。")
    for x, label in [(48, "每一项都在争取注意"), (624, "围绕当前任务组织")]:
        text(x, 204, label, 26, 700)
        rect(x, 230, 528, 594)

    rect(72, 254, 480, 66, PALE, GREEN, 9)
    text(94, 297, "课程：议论文写作", 27, 700)
    rect(72, 338, 480, 90, "white", GREEN, 9)
    text(94, 391, "准备明天的讲评", 28, 700)
    rect(72, 446, 480, 78, "white", GREEN, 9)
    text(94, 495, "3条回答需要比较", 27, 700)
    rect(72, 542, 480, 66, "white", GREEN, 9)
    text(94, 585, "更新时间：14:20", 25, 700)
    button(72, 640, 228, "回到列表")
    button(324, 640, 228, "准备讲评")
    button(72, 716, 480, "移除草稿")

    text(652, 282, "课程：议论文写作", 21, 500, MUTED)
    text(652, 355, "准备明天的讲评", 32, 700)
    text(652, 403, "3条回答需要比较", 24, 400)
    text(652, 449, "更新时间：14:20", 20, 400, MUTED)
    rule(652, 488, 1124, 488)
    text(652, 550, "先比较材料，再组织讲评内容", 22, 400, MUTED)
    button(652, 614, 224, "准备讲评")
    button(900, 614, 224, "回到列表", "secondary")
    button(652, 710, 156, "移除草稿", "text")
    text(824, 744, "设计要求：说明实际后果", 18, 400, MUTED)

    rect(48, 858, 1104, 126, PALE, PALE, 12)
    text(72, 901, "先发现：当前任务", 23, 700)
    text(420, 901, "再判断：材料与状态", 23, 700)
    text(798, 901, "仍可找：定位与其他操作", 23, 700)
    text(72, 947, "弱化不是隐藏。这里的示意不定义“移除”的后果；真实功能必须明确说明。", 21, 400, MUTED)
    finish("hierarchy-current-task.svg", height, "原创场景与构图 · 示意不代表功能实现、用户试用或效果验证")


def labels_structure():
    height = 1130
    begin(height, "标签、内容与文档结构", "读进度、查属性和输入内容需要不同的标签强调。下半图分别呈现文档结构与视觉样式，二者不能互相代替。",
          "图 05 · 原创示意 / 标签与结构", "标签的作用，来自读者正在做什么", "数据展示可减少重复；输入目的与内容关系仍需清楚表达。")
    xs = [48, 424, 800]
    for x in xs:
        rect(x, 206, 352, 450)
    text(72, 254, "读进度", 26, 700)
    text(72, 298, "先看带单位的结果", 20, 400, MUTED)
    text(72, 388, "3条回答", 40, 700)
    text(72, 432, "待讲评", 25, 500)
    text(72, 548, "数字、单位和状态", 21, 400)
    text(72, 584, "共同构成完整含义。", 21, 400)

    text(448, 254, "查属性", 26, 700)
    text(448, 298, "标签成为扫描入口", 20, 400, MUTED)
    for y, label, value in [(356, "授课时间", "明天 10:00"), (452, "班级", "写作一班"), (548, "主题", "论证结构")]:
        text(448, y, label, 21, 700)
        text(448, y + 36, value, 23, 400)

    text(824, 254, "输入内容", 26, 700)
    text(824, 298, "明确说明字段用途", 20, 400, MUTED)
    text(824, 363, "讲评标题", 22, 600)
    rect(824, 385, 304, 64, "white", MUTED, 6)
    text(844, 425, "论证结构复盘", 23)
    text(824, 548, "已填内容不能代替", 21)
    text(824, 584, "持续可见的字段标签。", 21)

    text(48, 718, "结构表达“是什么”，样式表达“此刻先看什么”", 28, 700)
    rect(48, 746, 528, 266, PALE, PALE, 12)
    rect(624, 746, 528, 266)
    text(72, 788, "文档结构示意", 20, 700, MUTED)
    text(72, 838, "一级标题：讲评准备", 24, 600)
    text(112, 891, "二级标题：教学目标", 23)
    text(112, 944, "二级标题：答案筛选", 23)
    text(648, 788, "视觉呈现示意", 20, 700, MUTED)
    text(648, 832, "讲评准备", 21, 500, MUTED)
    text(648, 886, "教学目标", 30, 700)
    text(648, 924, "明确这次讲评要帮助学生做到什么。", 19)
    text(648, 976, "答案筛选", 25, 600)
    finish("hierarchy-labels-structure.svg", height, "原创示意 · 不是网页实现；输入关联、标题结构和辅助技术读取仍需实际核验")


def action_consequence():
    height = 1200
    begin(height, "操作主次与操作后果", "上方分别提出任务优先级和操作后果问题；下方展示准备页和实际删除步骤。原创例子设定为删除讲评草稿不可恢复，原始回答保留。",
          "图 06 · 原创示意 / 动作与后果", "当前要推进什么，执行后会改变什么", "主次决定相对强调；后果决定命名、说明、确认和恢复路径。")
    rect(48, 196, 528, 150, PALE, PALE)
    rect(624, 196, 528, 150, "#f5ebe5", "#f5ebe5")
    text(72, 242, "问题一：与当前任务的关系", 26, 700)
    text(72, 286, "现在要继续编辑，还是执行删除？", 22)
    text(648, 242, "问题二：执行的实际后果", 26, 700)
    text(648, 286, "改变哪些内容？能否恢复？", 22)

    text(48, 404, "准备讲评时", 26, 700)
    text(624, 404, "确实要删除时", 26, 700)
    rect(48, 430, 528, 540)
    rect(624, 430, 528, 540)
    text(76, 478, "讲评草稿", 21, 500, MUTED)
    text(76, 533, "论证结构复盘", 30, 700)
    text(76, 585, "继续整理共同问题与反馈顺序。", 22)
    button(76, 637, 472, "继续编辑")
    button(76, 711, 472, "查看原始回答", "secondary")
    rule(76, 810, 548, 810)
    button(76, 840, 222, "永久删除草稿", "danger-text")
    text(76, 924, "入口仍可辨认，名称不隐去后果。", 20, 400, MUTED)

    text(652, 478, "删除讲评草稿", 21, 500, MUTED)
    text(652, 533, "确认永久删除这份草稿", 29, 700)
    text(652, 586, "对象：论证结构复盘", 23)
    text(652, 632, "只删除这份讲评草稿。", 22)
    text(652, 675, "学生原始回答保留。", 22)
    rect(652, 704, 472, 66, "#f7ece7", "#f7ece7", 8)
    text(672, 746, "本例设定：删除后不可恢复。", 22, 600, RED)
    button(652, 808, 472, "永久删除这份草稿", "danger")
    button(652, 884, 472, "返回继续编辑", "secondary")

    text(48, 1021, "若实际可以恢复，应改写说明并提供恢复路径；停用也不等同于删除。", 23, 600)
    text(48, 1066, "文字外观的动作仍须有正确控件语义；危险或选中状态不能只依赖颜色。", 22, 400, MUTED)
    finish("hierarchy-action-consequence.svg", height, "原创条件与构图 · 不是来源弹窗复刻，也不是所有删除场景必须采用的流程")


if __name__ == "__main__":
    current_task()
    labels_structure()
    action_consequence()
