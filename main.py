from RecipeBook import RecipeBook
from PIL import Image
"""ספר מתכונים"""
book=RecipeBook()
name=input("Hello to the recipe book\nenter your name\n")
print(f"Hello to {name}")
img=Image.open('image/InkedPay.jpg')
img.show()
"""משנה המסייע לבדיקת תקינות,כל עוד המשתמש מכניס קלט לא חוקי"""
flag1=True
while flag1==True:
  try:
      """הצגת כל האופציות למשתמש"""
      choosing = int(input("Press 1 to add recipe\nPress 2 to search by name\nPress 3 to search by ingredients\nPress 4 to show the book\nPress 5 to exit\n"))
      flag1=False
      while choosing != 5:
          flag = True
          if choosing==1:
              book.addRecipe()
          if choosing==2:
              recipeName=input("Enter recipeName\n")
              book.PrintRecipesByName(recipeName)
          if choosing==3:
              book.SearchIngredients()
          if choosing==4:
              book.printBook()
          while flag==True:
            try:
                choosing = int(input("Press 1 to add recipe\nPress 2 to search by name\nPress 3 to search by ingredients\nPress 4 to show the book\nPress 5 to exit\n"))
                flag=False
            except:
                print("You tried to enter text instead of number\n")

      book.writeBook()
  except:
      print("You tried to enter text\n")
print("We are so enjoyed with you")
