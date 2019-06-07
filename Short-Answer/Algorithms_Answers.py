#  Exercise 1:

#-------------SOLUTION 1a---------------:

#  a) If we are to simply return the value of "a" AFTER the execution 
#     of the 'while' loop, then the running time complexity of this 
#     snippet of pseudocode is "constant time" or O(1). This is because
#     as "n" increases in size (arbitrarily), the number of operations
#     performed by this algorithm does NOT change. Please run the
#     following code below to see example outputs that support this
#     hypothesis.

def exercise_a(n):
    a = 0
    operation_counter = 0
    while (a < n * n * n):
        operation_counter += 1
        a = a + n * n
    
    return (f"If n = {n}; then the total number of operations is: {operation_counter}")

print("\n Example Outputs for 'exercise_a()': \n-----------------------------------")
print(exercise_a(1))
print(exercise_a(2))
print(exercise_a(3))
print(exercise_a(4))
print(exercise_a(5))
print(exercise_a(6))
print(exercise_a(7))
print(exercise_a(8))
print(exercise_a(9)) 
print(exercise_a(10))
print(exercise_a(20))


#--------------------SOLUTION 1b--------------------:

#  a) i) If we are to simply return the value of "sum" AFTER executing all
#        of the 'for' loops, then the running time complexity of this 
#        snippet of pseudocode is "exponential time" or O(2^n). This is because
#        as "n" increases in size (arbitrarily), the number of operations
#        performed by this algorithm increases exponentially. Please run the
#        following code below to see example outputs that support this
#        hypothesis.

def exercise_b(n):
    sum = 0
    operation_counter = 0
    for i in range(n):
        operation_counter += 1
        i += 1
        for j in range(i + 1, n):
            operation_counter += 1
            j += 1
            for k in range(j + 1, n):
                operation_counter += 1
                k += 1
                for l in range(k + 1, 10 + k):
                    operation_counter += 1
                    l += 1
                    sum += 1 
    return (f"If n = {n}; then the total number of operations is: {operation_counter}")
  
print("\n Example Outputs for 'exercise_b()': \n-----------------------------------")
print(exercise_b(1))   
print(exercise_b(2))   
print(exercise_b(3))   
print(exercise_b(4))    
print(exercise_b(5)) 
print(exercise_b(6))  
print(exercise_b(7))  
print(exercise_b(8))      
print(exercise_b(9))  
print(exercise_b(10))  
print(exercise_b(20))  