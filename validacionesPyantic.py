from pydantic import BaseModel, ValidationError, field_validator, Field
from fastapi import FastAPI
from typing import Optional, Annotated, Any



class User(BaseModel):
    username: str = Field(min_length=4, max_length=50)
    password: str
    email: str
    age: Optional[int]= None
    
    @field_validator('username')
    def username_length(cls, username):
        if len(username)<4:
            raise ValueError('La longitud mínima es 4')
        if len(username)>50:
            raise ValueError('La longitud máxima es 50')
        return username

        
user = User(username='Lino', password='1234',email='linobenavidesgabaldon@gmail.com')
user2 = User(username='Lino', password='1234',email='linobenavidesgabaldon@gmail.com', age=2)



print("User: ", user)
print("User2: ", user2)

try:
    user3 = User(username="Lino", password="1234")
except ValidationError as e:
    print(e.json())

try:
    user4 = User(username="Alí", password="1234", email='linobenavidesgabaldon@gmail.com')
except ValidationError as e:
    print(e.json())

try:
    user4 = User(username="jhbdhgbvsvdfytsabdhiufhdsnjopirthnsewiufhbndiujnfi9pdfgfgfdhfhfghndsfgjmhjgfdhbfhe", password="1234", email='linobenavidesgabaldon@gmail.com')
except ValidationError as e:
    print(e.json())


class Item(BaseModel):
    name: str
    desciption: str | None= None
    price: float
    tax: float | None= None
    tags = list[str] = []

app = FastAPI()

@app.post("/items/")
async def create_item(item : Item):
    return item


@app.post("/items/{item_id}")
async def update_item(item_id : int, item: Item, user : User):
    results = {"item_id" : item_id, "item": item, "user": user}
    return results

"""
@app.put("/items/{item_id}")
async def update_item( item_id: Annotated(int, Path(title="ID del item", ge=0, LE=1000)], q: str | None = None, item = Item | None =  None,):
    results = {"item_id": item_id}
    if q: 
        results = ({"q": q})
    if item:
        results.update({"item_id": item})
        return results
"""

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    resuls = {"item_id": item_id, "item": item, "user": user}
    return resuls


@app.post("/items/")
async def read_item(item : Item) ->list[Item]:
    return [
        Item(name= "Portal Gun" , price= 42.0),
        Item(name= "Plumbus" , price= 32.0)

    ]
   

@app.post("/items/")
async def read_item(item : Item) -> Any:
    return [
        Item(name= "Portal Gun" , price= 42.0),
        Item(name= "Plumbus" , price= 32.0)

    ]












