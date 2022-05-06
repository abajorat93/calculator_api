# Setup
* Create a virtual environment with:
```
python3 -m venv venv
```

* Activate the virtual environment

```
source venv/bin/activate
```

# Install calculator library
Run the following command to install the calculator library.

```
pip install calculator-0.3.0-py3-none-any.whl
```

# Install the other libraries
Run the following command to install the other libraries.

```
pip install -r requirements.txt
```


# Run FastAPI
Run next commando to start calculator api locally

```
uvicorn app.main:app --reload
```

# Logging levels
* DEBUG: Detailed information, typically of interest only when diagnosing problems.

* INFO: Confirmation that things are working as expected.

* WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

* ERROR: Due to a more serious problem, the software has not been able to perform some function.

* CRITICAL: A serious error, indicating that the program itself may be unable to continue running.