// 이곳에 코드를 작성합니다.
const inputs = [
  [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
  [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
  [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
]

function solution(K, N, M, chargers) {
  let loc = 0
  let fuel = K
  let count = 0
  // console.log('\n');
  while (loc <N ){
    // 충전기가 있는지 여부 && fuel > -1
    if (chargers.includes(loc + fuel) === true ){
      loc = loc +fuel
      fuel = K
      count +=1
      
      if (loc + fuel >= N){
        console.log(count);
        break
      }
    }
    else{
      fuel -= 1
      if (fuel=== 0){
        count =0
        console.log(count);
        break
      }
    }
    
  } 
  
}

for (const input of inputs) {
  solution(input[0], input[1], input[2], input[3])
}