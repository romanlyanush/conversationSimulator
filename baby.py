from random import choice

questions = ["Why the sky is blue?: ", "Why you and mommy fight alot?: ", "Why Kenny was killed?: "]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("Why?: ").strip().lower()

print("OH... Okay")

