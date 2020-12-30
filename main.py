from typing import Optional
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os
import shutil
import ocr


app = FastAPI()

app.mount("/assets", StaticFiles(directory="assets"), name="assets")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("homepage.html", {"request":request} )
# def read_root():
    # return {"Hello": "World"}

# @app.get("/details/{name}/{city}/{gender}")
# def read_item(city: str,gender:str ,name: Optional[str] = None):
    # return {"kota": city, "jenis kelamin":gender ,"nama": name}

@app.post("/extract")
async def do_ocr(image: UploadFile = File(...)):
    temp_data = save_file_to_disk(image, path="temp", save_as="temp")
    convert = await ocr.read_image(temp_data)
    return {"filename": image.filename, "text": convert}

def save_file_to_disk(uploaded_data, path=".", save_as="default"):
    extension = os.path.splitext(uploaded_data.filename)[-1]
    temp_file = os.path.join(path, save_as + extension)
    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(uploaded_data.file, buffer)
    return temp_file
