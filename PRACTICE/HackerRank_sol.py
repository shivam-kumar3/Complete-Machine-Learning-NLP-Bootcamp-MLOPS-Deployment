def numCells(grid):
    # Write your code here
    res = 0
    for i in range(len(grid)):
        for k in range (len(grid[0])):
            val = grid[i][k]
            flag = 1
            for ii in range (max(0,i-1),min(len(grid),i+2)):
                for kk in range(max(0,k-1),min(len(grid[0]),k+2)):
                    if (ii,kk)!=(i,k) and val<= grid[ii][kk] :
                         flag=0
                         break 
                if flag == 0:
                     break
            else:
                res+=1
    return res


def missingCharacters(s):
    # Write your code here
    all_char = set('abcdefghijklmnopqrstuvwxyz')
    all_num = set('0123456789')
    
    # convert the input string into lower case
    s_set = set(s.lower())
    
    # find the missing value 
    missing_digit = sorted(all_num - s_set)
    missing_char = sorted(all_char - s_set)
    
    # combine them together
    result = ''.join(missing_digit + missing_char)
       
    return result
string = 'shivam1231'

print(missingCharacters(string))

# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def numCells(grid):
    # Write your code here
    res = 0 
    for i in range(len(grid)):
        for k in range(len(grid[0])):
            val = grid[i][k]
            flag = 1
            for z in range(max(0,i-1), min(len(grid),i+2)):
                for zz in range(max(0,k-1), min(len(grid[0]),k+2)):
                    if (z,zz) != (i,k) and val <= grid[z][zz]:
                        flag = 0
                        break
                if flag == 0:
                    break
            else:
                res += 1
    return res