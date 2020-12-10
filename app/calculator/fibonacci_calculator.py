from calculator.base_class.base_one_dimansion_recursive_calculetor import BaseOneDimensionRecursiveCalculator


class FibonacciCalculator(BaseOneDimensionRecursiveCalculator):

    def __init__(self):
        redis_key = "Fibonacci"
        dependent_term_count = 2
        super(FibonacciCalculator, self).__init__(redis_key, dependent_term_count)

    def recursive_formula(self, dependent_terms,index):
        return dependent_terms[0] + dependent_terms[1]
