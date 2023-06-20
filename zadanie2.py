#Кретов Данила Иванович Группа 44-22-116 Вариант 7 Задание 2
import unittest

class CalculationTest(unittest.TestCase):
     def test_case_x_less_than_1_1(self):
         result = calculate_value(1)
         self.assertEqual(result, math.exp(math.sin(1)) + math.tan(1))

     def test_case_x_greater_than_or_equal_to_1_1(self):
         result = calculate_value(2)
         self.assertEqual(result, math.log(abs(math.sin(2) + math.sqrt(2*2))))

if __name__ == '__main__':
    unittest.main()