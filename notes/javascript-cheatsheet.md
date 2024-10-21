# Javascript Cheatsheet

## Variables

### let

```js
let name = "John";
```

### var

```js
var name = "John";
```

### let vs. var

#### let

```js
console.log(name);
let name = "John";

// ReferenceError: Cannot access 'name' before initialization
```

### const (constant variables)

```js
const name = "John";
let name = "Jason";
// Uncaught SyntaxError: redeclaration of const name
```

#### var

```js
console.log(name);
let var = "John";

// undefined
```

## Functions

```js
function sayHello(name) {
  console.log("Hello ", name);
}

sayHello("John");

// Hello John
```

### Lambda Functions

```js
const sayHello = (name) => {
  console.log(name);
};

sayHello("John");
// Hello John
```

## Conditional Statements (if, else, else if)

```js
let num = 1;

if (num == 1) {
  console.log("Number is 1");
} else if (num == 2) {
  console.log("Number is 2");
} else {
  console.log("Error");
}

// Number is 1
```

## Switch Statements

```js
let place = 1;

switch (place) {
  case 1:
    console.log("First place");
    break;
  case 2:
    console.log("Second place");
    break;
  case 3:
    console.log("Third place");
    break;
  default:
    console.log("Participation");
}

// First Place
```
