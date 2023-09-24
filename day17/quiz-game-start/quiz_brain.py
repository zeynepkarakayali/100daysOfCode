# TODO: asking the questions
class QuizBrain():
    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_q.question}. (True/False)?: ").lower()
        self.check_answer(user_answer, current_q.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user_answer, real_answer):
        if user_answer == real_answer.lower():
            self.score += 1
            print(f"You got it right. ")
        else:
            print("Sorry, that's wrong. ")
        print(f"The correct answer was: {real_answer}. ")
        print(f"Your current score is: {self.score}/{self.question_number}. ")
        print("\n")

# TODO: checking if the answer was correct

# TODO: checking if we're at the end of the quiz