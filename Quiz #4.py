#Scalar Check
def Check_Scalar(scalar):
  status = True
  if (type(scalar) != int) and (type(scalar) != float) and (type(scalar) != complex):
    status = False
  return status

#Vector Check
def Check_Vector(vector):
  status = True
  for i in range(len(vector)):
    if Check_Scalar(vector[i]) == False:
      status = False
  return status

#Matrix Check
def Check_Matrix(matrix):
  status = True
  for i in range(len(matrix)):
    if Check_Vector(matrix[i]) == False:
      status = False
  return status

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
      for i in range(len(vector)):
        x += vector[i]**2
      x = x**(1/2)
    return x

def normalize(vector):
  "This function takes the 2Norm. This fuction computes the square of every elemnet and adds them up at the end. We use the 2Norm to calculate the norm if a vector. This fuction returns a vector"
  if Check_Vector(vector) == False:
    print ("Invalid Input")
  else:
    x = twoNorm(vector)
    y = []
    for i in range(len(vector)):
      #This line takes the division of each element by the max magnitude and stores it to the blank list
      y.append(vector[i]/x)
      #This line returns a vector with the division
    return y

def dot(vector01,vector02):
  "This fuction takes in two vectors and first checks if they are lists. Then it checks if they are of the same dimensions. Then if they are of the same dimensions it multiplies the elements in the same positions and adds them at the end. If they are not of the same dimensions it return invalid input."
  if Check_Vector(vector01) == False:
    print("invalid input")
  if Check_Vector(vector02) == False:
    print("invalid input")
  else:
    x = 0
    #If the dimensions are the same go ahead and do the multiplication of each element
    for i in range(len(vector01)):
      #After the multiplication we are adding it to x and giving us the answer at the end as a scalar
      x+=vector01[i]*vector02[i]
    return x

def scalarVecMulti(scalar,vector):
  "This fuction takes in a scalar and multiplies it with a vector. First in takes the lenght of the vector and multiplies the first element of the vector to the scalar and it stores it to the blank list. Then it does this for all elements and returns a vector."
  if Check_Scalar(scalar) == False:
    print("invalid input")
  if Check_Vector(vector) == False:
    print("invalid input")
  else:
    x=[]
    for i in range(len(vector)):
      #This lines takes the elements of the vector and multiplies if by the scalar respectively and stores it into a blank list.
      x.append(scalar * vector[i])
      #This line returns the vector
    return x 

def vecSubtract(vector03,vector04):
  "This fuction takes in two vector of the same dimension and subtracts them. First in checks if the dimension are the same, if they aren't it prints invalid input. If they are the same dimension it takes the first element of the first vector and the first element of the second vector and stores it on a blank matrix. It keeps doing this for all elements in the vector"
  #This line makes sure the dimensions are equal
  if Check_Vector(vector03) == False:
    print("invalid input")
  if Check_Vector(vector04) == False:
    print("invalid input")
  else:
    if len(vector03)==len(vector04):
      x = []
      for i in range(len(vector03)):
      #This line takes in the subtraction and stores them to the blank matrix to retunr a vector
        x.append(vector03[i]-vector04[i])    
      return x
    else:
      return None
      print("Invalid Input")
def GS(A):
  "This fuction is to take the Modified Gram-Schmidt of a Matrix. This takes the QR Factorization of the matrix. We use all of the fuction that we used for previous quizzes. This is to help us take the Norm of the vectors. We use the two norm to normalize the vector. Then we take the dot product of the normalized vector and the second vector. Then scalar vector multiplication of the dot product and the normalized vector and gave the variable a name. Then we subtract the second vector minus the variable that we assigned a name too. We get our factorization "
  # This for loop will check each element of the vector to see if it's a number. 
  if Check_Matrix(A) == False:
    print("invalid input")
  else:
    n = len(A)
    m = len(A[0])
    V = A
    #These are blank matrices with the correct dimensions
    R =[[0]*n for i in range(n)]
    Q =[[0]*m for i in range(n)]
    for i in range(n):
      #This line computes the twoNorm of the first vector in the matrix
      R[i][i] = twoNorm(V[i])
      #This line normalizes the first vector in the matrix
      Q[i] = normalize(V[i])
      for j in range(i+1,n):
        #This line take the dot product of the normalized vector and the second vector
        R[i][j] = dot(Q[i],V[j])
        #This variable is for the purpose of taking the scalar vector multiplication of the dot product and the normalized vector and gave it the name temp
        temp = scalarVecMulti(R[i][j],Q[i]) 
        #This line takes the Subtraction of the second vector in the matrix minus the temp variable that we assigned
        V[j] = vecSubtract(V[j],temp)
    return [Q,R]  
