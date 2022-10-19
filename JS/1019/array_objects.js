/*
 데이터 타입중 참조 타입!
 array object
객체 안쪽 속성들은 메모리에 할당되어있고, 해당객체는 메모리의 시작 주소를 가리킴.
*/

/*배열*/
/*
 순서 보장. 
 주로 대괄호로 생성 []
 0~ n으로 접근
 길이 : array.length
 */
const numbers = [1, 2, 3, 4, 5]

console.log(numbers[0])      // 1
console.log(numbers[-1])     // undefined
console.log(numbers.length)  // 배열 길이 출력

/*
메서드 기초
reverse, push&pop, unshift& shift, includes, indexof, join
파이썬이랑 비교했을때 크게 다른점이 없다.
unshift = push(0)
shift  = insert(0)
*/

const numbers2 = [1, 2, 3, 4, 5]
// remove
numbers2.reverse()
console.log(numbers2)
// push
numbers2.push(6)
console.log(numbers2)
// pop
numbers2.pop(6)
console.log(numbers2)
// unshift
numbers2.unshift(1)
console.log(numbers2)
// shift
numbers2.shift(-1)
console.log(numbers2)
// includes
numbers2.includes(6)
console.log(numbers2)
// indexof
numbers2.push(3)
console.log(numbers2)
// join
result = numbers2.join('')
console.log(result)

/*
 Array Helper Method
 배열 순회하며 특정 로직 수행.
 매서드 호출시 인자로 callback 함수 받음
 callback 함수: 함수의 내부에서 실행될 목적으로 인자로 넘겨 받는 함수
*/

/*
예시  forEach, map, filter, reduce, find, some, every
 */
const colors = ['red','blue','green','yellow']
// forEach
printFunc = function (color){
    console.log(color)
}
colors.forEach(printFunc)
// colors.forEach((color) => console.log(color))

// map
const nums = [1, 2, 3]
printMap = function (num) {
    return num * 2
}
const printDouble = nums.map(printMap)
// const printDouble = nums.map((num)=> number *2)
console.log(printDouble)

// filter

