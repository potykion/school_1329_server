# Info

Methods for groups CRUD and user adding to groups.

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

### Response fields

Name | Description
--- | ---
**success** | true if group is successfully deleted

### Example request

```
curl -X DELETE https://school-1329-server.appspot.com/api/groups/1 \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97'
```

### Example response

```
{
    "success": true
}
```

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

## POST /api/groups/{id}/remove_user

Remove token-user to group with {id}.

### Request headers

Name | Description | Example
--- | --- | ---
**Authorization** | token received on register or login | Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97

### Response fields

Name | Description
--- | ---
**success** | true if user is successfully removed to group

### Example request

```
curl -X POST \
  https://school-1329-server.appspot.com/api/groups/1/remove_user \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97'
```

### Example response
```
{
    "success": true
}
```

## GET /api/groups/user_groups

List token-user groups.

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
  https://school-1329-server.appspot.com/api/groups/user_groups \
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

## GET /api/groups/{id}/users

List users from group with {id}.

### Request headers

Name | Description | Example
--- | --- | ---
**Authorization** | token received on register or login | Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97

### Response fields

Name | Description
--- | ---
**username** | user name
**level** | user level (1 - student, 2 - teacher)

### Example request

```
curl -X GET \
  https://school-1329-server.appspot.com/api/groups/1/users \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97'
```

### Example response
```
[
    {
        "username": "poty",
        "level": 1
    }
]
```

## GET /api/groups/{id}/events

List group with {id} events.

### Request headers

Name | Description | Example
--- | --- | ---
**Authorization** | token received on register or login | Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97

### Response fields

Name | Description
--- | ---
**id** | event id
**title** | event title
**place** | event place
**description** | event description
**created_by** | username of event creator
**participation_groups** | list of group ids that participate in the event
**start_date** | event start date in UTC
**end_date** | event end date in UTC

### Example request

```
curl -X GET \
  https://school-1329-server.appspot.com/api/groups/1/events \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97'
```

### Example response
```
[
    {
        "id": 1,
        "title": "Sample event",
        "place": "School",
        "description": "",
        "created_by": "poty",
        "participation_groups": [
            1
        ],
        "start_date": "2018-03-08T12:00Z",
        "end_date": null
    }
]
```
