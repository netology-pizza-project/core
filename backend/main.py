import os
import uuid
from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse, FileResponse
from sqlalchemy import create_engine
import psycopg2


conn = psycopg2.connect(dbname="postgres", user="postgres", password="<PASSWORD>", host="localhost", port="5432")

cursor = conn.cursor()
cursor.execute("""SELECT 
                    product_id, 
                    product_title, 
                    product_description, 
                    product_image, 
                    product_is_new, 
                    product_price 
                FROM products
                WHERE product_available is TRUE""")

print(cursor.fetchall())
product_list = cursor.fetchall()

cursor.close()
conn.close()


app = FastAPI()


@app.get("/")
# цикл, который собирает из БД все пиццы и возвращает json
async def root():

    return {"message": "Hello World"
            }


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
