class Shop:
      var = 8
      varA = 10
      def describe(self):
          print("Shop")
      def welcome(self):
          print("Hello from the Shop base class")
class CheeseShop(Shop):
      def describe(self):
          print("Hello and Welcome to the Cheese Shop")
          print("\tThis Shop sells only the finest Cheeses!")
class PetShop(Shop):
      var = 15
      varB = 15
      def describe(self):
          print("The Pet Shop")
      def methodPetShop(self):
          print("Hello from the Pet Shop")


CheeseShop().describe();

PetShop().describe();
