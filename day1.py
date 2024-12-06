import math
def read_input(file):
    f= open(file,'r')
    contents = f.readlines()
    f.close()
    print(contents)
    return contents



def lines_to_int(lines):
    nums1 = []
    nums2 = []
    for l in lines:
        l = l.strip("\n").split(' ')
        while '' in l:
            l.remove('')
        #since there is only two elements lets just convert
        l[0] = int(l[0])
        l[1] = int (l[1])
        nums1.append(l[0])
        nums2.append(l[1])
   
    return [nums1,nums2]


def sort_sum(nums1,nums2):
    nums1.sort()
    nums2.sort()
    tot = 0
    for i in range(len(nums1)):
        tot+= abs(nums1[i]-nums2[i])
    return tot

def similarity_score(nums1,nums2):
    # nums2 should be the left list
    multiplier = {}
    for n in nums2:
        multiplier[n] = multiplier.get(n,0)+1
    
    tot = 0
    for n in nums1:
        tot += n * multiplier.get(n,0)
    return tot

def main():
    lines = read_input('day1.txt')
    nums1,nums2 = lines_to_int(lines)
    print(sort_sum(nums1,nums2))
    print("similarity score:", similarity_score(nums1,nums2))

if __name__ == "__main__":
    main()