/*
You need to write regex that will validate a password 
to make sure it meets the following criteria:

At least six characters long
contains a lowercase letter
contains an uppercase letter
contains a number
Valid passwords will only be alphanumeric characters.
*/

function validate(password) {
  return /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)\w{6,}$/g.test(password);
}

console.log(validate('djI38D55'), 'djI38D55 - Expected true');
console.log(validate('a2.d412'), 'a2.d412 - Expected false');
console.log(validate('JHD5FJ53'), 'JHD5FJ53 - Expected false');
console.log(validate('!fdjn345'), '!fdjn345 - Expected false');
console.log(validate('jfkdfj3j'), 'jfkdfj3j - Expected false');
console.log(validate('123'), '123 - Expected false');
console.log(validate('abc'), 'abc - Expected false');
console.log(validate('Password123'), 'Password123 - Expected true');
