def password_gen():
    import random
    
    uppers = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    lowers = list('abcdefghijklmnopqrstuvwxyz')
    digits = list('1234567890')
    
    password = uppers.pop(random.randint(0, len(uppers)-1))
    password += lowers.pop(random.randint(0, len(lowers)-1))
    password += digits.pop(random.randint(0, len(digits)-1))
    
    remaining = uppers + lowers + digits
    for i in range(random.randint(3, 17)):
        password += remaining.pop(random.randint(0, len(remaining)-1))
        
    return password
