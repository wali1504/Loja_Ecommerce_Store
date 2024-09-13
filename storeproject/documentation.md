# E-Commerce Backend with Django

## Project Overview
This project will involve developing the backend of an e-commerce store using Django, with integration to a React.js frontend. The backend will handle user authentication, role-based access control, product and category management, order tracking, and more. The database will be managed using MySQL, with API endpoints provided through Django REST Framework.

## Project Structure
users/               # User management app
    models.py        # User models
    views.py         # User views (registration, login, etc.)
    urls.py          # URL routing for user-related views

products/            # Product and category management app
    models.py        # Product and category models
    views.py         # Product views (CRUD operations)
    urls.py          # URL routing for product-related views

orders/              # Order management app
    models.py        # Order models
    views.py         # Order views (user order display, tracking)
    urls.py          # URL routing for order-related views

admin/               # Admin management app 
    views.py         # Admin views (manage users, orders)
    urls.py          # URL routing for admin-related views

## Database Models

### User Model
- **Fields:**
  - `username`: String
  - `email`: Email
  - `password`: String
  - `role`: ChoiceField (User, Admin, etc.)
  - `profile_info`: OneToOne relationship with Profile model
- **Relationships:**
  - `orders`: One-to-Many relationship with Order model

### Profile Model
- **Fields:**
  - `user`: OneToOne relationship with User
  - `first_name`: String
  - `last_name`: String
  - `address`: Text
  - `phone_number`: String

### Product Model
- **Fields:**
  - `name`: String
  - `description`: Text
  - `price`: Decimal
  - `stock`: Integer
  - `category`: String
  - =

### Category Model
- **Fields:**
  - `name`: String
  - `description`: Text
- **Relationships:**
  - `products`: One-to-Many relationship with Product model

### Order Model
- **Fields:**
  - `user`: ForeignKey to User
  - `products`: ManyToManyField to Product
  - `total_price`: Decimal
  - `status`: ChoiceField (Pending, Shipped, Delivered)
  - `created_at`: DateTime
- **Relationships:**
  - `user`: ForeignKey relationship with User model

## API Endpoints

### User Endpoints
- **POST `/api/register/`**: Register a new user
  - **Request:** `{ "username": "string", "email": "string", "password": "string" }`
  - **Response:** `{ "id": "integer", "username": "string", "email": "string" }`
  
- **POST `/api/login/`**: Login user
  - **Request:** `{ "username": "string", "password": "string" }`
  - **Response:** `{ "token": "string" }`
  
- **GET `/api/profile/`**: Get user profile
- **PUT `/api/profile/`**: Update user profile

### Product Endpoints
- **GET `/api/products/`**: List all products
- **GET `/api/products/{id}/`**: Retrieve a single product
- **POST `/api/products/`**: Add a new product (Admin only)
  - **Request:** `{ "name": "string", "description": "string", "price": "decimal", "stock": "integer", "category_id": "integer", "image": "file" }`
  
- **PUT `/api/products/{id}/`**: Update a product (Admin only)
- **DELETE `/api/products/{id}/`**: Delete a product (Admin only)

### Category Endpoints
- **GET `/api/categories/`**: List all categories
- **POST `/api/categories/`**: Add a new category (Admin only)
  - **Request:** `{ "name": "string", "description": "string" }`
  
- **PUT `/api/categories/{id}/`**: Update a category (Admin only)
- **DELETE `/api/categories/{id}/`**: Delete a category (Admin only)

### Order Endpoints
- **GET `/api/orders/`**: List all orders for logged-in user
- **POST `/api/orders/`**: Create a new order
  - **Request:** `{ "product_ids": ["integer"] }`
  
- **GET `/api/orders/{id}/`**: Retrieve a single order
- **PUT `/api/orders/{id}/status/`**: Update order status (Admin only)
  - **Request:** `{ "status": "string" }`

### Admin Endpoints
- **GET `/api/admin/users/`**: List all users (Admin only)
- **GET `/api/admin/orders/`**: List all orders (Admin only)

## Roles & Permissions
- **Admin**: Full access to all endpoints (manage products, categories, users, and orders).
- **User**: Access to personal account management, view products, create orders, and track orders.
- **Guest**: Access to view products and categories.

## Next Steps
1. **Finalize Documentation**: Review and align on the draft with the team.
2. **Begin Development**: Set up the Django project, initialize the database models, and start building out the API endpoints.

