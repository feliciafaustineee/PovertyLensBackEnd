from fastapi import FastAPI
from app.utils import get_all_data, get_region, search_region

app = FastAPI()


@app.get("/")
def root():
    return {"message": "PovertyLens API is running"}


@app.get("/map")
def map_data():
    return get_all_data()


@app.get("/region")
def region(name: str):
    return get_region(name)


@app.get("/search")
def search(q: str):
    return search_region(q)

# kalo mau cobain
# di terminal ketik ini
# .\.venv\Scripts\Activate.ps1
# .\.venv\Scripts\python.exe -m pip install fastapi uvicorn
# .\.venv\Scripts\python.exe -m uvicorn main:app --reload
# buka link http nya (http://127.0.0.1:8000/docs)

# testnya
# /map -> try it out -> execute 
# /region -> ketik (cth: aceh, nias) -> execute
# /search -> ketik (cth: aceh, nias) -> execute