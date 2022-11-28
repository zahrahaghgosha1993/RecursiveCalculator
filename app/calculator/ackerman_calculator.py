
class AckermanCalculator():


    def ackerman(self,m, n):
        if m == 0:
            return n + 1
        if m > 0 and n == 0:
            print(n)
            return self.ackerman(m - 1, 1)
        return self.ackerman(m - 1, self.ackerman(m, n - 1))

