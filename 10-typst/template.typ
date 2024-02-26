// template
#let conf(body) = {
  
  set document(
    title: "typst learning",
    author: "SLY",
    date: auto,
  )

  set heading(numbering: "1.")

  // 目录
  [
    #set align(center)
    #outline(
      title: par("目录"),
      indent: 1em,
    )
  ]

  body
}


// https://github.com/mem-courses/linear-algebra/blob/main/global.typ
#let prob(bgcolor: luma(248), border: luma(88), text) = block(
  fill: bgcolor,
  width: 100%,
  inset: 0.8em,
  radius: 4pt,
  stroke: border + 0.5pt,
  text
)

#let note(..x) = { prob(bgcolor: rgb(219, 242, 249), border: rgb(51, 166, 184), ..x) }
#let info(..x) = { prob(bgcolor: rgb(210, 247, 253), border: rgb(88, 178, 220), ..x) }
#let warn(..x) = { prob(bgcolor: rgb(254, 234, 207), border: rgb(255, 196, 8), ..x) }
#let prof(..x) = { prob(bgcolor: luma(252), border: luma(135), ..x) }
#let answer(..x) = { prob(bgcolor: rgb(254, 234, 207), border: rgb(255, 196, 8), ..x) }