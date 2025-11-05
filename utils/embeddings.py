from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class VectorStore:
    def __init__(self, data):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.docs = data
        self.embeddings = self.model.encode(data)
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(np.array(self.embeddings))

    def search(self, query, top_k=3):
        query_vector = self.model.encode([query])
        _, indices = self.index.search(np.array(query_vector), top_k)
        return [self.docs[i] for i in indices[0]]
    
    def getembeddings(self):
        return self.embeddings
    
    def getindexembeddings(self):
        return self.index