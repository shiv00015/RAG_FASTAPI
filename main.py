from fastapi import Depends, FastAPI, Query, Request, Response, HTTPException, UploadFile, File
from tools.extractContent import ExtractContent
from utils.embeddings import VectorStore
from core.lifespan import lifespan
from utils.gemini_rag_pipeline import GeminiService
from utils.rag_pipeline import generate_answer
from pydantic import BaseModel


# class Login(BaseModel):
#     username: str
#     password: str
    
class AppStates(BaseModel):
    sent: object
    gemini: object


def get_extractor(req: Request):
    return req.app.state


# app = FastAPI(lifespan=lifespan)
app = FastAPI()


@app.get("/")
def root_utl(extractor: VectorStore = Depends(get_extractor)):
    result = extractor.getembeddings()
    print(result)
    return {"message": "Got runned", "emeddings": "done"}


# @app.post("/login")
# def login_app(res: Response, login: Login):
#     login.usernam
#     print(type(login))
    

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        extract = ExtractContent(contents=contents, filename=file.filename)
        texts = extract.extractor()
        app.state.gemini = GeminiService()
        app.state.sent = VectorStore(texts)
        return "Uploaded"
    except Exception as e:
        raise HTTPException(status_code="500", detail=e)
     


@app.get("/ask")
async def ask_question(
    question: str = Query("...", description="Ask question"),
    extractor: AppStates = Depends(get_extractor),
):
    try:
        retrieved_docs = extractor.sent.search(question, 6)
        context = " ".join(retrieved_docs)
        prompt = f"""You are an assistant that answers based only on the context. 
        Context: {context} Question: {question}, 
        please give answer in correct proper explaination where user can understatnd.
        
        note - don't add context in answer 
        role - you are best qna model.
        """
        answer =  await extractor.gemini.analyze_doc(prompt=prompt)
        # answer = generate_answer(context, question)
        return {"query": question, "answer": answer}
            
    except Exception as e:
        print('Exception', e)
        return HTTPException(detail="error", status_code="500")


if __name__ == "__main__":
    
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
