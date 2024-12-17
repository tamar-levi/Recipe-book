from Receipe import Recipe
"""מחלקת סלטים היורשת ממתכון"""
class Salad(Recipe):
    def __init__(self,ingredients,instructions,timeStoring):
        super(Salad,self).__init__(ingredients,instructions)
        self.timeStoring=timeStoring

    def printRecipe(self):
        """פונקציה המדפיסה את המתכון"""


        super(Salad,self).printRecipe()
        print(f"TimeStoring: {self.timeStoring}")

    def toArr(self):
        """פונקציה המחזירה מערך של תכונות המתכון"""
        return [self.ingredients,self.instructions,self.timeStoring]
