'''
You are given a complex list of n products, each with a name, price, and weight. Find out how many
duplicate products are present within the list. Duplicate products contain identical parameters for all fields
in the list (i.e. name, price, and weight).

name = [ball, bat, glove, glove, glove]
price = [2, 3, 1, 2, 1]
weight = [2, 5, 1, 1, 1]

'''

from mimetypes import init


class Problem:
    def __init__(self) -> None:
        self.name = ['ball', 'bat', 'glove', 'glove', 'glove']
        self.price = [2, 3, 1, 2, 1]
        self.weight = [2, 5, 1, 1, 1]

    def solution(self, name, price, weight):
        products = set()

        for i in range(len(name)):
            products.add(name[i] + ' ' + str(price[i]) + ' ' + str(weight[i]))

        return len(name) - len(products)

    def run(self):
        print(self.solution(self.name, self.price, self.weight))


if __name__ == "__main__":
    problem = Problem()
    problem.run()
