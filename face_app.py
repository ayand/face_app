from Graphics import *

#This is a program which helps you create any face you want.

face_window = Window("Your customized face", 600, 600)
head = Circle((300,300), 150)
head_color = input("red\nblue\nyellow\ngreen\norange\npurple\nblack\nwhite\nSelect any of these colors as your head's color.").lower()

choice1 = True
while choice1:
    if head_color == "red" or head_color == "blue" or head_color == "yellow" or head_color == "green" or head_color == "orange" or head_color == "purple" or head_color == "black" or head_color == "white":
        head.setFill(Color(head_color))
        head.setOutline(Color(head_color))
        head.draw(face_window)
        choice1 = False
    else:
        head_color = input("red\nblue\nyellow\ngreen\norange\npurple\nblack\nwhite\nPlease put in one of these colors only!")
    if head_color == "white":
        face_window.setBackground(Color("black"))

try:
    eye_number = int(input("1\n2\n3\nHow many eyes do you want your face to have?"))
    choice2 = True
    choice2a = True

    while choice2:
        if eye_number == 1:
            eyeball_1 = Circle((300,250), 40)
            eyeball_1.setFill(Color("white"))
            eyeball_1.draw(face_window)
            eye_color = input("red\nblue\nyellow\ngreen\norange\npurple\nblack\nPlease put in the color you want your face's eyes to be.").lower()
            while choice2a:
                if eye_color == "red" or eye_color == "blue" or eye_color == "yellow" or eye_color == "green" or eye_color == "orange" or eye_color == "purple" or eye_color == "black":
                    pupil = Circle((300, 265), 25)
                    pupil.setFill(Color(eye_color))
                    pupil.setOutline(Color(eye_color))
                    pupil.draw(face_window)
                    pupila = Circle((300, 275), 15)
                    pupila.setFill(Color("black"))
                    pupila.draw(face_window)
                    choice2a = False
                else:
                    eye_color = input("red\nblue\nyellow\ngreen\norange\npurple\nblack\nPlease only select the colors you are offered!")
            choice2 = False
        elif eye_number == 2:
            eyeball_1 = Circle((250, 250), 40)
            eyeball_1.setFill(Color("white"))
            eyeball_1.draw(face_window)
            eyeball_2 = Circle((350, 250), 40)
            eyeball_2.setFill(Color("white"))
            eyeball_2.draw(face_window)
            eye_color = input("red\nblue\nyellow\ngreen\norange\npurple\nblack\nPlease put in the color you want your face's eyes to be.").lower()
            while choice2a:
                if eye_color == "red" or eye_color == "blue" or eye_color == "yellow" or eye_color == "green" or eye_color == "orange" or eye_color == "purple" or eye_color == "black":
                    pupil1 = Circle((250, 265), 25)
                    pupil1.setFill(Color(eye_color))
                    pupil1.setOutline(Color(eye_color))
                    pupil1.draw(face_window)
                    pupil2 = Circle((350, 265), 25)
                    pupil2.setFill(Color(eye_color))
                    pupil2.setOutline(Color(eye_color))
                    pupil2.draw(face_window)
                    pupil1a = Circle((250, 275), 15)
                    pupil1a.setFill(Color("black"))
                    pupil1a.draw(face_window)
                    pupil2a = Circle((350, 275), 15)
                    pupil2a.setFill(Color("black"))
                    pupil2a.draw(face_window)
                    choice2a = False
                else:
                    eye_color = input("red\nblue\nyellow\ngreen\norange\npurple\nblack\nPlease only select the colors you are offered!")
            choice2 = False
        elif eye_number == 3:
            eyeball_1 = Circle((300, 250), 40)
            eyeball_1.setFill(Color("white"))
            eyeball_1.draw(face_window)
            eyeball_2 = Circle((210, 250), 40)
            eyeball_2.setFill(Color("white"))
            eyeball_2.draw(face_window)
            eyeball_3 = Circle((390, 250), 40)
            eyeball_3.setFill(Color("white"))
            eyeball_3.draw(face_window)
            eye_color = input("red\nblue\nyellow\ngreen\norange\npurple\nblack\nPlease put in the color you want your face's eyes to be.").lower()
            while choice2a:
                if eye_color == "red" or eye_color == "blue" or eye_color == "yellow" or eye_color == "green" or eye_color == "orange" or eye_color == "purple" or eye_color == "black":
                    pupil1 = Circle((300, 265), 25)
                    pupil1.setFill(Color(eye_color))
                    pupil1.setOutline(Color(eye_color))
                    pupil1.draw(face_window)
                    pupil2 = Circle((210, 265), 25)
                    pupil2.setFill(Color(eye_color))
                    pupil2.setOutline(Color(eye_color))
                    pupil2.draw(face_window)
                    pupil3 = Circle((390, 265), 25)
                    pupil3.setFill(Color(eye_color))
                    pupil3.setOutline(Color(eye_color))
                    pupil3.draw(face_window)
                    pupil1a = Circle((300, 275), 15)
                    pupil1a.setFill(Color("black"))
                    pupil1a.draw(face_window)
                    pupil2a = Circle((210, 275), 15)
                    pupil2a.setFill(Color("black"))
                    pupil2a.draw(face_window)
                    pupil3a = Circle((390, 275), 15)
                    pupil3a.setFill(Color("black"))
                    pupil3a.draw(face_window)
                    choice2a = False
                else:
                    eye_color = input("red\nblue\nyellow\ngreen\norange\npurple\nblack\nPlease only select the colors you are offered!")
            choice2 = False
        else:
            try:
                eye_number = int(input("1\n2\n3\nPlease put in one of these 3 numbers and nothing different!"))
            except:
                print("Now, now, you can't put in a string when we're asking you for an integer!")
except:
    print("Now, now, you can't put in a string when we're asking you for an integer!")

expression_choice = input("smile\nsadness\nWhat kind of expression do you want your face to have?").lower() #Tell me what you think!
choice3 = True
while choice3:
    if expression_choice=="smile":
        mouth_option = input("Open\nClosed\n\nDo you want your face's mouth to be open or closed?").lower()
        choice3a = True
        while choice3a:
            if mouth_option=="open":
                smile = Circle((300, 360), 60)
                if head_color=="red":
                    smile.setFill(Color("black"))
                    smile.setOutline(Color("black"))
                else:
                    smile.setFill(Color("red"))
                    smile.setOutline(Color("red"))
                smile.draw(face_window)
                coverup_rectangle = Rectangle((360,360), (240, 300))
                coverup_rectangle.setFill(Color(head_color))
                coverup_rectangle.setOutline(Color(head_color))
                coverup_rectangle.draw(face_window)
                choice3a = False
                choice3 = False
            elif mouth_option=="closed":
                smile = Circle((300,360), 60)
                smile.setFill(Color(head_color))
                smile.setWidth(2)
                if head_color=="red":
                    smile.setOutline(Color("black"))
                else:
                    smile.setOutline(Color("red"))
                smile.draw(face_window)
                coverup_rectangle = Rectangle((360,360), (240, 295))
                coverup_rectangle.setFill(Color(head_color))
                coverup_rectangle.setOutline(Color(head_color))
                coverup_rectangle.draw(face_window)
                choice3a = False
                choice3 = False
            else:
                mouth_option = input("Open\nClosed\n\nPlease pick only one of these two options!").lower()
    elif expression_choice=="sadness": #Isn't this awesome?!
        sadmouth = Circle((300,370), 60)
        sadmouth.setFill(Color(head_color))
        sadmouth.setWidth(2)
        if head_color=="red":
            sadmouth.setOutline(Color("black"))
        else:
            sadmouth.setOutline(Color("red"))
        sadmouth.draw(face_window)
        coverup_rectangle = Rectangle((240,370), (360, 431))
        coverup_rectangle.setFill(Color(head_color))
        coverup_rectangle.setOutline(Color(head_color))
        coverup_rectangle.draw(face_window)
        choice3a = False
        choice3 = False
    else:
        expression_choice = input("smile\nsadness\nPlease pick one of these expression only!").lower()

#Like all the choices we've given you? Please let us know!
 