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

* User
* Customer
* DeliveryBoy
* Route
* Plan
* Subscription
* PauseRequest
* Delivery
* Payment
* Complaint
* AddOn
* Invoice
* Referral
* CustomerDocument

### Supporting Entities

* DeliveryStatusHistory
* PaymentReminder
* ComplaintResolution
* MonthlyReport

These entities may evolve during implementation as additional business requirements are discovered.

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

## 11. Development Phases

### Phase 1: Foundation

* Project setup
* Authentication system
* User management
* Customer management

### Phase 2: Subscription System

* Plans
* Subscriptions
* Pause management
* Add-on management

### Phase 3: Delivery Operations

* Routes
* Delivery assignment
* Delivery status tracking
* Retry handling

### Phase 4: Billing and Complaints

* Invoice generation
* Payment tracking
* Referral management
* Complaint management

### Phase 5: Reporting and Dashboard

* Dashboard statistics
* Monthly reporting
* PDF generation
* Analytics

### Phase 6: Customer Self-Service

* Customer portal APIs
* Pause requests
* Complaint submission
* Bill viewing

---

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

## 13. Acceptance Criteria

The project will be considered successful if:

* Customer subscriptions can be managed digitally.
* Deliveries can be tracked by status.
* Billing and payments are recorded accurately.
* Complaints are logged and resolved through the system.
* Monthly reports can be generated automatically.
* Administrators can view operational statistics through a dashboard.
* Customers can pause subscriptions without manual intervention.
* Delivery personnel can update delivery statuses for their assigned routes.

---

## Conclusion

The Saanjh Ki Roti API aims to replace manual notebook-based operations with a centralized digital platform. The proposed architecture focuses on operational efficiency, accurate delivery tracking, billing automation, complaint management, and business visibility while providing a scalable foundation for future growth.
