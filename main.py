from fastapi import Depends, FastAPI, Query, Request
from utils.embeddings import VectorStore
from core.lifespan import lifespan
from utils.rag_pipeline import generate_answer

def get_extractor(req: Request):
    return req.app.state.sent

app = FastAPI(lifespan=lifespan)

@app.get('/')
def root_utl(extractor: VectorStore = Depends(get_extractor)):
    result = extractor.getembeddings()
    print(result)
    return {"message": "Got runned", "emeddings": "done"}


@app.get('/ask')
def ask_question(question: str = Query('...', description="Ask question"), extractor: VectorStore = Depends(get_extractor)):
    retrieved_docs = extractor.search(question)
    context = " ".join(retrieved_docs)
    answer = generate_answer(context, question)
    return {"query": question, "context": retrieved_docs, "answer": answer}
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)