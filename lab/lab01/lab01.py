def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    ans=1
    for i in range(n,n-k,-1):
        ans*=i
    return ans


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    ans,ws=0,1
    while y//pow(10,ws)!=0:
        ws+=1
    while ws:
        ans+=y//pow(10,ws-1)%10
        ws-=1
    return ans
    

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    ws,last,cur=0,0,0
    while n//pow(10,ws):
        ws+=1
    while ws:
        last=cur
        ws-=1
        cur=n//pow(10,ws)
        n%=pow(10,ws)
        if last==cur:
            print("True")
            return
    print("False")
    return