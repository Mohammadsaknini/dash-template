# DASH-TEMPLATE

## Overview

This repository provides a customizable template for building interactive web applications using the Dash framework in Python. The template is designed with a modular structure to help you quickly start developing scalable, data-driven dashboards with clean organization.

## Features

- **Modular Structure**: The project is organized into distinct directories such as `components`, `pages`, `assets`, and `utils`, each serving a specific purpose, ensuring that your codebase remains clean and maintainable.

- **Pages**
The pages directory follows a modular structure, with each page containing its own `layout` and `callbacks`. This separation helps keep the codebase organized and makes it easier to add new pages or modify existing ones.


- **Asset Management**:
  - **`assets`**: Contains static resources such as stylesheets (`sass`), scripts, images, and localized data (`locales`) to be used throughout the application.

- **Docker Support**:
  - Pre-configured `Dockerfile` and `docker-compose.yaml` to streamline the setup of a containerized development environment.

- **Logging Configuration**:
  - A customizable logging configuration file (`logging.conf`) is included to help monitor and debug the application.

## Getting Started

### Prerequisites

- Python 3.x
- Docker (optional, for containerized development)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/dash-template.git
    cd dash-template
    ```

2. Install Poetry and project dependencies:
    ```bash
    pip install poetry
    poetry install
    ```

3. Run the application:
    ```bash
    python app.py
    ```

### Running with Docker

If you prefer to run the application in a Docker container:

1. Make sure docker is installed on your system and running.
2. Build & run the container:
    ```bash
    cd dash-template
    sh entry.sh
    ```

## Customization

Feel free to customize the template according to your project requirements. The provided pages are merely examples showcasing the layout and can be modified or replaced as needed.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
