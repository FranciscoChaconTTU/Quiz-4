def twoNorm(vector):
  "twoNorm takes a vector as it's argument. It then computes the sum of  the squares of each element of the vector. It then returns the square root of this sum."
  # This variable will keep track of the validity of our input.
  inputStatus = True  
  # This for loop will check each element of the vector to see if it's a number. 
  for i in range(len(vector)):  
    if ((type(vector[i]) != int) and (type(vector[i]) != float) and (type(vector[i]) != complex)):
      inputStatus = False
      print("Invalid Input")
    # If the input is valid the function continues to compute the 2-norm
    if inputStatus == True:
      x = 0
      x = x + (vector[i]**2)
    x = x**(1/2)
    return x
def scalarVecMulti(scalar,vector):
  "This fuction takes in a scalar and multiplies it with a vector. First in takes the lenght of the vector and multiplies the first element of the vector to the scalar and it stores it to the blank list. Then it does this for all elements and returns a vector."
 # This variable will keep track of the validity of our input.
  inputStatus = True  
  # This for loop will check each element of the vector to see if it's a number. 
  for i in range(len(vector)):  
    if ((type(vector[i]) != int) and (type(vector[i]) != float) and (type(vector[i]) != complex)):
      inputStatus = False
      print("Invalid Input")
    # If the input is valid the function continues
    if inputStatus == True:
      x=[]
    #This lines takes the elements of the vector and multiplies if by the scalar respectively and stores it into a blank list.
    x.append(scalar*vector[i])
    #This line returns the vector
  return x 
def dot(vector01,vector02):
  "This fuction takes in two vectors and first checks if they are lists. Then it checks if they are of the same dimensions. Then if they are of the same dimensions it multiplies the elements in the same positions and adds them at the end. If they are not of the same dimensions it return invalid input."
   # This variable will keep track of the validity of our input.
  inputStatus = True  
  # This for loop will check each element of the vector to see if it's a number. 
  for i in range(len(vector01)): 
    if ((type(vector01[i])!=int) and (type(vector01[i])!=float) and (type(vector01[i]) !=complex) and len(vector01)==0 or len(vector02)==0):
      inputStatus = False
      print("Invalid Input")
  # If the input is valid the function continues
  if inputStatus == True and len(vector01)==len(vector02):
    x = 0
    #If the dimensions are the same go ahead and do the multiplication of each element
    for i in range(len(vector01)):
      #After the multiplication we are adding it to x and giving us the answer at the end as a scalar
      x+=vector01[i]*vector02[i]
    return x
  #If the dimensions are different print invalid input and return none
  else:
    print ("invalid input")
    return None
def vecSubtract(vector03,vector04):
  "This fuction takes in two vector of the same dimension and subtracts them. First in checks if the dimension are the same, if they aren't it prints invalid input. If they are the same dimension it takes the first element of the first vector and the first element of the second vector and stores it on a blank matrix. It keeps doing this for all elements in the vector"
  for i in range(len(vector03)):  
    if ((type(vector03[i]) != int) and (type(vector03[i]) != float) and (type(vector03[i]) != complex)):
      inputStatus = False
      print("Invalid Input")
  # If the input is valid the function continues to compute the 2-norm
  if inputStatus == True and len(vector03)==len(vector04):
    x = []
    #This line is taking the elements of vector one and subtracting vector two elements respectively 
    for i in range(len(vector03)):
      #This line takes in the subtraction and stores them to the blank matrix to retunr a vector
        x.append(vector03[i]-vector04[i])    
    return x
    #This line is to print invalid input if the dimensions aren't the same
  else:
    print("invalid input")
    return None
def QR_Fact(matrix):
  r_ii = twoNorm(matrix)
  y=[0]*len(matrix)
  if type(matrix) != list:
    print ("Error")
    return None
  if len(matrix)==0:
    print ("Error")  
    return None
  for i in range(len(matrix)):
    if type(matrix) != list:
      print ("Error")
      return None
    if len(matrix)==0:
      print ("Error")  
      return None
    for j in range(len(matrix[i])):
      if type(matrix[i][j]) !=int:
        print("Error")
        return None
      if type(matrix[i][j]) !=float:
        print("Error")
        return None
      if type(matrix[i][j]) !=complex:
        print("Error")
        return None
      else: 
        q_i=(matrix[i][j]/r_ii)
        y[i] += q_i
        return (y)
    r_ij=matrix[j][i] * matrix [j]
    v_j= matrix[j] - (r_ij*q_i)

matrix = [[1,0,2],[2,1,0]]
print (QR_Fact(matrix))
  
