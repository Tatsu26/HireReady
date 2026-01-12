from enum import Enum
from core.q_load import load_questions
from core.c_detector import ConceptDetector
QUESTIONS = load_questions()
class InterviewState(Enum):
    START = "START"
    ASK_QUESTION = "ASK_QUESTION"
    WAIT_FOR_ANSWER = "WAIT_FOR_ANSWER"
    EVALUATE = "EVALUATE"
    END = "END"
class InterviewSession:
    def __init__(self, interview_id: str):
        self.id = interview_id
        self.state = InterviewState.START
        self.current_question = None
        self.history = []
        self.score = 0
    def next_state(self):
        if self.state == InterviewState.START:
            self.state = InterviewState.ASK_QUESTION

        elif self.state == InterviewState.ASK_QUESTION:
            self.state = InterviewState.WAIT_FOR_ANSWER

        elif self.state == InterviewState.WAIT_FOR_ANSWER:
            self.state = InterviewState.EVALUATE

        elif self.state == InterviewState.EVALUATE:
            if len(self.history) >= 3:
                self.state = InterviewState.END
            else:
                self.state = InterviewState.ASK_QUESTION
    def ask_question(self):
        question = QUESTIONS[len(self.history)]
        self.current_question = question
        return question["question"]

    def submit_answer(self, answer: str):
        self.history.append({
            "question": self.current_question,
            "answer": answer
        })
        expected = self.current_question["expected_concepts"]
        detector = ConceptDetector(expected)
        found_concepts = detector.detect_concepts(answer)
        missing_concepts = set(expected) - found_concepts
        self.history[-1]["found_concepts"] = list(found_concepts)
        self.history[-1]["missing_concepts"] = list(missing_concepts)