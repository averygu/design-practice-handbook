"""Generate three original color diagrams and recompute their sRGB example.

Uses only the Python standard library. No third-party media or network.
"""
from html import escape
from pathlib import Path
import colorsys
import json

DEST = Path(__file__).resolve().parents[1] / 'assets' / 'diagrams'
INK, MUTED, ACCENT = '#203c3b', '#526a65', '#315e54'
BG, LINE, PALE = '#f6f7f3', '#c8d4cb', '#e9f0ea'
ERROR, ERROR_BG = '#8f2f39', '#fff1f2'
BLUE, BLUE_BG = '#285f8a', '#edf5fb'
P = []


def text(x, y, value, size=22, weight=400, fill=INK, anchor='start'):
    P.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" '
             f'fill="{fill}" text-anchor="{anchor}">{escape(value)}</text>')


def rect(x, y, w, h, fill='white', stroke=LINE, radius=12):
    P.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" '
             f'fill="{fill}" stroke="{stroke}"/>')


def line(x, y, xx, yy, stroke=LINE, width=1):
    P.append(f'<line x1="{x}" y1="{y}" x2="{xx}" y2="{yy}" stroke="{stroke}" stroke-width="{width}"/>')


def begin(h, number, title, subtitle, desc):
    P.clear()
    P.extend([f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{h}" '
              f'viewBox="0 0 1200 {h}" role="img" aria-labelledby="title desc">',
              f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>',
              '<style>text{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Noto Sans CJK SC",sans-serif}</style>',
              f'<rect width="1200" height="{h}" fill="{BG}"/>'])
    text(48, 52, f'图 {number:02d} · 原创示意 / 颜色与状态', 17, 700, ACCENT)
    text(48, 106, title, 36, 700)
    text(48, 150, subtitle, 21, 400, MUTED)


def finish(name, h, footer='原创场景与构图 · 静态说明图，不是已运行产品或完整无障碍验收'):
    line(48, h-72, 1152, h-72)
    text(48, h-36, footer, 17, 400, MUTED)
    P.append('</svg>')
    (DEST/name).write_text('\n'.join(P)+'\n', encoding='utf-8')


def color_roles():
    h=980
    begin(h,13,'先定用途，再为前景和承载面配对','角色表达使用目的；示例色值与角色数量不构成通用规范。',
          '左侧匿名改写练习包含正文、辅助说明、提交动作和提交失败提示。右侧解释相应前景与承载面的颜色角色。状态有明确文字，颜色只是补充。')
    text(48,211,'代表页面：改写练习',25,700)
    text(666,211,'从内容职责建立角色',25,700)
    rect(48,239,560,579)
    text(78,282,'练习 03',18,700,MUTED)
    text(78,328,'把原因说具体',30,700)
    text(78,372,'补出原因，再提交你的改写。',23)
    rect(78,404,500,118,fill=BG)
    text(100,443,'你的改写',18,700,MUTED)
    text(100,485,'这个例子展示了人物的选择。',23)
    text(78,560,'草稿已保存在这台设备',20,400,MUTED)
    rect(78,590,190,56,fill=ACCENT,stroke=ACCENT,radius=8)
    text(173,627,'重试提交',23,700,'white','middle')
    rect(78,674,500,112,fill=ERROR_BG,stroke=ERROR,radius=8)
    text(100,714,'提交失败',24,700,ERROR)
    text(100,754,'草稿仍保留，请重试。',22,400,ERROR)
    rows=[('正文 / 页面','#203c3b','#ffffff','让任务与答案保持可读。'),
          ('辅助 / 页面','#526a65','#ffffff','减少强调，不取消可读性。'),
          ('操作文字 / 操作填充','#ffffff','#315e54','醒目程度由当前任务决定。'),
          ('错误文字 / 错误承载面','#8f2f39','#fff1f2','先说明事实，再指出下一步。')]
    for i,(title,fg,bg,desc) in enumerate(rows):
        y=259+i*132
        rect(666,y,486,111,fill='white')
        rect(686,y+21,50,50,fill=bg,stroke=fg,radius=6)
        text(711,y+55,'字',22,700,fg,'middle')
        text(756,y+38,title,22,700)
        text(756,y+77,desc,20,400,MUTED)
    text(48,866,'同一角色可随外观换值；复用色值前，逐一检查实际组合和状态。',23,700)
    finish('05-color-by-role.svg',h)


def luminance(rgb):
    def lin(c): return c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4
    return sum(w*lin(c) for w,c in zip((.2126,.7152,.0722),rgb))


def calculations():
    rows=[]
    for hue in (160,280):
        rgb=colorsys.hls_to_rgb(hue/360,.4,.7)
        lum=luminance(rgb)
        rows.append({'hsl':[hue,70,40],'rgb_0_255':[c*255 for c in rgb],
                     'relative_luminance':lum,'contrast_white':1.05/(lum+.05),
                     'contrast_black':(lum+.05)/.05})
    return rows


def hsl_contrast():
    h=1040
    begin(h,14,'HSL明度相同，文字对比仍会不同','计算条件：不透明 sRGB · S = 70% · L = 40% · 前景为纯白或纯黑。',
          '两种色相为160与280的色块，各呈现白字和黑字。对比值分别约为2.85与7.37，以及7.83与2.68。相同HSL明度不保证相同文字对比；数值由指定参数计算，不是显示器测量。')
    for row,x in zip(calculations(),(48,624)):
        hue=row['hsl'][0]
        rgb=row['rgb_0_255']
        fill='rgb('+','.join(f'{c:.8g}' for c in rgb)+')'
        text(x,214,f'H {hue}° / S 70% / L 40%',25,700)
        rect(x,244,528,280,fill=fill,stroke=fill)
        text(x+30,304,'纯白文字',30,700,'#ffffff')
        text(x+30,354,f"对白色 {row['contrast_white']:.2f}:1",27,400,'#ffffff')
        line(x+30,388,x+498,388,'#ffffff',1)
        text(x+30,440,'纯黑文字',30,700,'#000000')
        text(x+30,490,f"对黑色 {row['contrast_black']:.2f}:1",27,400,'#000000')
        rect(x,548,528,152)
        text(x+24,587,f"相对亮度 Y = {row['relative_luminance']:.8f}",23,700)
        text(x+24,627,'白 / 黑：两种分别计算的前景',21,400,MUTED)
        text(x+24,666,'色块中的不足对比刻意保留供比较',21,400,MUTED)
    rect(48,732,1104,182,fill=PALE)
    text(76,776,'比较的是前景与背景，不是一个孤立的颜色。',26,700)
    text(76,820,'显示数值取两位小数；阈值判断使用未取整的计算结果。',22)
    text(76,860,'若改用取整色值、透明度或其他背景，需要重新计算。',22)
    text(76,896,'此例不建立色相的永久明暗排名，也不是色觉障碍模拟。',20,400,MUTED)
    finish('05-hsl-and-contrast.svg',h,'原创参数与独立计算 · 图像仅示意颜色差异，不是显示器测量或完整合规结论')


def status_icon(x,y,kind,color):
    if kind=='saved':
        P.append(f'<circle cx="{x}" cy="{y}" r="18" fill="none" stroke="{color}" stroke-width="3"/>')
        P.append(f'<path d="M {x-9} {y} l 6 7 l 13 -14" fill="none" stroke="{color}" stroke-width="3"/>')
    elif kind=='sent':
        P.append(f'<rect x="{x-18}" y="{y-18}" width="36" height="36" rx="4" fill="none" stroke="{color}" stroke-width="3"/>')
        P.append(f'<path d="M {x-10} {y} h 20 m -8 -8 l 8 8 l -8 8" fill="none" stroke="{color}" stroke-width="3"/>')
    else:
        P.append(f'<path d="M {x} {y-21} L {x+22} {y+18} L {x-22} {y+18} Z" fill="none" stroke="{color}" stroke-width="3"/>')
        line(x,y-9,x,y+4,color,3)
        P.append(f'<circle cx="{x}" cy="{y+11}" r="2" fill="{color}"/>')


def states():
    h=1040
    begin(h,15,'去掉色相，状态仍应说得清','左右状态文字与符号一致；右侧采用统一中性色，不模拟任何一种色觉体验。',
          '三行分别为草稿已保存、已提交、提交失败。每种状态都有不同形状符号、明确名称和说明。在有色和中性色两列中，文字和符号保持相同。')
    text(48,211,'有颜色：辅助定位',25,700)
    text(624,211,'统一中性色：核对信息',25,700)
    rows=[('saved','草稿已保存','保存在这台设备，尚未提交。',ACCENT,PALE),
          ('sent','已提交','系统已确认接收，可查看提交记录。',BLUE,BLUE_BG),
          ('failed','提交失败','草稿仍保留，可重试提交。',ERROR,ERROR_BG)]
    for i,(kind,title,desc,fg,bg) in enumerate(rows):
        y=244+i*183
        for x,f,b in ((48,fg,bg),(624,'#303030','#efefef')):
            rect(x,y,528,151,fill=b,stroke=f)
            status_icon(x+42,y+48,kind,f)
            text(x+80,y+58,title,29,700,f)
            text(x+24,y+111,desc,23,400,f)
    rect(48,823,1104,111)
    text(74,863,'文案必须跟真实结果一致。',25,700)
    text(74,904,'“已保存”“已提交”“仍保留”都需要对应证据；颜色不能替代事实。',22)
    finish('05-state-without-hue.svg',h)


if __name__=='__main__':
    DEST.mkdir(parents=True,exist_ok=True)
    color_roles()
    hsl_contrast()
    states()
    print(json.dumps(calculations(),ensure_ascii=False,indent=2))
