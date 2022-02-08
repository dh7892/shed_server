from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

HEATER=True
LIGHT=False

class Heater(BaseModel):
    on: bool

class Light(BaseModel):
    on: bool

@app.get("/heater")
async def heater_get():
    heater = Heater(on=HEATER)
    return heater

@app.put("/heater")
async def heater_put(heater: Heater):
    global HEATER
    HEATER = heater.on
    return heater

@app.get("/light")
async def light_get():
    light = Light(on=LIGHT)
    return light

@app.put("/light")
async def light_put(light: Light):
    global LIGHT
    LIGHT = light.on
    return light