
#outline(
   title: "目  录",
)

// 设置中文字体
#set text(font: "Noto Sans CJK SC")
// #set text(font: "Noto Sans Mono CJK SC")



// 目录页独占一页
#pagebreak()

// 添加页码
#set page(numbering: "1")


#set heading(numbering: "1.")



= 一级标题
== 二级标题

普通文本 _下划线_

有序列表
+ item 1
+ item 2
+ item 3


插入图片

#figure(
   image("assets/Figures/badge_sjtu.png"),
   caption: [
    上海交通大学校徽
   ],
) <badge_sjtu>

引用图片 @badge_sjtu



数学公式

行内公式 $Q = rho A v + C$

行间公式

$ 7.32 beta + sum_(i=0)^nabla Q_i / 2 $




引用参考文献@Yu2001

= 参考文献


#bibliography("refs.bib")
