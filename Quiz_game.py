questions = ("1. How many players are on the field for one team at the start of a match?: ",
"2. How many minutes are played in a regular soccer match (excluding extra time)?: ",
"3. What color card means a player is sent off?: ",
"4. Which country won the 2022 FIFA World Cup?: ",
"5. How many points does a team earn for winning a league match?: ",
"6. Who is allowed to use their hands during normal play?: ",
"7. What is awarded when a defender commits a foul inside their own penalty area?: ",
"8. Which competition is played between national teams?: ",
"9. What does VAR stand for?: ",
"10. What is the shape of a soccer ball?: ")



options = (("A. 9 ", "B. 10 ", "C. 11 ", "D. 12 "),
("A. 60", "B. 75", "C. 80", "D. 90"),
("A. Blue", "B. Yellow", "C. Red", "D. Green"),
("A. Brazil", "B. France", "C. Argentina", "D. Spain"),
("A. 1", "B. 2", "C. 3", "D. 5"),
("A. Every Player", "B. The goalkeeper(Inside the penalty area)", "C. The captain", "D. Defenders"),
("A. Throw In", "B. Corner Kick", "C. Free Kick", "D. Penalty Kick"),
("A. UEFA Champions League", "B. Premier League", "C. FIFA World Cup", "D. FA Cup"),
("A. Video Assistant Referee", "B. Video Action Replay", "C. Virtual Assistant Referee", "D. Video Automatic Review"),
("A. Cube", "B. Sphere", "C. Cylinder", "D. Pyramid"))



answers = ("C", "D", "C", "C", "C", "B", "D", "C", "A", "B")

guesses = []

score = 0

questions_num = 0


for question in questions:
    print("                       ")
    print("                       ")
    print(question)

    for option in options[questions_num]:
        print(option)

    guess = input("Enter (A, B, C, or D): ").upper()
    guesses.append(guess)

    if guess == answers[questions_num]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
        print(f"{answers[questions_num]} is the correct answer.")


    questions_num += 1

print("                       ")
print("       RESULTS         ")
print("                       ")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")