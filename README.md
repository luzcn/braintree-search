## Braintree search example

### How to use
- start server
```
 env FLASK_APP=app.py flask run

```

- send request
```
curl -G -d "id=hrmeg0ts" http://127.0.0.1:5000
 
```

### Heroku setup
- create the Heroku Procfile
```shell
touch Procfile
```
- Add the process type and command
```
web: gunicorn app:app
```
