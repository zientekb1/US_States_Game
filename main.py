import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)  # changes turtle to be a gif image
score = 0
correct_answers = []
states = pandas.read_csv("50_states.csv")
states_list = states.state.to_list()
# user keeps guessing until they have answered all 50 states
while len(correct_answers) < 50:
    # show text box that shows the score
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
    # if the user enters 'Exit' game will close and the states they didn't answer are stored in states to learn

    if answer_state == "Exit":
        states_not_guessed_correct = [state for state in states_list if state not in correct_answers]
        data = pandas.DataFrame(states_not_guessed_correct)
        data.to_csv("States_to_learn.csv")
        break

    for possibleAnswers in states_list:
        # compare what the user entered is in 50_states.csv
        if answer_state == possibleAnswers and answer_state not in correct_answers:
            score += 1
            # record the correct answer in a list
            correct_answers.append(answer_state)

            # locate the states col in 50_states.csv
            states_col = states[states.state == possibleAnswers]

            # create a turtle with the states name and have it float to where the state is on the map
            state_name = turtle.Turtle()
            state_name.hideturtle()
            state_name.penup()
            state_name.goto(int(states_col.x), int(states_col.y))
            state_name.write(possibleAnswers)
