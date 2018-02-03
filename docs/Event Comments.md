# Info

Methods for event comments CRUD.

# Methods

## GET /api/event_comments

List event comments.

### Request headers

Name | Description | Example
--- | --- | ---
**Authorization** | token received on register or login | Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97

### Request fields

Name | Description
--- | ---
**event** | event id


### Response fields

Name | Description
--- | ---
**id** | comment id
**text** | comment text
**created_by** | username of comment creator
**created** | comment created date in UTC

### Example request

```
curl -X GET \
  https://school-1329-server.appspot.com/api/event_comments \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97' \
  -F event=1
```

### Example response
```
[
    {
        "id": 1,
        "text": "Sample comment",
        "created_by": "poty",
        "created": "2018-03-08T12:00Z"
    }
]
```

## POST /api/event_comments

Create new event comment.

### Request headers

Name | Description | Example
--- | --- | ---
**Authorization** | token received on register or login | Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97

### Requests fields

Name | Description
--- | ---
**text** | comment text
**event** | event id

### Response fields

Name | Description
--- | ---
**id** | comment id
**text** | comment text
**created_by** | username of comment creator
**created** | comment created date in UTC

### Example request

```
curl -X POST \
  https://school-1329-server.appspot.com/api/event_comments \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97' \
  -H 'content-type: application/json' \
  -d '{
    "text": "Sample text",
    "event": "1"
    }'
```

### Example response
```
{
    "id": 1,
    "text": "Sample text",
    "created_by": "poty",
    "created": "2018-01-28T17:59Z"
}
```

## DELETE /api/event_comments/{id}

Delete event comment with {id}.

### Request headers

Name | Description | Example
--- | --- | ---
**Authorization** | token received on register or login | Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97

### Response fields

Name | Description
--- | ---
**success** | true if event is successfully deleted

### Example request

```
curl -X DELETE \
  https://school-1329-server.appspot.com/api/event_comments/1 \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97' \
```

### Example response

```
{
    "success": true
}
```