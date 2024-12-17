from Receipe import Recipe
"""מחלקה יורשת מסוג מתכון[מנה עיקרית]"""
class MainMeel(Recipe):
    def __init__(self,ingredients,instructions,isMeating):
        """אתחול תכונות המתכון"""
        super(MainMeel,self).__init__(ingredients,instructions)
        self.isMeating=isMeating

    def printRecipe(self):
        """הדפסת תכונות המתכון"""


        super(MainMeel,self).printRecipe()
        print(f"IsMeating: {self.isMeating}")


    def toArr(self):
        """החזרת רכיבי המתכון כמערך"""
        return [self.ingredients, self.instructions, self.isMeating]