import json
import os
import uuid
from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse, FileResponse
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


product_list = cursor.fetchall()
print(product_list)

cursor.close()
conn.close()

result = {}
for i in product_list:
    result[i[0]] = {"product_title": i[1],
                    "product_description": i[2],
                    "product_image": i[3],
                    "product_is_new": i[4],
                    "product_price": i[5]}


app = FastAPI()


@app.get("/")
async def root():

    return json.dumps(result, ensure_ascii=False)


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
