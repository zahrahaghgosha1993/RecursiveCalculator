# Calculator

## describtion:
a restful web service for calculate recursive function.

## installation With docker-compose:

```bash
docker-compose up
```

## installation:

* Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirement.

```bash
pip install -r requirements
```
* config redis in get_redis_client file
* run project by execute api.py
```bash
python app/api.py
```
## sample

```bash
curl --location --request POST 'http://127.0.0.1:5000/recursive_calculator/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "n":100,
    "function": "Fibonacci"
}'
```
implemented function: 
* Fibonacci
* Factorial
* Ackerman
