# Hello FastAPI

* https://fastapi.tiangolo.com/tutorial/

---

## Environment Set-Up:

Note: The back-end in FastAPI's [full-stack template](https://fastapi.tiangolo.com/project-generation/) uses [Poetry](https://python-poetry.org) for package and environment management. (Let's just roll with `venv` for now.)

### Create and Instantiate a `venv` Virtual Environment:

From [here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

##### Create:

* `python3 -m venv .venv`
  * `-m venv` = use the `venv` module
  * `.venv` = the name of the virtual environment folder

##### Instantiate:

* `source .venv/bin/activate`

##### Verify:

* `which python`
  * should output `/Users/..../.venv/bin/python`

##### Deactivate:

* `deactivate`

##### Create `requirements.txt`:

Note: This only saves dependencies installed with `pip`!

* `pip freeze > requirements.txt`

---

## `.gitignore`

Just using [what FastAPI's back-end uses](https://github.com/tiangolo/full-stack-fastapi-template/blob/master/backend/.gitignore) in their full-stack template.

---

## Start the Server in Development Mode:

* `fastapi dev main.py`
