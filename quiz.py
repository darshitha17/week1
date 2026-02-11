print("--------------------------------------")
print("Lets start the quiz")
print("--------------------------------------")
score=0
questions=["1.what is  2+2?","2.what's the capital of india?","3.Which animal says 'meow'?","4.what color is the sky?","5.Who's the king of jungle?"]
answers=["4","delhi","cat","blue","Lion"]
for i in range(5):
    print(questions[i])
    entered=input("enter answer:")
    entered.lower()
    if entered==answers[i]:
        print("Yay!Correct")
        score+=1
    else:
        print(f"Oops! The correct answer is {answers[i]}")
    i+=1
print("--------------------------------------")
print("We're done with the Quiz")
print(f"Your final score is {score}/5.")
print("--------------------------------------")

