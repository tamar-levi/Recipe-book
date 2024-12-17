from Receipe import Recipe



"""מחלקת עוגות היורשת ממתכון"""
class Cake(Recipe):



    def __init__(self,ingredients,instructions,time):
        super(Cake,self).__init__(ingredients,instructions)
        self.time=time

    def printRecipe(self):
        """פונקציה המדפיסה את המתכון"""

        super(Cake,self).printRecipe()
        print(f"BakeTime: {self.time}")

    def toArr(self):
        """פונקציה המחזירה מערך של תכונות המתכון"""
        return [self.ingredients, self.instructions, self.time]