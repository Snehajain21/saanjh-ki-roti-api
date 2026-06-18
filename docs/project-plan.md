# Saanjh Ki Roti API

# Project Requirements and Implementation Plan

## 1. Project Overview

Saanjh Ki Roti is a home-cooked tiffin subscription service operating in Vijaynagar, Kota. The business currently serves approximately 67 tiffins per day across multiple dietary categories and delivery routes.

Most business operations are currently managed manually using notebooks, phone calls, WhatsApp messages, and informal record keeping. As the customer base has grown, manual processes have started causing operational inefficiencies, food wastage, delayed updates, delivery tracking issues, and billing complications.

The objective of this project is to design and implement a FastAPI-based backend system that digitizes customer management, subscriptions, deliveries, billing, complaints, reporting, and operational tracking.

The system should provide role-based access for administrators, delivery personnel, and customers while ensuring accurate operational data and reducing manual effort.

---

## 2. Business Goals

### Primary Goals

* Reduce food wastage caused by inaccurate daily preparation counts.
* Maintain accurate subscription and pause tracking.
* Improve delivery visibility and accountability.
* Digitize billing and payment management.
* Track and resolve customer complaints efficiently.
* Generate operational reports automatically.
* Provide a centralized dashboard for business monitoring.

### Secondary Goals

* Store customer identity documents securely.

* Enable customer self-service actions.
* Improve route-based delivery management.
* Support referral and discount programs.
* Reduce dependency on WhatsApp and manual notebooks.

### Success Metrics

The system should help achieve:

* Accurate daily tiffin preparation counts.
* Reduced missed deliveries.
* Reduced food wastage.
* Faster complaint resolution.
* Improved payment collection.
* Automated monthly reporting.

---

## 3. User Roles and Permissions

### 3.1 Administrator (Saanjh)

The administrator has complete access to the system.

Responsibilities:

* Manage customers.
* Manage subscription plans.
* Approve and monitor pause requests.
* View dashboard statistics.
* Track deliveries.
* Manage delivery routes.
* Manage delivery personnel.
* Record payments.
* View billing information.
* Resolve complaints.
* Generate reports.
* Upload and manage customer documents.

Permissions:

* Full CRUD access across all modules.
* Access to all routes and deliveries.
* Access to all reports and analytics.

---

### 3.2 Delivery Boy

The delivery boy is responsible only for deliveries assigned to his route.

Responsibilities:

* View assigned deliveries.
* Update delivery status.
* Record failed delivery reasons.
* Process delivery retries.

Permissions:

* View only assigned route deliveries.
* Update delivery statuses.
* Cannot access customer financial information.
* Cannot view deliveries belonging to other routes.

---

### 3.3 Customer

The customer interacts with the service through their subscription.

Responsibilities:

* View subscription details.
* Pause subscription.
* View billing information.
* Raise complaints.
* Track payment status.

Permissions:

* Access only personal information.
* Access only own subscriptions.
* Access only own complaints and bills.

## 3.4 gi Developer Quick Start Guide

Purpose:

This section provides an onboarding path for new contributors. A developer should be able to understand the architecture and start implementing features within approximately 30 minutes.

Recommended Reading Order:

### Step 1: Functional Requirements

Read Section 4 to understand:

* Subscription plans
* Pause rules
* Delivery workflow
* Complaint SLA rules
* Billing cycles
* Add-on cutoff timings

### Step 2: Folder Structure

Read Section 11.1 to understand project organization and module responsibilities.

### Step 3: Models Layer

Read Section 11.3 to understand:

* Entities
* Relationships
* Field definitions
* Source-of-truth decisions

### Step 4: Services Layer

Read Section 11.5 to understand business logic responsibilities.

### Step 5: Definition of Done

Read Section 13 to understand V1 acceptance criteria and testable conditions.

Recommended onboarding path:

Functional Requirements → Folder Structure → Models Layer → Services Layer → Definition of Done

Following these sections should make a new contributor productive within approximately 30 minutes.


## 4. Functional Requirements

### 4.1 Customer Management

The system must allow administrators to:

* Register new customers.
* View customer profiles.
* Update customer information.
* Deactivate customers.
* Upload identity documents.
* View subscription history.
* View complaint history.
* View payment history.

Customer information should include:

* Full Name
* Phone Number
* Email (optional)
* Address
* Route
* Diet Preference
* Identity Document
* Account Status

---

### 4.2 Subscription Management

The system must support:

* Subscription creation
* Subscription renewal
* Subscription pause
* Subscription reactivation
* Subscription cancellation

Supported plans:

* Monthly Veg
* Monthly Premium
* Weekly Saver
* Diabetic Special

The system must track:

* Subscription start date
* Subscription end date
* Remaining service days
* Pause history
* Billing cycle
* Active status

---

### 4.3 Pause Management

Customers can pause subscriptions.

Business Rules:

* Maximum 7 pause days per billing cycle.
* Unused pause days do not carry forward.
* Additional pause days beyond the limit are forfeited.
* Pause requests should be recorded with timestamps.
* The system must prevent deliveries during pause periods.

---

### 4.4 Delivery Management

The system must:

* Generate daily delivery lists.
* Assign deliveries to routes.
* Track delivery status.
* Record failed deliveries.
* Manage retry attempts.

Delivery Status Flow:

Prepared → Out For Delivery → Delivered

OR

Prepared → Out For Delivery → Failed

Retry Flow:

Failed → Retry Scheduled → Delivered

OR

Failed → Retry Scheduled → Missed

---

### 4.5 Route Management

The system must support:

* Route creation
* Route assignment
* Delivery boy assignment
* Route statistics

Initial routes:

* East Vijaynagar
* West Vijaynagar
* Indra Vihar

---

### 4.6 Add-On Management

Administrators must be able to manage add-ons.

Examples:

* Extra Paneer
* Salad
* Raita
* Kheer

Business Rule:

Add-on requests must be submitted before 9:00 AM.

---

### 4.7 Billing and Payment Management

The system must:

* Generate bills automatically.
* Apply discounts.
* Track payment status.
* Maintain khaata balances.
* Generate payment reminders.

Supported payment methods:

* Cash
* UPI
* Khaata

---

### 4.8 Complaint Management

The system must:

* Log complaints.
* Assign severity.
* Track resolution deadlines.
* Record compensation provided.

Complaint Categories:

* Late Delivery
* Cold Food
* Wrong Order
* Missing Item
* Taste Complaint
* Other

Severity Levels:

* Low
* Medium
* High

---

### 4.9 Reporting System

The system must generate monthly reports containing:

* Total tiffins served
* Revenue collected
* Active customers
* Paused subscriptions
* Complaint statistics
* Delivery performance
* Top performing delivery boy

---

### 4.10 Dashboard

The administrator dashboard should display:

* Total tiffins for today
* Deliveries by route
* Deliveries by status
* Active subscriptions
* Today's complaints
* Pending payments
* Revenue summary

---

## 5. Core System Modules

The project will be divided into the following modules:

### Module 1: Authentication & Authorization

Responsibilities:

* Login
* Role management
* Permission checks
* Session management

---

### Module 2: Customer Management

Responsibilities:

* Customer registration
* Customer updates
* Customer records
* Document management

---

### Module 3: Subscription Management

Responsibilities:

* Plan assignment
* Pause tracking
* Renewal management
* Subscription lifecycle

---

### Module 4: Delivery Management

Responsibilities:

* Delivery creation
* Status tracking
* Retry handling
* Route mapping

---

### Module 5: Billing & Payments

Responsibilities:

* Invoice generation
* Payment tracking
* Discount processing
* Khaata management

---

### Module 6: Complaint Management

Responsibilities:

* Complaint registration
* Severity tracking
* Resolution tracking
* Compensation recording

---

### Module 7: Reporting & Analytics

Responsibilities:

* Monthly reports
* Operational summaries
* Delivery statistics
* Revenue analytics

---

## 6. Database Entities

The following entities are expected in the initial system design:

### Core Entities

• User

Role values:

* ADMIN
* CUSTOMER
* DELIVERY_BOY

Purpose:

Stores authentication credentials and role-based access information for all system users.

---

• Customer

Purpose:

Stores customer profile and contact information.

---

• Route

Purpose:

Stores delivery routes and route assignments.

---

• Plan

Purpose:

Stores subscription plans and pricing information.

---

• Subscription

Purpose:

Stores customer subscription details and lifecycle information.

---

• Delivery

Purpose:

Stores daily delivery records and delivery status.

---

• Payment

Purpose:

Stores payment transactions and payment status.

---

• Complaint

Purpose:

Stores customer complaints and their severity.

---

### Supporting Entities

• PauseRequest

Purpose:

Stores subscription pause history and serves as the authoritative source for pause calculations.

---

• AddOn

Purpose:

Stores the catalog of available add-on items.

---

• AddOnOrder

Purpose:

Stores customer-specific add-on orders and supports the 9:00 AM cutoff rule.

---

• Invoice

Purpose:

Stores billing records and invoice history.

---

• Referral

Purpose:

Stores customer referral relationships and reward eligibility.

---

• CustomerDocument

Purpose:

Stores Aadhaar and driving licence documents uploaded by customers.

---

• DeliveryStatusHistory

Purpose:

Stores delivery status transitions for audit and reporting.

---

• ComplaintResolution

Purpose:

Stores complaint resolution details and compensation records.

---

• PaymentReminder

Purpose:

Stores reminder history for upcoming and overdue payments.

---

• MonthlyReport

Purpose:

Stores monthly operational report snapshots and analytics.



## 7. Business Rules and Assumptions

This section defines the operational rules that govern the system.

### 7.1 Delivery Rules

* Deliveries are not scheduled on Sundays.
* Every delivery must belong to exactly one route.
* Every delivery must be assigned to one delivery boy.
* Delivery status must follow valid status transitions.
* Delivered orders cannot be reverted without administrator action.
* Failed deliveries require a failure reason.
* Failed deliveries receive one retry attempt.
* Retry deliveries are scheduled for 8:00 PM.
* If retry fails, the delivery is marked as missed.

---

### 7.2 Subscription Rules

* A customer can have only one active subscription at a time.
* Subscription start and end dates must be tracked.
* Customers may pause subscriptions.
* Pause requests cannot exceed seven days per billing cycle.
* Extra pause days are not carried forward.
* Paused subscriptions should not generate deliveries.
* Auto-paused subscriptions remain inactive until dues are cleared.

---

### 7.3 Billing Rules

* Monthly subscribers are billed on the first day of each month.
* Weekly subscribers are billed every Monday.
* Early payment discount is 10%.
* Referral discount is 5%.
* Referral rewards are granted only after the referred customer completes their first paid month.
* Payment reminders are sent five days before due dates.
* Subscriptions with dues exceeding ten days are automatically paused.

---

### 7.4 Complaint Rules

* Every complaint must have a category.
* Every complaint must have a severity level.
* Resolution deadlines are determined by severity.
* Compensation records must be maintained.
* Closed complaints cannot be modified without administrator approval.

---

### 7.5 Add-On Rules

* Add-on requests must be placed before 9:00 AM.
* Late requests are automatically rejected.
* Add-ons are linked to specific delivery dates.
* Add-ons must be reflected in billing records.

---

### 7.6 Customer Rules

* Customers must provide a unique phone number.
* Identity documents are optional but recommended.
* Inactive customers cannot create new requests.
* Customers can only access their own data.

---

## 8. Assumptions

The following assumptions are made during system design.

### Customer Assumptions

* One phone number represents one customer account.
* Customers are responsible for maintaining correct address information.
* Customers have internet access for self-service features.

### Operational Assumptions

* Route assignments are managed manually by administrators.
* Delivery boys use smartphones with internet connectivity.
* Delivery status updates are performed in real time.

### Billing Assumptions

* Prices are configured by administrators.
* Existing invoices are not modified retroactively after payment.
* Discounts are applied automatically by business rules.

### Reporting Assumptions

* Monthly reports are generated automatically.
* Reports are based on finalized operational data.

---

## 9. Things That Can Go Wrong (Risk Analysis and Edge Cases)

This section identifies situations that are not explicitly mentioned by the client but must be handled by the system.

### Customer Related Risks

#### Duplicate Phone Numbers

Scenario:

A customer attempts registration using an existing phone number.

Expected Handling:

* Reject duplicate registration.
* Administrator may merge records manually if required.

---

#### Address Change During Active Subscription

Scenario:

Customer changes address after subscription activation.

Expected Handling:

* Route assignment must be recalculated.
* Future deliveries should use updated address.

---

#### Customer Requests Pause After Food Preparation

Scenario:

Customer pauses after food has already been prepared.

Expected Handling:

* Current day's meal remains billable.
* Pause becomes effective from next eligible delivery.

---

### Subscription Risks

#### Plan Price Changes Mid-Cycle

Scenario:

Administrator changes plan pricing.

Expected Handling:

* Existing active subscriptions retain old pricing until renewal.
* New subscriptions use updated pricing.

---

#### Multiple Active Subscriptions

Scenario:

Customer accidentally receives multiple subscriptions.

Expected Handling:

* Prevent creation of overlapping active subscriptions.

---

### Delivery Risks

#### Delivery Boy Resigns

Scenario:

Delivery boy leaves while deliveries are assigned.

Expected Handling:

* Administrator reassigns deliveries.
* Pending deliveries remain visible until reassignment.

---

#### Incorrect Delivery Status

Scenario:

Delivery marked as delivered incorrectly.

Expected Handling:

* Administrator can override status.
* Audit trail records changes.

---

#### Route Capacity Exceeded

Scenario:

Number of customers exceeds route capacity.

Expected Handling:

* Administrator receives warning.
* Route redistribution required.

---

### Payment Risks

#### Failed Online Payment

Scenario:

Payment gateway confirms failure.

Expected Handling:

* Invoice remains unpaid.
* Retry payment option remains available.

---

#### Khaata Balance Growth

Scenario:

Customer accumulates excessive unpaid balance.

Expected Handling:

* Account flagged for review.
* Subscription may be auto-paused.

---

### Referral Risks

#### Self Referral

Scenario:

Customer attempts referring themselves.

Expected Handling:

* Referral rejected.

---

#### Fake Referral Accounts

Scenario:

Multiple accounts created solely for referral benefits.

Expected Handling:

* Administrator review required before reward approval.

---

### Complaint Risks

#### Complaint Submitted After Long Delay

Scenario:

Complaint submitted weeks after delivery.

Expected Handling:

* Mark as late complaint.
* Administrator decides resolution eligibility.

---

### Document Risks

#### Invalid Document Upload

Scenario:

Customer uploads unsupported file.

Expected Handling:

* Upload rejected.
* Validation error returned.

---

### Reporting Risks

#### Missing Operational Data

Scenario:

Deliveries or payments are not recorded properly.

Expected Handling:

* Reports identify incomplete data.
* Administrator receives warning.

## 10. Non-Functional Requirements

### Performance

* APIs should respond within acceptable response times.
* Dashboard statistics should be optimized for quick loading.
* Database queries should support future business growth.

### Security

* Passwords must be securely hashed.
* Role-based authorization must be enforced.
* Customers must only access their own information.
* Sensitive documents should be protected from unauthorized access.

### Reliability

* System should prevent data loss.
* Failed operations should be logged.
* Audit trails should be maintained for critical actions.

### Scalability

* System should support additional routes and delivery personnel.
* New subscription plans should be configurable without major code changes.

---

# 11. Implementation Plan

## 11.1 Proposed Folder Structure

```text
app/
│
├── main.py
│
├── core/
│   ├── config.py
│   ├── database.py
│   └── security.py
│
models/
│
├── user.py
├── customer.py
├── plan.py
├── subscription.py
├── route.py
├── delivery.py
├── payment.py
├── complaint.py
├── pause_request.py
├── addon.py
├── addon_order.py
├── invoice.py
├── referral.py
├── customer_document.py
├── delivery_status_history.py
├── complaint_resolution.py
├── payment_reminder.py
└── monthly_report.py
│
├── schemas/
│   ├── customer.py
│   ├── plan.py
│   ├── subscription.py
│   ├── delivery.py
│   ├── payment.py
│   └── complaint.py
│
├── services/
│   ├── customer_service.py
│   ├── subscription_service.py
│   ├── delivery_service.py
│   ├── payment_service.py
│   ├── complaint_service.py
│   └── report_service.py
│
├── routers/
│   ├── auth.py
│   ├── customers.py
│   ├── plans.py
│   ├── subscriptions.py
│   ├── deliveries.py
│   ├── payments.py
│   ├── complaints.py
│   └── reports.py
│
├── utils/
│   ├── validators.py
│   ├── date_utils.py
│   └── file_handler.py
│
└── tests/
```

---

## 11.2 Core Layer

### main.py

Purpose:

Application entry point.

Responsibilities:

* Create FastAPI application.
* Register all routers.
* Configure middleware.
* Initialize database connection.

Major Functions:

create_application()

Purpose:
Creates FastAPI application instance.

Returns:
FastAPI object.

Dependencies:

* config.py
* database.py
* all routers

---

### config.py

Purpose:

Stores application configuration.

Fields:

* DATABASE_URL
* SECRET_KEY
* JWT_ALGORITHM
* ACCESS_TOKEN_EXPIRE_MINUTES

Responsibilities:

* Centralized configuration management.
* Environment variable handling.

---


### database.py

Purpose:

Database configuration and session management.

Technology Choice:

The project will use SQLModel as the primary ORM layer.

Reasoning:

* SQLModel combines SQLAlchemy and Pydantic concepts.
* Database models and API data models remain closely aligned.
* Reduces duplication between table definitions and request/response schemas.
* Integrates naturally with FastAPI tutorials and documentation.
* Simplifies development for CRUD-heavy business applications.

Responsibilities:

* Create database engine.
* Create database sessions.
* Provide dependency injection for database access.
* Initialize database tables during application startup.

Functions:

get_session()

Purpose:

Provides a database session for API requests.

Returns:

SQLModel Session object.

Dependencies:

* SQLModel
* Database engine configuration

Trade-offs:

Advantages:

* Less boilerplate code.
* Better FastAPI integration.
* Easier schema maintenance.

Limitations:

* Slightly less flexible than using raw SQLAlchemy for highly complex ORM configurations.
* Additional abstraction layer over SQLAlchemy.


---

### security.py

Purpose:

Authentication and authorization utilities.

Functions:

hash_password()

Purpose:
Hash plain password.

Parameters:

* password

Returns:
Hashed password.

---

verify_password()

Purpose:
Verify password during login.

Parameters:

* plain_password
* hashed_password

Returns:
Boolean

---

create_access_token()

Purpose:
Generate JWT token.

Parameters:

* user_id
* role

Returns:
JWT token

---

## 11.3 Models Layer

### user.py

Purpose:

Stores authentication credentials and role information for system users.

Reason for Separate Model:

Authentication concerns are separated from customer business data to support role-based access and secure password management.

Fields:

---

Field: id

Type:
Integer

Required:
System Generated

Meaning:
Unique identifier for the user.

---

Field: username

Type:
String

Required:
Yes

Meaning:
Unique login identifier.

Validation:

* Must be unique.
* Cannot be empty.

---

Field: password_hash

Type:
String

Required:
Yes

Meaning:
Securely hashed password used for authentication.

Reasoning:

Passwords are never stored in plain text.

---

Field: role

Type:
String (Enum)

Required:
Yes

Allowed Values:

* ADMIN
* CUSTOMER
* DELIVERY_BOY

Meaning:

Determines permissions and API access.

---

Field: customer_id

Type:
Integer (Foreign Key)

Required:
No

Meaning:

Links a customer account to its authentication record.

Null For:

* Administrators
* Delivery personnel

Relationships:

* One Customer → One User account

Authentication Strategy:

Administrators and customers authenticate through User records.

Business data remains in customer.py while credentials are isolated in user.py.
--- 

### customer.py

Purpose:

Represents customer information and profile details.

---

Field: id

Type:
Integer

Required:
System Generated

Meaning:
Unique identifier for the customer.

Validation:
Must be unique.

---

Field: full_name

Type:
String

Required:
Yes

Meaning:
Full name of the customer.

Validation:
Cannot be empty.

---

Field: phone_number

Type:
String

Required:
Yes

Meaning:
Primary contact number used for communication.

Validation:

* Must be unique.
* Cannot be empty.

---

Field: email

Type:
String

Required:
No

Meaning:
Customer email address.

Validation:

* Must follow valid email format if provided.

---

Field: address

Type:
String

Required:
Yes

Meaning:
Delivery address of the customer.

Validation:

* Cannot be empty.

---

Field: route_id

Type:
Integer (Foreign Key)

Required:
Yes

Meaning:
Assigned delivery route.

Validation:

* Must reference an existing route.

---

Field: diet_type

Type:
String (Enum)

Required:
Yes

Meaning:
Customer dietary preference.

Allowed Values:

* Veg
* Non-Veg
* Jain
* Diabetic

---

Field: is_active

Type:
Boolean

Required:
No

Default:
True

Meaning:
Indicates whether the customer account is active.

---

Field: created_at

Type:
DateTime

Required:
System Generated

Meaning:
Timestamp when the customer account was created.

---

Relationships

* One Customer → One User Account
* One Customer → One Active Subscription
* One Customer → Many Payments
* One Customer → Many Complaints
* One Customer → Many AddOnOrders

---

Business Rules

* Phone numbers must be unique.
* Inactive customers cannot create subscriptions.
* Customers can access only their own information.

--- 

### plan.py

Purpose:

Stores subscription plans offered by the business.

---

Field: id

Type:
Integer

Required:
System Generated

Meaning:
Unique identifier for the plan.

Validation:
Must be unique.

Example:
1

---

Field: name

Type:
String

Required:
Yes

Meaning:
Display name of the subscription plan.

Validation:
Cannot be empty.

Examples:

* Monthly Veg
* Monthly Premium
* Weekly Saver
* Diabetic Special

---

Field: price

Type:
Decimal(10,2)

Required:
Yes

Meaning:
Subscription price charged to the customer.

Validation:

* Must be greater than zero.
* Stored using Decimal to prevent floating-point rounding errors.

Example:

2800.00

---

Field: billing_cycle

Type:
String (Enum)

Required:
Yes

Meaning:
Determines how frequently the customer is billed.

Allowed Values:

* Weekly
* Monthly

Example:

Monthly

---

Field: meal_type

Type:
String

Required:
Yes

Meaning:
Defines meal coverage provided by the plan.

Allowed Values:

* Lunch
* Lunch and Dinner

Example:

Lunch and Dinner

---

Field: daily_food_cost

Type:
Decimal(10,2)

Required:
Yes

Meaning:
Estimated daily preparation cost for a customer enrolled in the plan.

Validation:

* Must be greater than zero.
* Stored using Decimal for financial accuracy.

Example:

85.50

---

Field: is_active

Type:
Boolean

Required:
No

Default:
True

Meaning:
Indicates whether the plan is currently available for new subscriptions.

Example:

True

---

Business Rules:

* Plan names must be unique.
* Existing subscriptions retain their current pricing until renewal.
* Deactivated plans cannot be assigned to new customers.


### subscription.py

Purpose:

Stores active customer subscriptions.

Fields:

id

Type:
Integer

Required:
System Generated

Meaning:
Unique subscription identifier.

---

customer_id

Type:
Integer (Foreign Key)

Required:
Yes

Meaning:
Customer associated with the subscription.

---

plan_id

Type:
Integer (Foreign Key)

Required:
Yes

Meaning:
Selected subscription plan.

---

plan_price_snapshot

Type:
Decimal(10,2)

Required:
Yes

Meaning:
Stores the plan price at the time the subscription is created.

Reasoning:

Protects active subscriptions from future plan price changes.

Example:

Customer subscribes when Monthly Veg costs:

2800.00

Later the administrator updates the plan price to:

3200.00

The active subscription continues using:

2800.00

until renewal.

 ---

start_date

Type:
Date

Required:
Yes

Meaning:
Date on which the subscription becomes active.

---

end_date

Type:
Date

Required:
Yes

Meaning:
Date on which the subscription expires.

---

pause_limit_days

Type:
Integer

Required:
Yes

Default:
7

Meaning:
Maximum pause days allowed per billing cycle.

---

status

Type:
String (Enum)

Required:
Yes

Allowed Values:

* Active
* Paused
* Cancelled
* Expired

Meaning:
Current subscription state.

---

Pause Tracking Design

Authoritative Source:

PauseRequest records are the source of truth for all pause calculations.

Reasoning:

The system stores every pause event with start date, end date, and duration.

Derived Values:

The remaining pause allowance is calculated from pause history rather than stored independently.

Formula:

remaining_pause_days =
pause_limit_days - total_pause_days_used

Benefits:

* Prevents data inconsistency.
* Maintains complete audit history.
* Supports accurate reporting.
* Eliminates duplicate sources of truth.

Reporting Strategy:

Monthly reports will calculate pause usage from PauseRequest history records rather than a stored remaining_pause_days value.

---


Pricing Snapshot Design

Authoritative Source:

The Subscription record stores a plan_price_snapshot value when the subscription is created.

Reasoning:

Plan prices may change over time.

Existing subscribers should continue using the agreed subscription price until renewal.

This prevents historical invoices from changing when administrators update plan pricing.

Reporting Strategy:

Revenue calculations and invoice generation use plan_price_snapshot rather than the current Plan price.

---

Validations:

* One active subscription per customer.
* End date must be greater than start date.
* Pause limit cannot be negative.

### route.py

Purpose:

Stores delivery routes and route assignments.

---

Field: id

Type:
Integer

Required:
System Generated

Meaning:
Unique identifier for the route.

Validation:

Must be unique.

---

Field: route_name

Type:
String

Required:
Yes

Meaning:
Name of the delivery route.

Validation:

* Cannot be empty.
* Must be unique.

Examples:

* East Vijaynagar
* West Vijaynagar
* Indra Vihar

---

Field: user_id

Type:
Integer (Foreign Key)

Required:
Yes

Meaning:
User assigned to the route.

Validation:

Must reference a User record having role = DELIVERY_BOY.
---

Field: is_active

Type:
Boolean

Required:
No

Default:
True

Meaning:
Indicates whether the route is currently active.

---

Relationships

* One Route → Many Customers
* One Route → Many Deliveries
* One Route → One Delivery Boy

---

Business Rules

* Every route must have one assigned delivery boy.
* Route names must be unique.
* Inactive routes cannot receive new customer assignments.
* Route statistics are generated using delivery records.

---

### delivery.py

Purpose:

Stores daily delivery records and delivery status tracking.

---

Field: id

Type:
Integer

Required:
System Generated

Meaning:
Unique identifier for the delivery.

Validation:

Must be unique.

---

Field: customer_id

Type:
Integer (Foreign Key)

Required:
Yes

Meaning:
Customer receiving the delivery.

Validation:

Must reference an existing customer.

---

Field: route_id

Type:
Integer (Foreign Key)

Required:
Yes

Meaning:
Route assigned for the delivery.

Validation:

Must reference an existing route.

---

Field: status

Type:
String (Enum)

Required:
Yes

Default:
Prepared

Meaning:
Current delivery status.

Allowed Values:

* Prepared
* Out For Delivery
* Delivered
* Failed
* Retry Scheduled
* Missed

---

Field: retry_count

Type:
Integer

Required:
No

Default:
0

Meaning:
Number of retry attempts made for the delivery.

Validation:

* Cannot be negative.
* Maximum allowed value is 1.

---

Field: failure_reason

Type:
String

Required:
No

Meaning:
Reason for delivery failure.

Examples:

* Customer not available
* Incorrect address
* Customer cancelled order

---

Field: delivered_at

Type:
DateTime

Required:
No

Meaning:
Timestamp when delivery was successfully completed.

---

Relationships

* One Customer → Many Deliveries
* One Route → Many Deliveries
* One Delivery → Many DeliveryStatusHistory records

---

Business Rules

* Every delivery must belong to exactly one route.
* Failed deliveries require a failure reason.
* Deliveries can be retried only once.
* Retry deliveries are scheduled for 8:00 PM.
* Delivered deliveries cannot be modified without administrator action.
* Delivery status transitions must follow the defined workflow.

Status Flow:

Prepared → Out For Delivery → Delivered

OR

Prepared → Out For Delivery → Failed

Retry Flow:

Failed → Retry Scheduled → Delivered

OR

Failed → Retry Scheduled → Missed

---
### payment.py

Purpose:

Stores customer payment transactions and payment status information.

---

Field: id

Type:
Integer

Required:
System Generated

Meaning:
Unique identifier for the payment record.

Validation:

Must be unique.

---

Field: customer_id

Type:
Integer (Foreign Key)

Required:
Yes

Meaning:
Customer associated with the payment.

Validation:

Must reference an existing customer.

---

Field: amount

Type:
Decimal(10,2)

Required:
Yes

Meaning:
Amount received from the customer.

Validation:

* Must be greater than zero.
* Stored using Decimal to ensure financial accuracy.

---

Field: payment_method

Type:
String (Enum)

Required:
Yes

Meaning:
Method used to make the payment.

Allowed Values:

* Cash
* UPI
* Khaata

---

Field: payment_date

Type:
DateTime

Required:
System Generated

Meaning:
Timestamp when the payment was recorded.

---

Field: payment_status

Type:
String (Enum)

Required:
Yes

Meaning:
Current status of the payment.

Allowed Values:

* Pending
* Paid
* Failed
* Overdue

Default:

Pending

---

Field: transaction_reference

Type:
String

Required:
No

Meaning:
External reference number for UPI or online transactions.

Examples:

* UTR123456789
* TXN987654321

---

Relationships

* One Customer → Many Payments
* One Payment → One Invoice

---

Business Rules

* Payment amount must be greater than zero.
* Monthly subscribers are billed on the first day of the month.
* Weekly subscribers are billed every Monday.
* Early payments receive a 10% discount.
* Payment reminders are generated five days before due dates.
* Subscriptions with dues exceeding ten days are automatically paused.
* Khaata balances are tracked separately through invoices and payment records.

---

### complaint.py

Purpose:

Stores customer complaints, resolution tracking, severity information, and compensation records.

Fields:

---

Field: id

Type:
Integer

Required:
System Generated

Meaning:
Unique identifier for the complaint.

Validation:
Must be unique.

---

Field: customer_id

Type:
Integer (Foreign Key)

Required:
Yes

Meaning:
Customer who raised the complaint.

Validation:
Must reference an existing customer.

---

Field: category

Type:
String (Enum)

Required:
Yes

Meaning:
Type of complaint submitted.

Allowed Values:

* Late Delivery
* Cold Food
* Wrong Order
* Missing Item
* Taste Complaint
* Other

---

Field: severity

Type:
String (Enum)

Required:
Yes

Meaning:
Determines complaint priority and resolution deadline.

Allowed Values:

* Low
* Medium
* High

---

Field: description

Type:
Text

Required:
Yes

Meaning:
Detailed explanation of the complaint provided by the customer.

Validation:
Cannot be empty.

---

Field: created_at

Type:
DateTime

Required:
System Generated

Meaning:
Timestamp when the complaint was created.

---

Field: resolution_deadline

Type:
DateTime

Required:
System Generated

Meaning:
Deadline by which the complaint must be resolved.

Calculation:

* Low Severity → created_at + 48 hours
* Medium Severity → created_at + 24 hours
* High Severity → created_at + 6 hours

---

Field: status

Type:
String (Enum)

Required:
Yes

Default:
Open

Allowed Values:

* Open
* In Progress
* Resolved
* Closed

Meaning:
Current state of the complaint.

---

Field: compensation

Type:
String

Required:
No

Meaning:
Compensation provided to the customer.

Examples:

* Free next day's tiffin
* 50% discount on next add-on
* No compensation

---

Severity Deadline Mapping

The system will maintain a centralized severity configuration.

Mapping:

* Low → 48 Hours
* Medium → 24 Hours
* High → 6 Hours

Implementation Strategy:

The mapping will be stored in a centralized constants/configuration layer rather than manually entered for each complaint.

Reasoning:

* Keeps business rules consistent.
* Prevents accidental deadline mismatches.
* Simplifies future business rule changes.
* Ensures all complaints follow the same SLA policy.

---

Overdue Complaint Logic

A complaint is considered overdue when:

current_time > resolution_deadline

AND

status is not Resolved or Closed.

The API will calculate overdue status dynamically rather than storing it as a separate database field.

---

Relationships

* One Customer → Many Complaints
* One Complaint → One ComplaintResolution

---

Business Rules

* Every complaint must have a category.
* Every complaint must have a severity level.
* Resolution deadline is automatically calculated.
* Closed complaints cannot be modified without administrator permission.
* Compensation records must be maintained for resolved complaints.

### pause_request.py

Purpose:

Stores customer subscription pause requests and pause history records.

Reason for Separate Model:

PauseRequest records are the authoritative source of truth for pause tracking, reporting, and pause allowance calculations.

---

Field: id

Type:
Integer

Required:
System Generated

Meaning:
Unique identifier for the pause request.

Validation:

Must be unique.

---

Field: subscription_id

Type:
Integer (Foreign Key)

Required:
Yes

Meaning:
Subscription associated with the pause request.

Validation:

Must reference an existing subscription.

---

Field: start_date

Type:
Date

Required:
Yes

Meaning:
Date from which the pause becomes effective.

Validation:

Cannot be before the current date.

---

Field: end_date

Type:
Date

Required:
Yes

Meaning:
Date on which the pause period ends.

Validation:

Must be greater than or equal to start_date.

---

Field: pause_days

Type:
Integer

Required:
System Generated

Meaning:
Total number of pause days requested.

Calculation:

pause_days = end_date - start_date + 1

Validation:

Must be greater than zero.

---

Field: requested_at

Type:
DateTime

Required:
System Generated

Meaning:
Timestamp when the pause request was submitted.

---

Field: status

Type:
String (Enum)

Required:
Yes

Default:
Approved

Meaning:
Current state of the pause request.

Allowed Values:

* Approved
* Rejected
* Cancelled

---

Relationships

* One Subscription → Many PauseRequests

---

Business Rules

* Maximum seven pause days are allowed per billing cycle.
* Unused pause days do not carry forward.
* Additional pause days beyond the limit are forfeited.
* Deliveries must not be generated during approved pause periods.
* Monthly reports calculate pause usage using PauseRequest records.
* Pause history remains permanently available for auditing and reporting.


---

### addon.py

Purpose:

Stores the catalog of add-on items offered by the business.

Reason for Separate Model:

The AddOn model represents available add-on products. Customer-specific purchases are stored separately in AddOnOrder records.

---

Field: id

Type:
Integer

Required:
System Generated

Meaning:
Unique identifier for the add-on item.

Validation:

Must be unique.

---

Field: name

Type:
String

Required:
Yes

Meaning:
Display name of the add-on item.

Validation:

* Cannot be empty.
* Must be unique.

Examples:

* Extra Paneer
* Salad
* Raita
* Kheer

---

Field: price

Type:
Decimal(10,2)

Required:
Yes

Meaning:
Price charged for one unit of the add-on.

Validation:

* Must be greater than zero.
* Stored using Decimal to ensure financial accuracy.

Examples:

50.00

100.00

---

Field: is_active

Type:
Boolean

Required:
No

Default:
True

Meaning:
Indicates whether the add-on is currently available for ordering.

---

Relationships

* One AddOn → Many AddOnOrders

---

Business Rules

* Inactive add-ons cannot be ordered.
* Add-on catalog changes do not affect previously placed AddOnOrder records.
* Add-on revenue calculations are based on AddOnOrder records rather than the catalog.
* Same-day add-on requests must be placed before 9:00 AM.


---

### addon_order.py

Purpose:

Stores customer add-on orders.

Reason for Separate Model:

The AddOn model represents the catalog of available add-ons, while AddOnOrder captures customer-specific purchases and supports cutoff validation, billing, and reporting.

Fields:

---

Field: id

Type:
Integer

Required:
System Generated

Meaning:

Unique identifier for the add-on order.

---

Field: customer_id

Type:
Integer (Foreign Key)

Required:
Yes

Meaning:

Customer who requested the add-on.

---

Field: addon_id

Type:
Integer (Foreign Key)

Required:
Yes

Meaning:

Reference to the add-on catalog item.

---

Field: delivery_date

Type:
Date

Required:
Yes

Meaning:

Date on which the add-on should be delivered.

---

Field: quantity

Type:
Integer

Required:
Yes

Meaning:

Number of add-on units requested.

Validation:

Must be greater than zero.

---

Field: ordered_at

Type:
DateTime

Required:
System Generated

Meaning:

Timestamp when the customer placed the add-on order.

Business Rule:

Orders placed after 9:00 AM are rejected for the same day's delivery.

---

Relationships:

* One Customer → Many AddOnOrders
* One AddOn → Many AddOnOrders

Reporting Strategy:

Monthly revenue reports calculate add-on income using AddOnOrder records rather than the AddOn catalog.

---

### invoice.py

Purpose:

Stores billing records generated for customer subscriptions.

Reason for Separate Model:

Invoices represent billing snapshots and preserve financial history independently of payments and subscription changes.

---

Field: id

Type:
Integer

Required:
System Generated

Meaning:
Unique identifier for the invoice.

Validation:

Must be unique.

---

Field: customer_id

Type:
Integer (Foreign Key)

Required:
Yes

Meaning:
Customer associated with the invoice.

Validation:

Must reference an existing customer.

---

Field: billing_period

Type:
String

Required:
Yes

Meaning:
Billing cycle covered by the invoice.

Examples:

* June 2026
* Week 24, 2026

---

Field: invoice_amount

Type:
Decimal(10,2)

Required:
Yes

Meaning:
Original amount before discounts.

Validation:

Must be greater than zero.

---

Field: discount_amount

Type:
Decimal(10,2)

Required:
No

Default:
0.00

Meaning:
Total discount applied to the invoice.

Examples:

* Early payment discount
* Referral discount

---

Field: final_amount

Type:
Decimal(10,2)

Required:
Yes

Meaning:
Amount payable after applying discounts.

Formula:

final_amount =
invoice_amount - discount_amount

Validation:

Must be greater than or equal to zero.

---

Field: payment_status

Type:
String (Enum)

Required:
Yes

Default:
Pending

Meaning:
Current payment state of the invoice.

Allowed Values:

* Pending
* Paid
* Overdue
* Cancelled

---

Field: generated_at

Type:
DateTime

Required:
System Generated

Meaning:
Timestamp when the invoice was generated.

---

Relationships

* One Customer → Many Invoices
* One Invoice → Many Payments

---

Business Rules

* Monthly subscribers are billed on the first day of each month.
* Weekly subscribers are billed every Monday.
* Early payments receive a 10% discount.
* Referral rewards provide a 5% discount.
* Discounts are applied before final amount calculation.
* Historical invoices remain unchanged after plan price modifications.
* Invoices are generated using the subscription's plan_price_snapshot value.


---

### referral.py

Purpose:

Stores customer referral relationships and referral reward eligibility.

Reason for Separate Model:

Referral records track referral history independently from billing and customer records to support reward validation and fraud prevention.

---

Field: id

Type:
Integer

Required:
System Generated

Meaning:
Unique identifier for the referral record.

Validation:

Must be unique.

---

Field: referrer_customer_id

Type:
Integer (Foreign Key)

Required:
Yes

Meaning:
Customer who made the referral.

Validation:

Must reference an existing customer.

---

Field: referred_customer_id

Type:
Integer (Foreign Key)

Required:
Yes

Meaning:
Customer who was referred.

Validation:

Must reference an existing customer.

---

Field: referral_status

Type:
String (Enum)

Required:
Yes

Default:
Pending

Meaning:
Current status of the referral.

Allowed Values:

* Pending
* Eligible
* Reward Applied
* Rejected

---

Field: reward_applied

Type:
Boolean

Required:
No

Default:
False

Meaning:
Indicates whether the referral reward has been granted.

---

Field: created_at

Type:
DateTime

Required:
System Generated

Meaning:
Timestamp when the referral was created.

---

Relationships

* One Customer → Many Referrals Made
* One Customer → Many Referrals Received

---

Business Rules

* Customers cannot refer themselves.
* Referral rewards are granted only after the referred customer completes their first paid month.
* Referral discounts provide a 5% billing discount.
* Fraudulent or duplicate referrals may be rejected by administrators.
* Referral rewards can only be applied once per successful referral.


---

### customer_document.py

Purpose:

Stores identity documents uploaded by customers.

Reason for Separate Model:

Customer documents are managed independently from customer profiles to support secure storage and multiple document uploads.

---

Field: id

Type:
Integer

Required:
System Generated

Meaning:
Unique identifier for the document record.

Validation:

Must be unique.

---

Field: customer_id

Type:
Integer (Foreign Key)

Required:
Yes

Meaning:
Customer associated with the document.

Validation:

Must reference an existing customer.

---

Field: document_type

Type:
String (Enum)

Required:
Yes

Meaning:
Type of identity document uploaded.

Allowed Values:

* Aadhaar
* Driving License

---

Field: file_path

Type:
String

Required:
Yes

Meaning:
Storage path of the uploaded document.

Validation:

Cannot be empty.

---

Field: uploaded_at

Type:
DateTime

Required:
System Generated

Meaning:
Timestamp when the document was uploaded.

---

Relationships

* One Customer → Many CustomerDocuments

---

Business Rules

* Document uploads are optional.
* Unsupported file formats are rejected.
* Customers may upload multiple documents.
* Documents should only be accessible to authorized users.
* Document paths must remain valid even if customer profile information changes.


---

### delivery_status_history.py

Purpose:

Stores the history of delivery status changes for audit and reporting purposes.

Reason for Separate Model:

Delivery records store only the current status, while DeliveryStatusHistory preserves every status transition.

---

Field: id

Type:
Integer

Required:
System Generated

Meaning:
Unique identifier for the status history record.

Validation:

Must be unique.

---

Field: delivery_id

Type:
Integer (Foreign Key)

Required:
Yes

Meaning:
Delivery associated with the status change.

Validation:

Must reference an existing delivery.

---

Field: old_status

Type:
String (Enum)

Required:
Yes

Meaning:
Previous status of the delivery.

Allowed Values:

* Prepared
* Out For Delivery
* Delivered
* Failed
* Retry Scheduled
* Missed

---

Field: new_status

Type:
String (Enum)

Required:
Yes

Meaning:
Updated status of the delivery.

Allowed Values:

* Prepared
* Out For Delivery
* Delivered
* Failed
* Retry Scheduled
* Missed

---

Field: changed_at

Type:
DateTime

Required:
System Generated

Meaning:
Timestamp when the status change occurred.

---

Field: changed_by

Type:
Integer (Foreign Key)

Required:
Yes

Meaning:
User who performed the status update.

Validation:

Must reference an existing User record.

---

Relationships

* One Delivery → Many DeliveryStatusHistory records
* One User → Many DeliveryStatusHistory records

---

Business Rules

* Every delivery status change must be recorded.
* Status history records are immutable.
* Administrators may override delivery statuses.
* Audit trails must remain available for reporting and troubleshooting.
* Historical status changes are used for delivery analytics.


---

### complaint_resolution.py

Purpose:

Stores complaint resolution details and compensation records.

Reason for Separate Model:

The Complaint model stores the complaint itself, while ComplaintResolution stores how the complaint was resolved and what compensation was provided.

---

Field: id

Type:
Integer

Required:
System Generated

Meaning:
Unique identifier for the complaint resolution record.

Validation:

Must be unique.

---

Field: complaint_id

Type:
Integer (Foreign Key)

Required:
Yes

Meaning:
Complaint associated with this resolution.

Validation:

Must reference an existing complaint.

---

Field: resolution_notes

Type:
Text

Required:
Yes

Meaning:
Description of the action taken to resolve the complaint.

Validation:

Cannot be empty.

Examples:

* Customer contacted and replacement meal provided.
* Delivery timing issue explained and compensated.

---

Field: compensation_provided

Type:
String

Required:
No

Meaning:
Compensation granted to the customer.

Examples:

* Free next day's tiffin.
* 50% discount on next add-on.
* No compensation.

---

Field: resolved_at

Type:
DateTime

Required:
System Generated

Meaning:
Timestamp when the complaint was resolved.

---

Field: resolved_by

Type:
Integer (Foreign Key)

Required:
Yes

Meaning:
Administrator who resolved the complaint.

Validation:

Must reference an existing User record.

---

Relationships

* One Complaint → One ComplaintResolution
* One User → Many ComplaintResolution records

---

Business Rules

* Every resolved complaint must have resolution notes.
* Compensation records must be preserved for reporting.
* Complaint resolutions are immutable after closure.
* Resolution information is used in monthly complaint analytics.
* Closed complaints cannot be modified without administrator permission.


---

### payment_reminder.py

Purpose:

Stores records of payment reminders sent to customers.

Reason for Separate Model:

Payment reminders are stored independently to maintain reminder history and support billing analytics.

---

Field: id

Type:
Integer

Required:
System Generated

Meaning:
Unique identifier for the payment reminder.

Validation:

Must be unique.

---

Field: customer_id

Type:
Integer (Foreign Key)

Required:
Yes

Meaning:
Customer receiving the payment reminder.

Validation:

Must reference an existing customer.

---

Field: reminder_date

Type:
DateTime

Required:
System Generated

Meaning:
Timestamp when the reminder was generated or sent.

---

Field: reminder_type

Type:
String (Enum)

Required:
Yes

Meaning:
Type of reminder sent to the customer.

Allowed Values:

* Upcoming Due Reminder
* Overdue Reminder
* Auto-Pause Warning

---

Field: status

Type:
String (Enum)

Required:
Yes

Default:
Sent

Meaning:
Current state of the reminder.

Allowed Values:

* Pending
* Sent
* Failed

---

Relationships

* One Customer → Many PaymentReminders

---

Business Rules

* Payment reminders are generated five days before the due date.
* Customers with overdue balances exceeding ten days receive auto-pause warnings.
* Reminder history is retained for audit and reporting purposes.
* Failed reminder attempts may be retried.
* Reminder records do not modify invoice or payment data.


---

### monthly_report.py

Purpose:

Stores generated monthly operational reports and summary statistics.

Reason for Separate Model:

Monthly reports provide historical business insights and preserve reporting snapshots independently of live operational data.

---

Field: id

Type:
Integer

Required:
System Generated

Meaning:
Unique identifier for the monthly report.

Validation:

Must be unique.

---

Field: report_month

Type:
String

Required:
Yes

Meaning:
Month and year covered by the report.

Examples:

* June 2026
* July 2026

Validation:

Cannot be empty.

---

Field: total_tiffins_served

Type:
Integer

Required:
Yes

Meaning:
Total number of tiffins delivered during the reporting period.

Validation:

Must be greater than or equal to zero.

---

Field: total_revenue

Type:
Decimal(10,2)

Required:
Yes

Meaning:
Total revenue generated during the reporting period.

Validation:

Must be greater than or equal to zero.

---

Field: total_complaints

Type:
Integer

Required:
Yes

Meaning:
Number of complaints registered during the reporting period.

Validation:

Must be greater than or equal to zero.

---

Field: total_pause_requests

Type:
Integer

Required:
Yes

Meaning:
Number of subscription pauses recorded during the reporting period.

Validation:

Must be greater than or equal to zero.

---

Field: top_delivery_boy_id

Type:
Integer (Foreign Key)

Required:
No

Meaning:
Delivery personnel with the highest successful delivery count.

---

Field: generated_at

Type:
DateTime

Required:
System Generated

Meaning:
Timestamp when the report was generated.

---

Relationships

* Monthly reports aggregate information from Deliveries, Payments, Complaints, and PauseRequests.
* One Delivery Boy may appear in many monthly reports.

---

Business Rules

* Reports are generated once per month.
* Reports use finalized operational data.
* Historical reports remain immutable after generation.
* Revenue statistics use invoice and payment records.
* Complaint statistics use complaint and complaint resolution records.
* Pause statistics are calculated from PauseRequest history.
* Delivery performance metrics are calculated from delivery records.


## 11.4 Schema Layer

### CustomerCreate

Purpose:

Validate customer creation requests.

Fields:

* full_name
* phone_number
* address
* diet_type

Validation:

* Name required.
* Phone required.
* Address required.

---

### CustomerUpdate

Purpose:

Validate customer update requests.

Fields:

* full_name
* address
* diet_type

---

### SubscriptionCreate

Purpose:

Validate subscription creation.

Fields:

* customer_id
* plan_id
* start_date

---

### DeliveryUpdate

Purpose:

Validate delivery status updates.

Fields:

* delivery_id
* status
* failure_reason

---

### ComplaintCreate

Purpose:

Validate complaint registration.

Fields:

* customer_id
* category
* severity
* description

---

## 11.5 Service Layer

### customer_service.py

Functions:

create_customer()

Responsibilities:

* Validate customer data.
* Check duplicate phone number.
* Save customer.

Parameters:

* customer_data

Returns:

* Customer object

---

update_customer()

Responsibilities:

* Update customer information.

Parameters:

* customer_id
* update_data

Returns:

* Updated customer

---

deactivate_customer()

Responsibilities:

* Mark customer inactive.

Parameters:

* customer_id

Returns:

* Success message

---

### subscription_service.py

Functions:

create_subscription()

renew_subscription()

pause_subscription()

resume_subscription()

cancel_subscription()

Responsibilities:

* Manage complete subscription lifecycle.

---

### delivery_service.py

Functions:

generate_daily_deliveries()

assign_route()

update_delivery_status()

retry_failed_delivery()

Responsibilities:

* Manage delivery operations.

---

### payment_service.py

Functions:

generate_invoice()

record_payment()

apply_discount()

send_payment_reminder()

Responsibilities:

* Manage billing workflow.

---

### complaint_service.py

Functions:

create_complaint()

assign_severity()

resolve_complaint()

record_compensation()

Responsibilities:

* Manage complaint lifecycle.

---

### report_service.py

Functions:

generate_monthly_report()

calculate_revenue()

calculate_delivery_statistics()

Responsibilities:

* Generate business reports.

---

## 11.6 Router Layer

### auth.py

Endpoints:

* POST /login
* POST /logout

---

### customers.py

Endpoints:

* POST /customers
* GET /customers
* GET /customers/{id}
* PUT /customers/{id}
* DELETE /customers/{id}

---

### plans.py

Endpoints:

* POST /plans
* GET /plans
* PUT /plans/{id}

---

### subscriptions.py

Endpoints:

* POST /subscriptions
* GET /subscriptions
* POST /subscriptions/pause
* POST /subscriptions/resume

---

### deliveries.py

Endpoints:

* GET /deliveries
* PUT /deliveries/{id}/status
* POST /deliveries/retry

---

### payments.py

Endpoints:

* POST /payments
* GET /payments
* GET /invoices

---

### complaints.py

Endpoints:

* POST /complaints
* GET /complaints
* PUT /complaints/{id}/resolve

---

### reports.py

Endpoints:

* GET /reports/monthly
* GET /reports/dashboard

---

## 11.7 Validation Strategy

The system will enforce the following validations:

* Phone number must be unique.
* One active subscription per customer.
* Pause duration cannot exceed seven days.
* Add-ons must be requested before 9:00 AM.
* Payment reminders must be generated automatically.
* Failed deliveries require a failure reason.
* Complaint severity must be valid.
* Route assignment must exist before delivery generation.
* Customer documents must be valid file types.
* Referral rewards cannot be self-generated.

---

## 11.8 API Summary

Estimated API Modules:

* Authentication APIs
* Customer APIs
* Plan APIs
* Subscription APIs
* Delivery APIs
* Payment APIs
* Complaint APIs
* Report APIs

Total Estimated Endpoints: 35–50 APIs

```
```


## 12. Future Enhancements

The following features are outside the current scope but may be considered in future versions:

* Mobile application for customers
* Mobile application for delivery personnel
* Real-time delivery tracking
* SMS notifications
* WhatsApp integration
* Online payment gateway integration
* GPS route optimization
* Inventory management integration
* AI-based demand forecasting

---

## 13. Definition of Done (V1)

The V1 release will be considered complete only when all of the following conditions are satisfied.

### 13.1 Customer Management

1. POST /customers creates a customer successfully and returns HTTP 201.

2. GET /customers/{id} returns customer details including route assignment and diet preference.

3. Duplicate phone numbers are rejected with HTTP 409 Conflict.

4. Customer identity documents can be uploaded and linked to the customer profile.

---

### 13.2 Subscription Management

5. POST /subscriptions creates a subscription successfully.

6. The system prevents multiple active subscriptions for the same customer.

7. POST /subscriptions/pause records a pause request.

8. Pause requests exceeding seven days per billing cycle are rejected.

9. Subscription pricing remains unchanged after a plan price update due to the stored plan_price_snapshot value.

---

### 13.3 Delivery Management

10. Daily deliveries can be generated automatically for active subscriptions.

11. Delivery status can transition from Prepared → Out For Delivery → Delivered.

12. Failed deliveries require a failure reason.

13. Failed deliveries can be retried once.

14. Delivery personnel can only view deliveries assigned to their route.

---

### 13.4 Billing and Payments

15. Invoices can be generated for active subscriptions.

16. Payment records can be created using Cash, UPI, or Khaata.

17. Early-payment discounts are applied correctly.

18. Referral discounts are applied only after referral eligibility requirements are met.

19. Payment reminders can be generated for upcoming due dates.

---

### 13.5 Complaint Management

20. POST /complaints creates a complaint successfully.

21. Complaint severity automatically generates the correct resolution deadline.

22. Low severity complaints receive a 48-hour deadline.

23. Medium severity complaints receive a 24-hour deadline.

24. High severity complaints receive a 6-hour deadline.

25. Overdue complaints are identified correctly by the system.

---

### 13.6 Reporting and Dashboard

26. Monthly reports can be generated through the reporting module.

27. Reports include revenue, complaints, pause statistics, and delivery statistics.

28. Dashboard endpoint returns daily operational metrics.

29. Dashboard displays delivery counts grouped by status.

30. Dashboard displays route-wise delivery statistics.

---

### 13.7 API Quality

31. All APIs appear in FastAPI OpenAPI documentation.

32. Request validation errors return HTTP 422.

33. Unauthorized access returns HTTP 401.

34. Forbidden role access returns HTTP 403.

35. Automated test suite passes successfully before release.

---

### Release Approval Condition

V1 is considered complete only when all Definition of Done items pass manual testing and automated testing without critical defects.


---

## Conclusion

The Saanjh Ki Roti API aims to replace manual notebook-based operations with a centralized digital platform. The proposed architecture focuses on operational efficiency, accurate delivery tracking, billing automation, complaint management, and business visibility while providing a scalable foundation for future growth.
