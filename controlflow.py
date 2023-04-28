# //Write a function that uses while, if and continue statements to print
# //all the even numbers between 0 and 50. 
def even_numbers():
      x=0
      while x<50:
        x+=1
        if x %2!=0:
            continue
        print(x)
        
even_numbers()        
 

# //Write a function that takes a list of
# //integers as input and prints the sum of all the even numbers in the list. 
def sum_of_even(numbers):
    x=0
    for i in numbers:
        if i%2==0:
           x+=i
    return x 
numbers=[23,12,43,34,16] 
print(sum_of_even(numbers))  


# //Write a function that takes an integer argument and 
# //prints "Prime" if the number is prime, and "Not prime"
# if the number is not prime.
def is_primenumber(n):
   
    if n <= 1:
        print("Not prime")
        return
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print("Not prime")
            return
    print("Prime")
    
is_primenumber(5)    
    
# //Write a function that takes any two integers as input, and prints the sum of all the numbers
# //between the two integers (inclusive) that are divisible by 3.

def sum_divisible_by_3(x, y):
   
    if x > y:
        a, y = y, x
    
    total = 0
    for i in range(x, y+1):
        if i % 3 == 0:
            total += i
            
            return total
        
print(sum_divisible_by_3(10,20))        
    
    
     


        