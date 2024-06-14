# FastAPI AWS S3 Service

Welcome to the FastAPI AWS S3 Service project! This project provides a backend API built with FastAPI for managing AWS S3 buckets and objects, along with user authentication via Okta.

## Table of Contents

- [Features](#features)
- [Folder Structure](#folder-structure)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Server](#running-the-server)
  - [Endpoints](#endpoints)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Authentication**: User authentication using Okta.
- **AWS S3 Operations**: CRUD operations for managing S3 buckets and objects.
- **Modular Structure**: Organized codebase using `APIRouter` for separation of concerns.
- **Environment-based Configuration**: Configuration via `.env` file for sensitive information.

## Folder Structure

```
my_fastapi_project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   └── __init__.py
│   ├── schemas/
│   │   └── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── s3.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── s3_service.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   └── utils/
│       └── __init__.py
├── .env
├── requirements.txt
└── README.md
```

## Setup

### Prerequisites

- Python 3.7+
- `pip` package manager
- AWS account with S3 access credentials
- Okta developer account (for authentication)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/my_fastapi_project.git
   cd my_fastapi_project
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Server

Run the FastAPI server with Uvicorn:

```bash
uvicorn app.main:app --reload
```

The server will start at `http://localhost:8000`.

### Endpoints

- **Authentication**:
  - `POST /auth/login`: Authenticate a user with Okta.
  - `POST /auth/logout`: Log out a user.

- **AWS S3 Operations**:
  - `POST /s3/credentials`: Store AWS S3 credentials.
  - `PUT /s3/credentials`: Update AWS S3 credentials.
  - `DELETE /s3/credentials`: Delete AWS S3 credentials.
  - `GET /s3/buckets`: List all S3 buckets.
  - `GET /s3/buckets/{bucket_name}`: List items in a specific S3 bucket.
  - `POST /s3/buckets/{bucket_name}/items`: Add an item to a specific S3 bucket.
  - `DELETE /s3/buckets/{bucket_name}/items/{item_name}`: Delete an item from a specific S3 bucket.

## Environment Variables

Create a `.env` file in the root directory with the following environment variables:

```
OKTA_CLIENT_ID=your_okta_client_id
OKTA_CLIENT_SECRET=your_okta_client_secret
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
```

## Contributing

Contributions are welcome! Fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
