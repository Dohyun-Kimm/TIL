const products = [
  { name:'cucumber',type: 'vegetable'},
  { name:'banana',type: 'fruit'},
  { name:'carrot',type: 'vegetable'},
  { name:'apple',type: 'fruit'},

]

const fruitFilter = function(product){
  return product.type === 'fruit'
}

const fruits = products.filter( function(product){
  return product.type === 'fruit'
})

const fruits2 = products.filter( product => product.type === 'fruit')


console.log(fruits);

