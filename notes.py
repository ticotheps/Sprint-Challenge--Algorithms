# def exercise_a(n):
#     a = 0
#     while (a < n * n * n):
#         a = a + n * n
#     print(f"If n = {n}; then a = {a}")

# exercise_a(1)
# exercise_a(2)
# exercise_a(3)
# exercise_a(4)
# exercise_a(5)
# exercise_a(6)
# exercise_a(7)
# exercise_a(8)
# exercise_a(9)
# exercise_a(10)

def exercise_b(n):
    sum = 0
    for i in range(n):
        i += 1
        for j in range(i + 1, n):
            j += 1
            for k in range(j + 1, n):
                k += 1
                for l in range(k + 1, 10 + k):
                    l += 1
                    sum += 1 
    return sum
  
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
