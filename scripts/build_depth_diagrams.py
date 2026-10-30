"""Create original depth illustrations without source assets or network access."""
import sys
sys.dont_write_bytecode = True
from html import escape
from build_space_diagrams import P, text, rect, line, marker, INK, MUTED, GREEN, BG, PALE, LINE, DEST


def begin(number, title, subtitle, desc):
    P.clear()
    P.extend(['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1200" viewBox="0 0 1200 1200" role="img" aria-labelledby="title desc">',
              f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>',
              '<style>text{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Noto Sans CJK SC",sans-serif}</style>',
              f'<rect width="1200" height="1200" fill="{BG}"/>'])
    text(48,52,f'图 {number:02d} · 原创示意 / 深度与层级',17,700,GREEN)
    text(48,106,title,36,700)
    text(48,148,subtitle,21,400,MUTED)
    # Components are deliberately separated; these are illustration parameters, not platform tokens.
    P.append('<defs>')
    for name, wide_blur, wide_y, wide_alpha, contact_blur, contact_y, contact_alpha in [
        ('temporary',13,12,.17,2,2,.12),('rest',8,6,.12,1.2,2,.22),('lift',18,19,.16,1.2,1,.035)]:
        P.append(f'''<filter id="{name}" x="-30%" y="-40%" width="160%" height="190%" color-interpolation-filters="sRGB">
<feGaussianBlur in="SourceAlpha" stdDeviation="{wide_blur}" result="wideBlur"/>
<feOffset in="wideBlur" dy="{wide_y}" result="wideOffset"/>
<feFlood flood-color="#203c3b" flood-opacity="{wide_alpha}" result="wideColor"/>
<feComposite in="wideColor" in2="wideOffset" operator="in" result="wide"/>
<feGaussianBlur in="SourceAlpha" stdDeviation="{contact_blur}" result="contactBlur"/>
<feOffset in="contactBlur" dy="{contact_y}" result="contactOffset"/>
<feFlood flood-color="#203c3b" flood-opacity="{contact_alpha}" result="contactColor"/>
<feComposite in="contactColor" in2="contactOffset" operator="in" result="contact"/>
<feMerge><feMergeNode in="wide"/><feMergeNode in="contact"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>''')
    P.append('</defs>')


def finish(file):
    line(48,1128,1152,1128)
    text(48,1164,'原创场景与构图 · 静态关系示意，不代表真实操作、无障碍验收或学习结果',17,400,MUTED)
    P.append('</svg>')
    (DEST/file).write_text('\n'.join(P)+'\n')


def shadow_rect(x,y,w,h,style):
    P.append(f'<g filter="url(#{style})">')
    rect(x,y,w,h,'white',LINE,12)
    P.append('</g>')


def focus(x,y,w,h):
    P.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="none" stroke="{GREEN}" stroke-width="3"/>')


def button(x,y,w,label,fill=GREEN):
    rect(x,y,w,54,fill,fill,8)
    text(x+w/2,y+35,label,21,650,'white','middle')


def layers():
    begin(16,'临时层、已选内容与焦点，各说一件事','匿名教师工作台；展开面板的外观不等于菜单或对话框行为已经实现。',
          '左侧练习列表中第二行有已选标记，调整安排按钮下方展开带边界与阴影的面板。面板中移动到明天一项有独立焦点环。右侧分别说明普通内容、临时层和键盘焦点。')
    rect(48,218,708,640)
    text(80,268,'安排下一次练习',29,700)
    text(80,307,'先选择练习，再调整时间。',21,400,MUTED)
    line(80,335,724,335)
    text(100,388,'01   识别段落主张',23)
    text(650,388,'今天',20,400,MUTED)
    line(80,421,724,421)
    rect(80,438,644,100,PALE,PALE,8)
    rect(80,438,5,100,GREEN,GREEN,0)
    text(102,478,'02   补出具体原因',23,650)
    text(102,514,'已选',19,600,GREEN)
    button(532,458,168,'调整安排')
    text(100,596,'03   检查论据关联',23)
    text(650,596,'明天',20,400,MUTED)
    line(80,634,724,634)
    text(100,685,'04   独立完成改写',23)
    text(650,685,'周末',20,400,MUTED)
    # Temporary panel is anchored to the action, and is deliberately not a modal dialog.
    shadow_rect(414,526,286,245,'temporary')
    text(436,565,'调整已选练习',21,700)
    line(434,582,680,582)
    focus(430,598,254,55)
    text(448,633,'移动到明天',22,650)
    text(448,697,'选择其他日期',22)
    text(448,744,'关闭',21,500,GREEN)
    marker(740,385,1)
    marker(710,554,2)
    marker(700,626,3)
    for y,n,heading,rows in [
      (268,1,'普通内容',['列表仍属于同一页面。','已选标记说明操作对象。']),
      (464,2,'临时层',['边界与阴影帮助分离。','位置说明它从哪里出现。']),
      (660,3,'键盘焦点',['当前操作有独立指示。','它不等于“已选练习”。'])]:
        marker(810,y,n);text(840,y+7,heading,25,700)
        for j,row in enumerate(rows):text(790,y+62+j*38,row,21,400,MUTED)
    rect(48,912,1104,148,PALE,PALE)
    text(76,956,'先分清事实，再选择视觉效果',26,700)
    text(76,998,'选择、展开、焦点和完成是不同状态。',23)
    text(76,1035,'一次加深阴影，不能替代它们各自的含义与实际行为。',21,400,MUTED)
    finish('06-layers-by-purpose.svg')


def components():
    begin(17,'把接触处暗边与宽范围柔影分开判断','这是一组项目内的表现选择，不是物理高度公式，也不规定双阴影必须存在。',
          '左右使用相同练习条目。列表中的条目保留局部接触暗边和较近柔影；临时抬起条目让接触暗边减弱而宽范围柔影展开。下方分别解释两个分量，不要求两者同时变淡。')
    for x,title,sub,style in [(48,'列表中的内容','靠近承载面','rest'),(624,'临时抬起的内容','暂时与原位置分离','lift')]:
        text(x,216,title,26,700)
        rect(x,248,528,380,PALE,PALE,12)
        text(x+28,290,sub,20,400,MUTED)
        shadow_rect(x+58,340,412,188,style)
        text(x+82,384,'练习 02',19,500,MUTED)
        text(x+82,429,'补出具体原因',29,700)
        text(x+82,479,'把理由写成可理解的解释。',21)
        text(x+28,591,'静态示意；没有运行拖动操作',19,400,MUTED)
    rect(48,676,528,210)
    rect(624,676,528,210)
    text(76,722,'接触处暗边',25,700)
    text(76,764,'让靠近表面的局部边缘清楚。',22)
    text(76,805,'在本例抬起时减弱，',22)
    text(76,843,'不再强调紧贴承载面的关系。',22)
    text(652,722,'宽范围柔影',25,700)
    text(652,764,'提供较宽范围的分离线索。',22)
    text(652,805,'在本例抬起时保留并展开，',22)
    text(652,843,'不要求跟着接触暗边一起变淡。',22)
    rect(48,932,1104,134,PALE,PALE)
    text(76,976,'变弱的是哪一部分？先回答这个问题。',26,700)
    text(76,1017,'再检查对象状态、承载背景、主题和实际渲染；不以“越深越高级”作判断。',21,400,MUTED)
    finish('06-shadow-components.svg')


def overlap():
    begin(18,'重叠服务关系，窄屏可以回到正常排列','两侧保留相同核心任务；示意尺寸不作默认参数，操作与焦点还需真实验证。',
          '左侧较宽窗口中下一次练习卡跨越深色课程介绍区和下方任务区的边界。右侧较窄窗口中相同课程、任务、时长和开始按钮按上下顺序排列。开始按钮周围的焦点轮廓不被裁切；实际响应和交互未实现。')
    text(48,214,'宽窗口：跨区连接',25,700)
    text(788,214,'窄窗口：顺序展开',25,700)
    rect(48,246,680,614)
    rect(48,246,680,216,GREEN,GREEN,12)
    # square off header lower corners while keeping outer frame corners round
    rect(48,430,680,32,GREEN,GREEN,0)
    text(80,294,'写清一个论证',30,700,'white')
    text(80,336,'从主张、理由到证据。',23,400,'white')
    text(80,382,'下一步：完成一条解释句。',21,400,'white')
    shadow_rect(96,416,584,264,'temporary')
    text(126,460,'下一次练习',21,650,MUTED)
    text(126,503,'补出具体原因',29,700)
    text(126,546,'预计 8 分钟',21,400,MUTED)
    focus(122,573,244,68)
    button(128,580,232,'开始练习')
    text(80,747,'后续任务',24,700)
    text(80,792,'检查论据关联 → 独立改写',22)
    line(48,462,88,462,GREEN,2)
    text(76,901,'卡片跨区，但没有覆盖后续任务。',21,400,MUTED)
    rect(788,246,364,744)
    rect(788,246,364,206,GREEN,GREEN,12)
    rect(788,420,364,32,GREEN,GREEN,0)
    text(816,294,'写清一个论证',29,700,'white')
    text(816,337,'从主张、理由到证据。',21,400,'white')
    text(816,378,'下一步：',21,400,'white')
    text(816,416,'完成一条解释句。',21,400,'white')
    # Normal flow, no overlap retained at narrow width.
    rect(812,480,316,280,'white',LINE,10)
    text(836,523,'下一次练习',20,650,MUTED)
    text(836,567,'补出具体原因',26,700)
    text(836,610,'预计 8 分钟',21,400,MUTED)
    focus(832,641,276,68)
    button(838,648,264,'开始练习')
    text(816,817,'后续任务',24,700)
    text(816,858,'检查论据关联',22)
    text(816,897,'独立改写',22)
    text(816,954,'内容继续向下排列',19,400,MUTED)
    text(48,1016,'验收重叠：长标题、文字放大、容器裁切、焦点和触控区域。',25,700)
    text(48,1058,'需要保留的是任务关系；负外边距与叠放效果可以随窗口改变。',22,400,MUTED)
    finish('06-overlap-and-reflow.svg')


if __name__=='__main__':
    DEST.mkdir(parents=True,exist_ok=True)
    layers();components();overlap()
    print('Created D16–D18 original SVG files.')
