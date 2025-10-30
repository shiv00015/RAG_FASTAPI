import aiofiles

def readFIle():
    with open('knowledge.txt', 'r') as f:
        print([line.strip() for line in f.readlines() if line.strip()])
        

# async def load_file():
#     async with aiofiles.open('knowledge.txt', 'r') as f:
#         docs = [line.strip() for line in await f.read() if line.strip()]
#         print('life')
#         print(docs)
        
# if __name__ == "__main__":
#     await load_file()