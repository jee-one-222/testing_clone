def average(*num):
    if num:
        l=len(num)
        s=sum(num)
        avg=s/l
        return avg#can do all these in return statement itself, < return sum(num)/len(args)
    else:
        return None
    
print(average(5,7,9,11,13))