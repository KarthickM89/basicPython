# Dictionary inside the list, it can be in a vice-versa
people = [
  {"name": "abb", "house": "london"},
  {"name": "joo", "house":"paris"},
  {"name": "nick", "house":"seol"},
  {"name": "kit", "house":"delhi"}
]

#def f(person):
#  return person["house"]

#people.sort(key=f)


# This lambda is a function used instead of defining a seperate function 
people.sort(key=lambda person: person["house"])

print(people)