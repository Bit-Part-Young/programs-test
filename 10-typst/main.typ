#import "template.typ": *

- 文献及引用

文献@Pei2023 做了XXX，文献#cite(<Yin2021>, form: "full") 得到了XXX。

#bibliography(
  "refs.bib", 
  style: "nature",
  // style: "gb-7714-2015-numeric",
)

- 脚本

#for c in "ABC" [
  #c is a letter.
]

#let n = 2
#while n < 10 {
  n = n*2 - 1
  (n,)
}


- 其他一些有用的东西

#note[这是一个note]

#warn[这是一个warn]

#info[这是一个info]

#prof[这是一个prof]

#answer[这是一个answer]
