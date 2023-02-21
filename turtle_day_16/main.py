
from turtle import Turtle, Screen, pos

# from turtle import Turtle ""same thing but insted just use '.Turtle()'
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.begin_fill()
#
# while True:
#     timmy.forward(100)
#     timmy.left(120)
#     timmy.right(60)
#     timmy.forward(150
#                   )
#     if abs(pos()) :
#         break
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("City name",["Adelaide", "Funchal","Machico"])
table.add_column("Area", [1234, 2345, 6543, ])
table.add_column("Population", [11200, 1390, 4536])
table.add_column("Meses Quentes", ["Junho", "Julho", "Agosto"])
table.align = "l"
print(table)