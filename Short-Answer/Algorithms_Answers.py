#  Exercise 1:

#  THE TWO CASES FOR SOLUTION 1a:

#  a) i) If we are to simply return the value of "a" AFTER the execution 
#        of the 'while' loop, then the running time complexity of this 
#        snippet of pseudocode is "constant time" or O(1). This is because
#        as "n" increases in size (arbitrarily), the number of operations
#        performed by this algorithm does NOT change. Please see the
#        commented code below.

def exercise_a_i(n):
    a = 0
    while (a < n * n * n):
        a = a + n * n
    
    return (f"If n = {n}; then a = {a}")

print("Example Outputs for 'exercise_a_i()':")
print(exercise_a_i(1))   # Output: If n = 1; then a = 1
print(exercise_a_i(2))   # Output: If n = 2; then a = 8
print(exercise_a_i(3))   # Output: If n = 3; then a = 27
print(exercise_a_i(4))   # Output: If n = 4; then a = 64
print(exercise_a_i(5))   # Output: If n = 5; then a = 125
print(exercise_a_i(6))   # Output: If n = 6; then a = 216
print(exercise_a_i(7))   # Output: If n = 7; then a = 343
print(exercise_a_i(8))   # Output: If n = 8; then a = 512
print(exercise_a_i(9))   # Output: If n = 9; then a = 729
print(exercise_a_i(10))  # Output: If n = 10; then a = 1000
print(exercise_a_i(20))  # Output: If n = 20; then a = 8000

#  a) ii) If we are to return the value of "a" DURING the execution 
#         of the 'while' loop, then the running time complexity of this 
#         snippet of pseudocode would still be "constant time" or O(1).
#         This is because as "n" increases in size (arbitrarily), 
#         the number of operations performed by this algorithm stays 
#         the same, despite having different value for outputs. Please 
#         see the commented code below.

def exercise_a_ii(n):
    a = 0
    while (a < n * n * n):
        a = a + n * n
        return (f"If n = {n}; then a = {a}")

print("DIFFERENT Example Outputs for 'exercise_a_ii()':")
print(exercise_a_ii(1))   # Output: If n = 1; then a = 1
print(exercise_a_ii(2))   # Output: If n = 2; then a = 4
print(exercise_a_ii(3))   # Output: If n = 3; then a = 9
print(exercise_a_ii(4))   # Output: If n = 4; then a = 16
print(exercise_a_ii(5))   # Output: If n = 5; then a = 25
print(exercise_a_ii(6))   # Output: If n = 6; then a = 36
print(exercise_a_ii(7))   # Output: If n = 7; then a = 49
print(exercise_a_ii(8))   # Output: If n = 8; then a = 64
print(exercise_a_ii(9))   # Output: If n = 9; then a = 81
print(exercise_a_ii(10))  # Output: If n = 10; then a = 100
print(exercise_a_ii(20))  # Output: If n = 20; then a = 400