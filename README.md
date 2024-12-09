
# Ice Cream Parlor Application

This is a simple Python application for managing an ice cream parlor's offerings, inventory, and customer concerns.

## Features
- Manage seasonal flavor offerings.
- Track allergen information.
- Maintain a cart of favorite items.

## How to Run
1. Clone this repository:
    ```
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Build and run the application using Docker:
    ```
    docker build -t ice_cream_app .
    docker run -p 5000:5000 ice_cream_app
    ```

3. Access the application at `http://localhost:5000`.

## API Endpoints
- `GET /flavors`: List all flavors.
- `POST /flavors`: Add a new flavor.
- `GET /allergens`: List all allergens.
- `POST /allergens`: Add a new allergen.
- `GET /cart`: View cart items.
- `POST /cart`: Add a flavor to the cart.

## Testing
To test, use tools like Postman or cURL to make requests to the API endpoints.

---

## Docker Commands
- Build the Docker image:
  ```
  docker build -t ice_cream_app .
  ```
- Run the Docker container:
  ```
  docker run -p 5000:5000 ice_cream_app
  ```

---
