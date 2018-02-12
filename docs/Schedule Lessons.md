# Info

Methods for schedule lessons CRUD and schedule listing.

# Methods

## POST /api/schedule_lessons

Create new schedule lesson.

### Request headers

Name | Description | Example
--- | --- | ---
**Authorization** | token received on register or login | Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97

### Requests fields

Name | Description
--- | ---
**start_time** | lesson start time (hours and minutes)
**end_time** | (optional) lesson end time (hours and minutes), if not provided them it equals to start time + lesson duration (45 minutes)
**weekday** | lesson weekday (1 - monday, 2 - tuesday, etc.)
**groups** | list of lesson groups
**subject** | lesson subject
**place** | lesson place

### Response fields

Name | Description
--- | ---
**id** | subject lesson id
**start_time** | lesson start time (hours and minutes)
**end_time** | lesson end time (hours and minutes)
**weekday** | lesson weekday (1 - monday, 2 - tuesday, etc.)
**groups** | list of lesson groups
**subject** | lesson subject
**teacher** | lesson teacher username
**place** | lesson place

### Example request

```
curl -X POST \
  https://school-1329.herokuapp.com/api/schedule_lessons \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97' \
  -H 'content-type: application/json' \
  -d '{
    "start_time": "12:00",
    "weekday": 1,
    "groups": [1],
    "subject": 1,
    "place": "wkola"
    }'
```

### Example response
```
{
    "id": 1,
    "place": "wkola",
    "start_time": "12:00",
    "end_time": "12:45",
    "weekday": 1,
    "groups": [1],
    "subject": 1,
    "teacher": "poty"
}
```

## PUT /api/schedule_lessons/{id}

Update schedule lesson with {id}.

### Request headers

Name | Description | Example
--- | --- | ---
**Authorization** | token received on register or login | Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97

### Requests fields

Name | Description
--- | ---
**start_time** | lesson start time (hours and minutes)
**end_time** | (optional) lesson end time (hours and minutes), if not provided them it equals to start time + lesson duration (45 minutes)
**weekday** | lesson weekday (1 - monday, 2 - tuesday, etc.)
**groups** | list of lesson groups
**subject** | lesson subject
**place** | lesson place

### Response fields

Name | Description
--- | ---
**id** | subject lesson id
**start_time** | lesson start time (hours and minutes)
**end_time** | lesson end time (hours and minutes)
**weekday** | lesson weekday (1 - monday, 2 - tuesday, etc.)
**groups** | list of lesson groups
**subject** | lesson subject
**teacher** | lesson teacher username
**place** | lesson place

### Example request

```
curl -X PUT \
  https://school-1329.herokuapp.com/api/schedule_lessons/1 \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97' \
  -H 'content-type: application/json' \
  -d '{
    "start_time": "13:00",
    "weekday": 2,
    "groups": [1],
    "subject": 1,
    "place": "wkola2"
    }'
```

### Example response
```
{
    "id": 1,
    "place": "wkola2",
    "start_time": "13:00",
    "end_time": "13:45",
    "weekday": 2,
    "groups": [1],
    "subject": 1,
    "teacher": "poty"
}
```

## DELETE /api/schedule_lessons/{id}

Delete subject lesson with {id}.

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
  https://school-1329.herokuapp.com/api/schedule_lessons/1 \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97' \
```

### Example response

```
{
    "success": true
}
```

## GET /api/schedule_lessons/user_schedule

List user schedule.

### Request headers

Name | Description | Example
--- | --- | ---
**Authorization** | token received on register or login | Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97

### Response fields

Response is dictionary where key is weekday (1 - monday, 2 - tuesday, etc.) and value is lesson with following fields:

Name | Description
--- | ---
**id** | lesson id
**teacher** | lesson teacher username
**subject** | lesson subject title
**start_time** | lesson start time
**end_time** | lesson end time
**place** | lesson place

### Example request

```
curl -X GET \
  https://school-1329.herokuapp.com/api/schedule_lessons/user_schedule \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97'
```

### Example response
```
{
    "1": [
        {
            "id": 1,
            "start_time": "12:00",
            "end_time": "12:45",
            "subject": "Русский",
            "teacher": "poty",
            "place": "wkola"
        }
    ],
    "2": [],
    "3": [],
    "4": [],
    "5": [],
    "6": [],
    "7": []
}
```
