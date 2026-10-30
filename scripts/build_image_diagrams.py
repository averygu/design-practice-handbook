"""Original image-purpose diagrams; generated geometry, no source images or network."""
from pathlib import Path
from html import escape

DEST=Path(__file__).resolve().parents[1]/'assets'/'diagrams'
INK,MUTED,GREEN='#203c3b','#526a65','#315e54'
BG,LINE,PALE='#f6f7f3','#c8d4cb','#e9f0ea'
P=[]

def text(x,y,s,size=22,weight=400,fill=INK,anchor='start'):
 P.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{escape(s)}</text>')
def rect(x,y,w,h,fill='white',stroke=LINE,r=12):
 P.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}"/>')
def line(x,y,xx,yy,stroke=LINE,width=1):
 P.append(f'<line x1="{x}" y1="{y}" x2="{xx}" y2="{yy}" stroke="{stroke}" stroke-width="{width}"/>')
def begin(h,n,title,subtitle,desc):
 P.clear();P.extend([f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1200" height="{h}" viewBox="0 0 1200 {h}" role="img" aria-labelledby="title desc">',f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>','<style>text{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Noto Sans CJK SC",sans-serif}</style>',f'<rect width="1200" height="{h}" fill="{BG}"/>'])
 text(48,52,f'图 {n:02d} · 原创示意 / 图片与用途',17,700,GREEN)
 text(48,106,title,36,700);text(48,150,subtitle,21,400,MUTED)
def finish(name,h,footer='原创图形与场景 · 不是真实照片、产品截图、学生作业或完整无障碍验收'):
 line(48,h-72,1152,h-72);text(48,h-36,footer,17,400,MUTED);P.append('</svg>');(DEST/name).write_text('\n'.join(P)+'\n')

def purpose():
 h=1010
 begin(h,19,'先问图片在这里承担什么用途','信息、动作与装饰的处理取决于页面上下文，不能只看文件类型。','三列分别说明信息图、图像入口和装饰。信息图表达先观察再改写；入口的名称是查看完整练习图；装饰不承担唯一信息。图中元素均为原创，图像入口不是可操作控件。')
 for x,title in [(48,'传递信息'),(432,'作为入口'),(816,'只作装饰')]:
  text(x,215,title,27,700);rect(x,244,336,466)
 # Information image with an original two-step relation.
 rect(72,276,288,192,fill=PALE)
 rect(86,337,105,61,stroke=GREEN,r=7);text(138,376,'观察',26,700,INK,'middle')
 line(199,367,232,367,GREEN,3);P.append(f'<path d="M 221 357 L 232 367 L 221 377" fill="none" stroke="{GREEN}" stroke-width="3"/>')
 rect(241,337,105,61,stroke=GREEN,r=7);text(293,376,'改写',26,700,INK,'middle')
 text(72,515,'要保留：顺序与关系',23,700)
 text(72,558,'替代内容应传达：',21,400,MUTED)
 text(72,598,'先观察原句，再改写。',22)
 text(72,670,'复杂信息可另配详细说明。',19,400,MUTED)
 # A drawn paper and magnifier as a standalone image entry; accessible name is annotation.
 rect(456,276,288,192,fill=PALE)
 rect(547,303,82,112,fill='white',stroke=GREEN,r=5)
 for y,w in [(327,48),(346,37),(365,44)]:line(563,y,563+w,y,GREEN,3)
 P.append(f'<circle cx="627" cy="397" r="27" fill="white" stroke="{GREEN}" stroke-width="4"/>')
 line(647,417,670,440,GREEN,5)
 text(456,515,'要保留：动作或目的地',23,700)
 text(456,558,'这个入口的名称是：',21,400,MUTED)
 text(456,598,'查看完整练习图',22)
 text(456,670,'有等效文字时避免重复朗读。',19,400,MUTED)
 # Purely decorative motif and independent meaningful text.
 rect(840,276,288,192,fill=PALE)
 for y in (304,327,350):P.append(f'<path d="M 860 {y} Q 908 {y-25} 956 {y} T 1052 {y} T 1108 {y}" fill="none" stroke="#b3c6bb" stroke-width="3"/>')
 text(864,420,'开始练习',29,700)
 text(864,452,'页面文字，不属于装饰图',15,400,MUTED)
 text(840,515,'要保留：正文与动作',23,700)
 text(840,558,'纹样没有额外含义：',21,400,MUTED)
 text(840,598,'可作为装饰处理。',22)
 text(840,670,'仅纹样用空alt，保留正文。',19,400,MUTED)
 rect(48,755,1104,147,fill=PALE)
 text(76,798,'先判断用途，再选择技术。',27,700)
 text(76,840,'有意义的图像需要保留等效信息；纯装饰不应增加无关朗读。',23)
 text(76,877,'本图是说明图，入口名称与替代内容仅为设计示例。',21,400,MUTED)
 finish('07-image-purpose.svg',h)


def text_on_images():
 h=1010
 begin(h,20,'对比要覆盖文字实际出现的位置','三处使用同一原创几何背景；文字承载方式变化，各自有取舍。','同一抽象背景有明暗不同区域。左侧白字直接叠放，局部接近背景；中间白字放在不透明深色底面；右侧把深色文字放在图片之外的白色区域。这不是照片修图或实测合规证据。')
 P.append('<defs><g id="scene">')
 rect(0,0,320,250,fill='#f4e7bd',stroke='none',r=0)
 P.append('<path d="M 0 0 H 72 V 250 H 0 Z" fill="#234d48"/>')
 P.append('<path d="M 0 250 L 150 100 L 260 250 Z" fill="#6b9987"/>')
 P.append('<circle cx="254" cy="66" r="41" fill="#fbf8ec"/>')
 line(151,0,151,250,'#dabf83',3)
 P.append('</g></defs>')
 for x,title in [(48,'直接叠放'),(432,'给文字独立底面'),(816,'文字移到图外')]:
  text(x,213,title,25,700);rect(x,244,336,366)
  P.append(f'<use xlink:href="#scene" transform="translate({x+8} 252)"/>')
  if x==48:text(x+32,340,'练习说明',34,700,'white')
  elif x==432:
   rect(x+24,391,288,82,fill='#234d48',stroke='none',r=7);text(x+48,444,'练习说明',34,700,'white')
  else:text(x+32,565,'练习说明',34,700,INK)
 for x,lines in [(48,['局部背景接近字色，','文字可能失去边界。']),
                 (432,['底面稳定，但遮住部分图像；','需要检查是否挡住必要信息。']),
                 (816,['另占文字空间，','图片内容可以保留。'])]:
  for j,s in enumerate(lines):text(x,658+j*36,s,21)
 rect(48,755,1104,147,fill=PALE)
 text(76,798,'遮罩、位置和文字区域，都要与内容一起检查。',27,700)
 text(76,840,'替换图片、换行或改变尺寸后，重新检查文字背后的实际区域。',23)
 text(76,877,'固定遮罩比例或柔影参数，不保证所有照片与字号都可读。',21,400,MUTED)
 finish('07-text-on-images.svg',h)


def crop_context():
 h=1230
 begin(h,21,'容器整齐，不能以丢失内容为代价','同一原创练习图进入相同大小的框；居中裁切与完整容纳的几何结果不同。','原图左侧有题号03，中间有原句与改写，右侧有老师反馈位置。居中cover将两侧裁掉；contain保留全图并留下上下空白。示例是原创图形，不是真实学生作业，也不是上传组件运行结果。')
 P.append('<defs><g id="worksheet">')
 rect(0,0,800,240,fill='white',stroke=GREEN,r=0)
 rect(0,0,180,240,fill=PALE,stroke='none',r=0)
 rect(620,0,180,240,fill='#f2eadb',stroke='none',r=0)
 text(24,64,'题号 03',28,700);text(24,112,'完整要求',24);text(24,154,'保留原意',24)
 text(220,64,'原句与改写',30,700);text(220,112,'补出具体原因。',26)
 line(220,150,580,150,LINE,3);line(220,184,540,184,LINE,3)
 text(640,64,'老师反馈',28,700);text(640,112,'反馈位置',24);text(640,154,'需保留',24)
 P.append('</g><clipPath id="coverclip"><rect x="48" y="690" width="510" height="300"/></clipPath><clipPath id="containclip"><rect x="642" y="690" width="510" height="300"/></clipPath></defs>')
 text(80,218,'原图：题号、答案、反馈共同组成上下文',26,700)
 P.append('<use xlink:href="#worksheet" transform="translate(80 248) scale(1.3)"/>')
 text(48,636,'居中 cover：填满，也会裁切',25,700)
 text(642,636,'contain：保留全图，接受空白',25,700)
 # Exact common geometry: source 800x240, viewport 510x300.
 # cover: scale 1.25 -> 1000x300, centred offset -245.
 rect(48,690,510,300,fill='#edf0ee',stroke=GREEN,r=0)
 P.append('<g clip-path="url(#coverclip)"><use xlink:href="#worksheet" transform="translate(-197 690) scale(1.25)"/></g>')
 rect(48,690,510,300,fill='none',stroke=GREEN,r=0)
 # contain: scale .6375 -> 510x153, centred y offset 73.5.
 rect(642,690,510,300,fill='#edf0ee',stroke=GREEN,r=0)
 P.append('<g clip-path="url(#containclip)"><use xlink:href="#worksheet" transform="translate(642 763.5) scale(.6375)"/></g>')
 rect(642,690,510,300,fill='none',stroke=GREEN,r=0)
 text(48,1034,'题号与反馈不在可见区域中。',23,700)
 text(642,1034,'信息保留，但仍需检查文字大小。',23,700)
 text(48,1092,'对作业、票据等内容：提供完整查看，不让预览裁切替换原始证据。',24,700)
 finish('07-crop-and-context.svg',h,'原创几何对照 · 尺寸只说明裁切关系 · 不是实际上传组件、学生作业或用户验证')

if __name__=='__main__':
 DEST.mkdir(parents=True,exist_ok=True)
 purpose();text_on_images();crop_context()
 print('Generated 3 original image-purpose diagrams; crop source 800x240, viewport 510x300.')
