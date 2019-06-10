# product-api-example

Run using docker-compose:

```
docker-compose up -d
docker-compose exec product_api bash
```

Install the dependencies:

```
pip install -r requirements.txt
```

Run the API:

```
python product_api.py
```

Now is it possible to access the endpoints (e.g. http://localhost:8082/products)

## Validate consumer contract

Run pact-verifier for the latest version:

```
pact-verifier --provider-base-url http://<product_endpoint> --pact-url http://<pact_broker_url>/pacts/provider/Product/consumer/Checkout/latest
```

Run pact-provider for a specific version:

```
pact-verifier --provider-base-url http://<product_endpoint> --pact-url http://<pact_broker_url>/pacts/provider/Product/consumer/Checkout/version/<version>
```

Publish provider results:

```
pact-verifier --provider-base-url http://<product_endpoint> --pact-url http://<pact_broker_url>/pacts/provider/Product/consumer/Checkout/latest --provider-app-version <provider-version> --publish-verification-results
```


