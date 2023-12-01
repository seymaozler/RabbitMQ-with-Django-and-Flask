# RabbitMQ-with-Django-and-Flask
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- ABOUT THE PROJECT -->
## About The Project
In this project, a communication system between applications is established using Django, FastAPI, and RabbitMQ. CRUD operations for products are carried out in the admin section created in Django, while in the main section created in FastAPI, these products are listed and liked.
### Built With

* FastAPI
* Django
* MySQL
* RabbitMQ
* Docker

<!-- GETTING STARTED -->
## Getting Started
### Prerequisites

Before running, make sure you have Docker installed on your system.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/seymaozler/RabbitMQ-with-Django-and-Flask.git
   ```
2. Create a virtual environment and activate it
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install requirements
   ```sh
   pip install -r requirements.txt
   ```
4. Build the Docker containers:
   ``` sh
   docker-compose build
   ```
5. Start the Docker containers:
   ``` sh
   docker-compose up
   ```



