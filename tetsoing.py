

def addToArrayForm(A, K):
    #Your Code Here
    if len(A) > 1 and A[0] == '0':
        print('Array starts with 0. Please enter valid number.')
        return None
    else:
        n_str = ''.join(A)
        if n_str.isdigit():
            n = int(n_str)
            AK_sum = n + K
            return str(AK_sum)
        else:
            print('String contains characters other than digits.')
            return None


print(addToArrayForm(['4', 'a', '0'], 450))
