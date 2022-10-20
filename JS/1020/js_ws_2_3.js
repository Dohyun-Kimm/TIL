/* 
      1. 아래 코드를 object destructuring을 활용해 리팩토링 하시오.
      2. Rest operator를 활용해 아래 코드를 리팩토링 하시오.
      3. Spread operator를 활용해 아래 코드를 리팩토링 하시오.
    */

    // 1-1
    const savedFile = {
      name: 'profile',
      extension: 'jpg',
      size: 29930
    }
    const {name, extension,size} = savedFile
    // console.log(name);
    console.log(`The file ${name}.${extension} is size of ${size} bytes.`)
    

    // 1-2
    const data = {
      username: 'myName',
      password: 'myPassword',
      email: 'my@mail.com',
    }

    // const username = data.username
    // const password = data.password
    // const email = data.email
    const {username, password, email} = data
    console.log(data)
    
    // 2
    // function addNumbers(a,b,c,d,e) {
    //   const numbers = [a, b, c, d, e];
    //   return numbers.reduce((sum, number) => { 
    //     return sum + number
    //   }, 0)
    // }
    
    function addNumbers(...numbers){
      const total = numbers.reduce((sum,number) => (sum += number),0)
      console.log(total);
    }
    addNumbers(1,2,3,4,5)

    // 3-1
    const defaultColors = ['red', 'green', 'blue'];
    const favoriteColors = ['navy', 'black', 'gold', 'white']
    // const palette = defaultColors.concat(favoriteColors);
    // console.log(palette);
    const palette2 = [...defaultColors,...favoriteColors]
    console.log(palette2);

    // 3-2
    const info1 = { name: 'Tom', age: 30 }
    const info2 = { isMarried: true, balance: 3000 }
    const fullInfo = Object.assign(info1, info2)
    // console.log(fullInfo);
    const fullInfo2= {...info1,...info2}
    console.log(fullInfo2);