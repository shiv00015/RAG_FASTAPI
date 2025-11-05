from fastapi import Depends, FastAPI, Query, Request, Response, HTTPException
from utils.embeddings import VectorStore
from core.lifespan import lifespan
from utils.gemini_rag_pipeline import GeminiService
from utils.rag_pipeline import generate_answer
from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str
    
class AppStates(BaseModel):
    sent: object
    gemini: object


def get_extractor(req: Request):
    return req.app.state


app = FastAPI(lifespan=lifespan)


@app.get("/")
def root_utl(extractor: VectorStore = Depends(get_extractor)):
    result = extractor.getembeddings()
    print(result)
    return {"message": "Got runned", "emeddings": "done"}


@app.post("/login")
def login_app(res: Response, login: Login):

    login.usernam
    print(type(login))


@app.get("/ask")
async def ask_question(
    req: Request,
    question: str = Query("...", description="Ask question"),
    extractor: AppStates = Depends(get_extractor),
):
    # print('state gemini', extractor.gemini)
    # _gemini = req.state.gemini
    try:
        retrieved_docs = extractor.sent.search(question)
        context = " ".join(retrieved_docs)
        prompt = f"""You are an assistant that answers based only on the context. Context: {context} Question: {question} Answer:"""
        print("prompt", prompt)
        print('extractor', extractor)
        answer =  await extractor.gemini.analyze_doc(prompt=prompt)
        # answer = generate_answer(context, question)
        return {"query": question, "answer": answer}
            
    except Exception as e:
        print('Exception', e)
        return HTTPException(detail="error", status_code="500")


if __name__ == "__main__":
    
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
