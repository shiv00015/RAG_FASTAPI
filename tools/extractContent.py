from PyPDF2 import PdfReader
import docx

class ExtractContent:
    def __init__(self, **kwargs: dict):
        self.contents = kwargs.get("contents")
        self.filename = kwargs.get("filename")
    
    def __getBytesIO(self):
        from io import BytesIO
        return BytesIO(self.contents)
        
    def __pdfextract(self):
        pdf =  PdfReader(self.__getBytesIO())
        text = []
        
        for page in pdf.pages:
            for line in page.extract_text().splitlines():
                if line.strip():
                    text.append(line.strip()) 
        return text
    
    def __docextract(self):
        document = docx.Document(self.__getBytesIO())
        text = []
        for para in document.paragraphs:
            if para.text.strip():
                    text.append(para.text.strip())
        return text
    
    def __txtextract(self):
        texts = self.contents.decode("utf-8")
        docs = [line.strip() for line in texts.splitlines() if line.strip()]
        return docs
        
    def extractor(self, **kwargs):
        if self.filename.endswith(".pdf"):
            text = self.__pdfextract()
        elif self.filename.endswith('.docx'):
            text = self.__docextract()
        elif self.filename.endswith(".txt"):
            text = self.__txtextract()
        return text