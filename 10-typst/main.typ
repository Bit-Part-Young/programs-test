#import "template.typ": *

#show: conf


= 基本语法



== 图片

== box

== grid

== block

== 文献及引用

文献@Pei2023 做了XXX，文献#cite(<Yin2021>, form: "full") 得到了XXX。

#bibliography(
  "refs.bib", 
  title: "参考文献",
  style: "nature",
  // style: "gb-7714-2015-numeric",
)

#line(length: 100%)

- 脚本

#for c in "ABC" [
  #c is a letter.
]

#let n = 2
#while n < 10 {
  n = n*2 - 1
  (n,)
}

// #line(length: 100%)

= packages推荐

== showybox

自定义盒子。

#showybox(
  [Hello world!]
)

#showybox(
  frame: (
    dash: "dashed",
    border-color: red.darken(40%)
  ),
  body-style: (
    align: center
  ),
  sep: (
    dash: "dashed"
  ),

  [This is an important message!],
)

#showybox(
  title: "Stokes' theorem",
  frame: (
    border-color: blue,
    title-color: blue.lighten(30%),
    body-color: blue.lighten(95%),
    footer-color: blue.lighten(80%)
  ),
  [
  Let $Sigma$ be a smooth oriented surface in $RR^3$ with boundary $diff Sigma equiv Gamma$. If a vector field $bold(F)(x,y,z)=(F_x (x,y,z), F_y (x,y,z), F_z (x,y,z))$ is defined and has continuous first order partial derivatives in a region containing $Sigma$, then

  $ integral.double_Sigma (bold(nabla) times bold(F)) dot bold(Sigma) = integral.cont_(diff Sigma) bold(F) dot dif bold(Gamma) $
  ]
)

= 其他一些有用的东西

#note[这是一个note]

#warn[这是一个warn]

#info[这是一个info]

#prof[这是一个prof]

#answer[这是一个answer]
