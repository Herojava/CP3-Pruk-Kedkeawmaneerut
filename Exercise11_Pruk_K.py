"""
n = 6
     *              5           (0*2)+1
    ***             4           (1*2)+1
   *****            3           (2*2)+1
  *******           2           (3*2)+1
 *********          1           (4*2)+1
***********         0           (5*2)+1
"""

number = int(input("Number ::"))
for row in range(number):
    number -= 1
    print(" "*number,"*"*(row*2+1))

