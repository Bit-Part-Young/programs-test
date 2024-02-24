#import "template.typ": 字体, 字号, chineseoutline
#import "@preview/outrageous:0.1.0"
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

#set heading(numbering: "1.")
#set page(numbering: "1")
#show outline.entry.where(
  level: 1
): it => {
  v(12pt, weak: true)
  strong(it)
}

#let table-stroke = 0.5pt



#{
  set align(center)
  set page(numbering: none)

  v(5em)

  par(text(
    font: 字体.黑体,
    size: 字号.一号,
    weight: "bold",
    "XXXX\n课程报告模板",
  ))

  v(8em)

  let info-key(body) = {
    // set align(right)
    rect(
      width: 100%,
      stroke: none,
      text(font: 字体.黑体, size: 字号.三号, weight: "bold", body),
    )
  }

  let info-value(body) = {
    rect(
      width: 100%,
      stroke: (bottom: table-stroke + black),
      text(
        font: 字体.黑体,
        // font: 字体.得意黑,
        size: 字号.三号,
        bottom-edge: "descender",
        body
      ),
    )
  }

  grid(
    columns: (100pt, 150pt),
    column-gutter: -5pt,
    row-gutter: 15pt,
    info-key[课程名称:], info-value[多尺度],
    info-key[姓  名:], info-value[张三],
    info-key[学 号:], info-value[XXXXXXX],
  )

  v(8em)

  text(
    font: 字体.黑体,
    size: 字号.三号,
    weight: "bold",
    "二0　　年　　月　　日",
  )

}

#pagebreak()

// 目录
#{

  set align(center)
  set text(font: 字体.黑体, size: 字号.小四)
  set page(numbering: "I")
  counter(page).update(1)

  outline(
    title: "目录",
    indent: 2em,
    )

  // Table of contents
  // chineseoutline(
  //   title: "目录",
  //   depth: 3,
  //   indent: true,
  // )

}

#pagebreak()


#counter(page).update(1)

= 实验目的


= 实验原理
参考文献引用@ZHU2023119062

= 实验内容
== 实验内容1
== 实验内容2

= 结果与讨论
== 结果
== 讨论

= 结论


#pagebreak()


#{
  // set align(center)

  bibliography(
    "refs.bib",
    title: "参考文献",
    style: "gb-7714-2015-numeric",
    )
}