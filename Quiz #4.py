import math
def QR_Fact(matrix):
  if type(matrix) != list:
    print ("Error")
    return None
  if len(matrix)==0:
    print ("Error")  
    return None
  x=0
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
      x+=vector[i]**2
      Norm=x**(1/2)
      Q_hat=matrix[i]/Norm
    return (Q_hat)
