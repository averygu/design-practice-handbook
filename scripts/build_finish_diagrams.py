"""Create original finishing and real-state illustrations; no source media."""
import sys
sys.dont_write_bytecode=True
from html import escape
from build_space_diagrams import P,text,rect,line,INK,MUTED,GREEN,BG,PALE,LINE,DEST


def begin(n,title,subtitle,desc):
 P.clear();P.extend(['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1200" viewBox="0 0 1200 1200" role="img" aria-labelledby="title desc">',f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>','<style>text{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Noto Sans CJK SC",sans-serif}</style>',f'<rect width="1200" height="1200" fill="{BG}"/>'])
 text(48,52,f'图 {n:02d} · 原创示意 / 收尾与真实状态',17,700,GREEN)
 text(48,106,title,36,700);text(48,148,subtitle,21,400,MUTED)


def finish(name):
 line(48,1128,1152,1128)
 text(48,1164,'原创场景与文案 · 静态示意，不代表真实产品、用户记录或无障碍验收',17,400,MUTED)
 P.append('</svg>');(DEST/name).write_text('\n'.join(P)+'\n')


def button(x,y,w,label,focused=False):
 if focused:P.append(f'<rect x="{x-6}" y="{y-6}" width="{w+12}" height="66" rx="10" fill="none" stroke="{GREEN}" stroke-width="3"/>')
 rect(x,y,w,54,GREEN,GREEN,7);text(x+w/2,y+35,label,21,650,'white','middle')


def radio(x,y,selected=False):
 P.append(f'<circle cx="{x}" cy="{y}" r="11" fill="white" stroke="{GREEN}" stroke-width="2"/>')
 if selected:P.append(f'<circle cx="{x}" cy="{y}" r="5" fill="{GREEN}"/>')


def borders():
 begin(22,'每条线都应有工作，焦点需要单独保留','相同内容、位置与字号；右侧减少内部框线，保留操作焦点的示意。',
       '左右相同反馈列表含两项待讲评练习，位置字号内容一致。左侧为标题、两行内容和操作区域分别加框；右侧去掉这些内部框线，依靠对齐和间距表达分组。两侧开始讲评按钮均保留焦点环。')
 for x,title,bordered in [(48,'重复框线较多',True),(624,'按关系减少框线',False)]:
  text(x,216,title,26,700);rect(x,246,528,604)
  if bordered:rect(x+24,270,480,96,'white',LINE,7)
  text(x+44,309,'练习讲评',28,700);text(x+44,346,'待反馈 2 项',20,400,MUTED)
  for y,no,name in [(395,'01','补出具体原因'),(555,'02','检查论据关联')]:
   if bordered:rect(x+24,y-20,480,136,'white',LINE,7)
   text(x+44,y+18,f'{no}  {name}',25,650)
   text(x+44,y+58,'状态：未讲评',21,400,MUTED)
  if bordered:rect(x+24,710,480,110,'white',LINE,7)
  button(x+44,740,208,'开始讲评',True)
 text(76,894,'线更多，不代表结构更容易理解。',21,400,MUTED)
 text(652,894,'去掉分组装饰线，不等于删除焦点。',21,400,MUTED)
 rect(48,950,1104,126,PALE,PALE)
 text(76,992,'先检查：装饰、分组、控件边界，还是状态？',26,700)
 text(76,1035,'本图未比较用户效果；长内容、密集数据与强制颜色模式仍需单独验收。',21,400,MUTED)
 finish('08-borders-by-role.svg')


def empty_states():
 begin(23,'同样没有条目，原因与下一步可以不同','匿名教师反馈台的四种情境；状态文案只有在对应事实成立时才能显示。',
       '四个面板分别为首次使用、筛选无结果、读取失败和全部处理完成。它们提供不同说明与动作：创建练习、清除筛选、重新加载和查看反馈记录。首次空白不与失败混淆，处理完成也不宣称学生已经掌握。')
 cases=[
  (48,218,'首次使用','还没有练习','创建练习后，学生的提交','会出现在这里。','创建练习'),
  (624,218,'筛选无结果','没有符合条件的提交','当前筛选：未讲评 · 本周','清除筛选可查看其他提交。','清除筛选'),
  (48,650,'读取失败','暂时无法读取提交','目前不能确认条目数量。','请重新加载后再判断。','重新加载'),
  (624,650,'处理完成','当前提交均已讲评','可查看已有反馈记录。','这不代表学习者已经掌握。','查看反馈记录')]
 for x,y,k,title,a,b,action in cases:
  text(x,y,k,25,700)
  rect(x,y+28,528,342)
  text(x+28,y+83,title,26,700)
  text(x+28,y+133,a,22)
  text(x+28,y+174,b,22)
  button(x+28,y+224,228,action)
  text(x+28,y+321,'示例状态 · 对应数据结果待实现',18,400,MUTED)
 text(48,1080,'加载尚未完成、没有权限，也应分别说明；不要伪装成“没有内容”。',23,650)
 finish('08-empty-states-by-cause.svg')


def semantics():
 begin(24,'改变外观，保留对象真正的含义','当前页面、单项选择与装饰强调不是同一种状态；先分清再润色。',
       '上方导航中反馈记录以文字和下划线标识当前页。中间练习方式用两个有文字标签的单选卡片，第一项带实心圆和已选说明。下方课程介绍有装饰性顶线与三条能力说明，刻意不用完成勾暗示学习进度。')
 rect(48,218,1104,180)
 text(76,261,'页面导航',24,700)
 text(76,321,'课程概览',23);text(268,321,'反馈记录',23,700,GREEN);text(460,321,'资料库',23)
 line(268,338,360,338,GREEN,3)
 text(780,273,'当前页',24,700)
 text(780,316,'说明所在位置，',22,400,MUTED)
 text(780,352,'与键盘焦点分别处理。',22,400,MUTED)
 rect(48,430,1104,322)
 text(76,474,'练习方式 · 选择一项',24,700)
 for x,selected,title,desc in [(76,True,'独立练习','先作答，再查看提示'),(420,False,'提示后练习','先看提示，再尝试作答')]:
  rect(x,510,312,180,PALE if selected else 'white',GREEN if selected else LINE,10)
  radio(x+26,544,selected);text(x+51,551,title,24,650)
  text(x+24,597,desc,20,400,MUTED)
  if selected:text(x+24,655,'已选',19,650,GREEN)
 text(780,526,'单项选择',24,700)
 text(780,568,'卡片需要名称、组关系',21,400,MUTED)
 text(780,606,'与真实可操作的状态。',21,400,MUTED)
 text(780,654,'绘出圆圈，不等于实现控件。',20,400,MUTED)
 rect(48,784,1104,288)
 rect(48,784,1104,5,GREEN,GREEN,0)
 text(76,833,'课程会练习什么',24,700)
 for i,t in enumerate(['理解观点之间的关系','解释理由与证据的联系','修改不够具体的表达']):
  text(76,881+i*44,'—  '+t,23)
 text(780,830,'装饰强调',24,700)
 text(780,872,'顶线帮助组织视觉，',22,400,MUTED)
 text(780,910,'不表示已选或已完成。',22,400,MUTED)
 text(780,958,'能力介绍也不是学习记录。',20,400,MUTED)
 finish('08-semantics-survive-restyling.svg')


if __name__=='__main__':
 DEST.mkdir(parents=True,exist_ok=True)
 borders();empty_states();semantics()
 print('Created D22–D24 original draft SVG files.')
