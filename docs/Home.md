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
- [PUT /api/groups/{id}](https://github.com/potykion/school_1329_server/wiki/Groups#post-apigroups) - Update group with {id}.
- [DELETE /api/groups/{id}](https://github.com/potykion/school_1329_server/wiki/Groups#delete-apigroupsid) - Delete group with {id}.
- [POST /api/groups/{id}/add_user](https://github.com/potykion/school_1329_server/wiki/Groups#post-apigroupsidadd_user) - Add token-user to group with {id}.



