# PATTERN 1
# n=5
# for i in range(n):
#     for j in range(n):
#         if i+j==2 or j-i==2 or i-j==2 or i+j==6:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# OUTPUT
#   *  
#  * * 
# *   *
#  * *
#   *

# PATTERN 2

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==4 or j==4:
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()
            
# OUTPUT:
# * * * * * 
# *       * 
# *       *
# *       *
# * * * * *

# PATTERN 3

# n=7
# for i in range(n):
#     for j in range(n):
#         if((j==0 or j==4) and i!=0) or ((i==0 or i==3)and (j>0 and j<4)):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()

# OUTPUT:    
#   * * *       
# *       *     
# *       *
# * * * * *
# *       *
# *       *
# *       *


# PATTERN 4


# for i in range(7):
#     for j in range(6):
#         if (j == 0) or (j == 5 and i != 0 and i != 3 and i != 6) or ((i == 0 or i == 3 or i == 6) and (j > 0 and j < 5)):
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()

#  OUTPUT:

#  * * * * *   
#  *         * 
#  *         *
#  * * * * *
#  *         *
#  *         *
#  * * * * *


# PATTERN 5

# for i in range(7):
#     for j in range(5):
#         if (j == 0) or (j == 4 and  (i != 0 and i != 3 )) or ((i == 0 or i == 3) and (j > 0 and j < 4)):
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()

# OUTPUT:-

#  * * * *   
#  *       * 
#  *       *
#  * * * *
#  *       *
#  *       *
#  *       *


# PATTERN 6

# for i in range(8):
#     for j in range(6):
#         if (j == 0) or (j == 3 and  (i != 0 and i != 3 and i != 6 and i != 4 and i != 7)) or ((i == 0 or i == 3) and (j > 0 and j < 3)) or (i-j == 2) :
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()

# OUTPUT:
#  * * *       
#  *     *     
#  *     *
#  * * *
#  *   *
#  *     *
#  *       *
#  *         *