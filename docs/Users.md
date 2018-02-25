# Info

Methods for registration code creation and user registration.

# Methods

## POST /api/users/create_code

Create registration code with given date and level.

### Request fields

Name | Description
--- | ---
**expiration_date** | expiration date in UTC, should be greater than current date
**level** | code level (1 - student, 2 - teacher)

### Response fields

Name | Description
--- | ---
**code** | registration code value generated randomly

### Example request

```
curl -X POST https://school-1329.herokuapp.com/api/users/create_code \
  -F expiration_date=2017-12-18T12:00:00 \
  -F level=1
```

### Example response 
```
{
    "code": "HGy2LdYN"
}
```

## POST /api/users/check_code

Check registration code by given value and level.

### Request fields

Name | Description
--- | ---
**level** | code level (1 - student, 2 - teacher)
**code** | registration code value

### Response fields

Name | Description
--- | ---
**correct** | true if code is correct, false otherwise

### Example request
```
curl -X POST https://school-1329.herokuapp.com/api/users/check_code \
  -F code=HGy2LdYN \
  -F level=1
```

### Example response
```
{
    "correct": true
}
```

## POST /api/users/register

Validate registration code and level, create user with username and password.

### Request fields

Name | Description
--- | ---
**level** | user level (1 - student, 2 - teacher)
**code** | registration code value
**username** | user name
**password** | user password
**fcm_token** | FCM token

### Response fields 

Name | Description
--- | ---
**token** | token used in any user related request

### Example request
```
curl -X POST https://school-1329.herokuapp.com/api/users/register \
  -F level=1 \
  -F code=HGy2LdYN \
  -F username=poty \
  -F password=sam
```

### Example response
```
{
    "token": "b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97"
}
```

## POST /api/users/login

Validate username and password, return user token.

### Request fields

Name | Description
--- | ---
**username** | user name
**password** | user password
**fcm_token** | FCM token

### Response fields

Name | Description
--- | ---
**token** | token used in any user related request

### Example request
```
curl -X POST https://school-1329.herokuapp.com/api/users/login \
  -F username=poty \
  -F password=sam
```

### Example response
```
{
    "token": "b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97"
}
```