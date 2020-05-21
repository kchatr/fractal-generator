"""
This program creates fractal trees and Koch snowflakes via recursive functions. 
Fractals are geometric structures that exhibit self-similarity infinitely. Due to this charectistic, fractals are an apt example of the uses and power of recursion. 

The program utilizes the Turtle library, which is an inbuilt module in Python for creating GUIs.

Author: Kaushik Chatterjee (https://github.com/kchatr)
Version: Python 3.6.8
"""

import turtle
tree = turtle.Turtle()

MIN_BRANCH_LENGTH = 5
def create_tree(turtle_instance, line_thickness, branch_length, sub_branch_diff, angle):
    if branch_length > MIN_BRANCH_LENGTH:
        tree.forward(branch_length)
        new_branch_length = branch_length - sub_branch_diff

        turtle_instance.left(angle)
        create_tree(turtle_instance, line_thickness, new_branch_length, sub_branch_diff, angle)

        turtle_instance.right(angle*2)
        create_tree(turtle_instance, line_thickness, new_branch_length, sub_branch_diff, angle)

        turtle_instance.left(angle)
        turtle_instance.backward(branch_length)    

def create_koch(turtle_instance, iterations, edge_length, edge_div_factor, angle):
    if iterations == 0:
        tree.forward(edge_length)
    else:
        iterations -= 1
        edge_length /= edge_div_factor

        create_koch(turtle_instance, iterations, edge_length, edge_div_factor, angle)
        turtle_instance.left(angle)

        create_koch(turtle_instance, iterations, edge_length, edge_div_factor, angle)
        turtle_instance.right(2*angle)

        create_koch(turtle_instance, iterations, edge_length, edge_div_factor, angle)
        turtle_instance.left(angle)

        create_koch(turtle_instance, iterations, edge_length, edge_div_factor, angle)

def main():
    tree.hideturtle()
    tree.setheading(90)
    
    print("This program creates a fractal tree. A fractal is a repeating geometric structure at infinitesimal scales.")
    start = input("Are you ready to proceed? [Y]/[N] ")

    if start.upper() == "Y":
        decision = input("Would you like to make a Koch Snowflake[K] or a Fractal Tree[F]?")

        if decision.upper() == "K":
          colour = input("\nWhat colour would you like the snowflake to be? ")
          iteration = int(input("How many iterations should the fractal be? Please enter a positive rational number. "))
          length = int(input("How long should the intital snowflake edge be? Please enter a positive rational number. It is reccommended to choose a length over 30. "))
          div = int(input("How much should the edge length scale at each iteration? Please enter a positive rational number. "))
          angle = int(input("At what angle should the sub-edges branch off from the parent? Please enter a positive rational number less than or equal to 90. "))
          
          print("\nHit Alt+Tab to see the fractal :D")
          print("*You may need to adjust the size of the turtle window*")
          tree.color(colour)
          for i in range(3):
            create_koch(tree, iteration, length, div, angle)
            tree.right(120)
          turtle.mainloop()

        elif decision.upper() == "F":
          colour = input("\nWhat colour would you like the tree to be? ")
          thickness = int(input("How thick should every branch be? Please enter a positive rational number. "))
          length = int(input("How long should the intital branch be? Please enter a positive rational number. It is reccommended to choose a length over 30. "))
          diff = int(input("How much smaller should the sub-branch be from its parent? Please enter a positive rational number. "))
          angle = int(input("At what angle should the sub-branches branch off from the parent? Please enter a positive rational number less than or equal to 90. "))
      
          print("\nHit Alt+Tab to see the fractal :D")
          print("*You may need to adjust the size of the turtle window*")
          tree.color(colour)
          create_tree(tree, thickness, length, diff, angle)
          turtle.mainloop()
        
        else:
          print("Invalid option. Rebooting to main menu...")
          main()
       
    elif start.upper() == "N":
        print("#Terminating program...")
        exit()
    else:
        print("Invalid input. Rebooting to main menu...")
        main()

if __name__ == "__main__":
    main()