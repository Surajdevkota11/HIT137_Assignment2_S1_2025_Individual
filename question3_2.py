"""
HIT137 - Assignment 2
Question 3: Recursive Geometric Pattern Generator

Student: Suraj Devkota
Student ID: S397467
Date: December 2026

Description:
This program draws recursive geometric patterns using turtle graphics.
Users can select the number of sides, initial side length, and recursion depth.
"""

import turtle
import sys

def draw_recursive_shape(t, sides, length, depth, angle_offset=0):
    """
    Draws a recursive geometric pattern with nested polygons.
    """
    if depth <= 0:
        return

    turn_angle = 360 / sides
    colors = ['blue', 'red', 'green', 'purple', 'orange', 'brown', 'pink']
    t.color(colors[depth % len(colors)])

    for _ in range(sides):
        t.forward(length)
        t.right(turn_angle)

    new_length = length * 0.6
    t.penup()
    t.forward(length * 0.2)
    t.left(90)
    t.forward(length * 0.2)
    t.right(90)
    t.pendown()

    t.right(angle_offset)
    draw_recursive_shape(t, sides, new_length, depth - 1, angle_offset)
    t.left(angle_offset)

    t.penup()
    t.left(90)
    t.backward(length * 0.2)
    t.right(90)
    t.backward(length * 0.2)
    t.pendown()


def get_user_input():
    """Get number of sides, length, and recursion depth from user."""
    print("🎨 RECURSIVE GEOMETRIC PATTERN SETTINGS")
    try:
        sides = int(input("Enter number of sides (3-10): "))
        if sides < 3:
            print("❌ Minimum 3 sides required.")
            return None
        length = int(input("Enter initial side length (50-500): "))
        if length < 50 or length > 500:
            print("❌ Length must be between 50 and 500.")
            return None
        depth = int(input("Enter recursion depth (1-7): "))
        if depth < 1 or depth > 7:
            print("❌ Depth must be between 1 and 7.")
            return None
        return sides, length, depth
    except ValueError:
        print("❌ Please enter valid integers only.")
        return None
    except KeyboardInterrupt:
        print("\n❌ Program cancelled by user.")
        return None


def setup_turtle():
    """Sets up the turtle graphics screen and turtle."""
    screen = turtle.Screen()
    screen.title("Recursive Geometric Pattern - Suraj Devkota (S397467)")
    screen.bgcolor("white")
    screen.setup(width=800, height=800)

    t = turtle.Turtle()
    t.speed(0)
    t.pensize(2)
    t.hideturtle()
    return screen, t


def main():
    print("="*60)
    print("🎨 RECURSIVE GEOMETRIC PATTERN GENERATOR")
    print("="*60)

    params = get_user_input()
    if params is None:
        return

    sides, length, depth = params
    print(f"\nDrawing {sides}-sided recursive pattern, side length={length}, depth={depth}")

    screen, t = setup_turtle()

    # Center the shape in the window
    t.penup()
    t.goto(-length/2, length/2)
    t.pendown()

    draw_recursive_shape(t, sides, length, depth, angle_offset=10)

    print("\n✅ Pattern drawing complete! Check the graphics window.")
    print("Close the window or press Ctrl+C to exit.")

    screen.mainloop()


if __name__ == "__main__":
    try:
        main()
    except turtle.Terminator:
        print("\n✅ Graphics window closed.")
    except KeyboardInterrupt:
        print("\n✅ Program terminated by user.")
        sys.exit(0)
