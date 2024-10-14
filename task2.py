import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size)
            t.left(angle)

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()

def main():
    order = int(input("Введіть рівень рекурсії: "))

    draw_koch_curve(order, 300)
    
if __name__ == "__main__":
    main()
