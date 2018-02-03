# Info

Methods for schedule subject CRUD.

# Methods

## GET /api/schedule_subjects

List all of the subjects.

### Request headers

Name | Description | Example
--- | --- | ---
**Authorization** | token received on register or login | Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97

### Response fields

Name | Description
--- | ---
**id** | subject id
**title** | subject title

### Example request

```
curl -X GET \
  https://school-1329-server.appspot.com/api/schedule_subjects \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97'
```

### Example response
```
[
    {
        "id": 1,
        "title": "English"
    }
]
```

## POST /api/schedule_subjects

Create new subject.

### Request headers

Name | Description | Example
--- | --- | ---
**Authorization** | token received on register or login | Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97

### Requests fields

Name | Description
--- | ---
**title** | subject title


### Response fields

Name | Description
--- | ---
**id** | subject id
**title** | subject title


### Example request

```
curl -X POST \
  https://school-1329-server.appspot.com/api/schedule_subjects \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97' \
  -H 'content-type: application/json' \
  -d '{
    "title": "English"
    }'
```

### Example response
```
{
    "id": 1,
    "title": "English"
}
```

## PUT /api/schedule_subjects/{id}

Update subject with {id}.

### Request headers

Name | Description | Example
--- | --- | ---
**Authorization** | token received on register or login | Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97

### Requests fields

Name | Description
--- | ---
**title** | subject title

### Response fields

Name | Description
--- | ---
**id** | subject id
**title** | subject title

### Example request

```
curl -X PUT \
  https://school-1329-server.appspot.com/api/schedule_subjects/1 \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97' \
  -H 'content-type: application/json' \
  -d '{
    "title": "English 2"
    }'
```

### Example response
```
{
    "id": 1,
    "title": "English 2"
}
```

## DELETE /api/schedule_subjects/{id}

Delete subject with {id}.

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
  https://school-1329-server.appspot.com/api/schedule_subjects/1 \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97' \
```

### Example response

```
{
    "success": true
}
```