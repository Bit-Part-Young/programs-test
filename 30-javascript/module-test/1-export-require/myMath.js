// myMath.js
function add(x, y) {
  return x + y;
}
function subtract(x, y) {
  return x - y;
}
function multiply(x, y) {
  return x * y;
}
function duplicate(x) {
  return x * 2;
}
// node.js 中的多个导出
module.exports = {
  add,
  subtract,
  multiply,
  duplicate,
};
