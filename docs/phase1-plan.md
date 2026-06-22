# Phase 1 — Foundation: Detailed Plan

## 1. Objective

The objective of Phase 1 is to establish the technical foundation required for the Saanjh Ki Roti system.

This phase focuses on project setup, authentication, database configuration, and plan management.

Only the User and Plan modules are implemented during this phase.

No business workflows such as subscriptions, deliveries, payments, complaints, reporting, referrals, or add-ons are included.

---

## 2. Scope

### Included

* Project structure
* Database configuration
* SQLModel integration
* User model
* Plan model
* Password hashing
* JWT token generation
* Current user dependency
* Authentication APIs
* Health endpoint
* Plan APIs
* Swagger documentation

### Excluded

* Subscription management
* Delivery management
* Payment management
* Complaint management
* Reporting
* Add-ons
* Referral system
* Pause requests

---

## 3. Build Order

Phase 1 implementation will follow the sequence below.

### Step 1

Create the project folder structure.

### Step 2

Configure database connectivity using SQLModel.

### Step 3

Create configuration and security utilities.

### Step 4

Implement User SQLModel.

### Step 5

Implement Plan SQLModel.

### Step 6

Create Pydantic request and response schemas.

### Step 7

Implement authentication services.

### Step 8

Implement JWT token generation and validation.

### Step 9

Implement current-user dependency.

### Step 10

Create authentication endpoints.

### Step 11

Create health endpoint.

### Step 12

Create plan endpoints.

### Step 13

Verify OpenAPI documentation.

### Step 14

Execute tests and validate Definition of Done.
## 4. Folder Structure

```text
app/
│
├── main.py
├── database.py
├── dependencies.py
│
├── core/
│     ├── config.py
│     └── security.py
│
├── models/
│     ├── user.py
│     └── plan.py
│
├── schemas/
│     ├── user.py
│     ├── auth.py
│     └── plan.py
│
├── services/
│     ├── auth_service.py
│     └── plan_service.py
│
├── routers/
│     ├── auth.py
│     ├── plans.py
│     └── health.py
│
└── tests/
      ├── test_auth.py
      ├── test_plan.py
      └── test_health.py
```

---

### main.py

Purpose:

Application entry point.

Responsibilities:

* Create FastAPI application.
* Register routers.
* Configure OpenAPI documentation.
* Initialize application settings.

---

### database.py

Purpose:

Configure SQLModel database connection.

Responsibilities:

* Create database engine.
* Create session factory.
* Provide database sessions.

---

### dependencies.py

Purpose:

Provide reusable FastAPI dependencies.

Responsibilities:

* Database session dependency.
* Current user dependency.

---

### core/config.py

Purpose:

Store project configuration variables.

Responsibilities:

* Database URL.
* JWT secret key.
* Token expiry configuration.

---

### core/security.py

Purpose:

Handle password hashing and token operations.

Responsibilities:

* Hash passwords.
* Verify passwords.
* Generate JWT tokens.
* Decode JWT tokens.

---

### models/user.py

Purpose:

Define User SQLModel.

Responsibilities:

* Store authentication information.
* Store user roles.

---

### models/plan.py

Purpose:

Define Plan SQLModel.

Responsibilities:

* Store meal plan information.
* Store pricing details.

---

### schemas/user.py

Purpose:

Request and response schemas for users.

Responsibilities:

* UserCreate schema.
* UserResponse schema.

---

### schemas/auth.py

Purpose:

Authentication schemas.

Responsibilities:

* LoginRequest schema.
* TokenResponse schema.

---

### schemas/plan.py

Purpose:

Plan request and response schemas.

Responsibilities:

* PlanCreate schema.
* PlanResponse schema.

---

### services/auth_service.py

Purpose:

Implement authentication business logic.

Responsibilities:

* Register users.
* Authenticate users.
* Generate access tokens.

---

### services/plan_service.py

Purpose:

Implement plan business logic.

Responsibilities:

* Create plans.
* Retrieve plans.

---

### routers/auth.py

Purpose:

Authentication endpoints.

Responsibilities:

* Register endpoint.
* Login endpoint.

---

### routers/plans.py

Purpose:

Plan APIs.

Responsibilities:

* Create plans.
* Retrieve plans.

---

### routers/health.py

Purpose:

Health check endpoint.

Responsibilities:

* Return application status.

---

### tests/test_auth.py

Purpose:

Authentication endpoint tests.

Functions:

test_register_user()

Purpose:

Verify successful user registration.

Steps:

* Send POST /auth/register request.
* Verify HTTP 201 response.
* Verify user record creation.

Expected Result:

User is registered successfully.

---

test_login_user()

Purpose:

Verify login and JWT generation.

Steps:

* Send POST /auth/login request using OAuth2PasswordRequestForm.
* Verify HTTP 200 response.
* Verify access_token exists.

Expected Result:

JWT token is returned.

---

### tests/test_plan.py

Purpose:

Plan endpoint tests.

Functions:

test_create_plan()

Purpose:

Verify plan creation.

Steps:

* Send POST /plans request.
* Verify HTTP 201 response.

Expected Result:

Plan record is created.

---

test_get_all_plans()

Purpose:

Verify plan retrieval.

Steps:

* Send GET /plans request.
* Verify HTTP 200 response.

Expected Result:

List of plans is returned.


---

### tests/test_health.py

Purpose:

Health endpoint tests.

Functions:

test_health_endpoint()

Purpose:

Verify application health endpoint.

Steps:

* Send GET /health request.
* Verify HTTP 200 response.
* Verify response contains status = healthy.

Expected Result:

Health endpoint returns healthy status.


## 5. Detailed File Implementation Plan

### 5.1 database.py

Purpose:

Provides database connectivity using SQLModel.

Functions:

---

#### create_db_and_tables()

Purpose:

Creates database tables during application startup.

Parameters:

None

Returns:

None

Responsibilities:

* Initialize SQLModel metadata.
* Create tables if they do not already exist.

---

#### get_session()

Purpose:

Provides database sessions through dependency injection.

Parameters:

None

Returns:

Session

Responsibilities:

* Open database session.
* Yield session object.
* Close session after request completion.

---

### 5.2 core/config.py

Purpose:

Stores application configuration.

Variables:

---

DATABASE_URL

Type:

String

Meaning:

SQLite database connection string.

Example:

sqlite:///saanjh_ki_roti.db

---

SECRET_KEY

Type:

String

Meaning:

JWT signing key.

---

ACCESS_TOKEN_EXPIRE_MINUTES

Type:

Integer

Meaning:

JWT expiration duration.

Default:

60

---

### 5.3 core/security.py

Purpose:

Handles password hashing and JWT operations.

Functions:

---

#### hash_password(password)

Purpose:

Converts plain text password into hashed password.

Parameters:

password

Type:

String

Returns:

String

Responsibilities:

* Hash password using bcrypt.

---

#### verify_password(plain_password, hashed_password)

Purpose:

Validates user password.

Parameters:

plain_password

Type:

String

hashed_password

Type:

String

Returns:

Boolean

Responsibilities:

* Compare user input password with stored hash.

---

#### create_access_token(user_id, role)

Purpose:

Generates JWT access token.

Parameters:

user_id

Type:

Integer

role

Type:

String

Returns:

String

Implementation Details:

Library:

python-jose

Algorithm:

HS256

JWT Claims:

sub

Meaning:

Stores user email.

role

Meaning:

Stores user role.

exp

Meaning:

Stores token expiration timestamp.

Responsibilities:

* Create JWT payload containing sub, role, and exp claims.
* Add expiration timestamp.
* Encode token using python-jose and the HS256 algorithm.
---

#### decode_access_token(token)

Purpose:

Decode and validate JWT token.

Parameters:

token

Type:

String

Returns:

Dictionary

Responsibilities:

* Decode JWT using python-jose.
* Validate HS256 signature.
* Validate expiration timestamp.
* Extract sub claim.
* Extract role claim.
* Return decoded payload.


---

### 5.4 dependencies.py

Purpose:

Contains reusable dependencies.

Functions:

---

#### get_current_user()

Purpose:

Returns currently authenticated user.

Parameters:

token

Type:

JWT Token

Returns:

User

Responsibilities:

* Decode token.
* Fetch user from database.
* Validate user existence.
* Raise HTTP 401 if token is invalid.
* Read sub claim to identify the user.
* Read role claim for authorization decisions.

---

#### get_current_admin()

Purpose:

Restricts endpoints to administrator users.

Parameters:

current_user

Type:

User

Returns:

User

Responsibilities:

* Retrieve current user from get_current_user().
* Verify that role = ADMIN.
* Allow access to administrator endpoints.
* Raise HTTP 403 if the authenticated user is not an administrator.

### 5.5 models/user.py

Purpose:

Defines the User SQLModel.

Fields:

id

Type:
Integer

Required:
System Generated

Meaning:
Unique user identifier.

---

name

Type:
String

Required:
Yes

Meaning:
Full name of the user.

---

email

Type:
String

Required:
Yes

Meaning:
Unique email address.

Validation:

Must be unique.

---

password_hash

Type:
String

Required:
Yes

Meaning:
Stores hashed password.

---

role

Type:
String (Enum)

Required:
Yes

Allowed Values:

* ADMIN
* CUSTOMER

Meaning:

Determines access privileges.

---

Functions:

None

Responsibilities:

* Store authentication data.
* Support role-based access.

---

### 5.6 models/plan.py

Purpose:

Defines meal plans.

Fields:

id

Type:
Integer

Required:
System Generated

Meaning:
Unique plan identifier.

---

name

Type:
String

Required:
Yes

Meaning:
Plan name.

---

price

Type:
Decimal(10,2)

Required:
Yes

Meaning:
Plan price.

---

meal_type

Type:
String (Enum)

Required:
Yes

Allowed Values:

* Lunch
* Lunch and Dinner

Meaning:

Meal combination included in the plan.

---

is_active

Type:
Boolean

Required:
Yes

Default:
True

Meaning:

Indicates whether the plan is available.

Responsibilities:

* Store plan information.

---

### 5.7 schemas/user.py

Purpose:

Request and response schemas for users.

Classes:

UserCreate

Fields:

* name
* email
* password

---

UserResponse

Fields:

* id
* name
* email
* role

Responsibilities:

* Request validation.
* API response serialization.

---

### 5.8 schemas/auth.py

Purpose:

Authentication schemas.

Authentication Input

Login uses FastAPI's OAuth2PasswordRequestForm.

Fields:

* username
* password

Meaning:

Credentials are submitted as form data rather than JSON request bodies.

Reasoning:

Using OAuth2PasswordRequestForm keeps the API compatible with Swagger UI's Authorize button and supports dependency composition with OAuth2PasswordBearer for protected endpoints.

---

TokenResponse

Fields:

* access_token
* token_type

Responsibilities:

* Login request validation.
* JWT response formatting.


---

TokenResponse

Fields:

* access_token
* token_type

Responsibilities:

* Login request validation.
* JWT response formatting.

---

### 5.9 schemas/plan.py

Purpose:

Plan request and response schemas.

Classes:

PlanCreate

Fields:

* name
* price
* meal_type

---

PlanResponse

Fields:

* id
* name
* price
* meal_type
* is_active

Responsibilities:

* Validate plan requests.
* Serialize responses.

---

### 5.10 services/auth_service.py

Purpose:

Authentication business logic.

Functions:

---

register_user()

Purpose:

Creates a new user.

Parameters:

user_data

Type:
UserCreate

Returns:

User

Responsibilities:

* Validate uniqueness.
* Hash password.
* Store user.

---

authenticate_user()

Purpose:

Validates login credentials.

Parameters:

email

Type:
String

password

Type:
String

Returns:

User

Responsibilities:

* Verify email.
* Verify password.

---

login_user()

Purpose:

Generates JWT token.

Parameters:

username

Type:
String

Meaning:

User email submitted through OAuth2PasswordRequestForm.

password

Type:
String

Meaning:

User password submitted through OAuth2PasswordRequestForm.

Returns:

TokenResponse

Responsibilities:

* Authenticate user.
* Generate access token.


---

### 5.11 services/plan_service.py

Purpose:

Plan business logic.

Functions:

---

create_plan()

Purpose:

Creates meal plan.

Parameters:

plan_data

Type:
PlanCreate

Returns:

Plan

Responsibilities:

* Validate request.
* Save plan.
* Only administrators are permitted to create plans.

---

get_all_plans()

Purpose:

Returns all active plans.

Parameters:

None

Returns:

List[Plan]

Responsibilities:

* Query plans.
* Return active plans.

---

### 5.12 routers/auth.py

Endpoints:

POST /auth/register

Purpose:

Register new user.

Returns:

HTTP 201

---

POST /auth/login

Purpose:

Authenticate user and generate JWT.

Returns:

HTTP 200

Responsibilities:

* User registration.
* User login.

---

### 5.13 routers/plans.py

Endpoints:

GET /plans

Purpose:

Retrieve all plans.

Returns:

HTTP 200

---

### POST /plans

Purpose:

Create meal plan.

Authorization:

Requires administrator access.

Dependency Chain:

OAuth2PasswordBearer

↓

get_current_user()

↓

get_current_admin()

↓

POST /plans

Success Response:

HTTP 201

Failure Responses:

HTTP 401

Unauthorized request.

HTTP 403

Non-admin user.

HTTP 422

Validation error.


---

### 5.14 routers/health.py

Endpoints:

GET /health

Purpose:

Verify application health.

Returns:

HTTP 200

Response:

{
"status":"healthy"
}

Responsibilities:

* Application monitoring.
## 6. SQLModel Classes

Phase 1 ships only two database models.

### User

Purpose:

Stores authentication and role information.

Relationships:

No foreign keys in Phase 1.

Fields:

* id
* name
* email
* password_hash
* role

Allowed Role Values:

* ADMIN
* CUSTOMER

---

### Plan

Purpose:

Stores meal plan information.

Relationships:

No foreign keys in Phase 1.

Fields:

* id
* name
* price
* meal_type
* is_active

Allowed Meal Types:

* Lunch
* Lunch and Dinner

---

## 7. Authentication Flow

### Registration Flow

Client

↓

POST /auth/register

↓

Validate request

↓

Hash password using bcrypt

↓

Create User record

↓

Save user in database

↓

Return HTTP 201

---

### Login Flow

Client

↓

POST /auth/login

↓

Validate email

↓

Verify password

↓

Generate JWT token

↓

Return access token

↓

HTTP 200

---

### Protected Endpoint Flow

Client

↓

Authorization Header

↓

Bearer Token

↓

get_current_user()

↓

decode_access_token()

↓

Validate token

↓

Load User

↓

Allow Request

OR

Return HTTP 401

---

## 8. Endpoint Specifications

### POST /auth/register

Purpose:

Register a new user.

Request:

* name
* email
* password

Success Response:

HTTP 201

Failure Response:

HTTP 409

Duplicate email.

---

### POST /auth/login

Purpose:

Authenticate user.

Request Type:

OAuth2PasswordRequestForm

Fields:

* username
* password

Success Response:

HTTP 200

Failure Response:

HTTP 401

Invalid credentials.

---

### GET /health

Purpose:

Verify application status.

Success Response:

HTTP 200

Response:

{
"status":"healthy"
}

---

### GET /plans

Purpose:

Retrieve available plans.

Success Response:

HTTP 200

Returns:

List of plans.

---

### POST /plans

Purpose:

Create meal plan.

Success Response:

HTTP 201

Failure Response:

HTTP 422

Validation error.

---

## 9. Definition of Done

Phase 1 is complete only when all conditions below are satisfied.

1. FastAPI application starts successfully.

2. SQLite database connection initializes successfully.

3. SQLModel metadata creates tables successfully.

4. User table is created.

5. Plan table is created.

6. POST /auth/register returns HTTP 201.

7. Duplicate email addresses return HTTP 409.

8. Passwords are stored using bcrypt hashing.

9. POST /auth/login returns JWT access token.

10. Invalid credentials return HTTP 401.

11. JWT token expiration is enforced.

12. Current user dependency validates access token.

13. Unauthorized requests return HTTP 401.

14. GET /health returns HTTP 200.

15. GET /health returns:

{
"status":"healthy"
}

16. POST /plans creates plans successfully.

17. Customer users attempting POST /plans receive HTTP 403.

18. Administrator users can successfully create plans.


19. GET /plans returns available plans.

20. Request validation errors return HTTP 422.

21. Swagger UI displays all endpoints.

22. Automated tests pass successfully before merge.

23. OpenAPI schema generation succeeds.

24. All Phase 1 endpoints are accessible through Swagger UI.
