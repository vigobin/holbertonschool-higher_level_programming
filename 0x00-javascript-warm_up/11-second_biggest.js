#!/usr/bin/node

if (process.argv.length < 3) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  let args = process.argv.slice(2);
  console.log(args)
  args.sort();
  args.reverse();
  console.log(args[1])
}
