# Docker Assignment 2

## Overview

This repository contains a Docker Compose setup for creating a PostgreSQL environment and appending data accordingly. The persisted data from this setup is stored in the `a-2-db-data` section of your Docker volumes.

## Prerequisites

- Docker and Docker Compose installed on your machine.

## Running the Setup

To run the Docker Compose setup, follow these steps:

1. Clone the repository:

```bash
git clone <repository-url>  # Replace <repository-url> with the actual URL of this GitHub repo
cd <repository-directory>   # Replace <repository-directory> with the actual directory of the repo
```

2. Run the Docker Compose file:

```bash
docker-compose up --build
```

This command will bring up the PostgreSQL environment and handle data operations as defined in the Compose file. 

## Data Persistence

The data generated and manipulated by this setup is stored persistently in the Docker volume named `<Folder Name>-db-data`. You can inspect the volume using Docker's volume commands.
