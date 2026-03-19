
##using slope concept
##TC:O(1) becz we are not using single loop at all

# def iscolinearPoints(x1,x2,x3,y1,y2,y3):
       
#   if((y2-y1)*(x3-x2)==(y3-y2)*(x2-x1)):

#     print("Given values are colinear")
#   else:
#     print("Values are not colinear")


##Approch 2 by calculating area of triangle
def iscolinearPoints(x1,x2,x3,y1,y2,y3):
  area = 0.5*(x1*(y2-y3) + x2*(y3-y1)+x3*(y1-y2))
  if area ==0:
    print("Given points are colinear")
  else:
    print("points are not colinear")
    





x1,x2,x3,y1,y2,y3 = 1,2,3,6,0,9
iscolinearPoints(x1,x2,x3,y1,y2,y3)
