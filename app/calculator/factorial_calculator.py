from calculator.base_class.base_one_dimansion_recursive_calculetor import BaseOneDimensionRecursiveCalculator


class FactorialCalculator(BaseOneDimensionRecursiveCalculator):

    def __init__(self):
        redis_key = "Factorial"
        dependent_term_count = 1
        super(FactorialCalculator, self).__init__(redis_key, dependent_term_count)

    def recursive_formula(self, dependent_terms, index):
        return dependent_terms[0]*index
