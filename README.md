# behave-selenium-template
Use this repository as template for behave selenium tests with page object model pattern

### Start Selenium Hub using docker-compose:

    docker-compose up -d

### Start demo app:

    pipenv run python demoapp/server.py

### Run all tests

    pipenv run behave
    
### Run happy path tests

    pipenv run behave --tags="@happyPath"

### Run negative tests

    pipenv run behave --tags="@negative"

### Format

    pipenv run autopep8 --in-place --recursive .
