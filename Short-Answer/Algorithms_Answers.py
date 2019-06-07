#  Exercise 1:

#-------------SOLUTION I a---------------:

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


#--------------------SOLUTION I b--------------------:

#  b)  If we are to simply return the value of "sum" AFTER executing all
#      of the 'for' loops, then the running time complexity of this 
#      snippet of pseudocode is "exponential time" or O(2^n). This is because
#      as "n" increases in size (arbitrarily), the number of operations
#      performed by this algorithm increases exponentially. Please run the
#      following code below to see example outputs that support this
#      hypothesis.

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


#--------------------SOLUTION I c--------------------:

#  c) If we are to simply return a numerical value of "bunny ears" AFTER
#     executing if/else statement, then the running time complexity of this 
#     snippet of pseudocode is "linear time" or O(n). This is because
#     as "n" increases in size (arbitrarily), the number of operations
#     performed by this algorithm increases in proportion to the linear 
#     increase of "n". Please run the following code below to see example 
#     outputs that support this hypothesis.

'''
def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
'''
#  In my example below: 
#  bunnyEars(bunnies) = exercise_c(n)
#  bunnies = n
#  2 + bunnyEars(bunnies-1) => 2 + exercise_c(n-1)
def exercise_c(n):
    operation_counter = 0
    if n == 0:
        return 0
    else:    
        operation_counter += 1
        ears = exercise_c(n-1)
        ears += 2
        
    print(f"When n = {n}, this counts as {operation_counter} operation; and the total number of ears is now: {ears}")    
    return ears
  
print("\n Example Outputs for 'exercise_c()': \n-----------------------------------")
print(exercise_c(1))   
print(exercise_c(2))   
print(exercise_c(3))   
print(exercise_c(4))   
print(exercise_c(5))   
print(exercise_c(6))   
print(exercise_c(7))   
print(exercise_c(8))   
print(exercise_c(9))   
print(exercise_c(10))   
print(exercise_c(20))  

#--------------------SOLUTION II--------------------:

#---------Understanding the Problem----------
#  -This building has "_n_" stories.

#  -A "story" is defined as 'any level part of a building that is covered
#   by a roof and also has a floor associated with it'. It also must have the
#   utility such that it could be used by people (for living, work, etc.).

#  -This building has "_f_" floors.

#  -A "floor," in this context, can be described as 'the portion of the story
#   that people walk on'.

#  -You have lots of eggs.

#  -Eggs have two states, so they can be either "intact" or "broken".

#  -Eggs can be dropped out of the building, from any floor.

#  -An egg is considered "broken" when it is thrown/dropped from ANY floor
#   that is HIGHER THAN or EQUAL to floor "_f_".

#  -If an egg is thrown/dropped from ANY floor that is LOWER than floor "_f_",
#   the egg will remain intact.

#  -PROBLEM: Write an algorithm (in English) to figure out the numerical value
#   of floor "_f_" so you can minimize the number of eggs that are "broken".