function descendingOrder(n) {
  for (let i = 0; i <= 9; i++) {
    console.log(String(n).matchAll(i))
  }
  let newNum = ""
  
}

// console.log(descendingOrder(0) === 0)
// console.log(descendingOrder(1) === 1)
// console.log(descendingOrder(111) === 111)
// console.log(descendingOrder(15) === 51)
// console.log(descendingOrder(1021) === 2110)
console.log(descendingOrder(123456789123456) === 987654321)
