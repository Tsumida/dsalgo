
from typing import List

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.cnt = 0
        self.discount = discount
        self.n = n
        self.pro_price = dict()
        for i in range(len(products)):
            self.pro_price[products[i]] = prices[i]

    def is_new_circle(self) -> bool:
        return self.cnt - self.n * (self.cnt // self.n) == 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        n = len(product)
        assert n == len(amount)
        factor = 0.0
        self.cnt += 1
        if self.is_new_circle():
            factor = self.discount / 100

        res = 0
        for i in range(n):
            name = product[i]
            res += self.pro_price[name] * amount[i]
        res = res * ( 1 - factor )
        print(res)
        return res


cashier = Cashier(3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100])
assert 500.0 == cashier.getBill([1,2],[1,2])
assert 4000.0 == cashier.getBill([3,7],[10,10])
assert 800.0 == cashier.getBill([1,2,3,4,5,6,7],[1,1,1,1,1,1,1])
assert 4000.0== cashier.getBill([4],[10])
assert 4000.0== cashier.getBill([7,3],[10,10])
assert 7350.0 == cashier.getBill([7,5,3,1,6,4,2],[10,10,10,9,9,9,7])
assert 2500.0 == cashier.getBill([2,3,5],[5,3,2])
