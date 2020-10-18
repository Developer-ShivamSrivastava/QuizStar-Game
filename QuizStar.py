from tkinter import *
import random

questions = [
    "How many Keywords are there in C Programming language ?",
    "Which of the following functions takes A console Input in Python ?",
    "Which of the following is the capital of India ?",
    "Which of The Following is must to Execute a Python Code ?",
    "The Taj Mahal is located in  ?",
    "The append Method adds value to the list at the  ?",
    "Which of the following is not a costal city of india ?",
    "Which of The following is executed in browser(client side) ?",
    "Which of the following keyword is used to create a function in Python ?",
    "To Declare a Global variable in python we use the keyword ?",
    "Who was the father of India ?",
    "When is independence day celebrated in India ?",
    "Which are the best mobile phone company in the world?",
    "Who is the rich person in the world?",
    "The circular and Molecular Biology is stuated at",
    "The famous Dilwara Temples stuated in",
    "In the Battle of Wandiwash, the English defeated ?",
    "What is 3*(2-1)?"
]

answer_choice = [
    ["23","32","33","43",],                                                         # 01
    ["get()","input()","gets()","scan()",],                                         # 02
    ["Mumbai","Delhi","Chennai","Lucknow",],                                        # 03
    ["TURBO C","Py Interpreter","Notepad","IDE",],                                  # 04
    ["Patna","Delhi","Benaras","Agra",],                                            # 05
    ["custom location","end","center","beginning",],                                # 06
    ["Bengluru","Kochin","Mumbai","vishakhapatnam",],                               # 07
    ["perl","css","python","java",],                                                # 08
    ["function","void","fun","def",],                                               # 09
    ["all","var","let","global",],                                                  # 10
    ["Shubhash Chandra Bosh", "Mahatma Ghadhi", "Lalbhadur Shastri" ,"None"],       # 11
    ["2 Jan,1923","23 Sept,1956","15 Aug,1947", "None"],                            # 12
    ["Sumsung","Apple","RealMe","Redmi"],                                           # 13
    ["Bilgates","Mukesh  Ambani","Salman Khan","None of these"],                    # 14
    ["Patna","Jaipur","Hyderabad","New Delhi"],                                     # 15
    ["Uttar Pradesh","Chennai","Rajisthan","New Delhi"],                            # 16
    ["the Dutch", "the French", "the Portuguese", "None of these"],                 # 17
    ["5","3","9","12"],                                                             # 18
]

answers =[1,1,1,1,3,1,0,1,3,3,1,2,1,0,2,2,1,1]

user_answer = []

indexes = []
def gen():          # gen() --> means generator
    global indexes
    while(len(indexes) < 5):
        x = random.randint(0,17)
        if x in indexes:
            continue
        else:
            indexes.append(x)
    # print(indexes)

def showResult(score):
    lableQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()

    labelimage = Label(
        root,
        background="#ffffff",
        border = 0
    )
    labelimage.pack(pady=(50,30))
    labelResultText = Label(
        root,
        font = ("Consolas",20),
        background="#ffffff"
    )
    labelResultText.pack()
    labelFinalScore = Label(
        root,
        font = ("Times",20),
        background = "#ffffff"
    )
    labelFinalScore.pack()
    if score >= 20:
        img = PhotoImage(file='great.png')
        labelimage.config(image=img)
        labelimage.image = img
        labelResultText.config(text="You are Excellent!!")
        labelFinalScore.config(text = f"Score: {score} of 25")
    elif 10 <= score < 20:
        img = PhotoImage(file='ok.png')
        labelimage.config(image=img)
        labelimage.image = img
        labelResultText.config(text="You are Very Nice!!")
        labelFinalScore.config(text=f"Score: {score} of 25")
    elif score < 10:
        img = PhotoImage(file='bad.png')
        labelimage.config(image=img)
        labelimage.image = img
        labelResultText.config(text="You should Work Hard!!")
        labelFinalScore.config(text=f"Score: {score} of 25")

def calc():
    global indexes, user_answer,answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score += 5
        x += 1
    # print(f"Score: {score} / 90")
    showResult(score)

ques = 1
def selected():
    global radiovar,user_answer
    global lableQuestion, r1, r2, r3, r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lableQuestion.config(text= questions[indexes[ques]])
        r1["text"] = answer_choice[indexes[ques]][0]
        r2["text"] = answer_choice[indexes[ques]][1]
        r3["text"] = answer_choice[indexes[ques]][2]
        r4["text"] = answer_choice[indexes[ques]][3]
        ques += 1
    else:
        # print(indexes)
        # print(user_answer)
        # print(answers)
        calc()

def startQuiz():
    global lableQuestion,r1,r2,r3,r4
    lableQuestion = Label(
        root,
        text=questions[indexes[0]],
        font=("Consolas",16),
        width=500,
        justify="center",
        wraplength=400,
        background = "#ffffff"
    )
    lableQuestion.pack(pady = (100,30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = answer_choice[indexes[0]][0],
        font = ("Times",12),
        value = 0,
        variable = radiovar,
        command = selected,
        background="#ffffff"
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text = answer_choice[indexes[0]][1],
        font = ("Times",12),
        value = 1,
        variable = radiovar,
        command = selected,
        background="#ffffff"
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text = answer_choice[indexes[0]][2],
        font = ("Times",12),
        value = 2,
        variable = radiovar,
        command = selected,
        background="#ffffff"
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text = answer_choice[indexes[0]][3],
        font = ("Times",12),
        value = 3,
        variable = radiovar,
        command = selected,
        background="#ffffff"
    )
    r4.pack(pady=5)

def startIsPressed():
    labelImage.destroy()
    labelText.destroy()
    labelInstruction.destroy()
    labelRules.destroy()
    btnStart.destroy()
    gen()
    startQuiz()

root = Tk()

root.title("QuizStar")
root.geometry("750x600")
root.config(background="#ffffff")
root.resizable(0,0)

img1 = PhotoImage(file = "QUIZ_LOGO.png")
labelImage = Label(root, image = img1, background="#ffffff")
labelImage.pack(pady=(40,0))

labelText = Label(root,text="QuizStar",font=("Comic sans MS",24,"bold"),background="#ffffff")
labelText.pack(pady=(0,50))

img2 = PhotoImage(file = "button1.png")
btnStart = Button(
    root,
    image=img2,
    relief=FLAT,
    border=0,
    background="#ffffff",
    command=startIsPressed
    )
btnStart.pack(pady=(0,20))

labelInstruction = Label(root,text="Read The Rules And\nClick the Start once you are ready!",
                            font=("Consolas",14),background="#ffffff",justify="center")
labelInstruction.pack(pady=(0,63))

labelRules = Label(
    root,
    text="This QuizStar game contains 18 questions from which you will have to answer only 5 questions\nOnce you select a radio button that will be a final choice\nhence think before you select.",
    width=100,
    font=("Times",14),
    background="#000000",
    foreground="#FACA2F"
    )
labelRules.pack()


root.mainloop()