from Desert import Desert
from Cake import Cake
from MainMeel import MainMeel
from Salad import Salad
import  json
from PIL import Image


class RecipeBook:
    def __init__(self):
        """אתחול ראשוני של הספר מתכונים"""
        # x={"cake":{"choclatCake": [["2 כוסות קמח","כף שמרים","כפית מלח","2 חבילות שוקולד"],"לערבב הכל יחד לשפוך לתבנית תנור לאחר האפייה לקרר ולשפוך את הציפוי",45]}
        #  ,"salad":{"vegteblsSalad":[["2 מללפון" ,"3 פלפל" ,"2 עגבניות" ,"1 בצל"] ,"לחתוך דק דק,לערבב ולטבל לפי הצורך" ,"3 ימים בקירור"]}
        #  ,"MainMeal":{"chicken": [["עוף" ,"בצל" ,"ברביקיו" ,"בטטה"],"לשטוף את העוף היטב פורסים על תבנית אחד ליד השני,מטבלים בהמון ברביקיו ומפזרים חתיכות בצל ובטטה" ,True]}
        #  ,"Desert":{"IceCream":[["6 ביצים" ,"2 כוסות סוכר" ,"5 כפות קקאו או וניל לבחירה"],"להקציף את הביצים המופרדות עם הסוכר במשך 10 דקות ולאחר מכן להוסיף בעדינות את שאר החומרים","חום לבן"]}}

        # with open("fileBook.txt", "w") as fileBook:
        #     json.dump(self.book, fileBook)
        # with open("fileBook.txt","w") as fileBook:
        #     json.dump(x,fileBook)

        """קריאה מהקובץ השומר את המתכונים לספר מתכונים  """
        with open("fileBook.txt","r") as fileBook:
            self.book = json.load(fileBook)
        """המרת האיברים בספר לאוביקטים מסוג המחלקות """

        for category in self.book.keys():
            for recipe in self.book[category].keys():
                if category=="cake":
                    self.book[category][recipe]=Cake( self.book[category][recipe][0], self.book[category][recipe][1], self.book[category][recipe][2])
                if category=="salad":
                    self.book[category][recipe] = Salad(self.book[category][recipe][0], self.book[category][recipe][1],self.book[category][recipe][2])
                if category=="MainMeal":
                    self.book[category][recipe] = MainMeel(self.book[category][recipe][0], self.book[category][recipe][1],self.book[category][recipe][2])
                if category=="Desert":
                    self.book[category][recipe] = Desert(self.book[category][recipe][0],self.book[category][recipe][1],self.book[category][recipe][2])

    def addRecipe(self):
        """פונקציה להוספת מתכון"""
        try:
          choose=int(input("Enter type of recipe:\npress 1 to cake\npress 2 to salad\npress 3 to mainMeal\npress 4 to desert\n"))
          while choose!=1 and choose!=2 and choose!=3 and choose!=4:
              print("yoo doesnt press correct choosing\n")
              choose = int(input("Enter type of recipe:\npress 1 to cake\npress 2 to salad\npress 3 to mainMeal\npress 4 to desert\n"))
          name = input("Enter recipeName\n")
          Arr = []
          ingredient = input("Enter ingredients to exit enter end\n")
          while ingredient != "end":
              Arr.append(ingredient)
              ingredient = input("Enter ingredients to exit enter end\n")
          instruction = input("Enter instruction\n")
          if choose==1:
              time=int(input("Enter bakingTime\n"))
              cake=Cake(Arr,instruction,time)
              self.book["cake"][name]=cake
          if choose==2:
              time=input("How many time to save\n")
              salad=Salad(Arr,instruction,time)
              self.book["salad"][name]=salad
          if choose==3:
              meat=bool(input("Is meating?\n"))
              mainMeal=MainMeel(Arr,instruction,meat)
              self.book["MainMeal"][name]=mainMeal
          if choose==4:
              color=input("Enter color\n")
              desert=Desert(Arr,instruction,color)
              self.book["Desert"][name]=desert
          print("המתכון התווסף בהצלחה!")
          # self.File()
        except ValueError:
            print("you tried to enter text instead of number\n")


    equal=lambda self,a,b:a==b
    def PrintRecipesByName(self,recipeToSearch):
        """פונקציה להדפסת מתכון לפי שם  מתכון"""
        flag = False
        for category in self.book:
            for recipe in self.book[category]:
                if self.equal(recipeToSearch,recipe)==True:
                   self.book[category][recipe].printRecipe()
                   flag=True
                   break
        if flag==False:
            print("The name isnt exist\n")

    def SearchIngredients(self):
        """ פונקציה לחיפוש מתכון לפי רכיב"""
        try:
            category=int(input("Enter category to search:\npress 1 to cake\npress 2 to salad\npress 3 to mainMeal\npress 4 to desert\n"))
            while category != 1 and category != 2 and category != 3 and category != 4:
                  print("yoo doesnt press correct choosing\n")
                  category = int(input("Enter type of recipe:\npress 1 to cake\npress 2 to salad\npress 3 to mainMeal\npress 4 to desert\n"))
            ingredient=input("Enter ingredient to search\n")
            List=[]
            if category==1:
                List=[self.book["cake"][cake] for cake in self.book["cake"].keys() if ingredient in self.book["cake"][cake].ingredients]
            if category == 2:
                List = [ self.book["salad"][salad] for salad in self.book["salad"].keys() if ingredient in self.book["salad"][salad].ingredients  ]
                print(List)
            if category == 3:
                List = [self.book["MainMeal"][mainMeal]  for mainMeal in self.book["MainMeal"].keys() if ingredient in self.book["MainMeal"][mainMeal].ingredients]
            if category == 4:
                List = [self.book["Desert"][desert]  for desert in self.book["Desert"].keys() if ingredient in self.book["Desert"][desert].ingredients]
            if List==None:
                print("There isnt search results\n")
            else:
              for i in List:
                  i.printRecipe()
        except ValueError:
            print("you tried to enter text instead of number\n")

    def writeBook(self):
        """ שמירת הספר בקובץ (המרה מאוביקט מחלקה למשתנה)"""
        for category in self.book.keys():
            for recipe in self.book[category].keys():
                self.book[category][recipe] = self.book[category][recipe].toArr()
        with open("fileBook.txt", "w") as fileBook:
            json.dump(self.book,fileBook)

    def printBook(self):
        """פונקציה המדפיסה את כל הספר"""
        print("My recipe book:\n")
        for category in self.book.keys():
            if category=='cake':
                img = Image.open('image/InkedchoclateCake.jpg')
            if category=='salad':
                img = Image.open('image/InkedLeave.jpg')
            if category=='MainMeal':
                img = Image.open('image/InkedMain.jpg')

            if category=='Desert':
                img = Image.open('image/InkedCake.jpg')
            img.show()

            print("\n")
            print(f"category:{ category}")
            for recipe in self.book[category].keys():
                print(f"recipe:{ recipe}")
                self.book[category][recipe].printRecipe()