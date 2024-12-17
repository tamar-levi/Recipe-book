from Receipe import Recipe

"""מחלקת קינוחים היורשת ממתכון"""
class Desert(Recipe):
    def __init__(self,ingredients,instructions,color):
        super(Desert,self).__init__(ingredients,instructions)
        self.color=color

    def printRecipe(self):
        """פונקציה המדפיסה את המתכון"""


        super(Desert,self).printRecipe()
        print(f"Color: {self.color}")

    def toArr(self):
        """פונקציה המחזירה מערך של תכונות המתכון"""
        return [self.ingredients, self.instructions, self.color]