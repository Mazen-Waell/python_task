def find_consecutive_sum(n):
    if n % 3 != 0 :
        return None 
    return  (n // 3)-1 , (n // 3) , (n // 3)+1


print(find_consecutive_sum(15))