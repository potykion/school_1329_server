# Info

Methods for group CRUD and user adding to groups.

# Methods

## GET /api/groups

List all of the groups.

### Request headers

Name | Description | Example
--- | --- | ---
**Authorization** | token received on register or login | Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97

### Response fields

Name | Description
--- | ---
**id** | group id
**title** | group title

### Example request

```
curl -X GET \
  https://school-1329-server.appspot.com/api/groups \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97'
```

### Example response
```
[
    {
        "id": 1,
        "title": "Sample group"
    }
]
```

## POST /api/groups

Create new group.

### Request headers

Name | Description | Example
--- | --- | ---
**Authorization** | token received on register or login | Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97

### Requests fields

Name | Description
--- | ---
**title** | group title

### Response fields

Name | Description
--- | ---
**id** | group id
**title** | group title

### Example request

```
curl -X POST https://school-1329-server.appspot.com/api/groups \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97' \
  -F 'title=Sample group'
```

### Example response
```
{
    "id": 1,
    "title": "Sample group"
}
```


## PUT /api/groups/{id}

Update group with {id}.

### Request headers

Name | Description | Example
--- | --- | ---
**Authorization** | token received on register or login | Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97

### Requests fields

Name | Description
--- | ---
**title** | group title

### Response fields

Name | Description
--- | ---
**id** | group id
**title** | group title

### Example request

```
curl -X PUT https://school-1329-server.appspot.com/api/groups/1 \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97' \
  -F title=Sam
```

### Example response
```
{
    "id": 1,
    "title": "Sam"
}
```

## DELETE /api/groups/{id}

Delete group with {id}.

### Request headers

Name | Description | Example
--- | --- | ---
**Authorization** | token received on register or login | Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97

### Example request

```
curl -X DELETE https://school-1329-server.appspot.com/api/groups/1 \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97'
```

### Example response

Response contains nothing, but status code is 204 No Content.


## POST /api/groups/{id}/add_user

Add token-user to group with {id}.

### Request headers

Name | Description | Example
--- | --- | ---
**Authorization** | token received on register or login | Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97

### Response fields

Name | Description
--- | ---
**success** | true if user is successfully added to group

### Example request

```
curl -X POST \
  https://school-1329-server.appspot.com/api/groups/1/add_user \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97'
```

### Example response
```
{
    "success": true
}
```
