#import "template.typ": *
#show outline.entry: outrageous.show-entry.with(
    // the typst preset retains the normal Typst appearance
    ..outrageous.presets.typst,
    // we only override a few things:
    // level-1 entries are italic, all others keep their font style
    font-style: (auto, auto),
    // no fill for level-1 entries, a thin gray line for all deeper levels
    fill: (none, auto),
    // fill: (none, line(length: 100%, stroke: black + .5pt)),
)

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


== codly


#show: codly-init.with()
#codly(
  languages: (
    // 这里只能写 rust，
    rust: (name: "Rust", icon: icon("assets/brand-python.svg"), color: rgb("#CE412B")),
    python: (name: "Python", icon: icon("assets/brand-rust.svg"), color: rgb("#3572A5")),
  )
)

Python源代码：

```python
def fibonaci(n):
    if n <= 1:
        return n
    else:
        return(fibonaci(n-1) + fibonaci(n-2))
```

Rust源代码：

```rust
pub fn main() {
    println!("Hello, world!");
}
```


== tablem

三线表：

#{
  set align(center)
  three-line-table[
    | *Name* | *Location* | *Height* | *Score* |
    | ------ | ---------- | -------- | ------- |
    | John   | Second St. | 180 cm   |  5      |
    | Wally  | Third Av.  | 160 cm   |  10     |
  ]
}


== drafting


= 其他一些有用的东西

#note[这是一个note]

#warn[这是一个warn]

#info[这是一个info]

#prof[这是一个prof]

#answer[这是一个answer]
