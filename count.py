import timeit

letters = {
  "a" : 0,
  "b" : 0,
  "c" : 0,
  "d" : 0,
  "e" : 0,
  "f" : 0,
  "g" : 0,
  "h" : 0,
  "i" : 0,
  "j" : 0,
  "k" : 0,
  "l" : 0,
  "m" : 0,
  "n" : 0,
  "o" : 0,
  "p" : 0,
  "q" : 0,
  "r" : 0,
  "s" : 0,
  "t" : 0,
  "u" : 0,
  "v" : 0,
  "w" : 0,
  "x" : 0,
  "y" : 0,
  "z" : 0
}

message = input(" What text to analyze? ")

startTime = timeit.default_timer()
for currentChar in message:
  if currentChar.isalpha():
    letters[currentChar.lower()] += 1

endTime = timeit.default_timer()
totalTime = endTime - startTime
print(letters)
print(f"Totale time was {totalTime}")
