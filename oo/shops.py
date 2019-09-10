class Shop:
      var = 8
      varA = 10
      def describe(self):
          print("Shop")
      def methShop(self):
          print("Hello from the Shop base class")
class CheeseShop(Shop):
      def describe(self):
          print("Hello and Welcome to the",)
          Shop.describe(self)
          print("This Shop sells only Cheese")
class PetShop(Shop):
      var = 15
      varB = 15
      def describe(self):
          print("The Pet Shop")
      def methPetShop(self):
          print("Hello from the Pet Shop")

