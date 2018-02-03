# About

School 1329 Server is used for registration code generation, user registration, events creation and more.

API requirements can be found [here](https://docs.google.com/document/d/1U416C0ZFSe9_fd1c0a17ZRZ5n9iF6L5hXCzhCVqJKSE/edit?usp=sharing).

**Base url:** https://school-1329-server.appspot.com

# Authorization

Most of the endpoints require authorization (e.g. [/api/groups/{id}/add_user](https://github.com/potykion/school_1329_server/wiki/Groups#post-apigroupsidadd_user)).


To make calls to such endpoints you need to pass authorization header containing user token:
```
Authorization: Token b140fc2e09e618dd7f5d2cad6ccdc587c80e8a97
```

To receive user token see [/api/users/register](https://github.com/potykion/school_1329_server/wiki/Users#post-apiusersregister) and [/api/users/login](https://github.com/potykion/school_1329_server/wiki/Users#post-apiuserslogin) endpoints.


# Methods

## Users

Methods for registration code creation and user registration.

- [POST /api/users/create_code](https://github.com/potykion/school_1329_server/wiki/Users#post-apiuserscreate_code) - Create registration code with given date and level.
- [POST /api/users/check_code](https://github.com/potykion/school_1329_server/wiki/Users#post-apiuserscheck_code) - Check registration code by given value and level.
- [POST /api/users/register](https://github.com/potykion/school_1329_server/wiki/Users#post-apiusersregister) - Validate registration code and level, create user with username and password.
- [POST /api/users/login](https://github.com/potykion/school_1329_server/wiki/Users#post-apiuserslogin) - Validate username and password, return user token.


## Groups

Methods for group CRUD and user adding to groups.

- [GET /api/groups](https://github.com/potykion/school_1329_server/wiki/Groups#get-apigroups) - List all of the groups.
- [POST /api/groups](https://github.com/potykion/school_1329_server/wiki/Groups#post-apigroups) - Create new group.
- [PUT /api/groups/{id}](https://github.com/potykion/school_1329_server/wiki/Groups#put-apigroupsid) - Update group with {id}.
- [DELETE /api/groups/{id}](https://github.com/potykion/school_1329_server/wiki/Groups#delete-apigroupsid) - Delete group with {id}.
- [POST /api/groups/{id}/add_user](https://github.com/potykion/school_1329_server/wiki/Groups#post-apigroupsidadd_user) - Add token-user to group with {id}.
- [POST /api/groups/{id}/remove_user](https://github.com/potykion/school_1329_server/wiki/Groups#post-apigroupsidremove_user) - Remove token-user to group with {id}.
- [GET /api/groups/user_groups](https://github.com/potykion/school_1329_server/wiki/Groups#get-apigroupsuser_groups) - List token-user groups.
- [GET /api/groups/{id}/users](https://github.com/potykion/school_1329_server/wiki/Groups#get-apigroupsidusers) - List users from group with {id}.
- [GET /api/groups/{id}/events](https://github.com/potykion/school_1329_server/wiki/Groups#get-apigroupsidevents) - List group with {id} events.


## Events

Methods for events CRUD.

- [GET /api/events](https://github.com/potykion/school_1329_server/wiki/Events#get-apievents) - List all of the events.
- [POST /api/events](https://github.com/potykion/school_1329_server/wiki/Events#post-apievents) - Create new event.
- [PUT /api/events/{id}](https://github.com/potykion/school_1329_server/wiki/Events#put-apieventsid) - Update event with {id}.
- [DELETE /api/events/{id}](https://github.com/potykion/school_1329_server/wiki/Events#delete-apieventsid) - Delete event with {id}.
- [GET /api/events/user_events](https://github.com/potykion/school_1329_server/wiki/Events#get-apieventsuser_events) - List user events.

## Event Comments

Methods for event comments CRUD.

- [GET /api/event_comments](https://github.com/potykion/school_1329_server/wiki/Event-Comments#get-apievent_comments) - List event comments.
- [POST /api/event_comments](https://github.com/potykion/school_1329_server/wiki/Event-Comments#post-apievent_comments) - Create new event comment.
- [DELETE /api/event_comments/{id}](https://github.com/potykion/school_1329_server/wiki/Event-Comments#delete-apieventsid) - Delete event comment with {id}.






