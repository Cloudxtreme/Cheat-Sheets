mood = 'great' if singing # one line conditional

is maps to ===
isnt compiles to !==
== and != compile to === and !==

if happy and knowsIt  # (happy && knowsIt)
  clapsHands()
  chaChaCha()
else
  showIt()

date = if friday then sue else jill

switch time
 when 6.00
  wakeUp()
  jotDownList()
 when 9.00 then startWorking()
 when 13.00 then eat()
 when 23.00
  finishUpWork()
  sleep()
 else doNothing()

## Arrays
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
start   = numbers[0..2]
middle  = numbers[3...-2]
end     = numbers[-2..]
copy    = numbers[..]

## for loops
for i in [0...arr.length]
    # code here

for element in arr
    # code here

for i in [0..n] by 1
    # code here


##
## Functions
##
playing = (console, game = "Mass Effect") ->
  alert "Playing #{game} on my #{console}."

playing 'Xbox 360', 'New Vegas'

# var playing;
# playing = function(console, game) {
#   if (game == null) {
#     game = "Mass Effect";
#   }
#   return alert("Playing " + game + " on my " + console + ".");
# };
# playing('Xbox 360', 'New Vegas');
