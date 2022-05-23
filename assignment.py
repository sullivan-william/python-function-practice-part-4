def max_num(a,b,c):
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)

print("max_num:")
max_num(9,12,4)

def mult_list(*args):
    result = 1
    for i in args:
        result = i * result
    print(result)

print("mult_list:")
mult_list(2,5,3)

def rev_string(str):
    result = str[::-1]
    print(result)

print("rev_string:")
rev_string("raw pals")

def num_within(num, a, z):
    if num >= a and num <= z:
        return True
    else:
        return False

print("num_within:")
print(num_within(12,3,16))
print(num_within(8,2,4))


# Not gonna lie, this one was way beyond me

triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

print("pascal:")
pascal(2)
pascal(5)