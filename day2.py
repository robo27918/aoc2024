def read_input(file):
    f= open(file,'r')
    contents = f.readlines()
    f.close()
    print(contents)
    return contents

def lines_to_levels(lines):
    levels = []
    for l in lines:
        l = l.strip("\n").split(' ')
        levels.append([int(digit) for digit in l])
    return levels

def isValid(level):
    if level[0] == level[1]:
        return False
    
    increase = level[0] < level[1] 
    if increase:
        for i in range(len(level)):
            if i > 0:
                if level[i-1] >= level[i]:
                    return False
                if abs(level[i-1]-level[i]) > 3:
                    return False
        return True
    else:# its decreasing but we can use the same logic as above by iterating backwards
        for i in range(len(level)-1,-1,-1):
            if i < len(level)-1:
                if level[i] <= level[i+1]:
                    return False
                if abs(level[i]- level[i+1])>3:
                    return False
        return True
def countValids(levels):
    tot = 0
    for l in levels:
        if isValid(l):
            tot +=1
    return tot
def main():
    #read the file and parse each line into a sequence of numbers
    levels = lines_to_levels(read_input('day2.txt'))

    #go thru each level and determine if at any point the two rules are broken
    print("the number of valid levels", countValids(levels))

    # # Test lists
    # test_list1 = [7, 6, 4, 2, 1]  # Safe
    # test_list2 = [1, 2, 7, 8, 9]  # Unsafe
    # test_list3 = [9, 7, 6, 2, 1]  # Unsafe
    # test_list4 = [1, 3, 2, 4, 5]  # Unsafe
    # test_list5 = [8, 6, 4, 4, 1]  # Unsafe
    # test_list6 = [1, 3, 6, 7, 9]  # Safe
    # print("Is valid:", isValid(test_list1))
    # print("Is valid:", isValid(test_list2))
    # print("Is valid:", isValid(test_list3))
    # print("Is valid:", isValid(test_list4))
    # print("Is valid:", isValid(test_list5))
    # print("Is valid:", isValid(test_list6))

    



if __name__ =="__main__":
    main()