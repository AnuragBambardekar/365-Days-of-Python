import turtle

def draw_text(text, font_size, color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.write(text, font=("Arial", font_size, "normal"))

def main():
    turtle.speed(2)  # Set the drawing speed

    # Draw "365 days of python programming"
    draw_text("365 days", 20, "blue", -50, 0)
    draw_text("of python", 20, "green", -50, -30)
    draw_text("programming", 20, "red", -50, -60)

    turtle.done()

if __name__ == "__main__":
    main()
