from fastapi import FastAPI
import httpx 
from bs4 import BeautifulSoup
from pydantic import BaseModel
from typing import List



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/prices")  
async def read_prices():
    url = str("https://carbu.com/belgie//index.php/bestPrice/Oost-Vlaanderen/BE_foi/1")
    return url
    #resp = httpx.get(url)
    #soup = BeautifulSoup('features="html.parser"')  

    #print(resp)
    #print(soup)
    


