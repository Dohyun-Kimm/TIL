console.log('hello, javascript');


// 함수 실습
// 함수 정의 방법 2가지 

// 함수 선언식 Hoisting: 호출 이후에 선언 되었는데 동작 '역류' 오류 안남

function add(num1, num2) {
    return num1 + num2
}
console.log(add(1,3))

// 함수 표현식
// 표현식 내에서 함수 정의( 우변에 정의) 호이스팅 오류 발생함.
const sub = function(num1,num2){
    return num1 - num2
}

console.log(sub(7,2))
// 표현식에서 함수이름을 명시하는 것도 가능 
// 표현식의 함수 이름은 호출될수 없음
const mySub = function newSub(num1,num2){
    return num1- num2
}
console.log(mySub(3,4)) // -1
console.log(newSub(4,3)) // ReferenceError
// 오류 뜬 시점 부터 밑은 코드가 안 돌아감.

// 매개변수와 인자의 개수 불일치 
// 매개 변수보다 인자가 많이 들어와도 오류가 나지 않는다.
const noArgs = function(){
    return `no Argument needed`
}

// 매개 변수 보다 인자의 개수가 적을 경우
// 빈 공간은 undefined로 출력 된다. 
const threeArgs = function (arg1, arg2,agr3) {
    return [arg1,arg2,arg3]
}
threeArgs(1,2) // [1,2, undefined]

// 전개 구문
// 배열이나 문자열 같은 반복 가능 객체를 요소, 인자로 확장

// 배열 예시
let fruits= [ 'apple','banana', 'pear']
let otherFruits = ['pineapple', 'watermellon', fruits]
console.log(otherFruits) // ['pineapple', 'watermellon','apple','banana', 'pear']
// element들이 배열에 포함됨


// 함수 예시
const restOpr = function ( arg1, arg2, ...restArgs){
    return [arg1, arg2, restArgs]
}
console.log(restArgs(1,2,3,4,5))    // [1,2,[3,4,5]]
console.log(restArgs(1,2))          // [1,2,[]]

// 화살표 함수
/* 
 함수를 간결하게 정의하기.
 규칙
 1. function 생략
 2. 매개변수가 1개일때  () 생략
 3. ㅎ함수가한줄일때 {}, return 생략
 항상 익명
*/

// 예시
const arrow = function(name){
    return `hello, ${name}`
}
console.log(arrow('kim'))
// 화살표 함수로 만들기
// 1. function  생략 , 매개변수와 중괄호 사이에 =>삽입
const arrow1 = (name) =>{
    return `hello, ${name}`
}
console.log(arrow1('kimm'))
// 2. () 생략
const arrow2 = name =>{
    return `hello, ${name}`
}
console.log(arrow2('kimmm'))
// 3. {},return 생략 
const arrow3 = name =>{ `hello, ${name}`}
console.log(arrow3('kkimmm'))
// 명확성과 일관성을 위해 ()는 보통 생략 안함.


// 응용 
// 1. 인자가 없을때
let noArg = () => 'No args'
noArgs = _ => 'No args'
// 2-1 object를 리턴 한다면 명시적으로 리턴을 적어준다.
let returnObject = () => {return { key : 'value'}} 
// 2-2 return을 적지 않으려면 괄호를 붙여야한다.
let returnObject2 = () => ({key:'value'})

// 즉시 실행 함수
// 선언과 동시에 실행되는 함수
// 함수 선언 끝에 () 추가하여선언되자마자실행
// 일회성 함수  초기화부분에 많이 사용
(function(num) { return num**3})(2)
(num => num **3)(2) 