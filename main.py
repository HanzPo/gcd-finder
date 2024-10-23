from math import floor

print("Enter two nonzero integers to find the GCD of:")

a = int(input("a = "))
b = int(input("b = "))

if (b > a):
  helper = a
  a = b
  b = helper

def gcd(a, b):

#  if (a == 0 and b == 0):
#    return 0
#  elif (a == 0):
#    return abs(b)
#  elif (b == 0):
#    return abs(a)

  rows = []
  rows.append([1, 0, a, 0])
  rows.append([0, 1, b, 0])

  running = True
  count = 2

  while running:
    current_row = []
    current_row.append(floor(rows[count - 2][2] / rows[count - 1][2] ))
    current_row.insert(0, rows[count - 2][2] % rows[count - 1][2])
    if (rows[count - 2][2] % rows[count - 1][2] == 0):
      running = False
      return [rows[count - 1][0], rows[count - 1][1], rows[count - 1][2]]
    
    current_row.insert(0, rows[count - 2][1] - (rows[count - 1][1] * current_row[1]))
    current_row.insert(0, rows[count - 2][0] - (rows[count - 1][0] * current_row[2]))

    rows.append(current_row)
    count += 1

  return []

result = gcd(a, b)

print(f"The GCD of {a} and {b} is {result[2]}")
print("We can verify this using Bezout's Lemma")
print(f"({result[0]}){a} + ({result[1]}){b} = {eval(f"({result[0]} * {a}) + ({result[1]} * {b})")}")