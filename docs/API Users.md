# Info

Methods for registration code creation and user registration.

# Methods

## /api/users/create_code

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
curl -X POST https://school-1329-server.appspot.com/api/users/create_code -F expiration_date=2017-12-18T12:00:00 -F level=1
```

### Example response 
```
{
    "code": "HGy2LdYN"
}
```
## /api/users/check_code

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
curl -X POST https://school-1329-server.appspot.com/api/users/check_code -F code=HGy2LdYN -F level=1
```

### Example response
```
{
    "correct": true
}
```

## /api/users/register

Validate password value and level, create user with username on success.

### Request fields

Name | Description
--- | ---
**password_value** | password value
**level** | user level (1 - student, 2 - teacher)
**username** | user name

### Response fields 

Name | Description
--- | ---
**username** | user name
**level** | user level (1 - student, 2 - teacher) 

### Example request
```
curl -X POST https://school-1329-server.appspot.com/api/users/register -F password_value=HGy2LdYN -F level=1 -F username=pocan
```

### Example response
```
{
    "username": "pocan",
    "level": 1
}
```
