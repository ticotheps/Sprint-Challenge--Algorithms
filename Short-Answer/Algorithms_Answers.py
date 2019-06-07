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

#--------------Devise a Plan---------------

#-------Binary Search Approach--------

#  1) First, we will subtract the numerical value of the highest floor (a variable
#     called "max_floor") by the numerical value of the lowest floor (a variable 
#     called "min_floor") to get a numerical value called "floor_difference".

#  2) Then, we will divide this value "floor_difference" by 2 (if this value is an 
#     odd number, round down to the nearest floor) and use this as our "drop_floor"
#     value, where we will be dropping/throwing 3 eggs from to determine if the eggs 
#     break or remain intact, when being dropped from that floor. 

#  3) We have decided to throw/drop three total eggs (instead of just one) from each
#     "drop_floor" to rule out any false positives or false negatives that might 
#     occur from decreased intra-rater reliability or uncontrollable external factors 
#     (i.e. - wind speed, inherent genetic defects of the eggs, etc.).

#  4) After all three eggs are dropped, the eggs will be inspected and each will be given
#     a numerical value of "0" to represent an intact "egg_shell_state" value or "-1"
#     to represent a broken "egg_shell_state" value.

#  5) Whichever state has more occurrences, "intact" or "broken", will determine the 
#     numerical "egg_shell_state" value that will be associated with the numerical
#     value of that specific floor.

#  6) Then, both numerical values, will be stored in a list (in this format -->
#     (_f_, egg_shell_state)), which is to then be stored inside of ANOTHER list called 
#     'humpty_dumptys_important_list'.

#-------Either Go to Step 7 or Step 8 to Continue--------

#  7a) If the associated "egg_shell_state" of a floor was determined to be "intact", then we
#      can safely assume that any values of "_f_" (floors) BELOW the current "drop_floor" value
#      will NOT produce a "broken" egg_shell_state value when dropped from those floors because
#      the acceleration of gravity near the earth (g = -9.81 m/s^2) only decreases as you move 
#      towards the earth's surface (i.e. - moving to a lower floor in the building). However,
#      we cannot assume much else, in terms of what eggs will do when dropped from a HIGHER floor.
#      Therefore, we must continue testing the remaining upper half of the building's floors.

#  7b) Then, our next step would be to set our "min_floor" value equal to the current "drop_floor"
#      value +1. Then, we will determine a NEW "drop_floor" value (to test from next) by subtracting
#      the NEW "min_floor" value from the unchanged "max_floor" value and then dividing that number 
#      by 2.

#  8a) If the associated "egg_shell_state" of a floor was determined to be "broken", then we
#      can safely assume that any values of "_f_" (floors) ABOVE the current "drop_floor" value
#      will ALSO produce a "broken" egg_shell_state value when dropped from those floors because
#      the acceleration of gravity near the earth (g = -9.81 m/s^2) only increases as you move 
#      away from the earth's surface (i.e. - moving to a higher floor in the building). However,
#      we cannot assume much else, in terms of what eggs will do when dropped from a LOWER floor.
#      Therefore, we must continue testing the remaining lower half of the building's floors.

#  8b) Then, our next step would be to set our "max_floor" value equal to the current "drop_floor"
#      value -1. Then, we will determine a NEW "drop_floor" value (to test from next) by subtracting
#      the unchanged "min_floor" value from the NEW "max_floor" value and then dividing that number 
#      by 2.

#  9) From here, we will continue following the binary search approach (steps 3-8) until we produce 
#     a DIFFERENT "egg_shell_state" value than what we produced at our initial "drop_floor" value. 
#     This newly discovered numerical "drop_floor" value will be set to a new variable called 
#     "game_changer_floor". 

#  10) The "game_changer_floor" value will be returned at the end of the algorithm and will mark the
#      value of "_f_" that we were originally searching for in our exercise.
