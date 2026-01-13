from fastapi import APIRouter
import uuid
from core.session import InterviewSession

router = APIRouter(prefix="/interview")

SESSIONS = {}

@router.post("/start")
def start_interview():
    interview_id = str(uuid.uuid4())
    session = InterviewSession(interview_id)
    SESSIONS[interview_id] = session

    session.next_state()
    question = session.ask_question()
    session.next_state()

    return {
        "interview_id": interview_id,
        "question": question
    }

@router.post("/answer")
def submit_answer(payload: dict):
    interview_id = payload["interview_id"]
    answer = payload["answer"]

    session = SESSIONS[interview_id]
    session.submit_answer(answer)
    session.next_state()  # EVALUATE
    session.next_state()  # ASK NEXT or END

    if session.state.name == "END":
        return {"message": "Interview ended"}

    question = session.ask_question()
    session.next_state()

    return {"question": question}