# Track and Trace API

*** The goal of the project is to create a RESTful API that allows to track and trace parcels. ***

Here are the objectives that influenced the design of the API:

1. Maintainability: The code is structured in a way that it is easy to maintain and extend.
2. Testability: The code is structured in a way that it is easy to test.
3. Readability: The code is structured in a way that it is easy to read and understand.
4. Scalability: The code is structured in a way that it is easy to scale.


## Clone the repository
    
```bash
    git clone https://github.com/rakibulmdalam/plab.git
```

## Installation without container

1. Install the dependencies

    ```bash
        pip install -r requirements.txt
    ```

2. Install Redis

    See https://redis.io/topics/quickstart

    For Ubuntu-
    ```bash
        sudo apt install redis-server
    ```
    For Mac-
    ```bash
        brew install redis
    ```

3. Run the tests

    ```bash
        pytest
    ```

    This will run all the tests in the tests folder which includes unit tests and integration tests.


4. Run the application

    ```bash
        python app.py
    ```

    to run application in debug mode

    ```bash
        python app.py --debug
    ```


5. View the OpenAPI documentation (swagger)

    ```bash
        http://localhost:5000/api/
    ```


## Installation with docker-compose

1. Install docker and docker-compose

    For docker installation see https://docs.docker.com/engine/install/
    For docker-compose installation see https://docs.docker.com/compose/install/

2. In parcellab/configs/ folder, change the REDIS_HOST to "redis" from "localhost"

3. Run docker-compose 

    ```bash
        docker-compose up
    ```

    This will run the application and redis in docker containers.

4. View the OpenAPI documentation (swagger)

    ```bash
        http://localhost:5000/api/
    ```