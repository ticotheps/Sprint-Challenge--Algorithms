#  Exercise 1:

#  a) If we are to simply return the value of "a" following execution 
#     of the 'while' loop, then the running time complexity of this 
#     snippet of pseudocode is "constant time" or O(1). This is because
#     as "n" increases in size (arbitrarily), the number of operations
#     performed by this algorithm does NOT change. Please see the
#     commented code below.


def exercise_a(n):
    a = 0
    while (a < n * n * n):
        a = a + n * n
    
    return (f"If n = {n}; then a = {a}")

print(exercise_a(1))   # Output: If n = 1; then a = 1
print(exercise_a(2))   # Output: If n = 2; then a = 8
print(exercise_a(3))   # Output: If n = 3; then a = 27
print(exercise_a(4))   # Output: If n = 4; then a = 64
print(exercise_a(5))   # Output: If n = 5; then a = 125
print(exercise_a(6))   # Output: If n = 6; then a = 216
print(exercise_a(7))   # Output: If n = 7; then a = 343
print(exercise_a(8))   # Output: If n = 8; then a = 512
print(exercise_a(9))   # Output: If n = 9; then a = 729
print(exercise_a(10))  # Output: If n = 10; then a = 1000
print(exercise_a(20))  # Output: If n = 20; then a = 8000
