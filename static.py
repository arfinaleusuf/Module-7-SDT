# static attribute (class attribute)
#  static attribute @staticmethod
# class methoed @ classmethod
#  defference between static methord and class method

class Shopping:
    cart = []  # class attribute # static attribute
    origin = 'chaina'

    def __init__(self, name ,location):
        self.name = name  # instance attribute
        self.location = location

    def purchase(self,item, price, amount):
        remaning = amount - price
        print(f'buying: {item} for price: {price} and remaining: {remaning}')

    @staticmethod
    def multiply(a ,b):
        result = a * b
        print(result)

    @classmethod
    def hudai_dekhi(self,item):
        print(self.name)
        print('hudai dekhi kintu kinmu na', item)

basundhara = Shopping('basundhara' , 'not popular')
# basundhara.purchase('lungi', 500, 1000)
basundhara.hudai_dekhi('lungi')
# Shopping.purchase('a',2,3,3)
Shopping.hudai_dekhi('Lungi')

Shopping.multiply(4,6)  #staic method
# basundhara.multiply(6,9)