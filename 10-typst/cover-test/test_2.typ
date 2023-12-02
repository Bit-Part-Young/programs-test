#let cover(
  name: "" , 
  studentId: "",
  school: "" , 
  body
) = {
  set align(center)
  // 姓名
  text()[姓   名:]
  underline(offset: 5pt)[#name] 
  linebreak()

  text()[学   号:]
  underline(offset: 5pt)[#studentId]
  linebreak()

  text()[学   院:]
  underline(offset: 5pt)[#school]
  linebreak()


  body
}

#cover(
  name: "张三",
  studentId: "1234567890",
  school: "材料科学与工程学院"
  // body: {
  //   set align(center)
  //   个人简历
  // }
)[]