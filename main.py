from math import floor

print("Enter two integers to find the GCD of:")

a = int(input("a = "))
b = int(input("b = "))

def gcd(a, b):
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
      return rows[count - 1][2]
    
    current_row.insert(0, rows[count - 2][1] - (rows[count - 1][1] * current_row[1]))
    current_row.insert(0, rows[count - 2][0] - (rows[count - 1][0] * current_row[2]))

    rows.append(current_row)
    count += 1


  return -1

print(gcd(a, b))