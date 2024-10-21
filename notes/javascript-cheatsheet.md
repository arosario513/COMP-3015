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

#### var

```js
console.log(name);
let var = "John";

// undefined
```

### const (constant variables)

```js
const name = "John";
let name = "Jason";
// Uncaught SyntaxError: redeclaration of const name
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

## Loops

### For Loops

```js
for (var i = 0; i < 5; i++) {
  console.log(i);
}

/*
0
1
2
3
4
*/
```

### While Loops

```js
var i = 0;

while (i < 5) {
  console.log(i);
  i++;
}

/*
0
1
2
3
4
*/
```

## OOP

### Class with Constructor

```js
class User {
  constructor(username, email) {
    this.username = username;
    this.email = email;
  }

  info() {
    console.log(`Username: ${this.username}\nEmail:   ${this.email}`);
  }
}

let user = new User("John", "jdoe@mail.com");
user.info();
/*
Username: John
Email:    jdoe@mail.com
*/
```

### Inheritance

```js
class User {
  constructor(username, email) {
    this.username = username;
    this.email = email;
  }

  info() {
    console.log(`Username: ${this.username}\nEmail:    ${this.email}\n`);
  }
}

class Admin extends User {
  constructor(username, email, id) {
    super(username, email);
    this.id = id;
  }

  info() {
    console.log(
      `Username: ${this.username}\nEmail:    ${this.email}\nID:       ${this.id}\n`,
    );
  }
}

let user = new User("Michael", "mmyers@mail.com");
let admin = new Admin("John", "jdoe@mail.com", "A100");

user.info();
/*
Username: Michael
Email:    mmyers@mail.com
*/
admin.info();
/*
Username: John
Email:    jdoe@mail.com
ID:       A100
*/
```
