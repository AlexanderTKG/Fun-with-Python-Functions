#Functions called max_num
def max_num(a,b,c):
  return max([a,b,c])

print(max_num(1,2,3))
print(max_num(250,125,1))
print(max_num(14,7,2))

#functions called multi_list
def mult_list(lst):
  if len(lst) == 0:
    return 0

  prod = lst[0]

  if len(lst) > 1:
    for i in lst[1:]:
      prod = prod * i

  return prod


print(mult_list([1,2,3]))
print(mult_list([]))
print(mult_list([10]))

#functions called rev_string
def rev_string(my_str):
  return my_str[::-1]

print(rev_string(""))
print(rev_string("Banana"))
print(rev_string("a line"))

# functions called nums_within
def nums_within(x,a,b):
  return x in range(a,b+1)
     
print(nums_within(3,2,4))     
print(nums_within(6,2,6))     
print(nums_within(18,2,9))

#functions called pascal

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

pascal(5)
pascal(9)