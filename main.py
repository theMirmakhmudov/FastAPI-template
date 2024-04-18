from typing import Optional

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()
templates = Jinja2Templates(directory="templates")

context = \
    [{"name": "Abdulmajid", "direction": "Front-end && Back-end"}, {"name": "Diyorbek", "direction": "Back-end Python"}]

data = {
    "name": "Abdulmajid",
    "direction": "Front-end && Back-end"
}


@app.get("/")
async def root(request: Request):
    #  return templates.TemplateResponse("index.html", {"request": request, "data": context})
    return data


@app.post("/items/")
async def create_item(item: Item):
    return item


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, )
