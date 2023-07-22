import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        # list comprehension
        missed_states = [i for i in all_states if i not in guessed_states]

        # missed_states = []
        # for i in all_states:
        #     if i not in guessed_states:
        #         missed_states.append(i)
        
        dictionary = {
            "Missed States": missed_states
        }
        data = pandas.DataFrame(dictionary)
        data.to_csv("learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        # turtle for writing states
        write_turtle = turtle.Turtle()
        write_turtle.penup()
        write_turtle.hideturtle()
        state_data = data[data.state == answer_state]
        write_turtle.goto(int(state_data.x), int(state_data.y))
        write_turtle.write(answer_state)



turtle.mainloop()


