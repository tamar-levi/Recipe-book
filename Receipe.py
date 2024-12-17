class Recipe():
 """מחלקת מתכון בסיס"""
 def __init__(self,ingredients,instructions):
    self.ingredients=ingredients
    self.instructions=instructions

 def printRecipe(self):
     """פונקצית דריסה להדפסת המתכון"""
     print("\n")
     print("Ingredients:\n")
     for i in self.ingredients:
         print(i)
     print("Instructions:\n")
     print(self.instructions)
