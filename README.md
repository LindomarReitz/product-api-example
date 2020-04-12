# product-api-example

Change the env `PACT_BROKER_URL`. If you want to use [PactFlow](https://pactflow.io/) change the env `PACT_BROKER_TOKEN`.

![Main workflow](https://github.com/LindomarReitz/product-api-example/workflows/Main%20workflow/badge.svg)

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

To use the env `PACT_BROKER_TOKEN` add the option `--pact-broker-token $PACT_BROKER_TOKEN`.

Run pact-verifier for the latest version:

```
pact-verifier --provider-base-url http://<product_endpoint> \
--pact-url $PACT_BROKER_URL/pacts/provider/Product/consumer/Checkout/latest
```

Run pact-provider for a specific version:

```
pact-verifier --provider-base-url http://<product_endpoint> \
--pact-url $PACT_BROKER_URL/pacts/provider/Product/consumer/Checkout/version/<version>
```

Publish provider results:

```
pact-verifier --provider-base-url http://<product_endpoint> \
--pact-url $PACT_BROKER_TOKEN/pacts/provider/Product/consumer/Checkout/latest \
--provider-app-version <provider-version> \
--publish-verification-results
```



