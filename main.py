# Made by: Cynthia S.

# Import
import simpleguitk
import random
import math

# Variables
message = ""
shape = ""

name = input("What is my patient's name?: ")
hello = ("What is my patient's name?: " + name)

# Main frame
frame = simpleguitk.create_frame("Baymax Written", 600, 500)

# Handler for mouse click
def OwButton():
    global message
    global shape
    message = "Rate your pain: "
    shape = "PlaceHolder"

def PowerButton():
  global message
  message = "Hello!!"


# Creating visual for each button
def draw_shape(canvas):
  if (shape == 'PlaceHolder'):
    # Message Details
      canvas.draw_text(message, [25, 60], 30, "Black", "monospace")

    # Small baymax face
      canvas.draw_circle((410, 40), 8, 20, "Black", "Black")
      canvas.draw_circle((510, 40), 8, 20, "Black", "Black")
      canvas.draw_line((410, 40), (510, 40), 3, "Black")
    # Rating Text Format
      canvas.draw_text(" 1    2    3    4    5", [55, 202], 25, "#50bf5b","monospace")
      canvas.draw_text(" 6    7    8", [55, 352], 25, "Orange", "monospace")
      canvas.draw_text("                9    10", [55, 352], 25, "Red", "monospace")
    # 1 Smiley face
      canvas.draw_circle((85, 125), 35, 3, "Black", "#fff896")
    # Smile Creation (topLine: 50px between)
      canvas.draw_circle((85, 128), 25, 3, "Black")
      canvas.draw_line((60, 128), (110, 128), 3, "Black")
    #cover smile circle
      canvas.draw_polygon([(60,125), (110, 125), (110, 105),(60, 105)], 3, "#fff896", "fff896")
      canvas.draw_line((75, 103), (95, 103), 3, "#fff896")
    # Eyes (32px between)
      canvas.draw_circle((68, 112), 1.8, 2, "Black", "Black")
      canvas.draw_circle((100, 112), 1.8, 2, "Black", "Black")
      
    # 2 Smiley face (100px between)
      canvas.draw_circle((185, 125), 35, 3, "Black", "#fff896")
      
    # 3 Smiley face
      canvas.draw_circle((285, 125), 35, 3, "Black", "#fff896")
      
    # 4 Smiley face
      canvas.draw_circle((385, 125), 35, 3, "Black", "#fff896")

    # 5 Smiley face
      canvas.draw_circle((485, 125), 35, 3, "Black", "#fff896")
      
  else:
    canvas.draw_circle((150, 200), 20, 20, "Black", "Black")
    canvas.draw_circle((450, 200), 20, 20, "Black", "Black")
    canvas.draw_line((150, 200), (450, 200), 8, "Black")

# Create a frame and assign callbacks to event handlers
frame.set_canvas_background("White")
frame.add_button("'Ow'", OwButton, 100)
frame.set_draw_handler(draw_shape)

# Start the frame animation
frame.start()

#ADD frame.add_button("'power'", PowerButton, 100)
