# full-stack-copilot

## Overview
This project is a cloud-native application designed to replace a legacy system called "Core Process". The new system leverages AWS services such as API Gateway, Lambda, and DynamoDB to handle financial processing for different entities. Additionally, a monitoring system is in place to track the new API's performance and ensure smooth transition from the legacy system.

## Project Structure
```
full-stack-copilot/
│
├── thing_service.py
├── thing_dao.py
├── lambda_function.py
├── tests/
│   ├── test_thing_service.py
│
├── .gitignore
├── README.md
├── pyproject.toml
└── LICENSE
```

### Files and Directories

- `thing_service.py`: Contains the `ThingService` class, which encapsulates the business logic for handling "things".
- `thing_dao.py`: Contains the `ThingDAO` class, which is responsible for data access operations on the DynamoDB table.
- `lambda_function.py`: The AWS Lambda function handler that processes incoming API requests, utilizing the `ThingService` class.
- `tests/`: Directory containing test modules.
    - `test_thing_service.py`: Unit tests for the `ThingService` class using the `unittest` framework and mocking the `ThingDAO` class.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `README.md`: This file, providing an overview and description of the project.
- `pyproject.toml`: Configuration file for managing project dependencies with Poetry.
- `LICENSE`: License file for the project.