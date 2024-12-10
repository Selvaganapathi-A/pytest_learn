from decimal import Decimal

from fastapi import FastAPI

app: FastAPI = FastAPI(title='Temperature')


@app.get('/')
def home():
    return {'about': 'convert temperature'}


@app.get('/celsius/{value}')
def to_celsius(value: Decimal):
    arg: Decimal = ((value - 32) * 5) / 9
    return {'celsius': arg.quantize(Decimal('1.00'))}


@app.get('/farenheight/{value}')
def to_farenheight(value: Decimal):
    arg: Decimal = ((value * 9) / 5) + 32
    return {'farenheight': arg.quantize(Decimal('1.00'))}


"""

uvx uvicorn app.package_01.script_03:app

python -m uvicorn app.package_01.script_03:app

"""
