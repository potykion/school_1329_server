# Info

Methods for notifications CRUD.

# Methods

## POST /api/notifications

Create new notification.

### Request headers

Name | Description | Example
--- | --- | ---
**Authorization** | token received on register or login | Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97

### Requests fields

Name | Description
--- | ---
**text** | Notification text
**frequency** | Notification frequency in crontab-style (https://crontab.guru/)
**send_once** | If true notification is sending only once
**groups** | Notification target-groups

### Response fields

Name | Description
--- | ---
**id** | event id
**text** | Notification text
**frequency** | Notification frequency in crontab-style (https://crontab.guru/)
**send_once** | If true notification is sending only once
**groups** | Notification target-groups
**created_by** | Notification creator username

### Example request

```
curl -X POST \
  https://school-1329.herokuapp.com/api/notifications \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97' \
  -H 'content-type: application/json' \
  -d '{
    "text": "Sample notification",
    "frequency": "* * * * *",
    "send_once": true,
    "groups": [1]
}'
```

### Example response
```
{
    "id": 1,
    "text": "Sample notification",
    "frequency": "* * * * *",
    "groups": [1],
    "send_once": true,
    "created_by": "potykion"
}
```


## PUT /api/notifications/{id}

Update notification with {id}.

### Request headers

Name | Description | Example
--- | --- | ---
**Authorization** | token received on register or login | Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97

### Requests fields

Name | Description
--- | ---
**text** | Notification text
**frequency** | Notification frequency in crontab-style (https://crontab.guru/)
**send_once** | If true notification is sending only once
**groups** | Notification target-groups

### Response fields

Name | Description
--- | ---
**id** | event id
**text** | Notification text
**frequency** | Notification frequency in crontab-style (https://crontab.guru/)
**send_once** | If true notification is sending only once
**groups** | Notification target-groups
**created_by** | Notification creator username


### Example request

```
curl -X PUT \
  https://school-1329.herokuapp.com/api/notifications/1 \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97' \
  -H 'content-type: application/json' \
  -d '{
     "text": "Sample notification 2",
    "frequency": "5 * * * *",
    "send_once": false,
    "groups": [1]
}'
```

### Example response
```
{
    "id": 1,
    "text": "Sample notification 2",
    "frequency": "5 * * * *",
    "groups": [1],
    "send_once": false,
    "created_by": "potykion"
}
```

## GET /api/notifications/list_sent_notifications

List notification that already sent.

### Request headers

Name | Description | Example
--- | --- | ---
**Authorization** | token received on register or login | Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97

### Response fields

Name | Description
--- | ---
**id** | event id
**text** | Notification text
**frequency** | Notification frequency in crontab-style (https://crontab.guru/)
**send_once** | If true notification is sending only once
**groups** | Notification target-groups
**created_by** | Notification creator username


### Example request

```
curl -X GET \
  https://school-1329.herokuapp.com/api/notifications/list_sent_notifications \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97'
```

### Example response
```
[
    {
        "id": 1,
        "text": "Sample notification 2",
        "frequency": "5 * * * *",
        "groups": [1],
        "send_once": false,
        "created_by": "potykion"
    }
]
```

## GET /api/notifications/list_created_notifications

List notifications which created by user.

### Request headers

Name | Description | Example
--- | --- | ---
**Authorization** | token received on register or login | Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97

### Response fields

Name | Description
--- | ---
**id** | event id
**text** | Notification text
**frequency** | Notification frequency in crontab-style (https://crontab.guru/)
**send_once** | If true notification is sending only once
**groups** | Notification target-groups
**created_by** | Notification creator username


### Example request

```
curl -X GET \
  https://school-1329.herokuapp.com/api/notifications/list_created_notifications \
  -H 'authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97'
```

### Example response
```
[
    {
        "id": 1,
        "text": "Sample notification 2",
        "frequency": "5 * * * *",
        "groups": [1],
        "send_once": false,
        "created_by": "potykion"
    }
]
```