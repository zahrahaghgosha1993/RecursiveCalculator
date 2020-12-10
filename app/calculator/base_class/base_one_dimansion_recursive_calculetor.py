from abc import ABC

from utils.get_redis_client import get_redis_client


class BaseOneDimensionRecursiveCalculator(ABC):

    def __init__(self, redis_key, dependent_term_count):
        self.redis_client = get_redis_client()
        self.redis_key = redis_key
        self.dependent_term_count = dependent_term_count

    @property
    def last_calculated_term_index(self):
        return self.redis_client.hlen(self.redis_key)-1

    def recursive_formula(self, dependent_terms, index):
        pass

    def calculate(self, n):
        last_calculated_term_index = self.last_calculated_term_index
        last_terms = self.redis_client.hmget(self.redis_key, [str(i) for i in range(last_calculated_term_index - self.dependent_term_count + 1, last_calculated_term_index + 1)])
        last_terms_list = [i.decode("utf-8") for i in last_terms]

        for i in range(last_calculated_term_index +1, n + 1):
            last_terms_list += [self.recursive_formula([int(j) for j in last_terms_list[-self.dependent_term_count:]], i)]

            self.cache(last_terms_list, last_calculated_term_index + 1)
        return last_terms_list[-1]

    def cache(self, terms_list, from_index):
        dct = {str(index + from_index): str(i) for index, i in enumerate(terms_list[self.dependent_term_count:])}
        self.redis_client.hmset(self.redis_key, dct)

