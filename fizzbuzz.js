for (var i=1; i < 20 + 1; i++) {
    if (i%3===0) {
        if (i%5===0) {
            console.log("FizzBuzz");
        } else {
            console.log("Fizz");
        }
    } else if (i%5===0) {
        console.log("Buzz");
    } else {
        console.log(i);
    }
}


# CoffeeScript:
for i in [1..20]
  console.log if i % 15 == 0
    'FizzBuzz'
  else if i % 5 == 0
    'Buzz'
  else if i % 3 == 0
    'Fizz'
  else
    i
