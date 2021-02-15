import unittest
from Calculator import Calc


class CalculatorTest(unittest.TestCase):
    def test_calculator_prefix(self):
        calculator = Calc()
        self.assertEqual(3, calculator.prefix_calculator("3"))
        self.assertEqual(3, calculator.prefix_calculator("+ 1 2"))
        self.assertEqual(7, calculator.prefix_calculator("+ 1 * 2 3"))
        self.assertEqual(5,calculator.prefix_calculator("+ * 1 2 3"))
        self.assertEqual(3,calculator.prefix_calculator("- / 10 + 1 1 * 1 2"))
        self.assertEqual(-3, calculator.prefix_calculator(" - 0 3"))
        self.assertEqual(1.5, calculator.prefix_calculator("/ 3 2"))

    def test_calculator_infix(self):
        calculator = Calc()
        self.assertEqual(3, calculator.infix_calculator("( 1 + 2 )"))
        self.assertEqual(7, calculator.infix_calculator("( 1 + ( 2 * 3 ) )"))
        self.assertEqual(5, calculator.infix_calculator("( ( 1 * 2 ) + 3 )"))
        self.assertEqual(-1.8, calculator.infix_calculator("( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )"))


if __name__ == '__main__':
    unittest.main()
