// myMath.mjs
// 默认导出 Default export
export default function add(x,y){
  return x + y
}
// 正常导出 Normal export
export function subtract(x,y){
  return x - y
}
// 多重导出 Multiple exports
function multiply(x,y){
  return x * y
}
function duplicate(x){
  return x * 2
}

export {
  multiply, duplicate
}