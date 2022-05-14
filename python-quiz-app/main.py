print("Welcome to computer quiz")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()

print("Okay! Lets play :)")

score=0

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score =+ 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")

if answer.lower() == "general processing unit":
    print("Correct!")
    score =+ 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    print("Correct!")
    score =+ 1
else:
    print("Incorrect!")

answer = input("What does ROM stand for? ")

if answer.lower() == "random operating unit":
    print("Correct!")
    score =+ 1
else:
    print("Incorrect!")

print("You got " + str((score/5) * 100) + '%.')