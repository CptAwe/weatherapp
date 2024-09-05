# Weather app

A simple app to exercise basic restAPI functionality using Python as the backend and MySQL as the database.

## Components

1. Python 3.12
2. MySQL 9.0

## Deployment

### Container

Recommended command: `docker compose up`

### Raw Instance

* Prerequisites:
    1. Python 3.12
    2. MySQL 9

1. Create a MySQL database using the [`DB.sql`](./DB.sql) script
1. Modify the [`.env`](./.env) file as see fit.
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment: `source .venv/bin/activate`
4. install all the necessary python modules: `pip install -r requirements.txt`
5. Run the test if necessary: `python src/test.py`
6. Run the app: `python src/app.py`

## Testing

To run the included unit tests simply run `src/test.py`

## TODOs

1. Dynamic role creation and assignment.
    * Use a separate `user_roles` table so that the roles can be edited on the fly
    * Use a separate `role_permissions` table so that the permissions of each role can by edited on the fly

2. Create a simple UI

## Notes

Leaving VScode `launch.json` for reference:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Tests",
      "type": "debugpy",
      "request": "launch",
      "program": "${workspaceFolder}/src/test.py",
      "envFile": "${workspaceFolder}/.env",
      "console": "integratedTerminal"
    },
    {
      "name": "Run",
      "type": "debugpy",
      "request": "launch",
      "program": "${workspaceFolder}/src/main.py",
      "console": "integratedTerminal",
      "envFile": "${workspaceFolder}/.env"
    }
  ]
}
```
