from fastapi import FastAPI
from mylib.arithmetic import add
import uvicorn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


app = FastAPI()

class Addition(BaseModel):
    firstNumber: int
    secondNumber: int

@app.post("/addition")
async def scrape_story(addition: Addition):
    result = add(firstNumber=addition.firstNumber,secondNumber=addition.secondNumber)
    payload = {"additionpage": f"The sum of {addition.firstNumber} and {addition.secondNumber} is {result}"}
    json_compatible_item_data = jsonable_encoder(payload)
    return JSONResponse(content=json_compatible_item_data)

@app.get("/")
async def root():
    return {"message": "Hello Functions"}
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Duke"}

@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together"""

    total = add(num1 ,num2)
    return {"total": total}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')