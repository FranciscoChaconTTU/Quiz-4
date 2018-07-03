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
  # This variable will keep track of the validity of our input.
  inputStatus = True  
   #This line takes the dimension of the vector
  for i in range(len(vector)):  
    # This for loop will check each element of the vector to see if it's a number. 
    if ((type(vector[i]) != int) and (type(vector[i]) != float) and (type(vector[i]) != complex)):
      inputStatus = False
      print("Invalid Input")
    # If the input is valid the function continues
    if inputStatus == True:
      #This line is used to called the twoNorm that we used before
      x = twoNorm(vector)
      y = []
      for i in range(len(vector)):
        #This line takes the division of each element by the max magnitude and stores it to the blank list
        y.append(vector[i]/x)
      #This line returns a vector with the division
      return y
def dot(vector01,vector02):
  "This fuction takes in two vectors and first checks if they are lists. Then it checks if they are of the same dimensions. Then if they are of the same dimensions it multiplies the elements in the same positions and adds them at the end. If they are not of the same dimensions it return invalid input."
  #This line makes sure the dimensions are equal
  if len(vector01)!=len(vector02):
    return None
    print("Wrong Dimensions1")
  # This variable will keep track of the validity of our input.
  if len(vector01)==len(vector02):
    inputStatus = True  
    # This for loop will check each element of the vector to see if it's a number. 
    for i in range(len(vector01)): 
      if ((type(vector01[i])!=int) and (type(vector01[i])!=float) and (type(vector01[i]) !=complex) and len(vector01)==0 or len(vector02)==0):
        inputStatus = False
        print("Invalid Input")
      # If the input is valid the function continues
      if inputStatus == True: 
        x = 0
        #If the dimensions are the same go ahead and do the multiplication of each element
        for i in range(len(vector01)):
          #After the multiplication we are adding it to x and giving us the answer at the end as a scalar
          x+=vector01[i]*vector02[i]
        return x
def scalarVecMulti(scalar,vector):
  "This fuction takes in a scalar and multiplies it with a vector. First in takes the lenght of the vector and multiplies the first element of the vector to the scalar and it stores it to the blank list. Then it does this for all elements and returns a vector."
  # This variable will keep track of the validity of our input.
  inputStatus = True  
  # This for loop will check each element of the vector to see if it's a number. 
  for i in range(len(vector)):  
    if type(vector[i]) != int and type(vector[i]) != float and type(vector[i])!= complex and type(scalar) != int:
      inputStatus = False
      print("Invalid Input")
      # If the input is valid the function continues
    if inputStatus == True:
      x=[]
      for i in range(len(vector)):
      #This lines takes the elements of the vector and multiplies if by the scalar respectively and stores it into a blank list.
        x.append(scalar * vector[i])
    #This line returns the vector
    return x 
def vecSubtract(vector03,vector04):
  "This fuction takes in two vector of the same dimension and subtracts them. First in checks if the dimension are the same, if they aren't it prints invalid input. If they are the same dimension it takes the first element of the first vector and the first element of the second vector and stores it on a blank matrix. It keeps doing this for all elements in the vector"
  #This line makes sure the dimensions are equal
  if len(vector03)!=len(vector04):
    return None 
    print("Wrong Dimensions2")
  else:
     # This variable will keep track of the validity of our input.
    inputStatus = True 
    # This for loop will check each element of the vector to see if it's a number. 
    for i in range(len(vector03)):
      for j in range(len(vector04)):
        if (type(vector03[i]) != int and type(vector04[j])!= int) and (type(vector03[i]) != float and type(vector04)[j]!= float) and (type(vector03[i]) != complex and type(vector04[j])!=complex):
          inputStatus = False
          print("Invalid Input")
        # If the input is valid the function continues to compute
        if inputStatus == True:
          x = []
          #This line takes in the subtraction and stores them to the blank matrix to retunr a vector
          x.append(vector03[i]-vector04[i])    
      return x
def GS(A):
  "This fuction is to take the Modified Gram-Schmidt of a Matrix. This takes the QR Factorization of the matrix. We use all of the fuction that we used for previous quizzes. This is to help us take the Norm of the vectors. We use the two norm to normalize the vector. Then we take the dot product of the normalized vector and the second vector. Then scalar vector multiplication of the dot product and the normalized vector and gave the variable a name. Then we subtract the second vector minus the variable that we assigned a name too. We get our factorization "
  # This for loop will check each element of the vector to see if it's a number. 
  if type(A) != list and len(A)==0:
    print ("Error1")
    return None
  for i in range(len(A)):
    if type(A[i]) != list and len(A[i])==0:
      print ("Error2")
      return None
    for j in range(len(A[i])):
      if type(A[i][j]) !=int and type(A[i][j]) !=float and type(A[i][j]) !=complex:
        print("Error3")
        return None
  #These are variables that we assign in our fuction
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
  return Q,R    

A = [[1,1,1,1,1,1,1,1,1,1],[.55,.6,.65,.70,.75,.80,.85,.90,.95,1.00],[.3025,.36,.4225,.49,.5625,.64,.7225,.81,.9095,1.00],[.166375,.216,.2274425,.343,.421875,.512,.614125,.729,.857375,1]]
print(GS(A)) 

QR=GS(A)
b=TMatVec(QR[0],y)
c=Backsub(QR[1],b)
