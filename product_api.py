from bottle import get, request, run, response
import json

with open('fixtures/products.json') as f:
    data = json.load(f)

@get("/products")
def users():
    return dict(products=data)

@get("/products/<productId>")
def get_by_id(productId):
    for product in data:
        if int(productId) == product['id']:
            return product

    response.status = 404
    response.content_type = 'application/json'
    return json.dumps({'error': 'Product with id {productId} not found!'.format(productId=productId)})

run(reloader=True, host='0.0.0.0', port=8082)