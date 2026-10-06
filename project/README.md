# Italian Wedding in Jeopardy

**Giorgia Campaniello**

"Italian Wedding in Jeopardy" is an adventure game that tells the story of a chef who is called to save a wedding by creating a menu at the last minute in order to be able to prepare food for the wedding's guests. The wedding will be held in Sicily, in the south of Italy. Unfortunately, the chef lives in Milan, in the north of Italy, and she has just a few ingredients when she begins her journey to the south. She will face some hurdles and meet some nice people who will help her save the wedding. 

Game structure: 

- folder **"project"**: it contains the whole text adventure game
- **"Italian Wedding in Jeopardy.py"**: it contains the main game, the objects and the main menu
- folder **"game_parts"**: package that contains the modules with the classes
- **"player.py"**: it contains the class Player with the player's name, items and location. It also contains the method moving
- **"location.py"**: it contains the class Location with the location's name and items
- **"item.py"**: it contains the class Item with the item's name and quantity
- **"__init__.py"**: it allows the main program to import the classes from game_parts
