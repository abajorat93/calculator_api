# Setup
* Create a virtual environment with:
```
python3 -m venv venv
```

* Activate the virtual environment

```
source venv/bin/activate
```

# Install the other libraries
Run the following command to install the other libraries.

```
pip install -r requirements.txt
```


## OPTIONAL: Install calculator library as a package
````
$ pip install ./dist/calculadora-0.3.0-py3-none-any.whl
````

# Tests

````
$ pytest tests/integration/ -v
````
````
tests/integration/test_integration.py::test_integration PASSED                                                                                [ 33%]
tests/integration/test_integration.py::test_integration_parametrize[5-5-5/4-3/4-5] PASSED                                                     [ 66%]
tests/integration/test_integration.py::test_integration_parametrize[8-7/5-15-3/8-137.475] PASSED                                              [100%]
````




# Run FastAPI
Run next commando to start calculator api locally

```
uvicorn src.main:app --reload
```

# Logging levels
* DEBUG: Detailed information, typically of interest only when diagnosing problems.

* INFO: Confirmation that things are working as expected.

* WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

* ERROR: Due to a more serious problem, the software has not been able to perform some function.

* CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

# RUn with Docker
```
docker build . -t calc_api 
docker run calc_api
```
