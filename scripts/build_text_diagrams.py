"""Build original reading illustrations; reuse the handbook's local drawing helpers."""
from html import escape
from pathlib import Path
import unicodedata
import sys

sys.dont_write_bytecode = True
from build_space_diagrams import P, text, rect, line, INK, MUTED, GREEN, BG, PALE, LINE

DEST = Path(__file__).resolve().parents[1] / "assets" / "diagrams"


def begin(h, n, title, subtitle, desc):
    P.clear()
    P.extend([f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{h}" '
              f'viewBox="0 0 1200 {h}" role="img" aria-labelledby="title desc">',
              f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>',
              '<style>text{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC",'
              '"Noto Sans CJK SC",sans-serif}.number{font-family:Menlo,monospace}</style>',
              f'<rect width="1200" height="{h}" fill="{BG}"/>'])
    text(48, 52, f"图 {n} · 原创示意 / 阅读与文字", 17, 700, GREEN)
    text(48, 106, title, 36, 700)
    text(48, 148, subtitle, 21, 400, MUTED)


def finish(filename, h):
    line(48, h-72, 1152, h-72)
    text(48, h-36, "原创教学示意 · 图中尺寸不是通用规格 · 未证明产品、无障碍符合性或学习效果", 17, 400, MUTED)
    P.append('</svg>')
    (DEST / filename).write_text("\n".join(P)+"\n", encoding="utf-8")


def link(x, y, value, size=22):
    text(x, y, value, size, 500, GREEN)
    line(x, y+5, x+len(value)*size, y+5, GREEN, 1.5)


def role(n, y, title, description):
    P.append(f'<circle cx="788" cy="{y-7}" r="16" fill="{GREEN}"/>')
    text(788, y-1, str(n), 18, 700, "white", "middle")
    text(820, y, title, 24, 700)
    text(820, y+39, description, 20, 400, MUTED)


def type_roles():
    h=1260
    begin(h, 10, "先定文字角色，再决定如何强调", "用字号、字重、位置与分组配合；不要求每个角色都有一种新字号。",
          "左侧原创反馈页包含练习定位、主要反馈、修改和查看入口，以及保存状态；右侧解释各自的阅读职责。下方将大标题与较小入口放在同一基线，并说明此做法不适用于所有对象。")
    rect(48, 218, 690, 626)
    text(82, 271, "练习2：解释一个选择", 22, 500, MUTED)
    text(82, 354, "把理由与选择连起来", 32, 700)
    text(82, 424, "你已经写出原因。", 24)
    text(82, 468, "再补一句：这个原因怎样支持你的选择？", 24)
    text(82, 555, "先读原答案，再决定要改哪一句。", 21, 400, MUTED)
    rect(82, 628, 230, 64, GREEN, GREEN, 8)
    text(197, 670, "修改这一句", 23, 650, "white", "middle")
    link(358, 669, "查看原答案", 22)
    line(82, 737, 704, 737)
    text(82, 787, "草稿已保存", 22, 500)
    role(1, 270, "定位", "让人知道读的是哪次练习")
    role(2, 412, "主要阅读", "让完整解释连续、清楚")
    role(3, 642, "行动与入口", "能发现，也能预测后果")
    role(4, 783, "状态", "保持可读，不与结果混淆")
    text(48, 906, "并排文字：检查基线，而非只看外框中心", 26, 700)
    rect(48, 936, 1104, 218, PALE, PALE)
    text(80, 1006, "阅读反馈", 35, 700)
    link(330, 1006, "查看原答", 22)
    line(80, 1006, 548, 1006, GREEN, 1)
    text(590, 1008, "同一文字行的对齐参考", 22, 500, MUTED)
    text(80, 1073, "基线不是所有字形的最底边；头像、图标、多行内容需要另行判断。", 22)
    text(80, 1112, "这里的按钮与链接只是静态示意，没有实现输入或导航。", 20, 400, MUTED)
    finish("04-type-by-role.svg",h)


PARA = "读完这段反馈后，先找出原答案中已经说清的部分，再标出需要补充的原因。修改时可以保留原来的观点，但要说明这个原因怎样支持你的选择。如果暂时无法解释，就回到材料里找依据，不要为了让句子显得完整而增加没有提供的事实。最后再读一遍，确认新的句子仍然表达你的意思。"


def wrap(s, cells):
    rows=[];current="";used=0
    closing="，。！？；：、）】》”’"
    for c in s:
        w=1 if unicodedata.east_asian_width(c) in 'WF' else .55
        if used+w>cells and current and c not in closing:
            rows.append(current);current="";used=0
        current+=c;used+=w
    if current:rows.append(current)
    return rows


def reading_width():
    h=1260
    begin(h,11,"正文可以拥有自己的阅读列宽","同一段中文、同一字号与行高；这里只改变正文列宽，再观察换行。",
          "上方反馈段落使用较宽的正文列，下方原文完整放入较窄列，字号与行高不变。右侧提示检查回行、连续理解与是否仍能找到相关动作，不规定普适汉字数量。")
    text(48, 208, "较宽的正文列", 25, 700)
    rect(48, 234, 1104, 296)
    for i,s in enumerate(wrap(PARA,47)):text(76,292+i*40,s,22)
    text(76,492,"行宽改变，回到下一行的距离也会改变。",20,400,MUTED)
    text(48, 594, "收窄正文列，保留全部内容",25,700)
    rect(48,620,700,420)
    for i,s in enumerate(wrap(PARA,28)):text(76,680+i*40,s,22)
    text(788,674,"检查实际阅读",24,700)
    for y,s in [(730,"能否连续理解？"),(778,"是否找错下一行？"),(826,"会不会频繁回看？"),(874,"相关入口还好找吗？")]:text(788,y,s,22)
    text(788,966,"这些是待验证的问题，",20,400,MUTED)
    text(788,1002,"不是图中已经测得的结果。",20,400,MUTED)
    text(48,1099,"不把英文字符经验换算成固定汉字数。",26,700)
    text(48,1140,"字体、字号、语言、窗口与阅读任务一起决定该怎样调整。",21,400,MUTED)
    finish("04-reading-width.svg",h)


def number(x,y,s,anchor="end"):
    P.append(f'<text class="number" x="{x}" y="{y}" text-anchor="{anchor}" font-size="24" fill="{INK}">{escape(s)}</text>')


def align_content():
    h=1160
    begin(h,12,"文字、数量与编号，使用不同的对齐判断","原创录音任务表 · 时长来自假设的十分之一秒记录，仅为展示格式。",
          "表格含任务编号001、014和102，名称、状态以及录音时长8.0、12.5和9.0秒。编号保留前导零，名称与状态左对齐；同单位同精度的时长采用等宽数字右对齐。打开录音入口始终有文字和下划线。")
    rect(48,218,1104,450)
    text(76,270,"编号",21,700)
    text(212,270,"练习任务",21,700)
    text(640,270,"状态",21,700)
    text(902,270,"时长（秒）",21,700,INK,"end")
    text(978,270,"操作",21,700)
    line(76,296,1124,296)
    rows=[("001","解释一次选择","待反馈","8.0"),
          ("014","补充一个理由","可重试","12.5"),
          ("102","给例子补上结论","已处理","9.0")]
    for i,(code,name,state,duration) in enumerate(rows):
        y=362+i*120
        number(76,y,code,"start")
        text(212,y,name,24)
        text(640,y,state,22)
        number(902,y,duration)
        link(978,y,"打开录音",21)
        if i<2:line(76,y+44,1124,y+44)
    text(48,730,"先确定在比较什么，再统一显示方式",26,700)
    for x,title,first,second in [
        (48,"文字","给长名称留出换行空间","不为等高删掉必要条件"),
        (424,"标识符","保留001这样的编号","不当成可以去零的数量"),
        (800,"可比较的数量","先核单位与记录精度","再检查数位与小数点")]:
        rect(x,766,352,206,PALE,PALE)
        text(x+24,810,title,25,700)
        text(x+24,862,first,21)
        text(x+24,905,second,21)
    text(48,1026,"右对齐不自动统一小数位；视觉表格也不能替代真实表头与数据关系。",21)
    finish("04-alignment-by-content.svg",h)


if __name__=="__main__":
    DEST.mkdir(parents=True,exist_ok=True)
    type_roles()
    reading_width()
    align_content()
