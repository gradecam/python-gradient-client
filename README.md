# GradeCam Gradient Sample Client

Provides a basic example of how to interact with GradeCam Gradient
through the integration API. The API can be used to perform rostering
programmatically.

## Getting a Client

```py
from gradient import factory

client = factory('https://app-int.gradecam.com', 'DEMO', 'cacd79fbb7524fbc93c468f51f7564b5')
```

## Create/Update some a Term

```py
terms = [
    {"id": "1", "name": "Fall 2022-2023", "start_date": "2022-08-01", "end_date": "2022-12-20" },
    {"id": "2", "name": "Winter 2022-2023", "start_date": "2023-01-04", "end_date": "2023-04-15" },
]
client.post(terms, 'terms')
```

## Retrieve a Term

```py
client.get('terms', '1')
```
