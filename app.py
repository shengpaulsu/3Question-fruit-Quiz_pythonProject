from Questions import Question
questions_prompts = [
    "What color are oranges?\n(a) Green\n(b) Purple\n(c) Orange\n\n",
    "What color are limes?\n(a) green\n(b) Magenta\n(c) Yellow\n\n",
    "What color are lemons?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]

questions = [
    Question(questions_prompts[0], "c"),
    Question(questions_prompts[1], "a"),
    Question(questions_prompts[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score+= 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)