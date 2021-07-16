#what are m and n after the following code is executed

n = 123456789
m = 0
while n != 0:
    m = (10 * m) + (n % 10)
    n //= 10

    print(m , n )
    
    # Answer: values of m (0,98,987,9876,98765,987654,9876543,98765432,987654321)
    #values of n (0,1,2,12,123,1234,12345,123456,1234567,12345678,123456789)