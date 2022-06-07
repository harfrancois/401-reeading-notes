ES6 Syntax and Feature Overview
https://www.taniarascia.com/es6-syntax-and-feature-overview/
Variable declaration
ES6 introduced the let keyword, which allows for block-scoped variables which cannot be hoisted or redeclared.
var x = 0
let x = 0

const keyword, which cannot be redeclared or reassigned, but is not immutable.
const CONST_IDENTIFIER = 0 // constants are uppercase by convention

Arrow functions
The arrow function expression syntax is a shorter way of creating a function expression. Arrow functions do not have 
their own this, do not have prototypes, cannot be used for constructors, and should not be used as object methods.


let func = (a) => {} // parentheses optional with one parameter
let func = (a, b, c) => {} // parentheses required with multiple parameters

Expressions can be embedded in template literal strings.
let str = `Release Date: ${date}`

Multi-line strings
Using template literal syntax, a JavaScript string can span multiple lines without the need for concatenation.

let str = `This text
            is on
Implicit returns
The return keyword is implied and can be omitted if using arrow functions without a block body.
function func(a, b, c) {
  return a + b + c
}
let func = (a, b, c) => a + b + c // curly brackets must be omitted

Key/property shorthand
ES6 introduces a shorter notation for assigning properties to variables of the same name.

let obj = {
  a,
  b,
}

Method definition shorthand
The function keyword can be omitted when assigning methods on an object.

var obj = {
  a: function (c, d) {},
  b: function (e, f) {},
}

let obj = {
  a(c, d) {},
  b(e, f) {},
}

Destructuring (object matching)
Use curly brackets to assign properties of an object to their own variable.

var obj = {a: 1, b: 2, c: 3}
let {a, b, c} = obj

Array iteration (looping)
A more concise syntax has been introduced for iteration through arrays and other iterable objects.

for (let i of arr) {
  console.log(i)
}

Default parameters
Functions can be initialized with default parameters, which will be used only if an argument is not invoked through the function.

let func = (a, b = 2) => {
  return a + b
}

Spread syntax
Spread syntax can be used to expand an array.

let arr1 = [1, 2, 3]
let arr2 = ['a', 'b', 'c']
let arr3 = [...arr1, ...arr2]

console.log(arr3) // [1, 2, 3, "a", "b", "c"]

Classes/constructor functions
ES6 introducess the class syntax on top of the prototype-based constructor function.

class Func {
  constructor(a, b) {
    this.a = a
    this.b = b
  }

  getSum() {
    return this.a + this.b
  }
}

let x = new Func(3, 4)

Inheritance
The extends keyword creates a subclass.

class Inheritance extends Func {
  constructor(a, b, c) {
    super(a, b)

    this.c = c
  }

  getProduct() {
    return this.a * this.b * this.c
  }
}

let y = new Inheritance(3, 4, 5)
y.getProduct() // 60

Modules - export/import

<script src="export.js"></script>
<script type="module" src="import.js"></script>

Promises/Callbacks
Promises represent the completion of an asynchronous function. They can be used as an alternative to chaining functions.

function makeRequest(method, url, callback) {
  var request = new XMLHttpRequest()

  request.open(method, url)
  request.onload = function () {
    callback(null, request.response)
  }
  request.onerror = function () {
    callback(request.response)
  }
  request.send()
}

makeRequest('GET', 'https://url.json', function (err, data) {
  if (err) {
    throw new Error(err)
  } else {
    console.log(data)
  }
})

function makeRequest(method, url) {
  return new Promise((resolve, reject) => {
    let request = new XMLHttpRequest()

    request.open(method, url)
    request.onload = resolve
    request.onerror = reject
    request.send()
  })
}

makeRequest('GET', 'https://url.json')
  .then((event) => {
    console.log(event.target.response)
  })
  .catch((err) => {
    throw new Error(err)
  })