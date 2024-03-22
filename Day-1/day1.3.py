function is_happy(n):
    seen <- empty set

    while n != 1:
        if n in seen:
            return False
        else:
            add n to seen
            sum_of_squares <- 0
            for each digit in convert n to string:
                sum_of_squares += (digit converted to int) ** 2
            n <- sum_of_squares
    
    return True
