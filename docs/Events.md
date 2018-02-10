# Info

Methods for event comments CRUD.

# Methods

## GET /api/events

List all of the events.

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
  https://school-1329.herokuapp.com/api/events \
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

## POST /api/events

Create new event.

### Request headers

Name | Description | Example
--- | --- | ---
**Authorization** | token received on register or login | Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97

### Requests fields

Name | Description
--- | ---
**title** | event title
**place** | event place
**description** | event description (optional)
**participation_groups** | list of group ids that participate in the event
**start_date** | event start date in UTC
**end_date** | event end date in UTC (optional)

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
curl -X POST \
  https://school-1329.herokuapp.com/api/events \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97' \
  -H 'content-type: application/json' \
  -d '{
    "title": "Sample event",
    "place": "School",
    "participation_groups": [1],
    "start_date": "2018-03-08T12:00Z"
}'
```

### Example response
```
{
    "id": 1,
    "title": "Sample event",
    "place": "School",
    "description": "",
    "participation_groups": [
        1
    ],
    "created_by": "poty",
    "start_date": "2018-03-08T12:00:00Z",
    "end_date": null
}
```


## PUT /api/events/{id}

Update event with {id}.

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
**title** | event title
**place** | event place
**description** | event description (optional)
**participation_groups** | list of group ids that participate in the event
**start_date** | event start date in UTC
**end_date** | event end date in UTC (optional)

### Example request

```
curl -X PUT \
  https://school-1329.herokuapp.com/api/events/1 \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97' \
  -H 'content-type: application/json' \
  -d '{
    "title": "Sample event",
    "place": "School 1329",
    "participation_groups": [],
    "start_date": "2018-03-08T12:00Z"
}'
```

### Example response
```
{
    "id": 1,
    "title": "Sample event",
    "place": "School 1329",
    "description": "",
    "participation_groups": [],
    "created_by": "poty",
    "start_date": "2018-03-08T12:00:00Z",
    "end_date": null
}
```

## DELETE /api/events/{id}

Delete event with {id}.

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
  https://school-1329.herokuapp.com/api/events/1 \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97' \
```

### Example response

```
{
    "success": true
}
```

## GET /api/events/user_events

List user events.

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
  https://school-1329.herokuapp.com/api/events/user_events \
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