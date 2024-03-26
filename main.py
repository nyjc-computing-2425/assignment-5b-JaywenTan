# Part 1
def read_csv(filename):
    # Type your code below
  
  """
  Returns Header and Data of CSV file in a list.
  
  Parameters
  ---------
  filename: str
  
  Returns 
  ---------
  a list of headers and a list of data from CSV file
  
  Example:
  >>> read_csv("pre-u-enrolment-by-age.csv")
  
  """
  with open(filename,"r") as f:
    a = f.readline().strip()
    data = []
    for e in f:
      check = (e.strip().split(","))
      check[0] = int(check[0])
      check[3] = int(check[3])
      data.append(check)
    return a,data

# Part 2
def filter_gender(enrolment_by_age, sex):
    # Type your code below
  """
  Returns data of CSV file without header and gender

  Parameters
  ---------
  enrolement_by_age: str
  sex: str

  Returns 
  ---------
  a list containing lists of years, age and enrolement_jc

  Example:
  >>> filter_gender("pre-u-enrolment-by-age.csv","MF")
  [[1984, '17 YRS', 8710],
  [1984, '18 YRS', 3927],
  [...],
  [...],
  ...]
  """
  lst = []
  for x in enrolment_by_age:
    if x[2] == sex:
      x.remove(sex)
      lst.append(x)
  return lst
  pass


# Part 3
def sum_by_year(enrolment):
    # Type your code below
  """
  Returns list containing lists of years nad number of students enrolled in that year

  Parameters
  ---------
  enrolement: str

  Returns 
  ---------
  a list containing lists of year and number of students enrolled in that year

  Example:
  """

  lst = []
  lst2 = []
  check = 0
  for x in enrolment:
    if check == 0:
      check = 1
      lst.append(x[0])
      lst.append(x[2])
    elif x[0] in lst:
      lst[1] += x[2]
    else:
      lst2.append(lst)
      lst = []
      lst.append(x[0])
      lst.append(x[2])
      
  lst2.append(lst)
      
  return lst2
  pass


# Part 4
def write_csv(filename, header, data):
    # Type your code below
  """
  Returns number of lines changed when file code is overwritten

  Parameters
  ---------
  filename: str
  header: str
  data: str

  Returns 
  ---------
  number of lines changed

  Example:
  """
  with open(filename,'w') as f:
    
    f.writelines(str(header))
    count = 1
    for x in data:
      f.writelines(str(x))
      count += 1
    return count


# TESTING
# You can write code below to call the above functions
# and test the output
