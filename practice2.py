def ispalindrome(str):
    for i in range(1, int(len(str)/2)):
        if str[i]==str[len(str)-i-1]:
             return True
    return False
print(ispalindrome(""))
# sum of two digits
num=int(input("enter the number"))
result=0
while num>0:
    digit=num%10
    result=result+digit
    num=num/10
print("sum is:",result)
def isPalindrome(s):
    ''' check if a number is a Palindrome '''
    s = str(s)
    return s == s[::-1]

def generate_palindrome(minx,maxx):
    ''' return a list of Palindrome number in a given range '''
    tmpList = []
    for i in range(minx,max+1):
        if isPalindrome(i):
            tmpList.append(i)
    return tmpList




