console.log('ws 1-2');
function palindrome(str) {
  // 문자열 뒤집기: 문자열을 배열로 쪼갠 다음 뒤집어서 다시 문자열로 만들기
    return str == str.split('').reverse().join('')
  }
  
  console.log(palindrome('level'));
  console.log(palindrome('hi'));
  
  // 출력
  // palindrome('level') => true
  // palindrome('hi') => false