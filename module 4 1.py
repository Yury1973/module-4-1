from fake_math import devide as error_devide
from true_math import devide as infinity_devide
result1 = error_devide(69, 3)
result2 = error_devide(3, 0)
result3 = infinity_devide(49, 7)
result4 = infinity_devide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
