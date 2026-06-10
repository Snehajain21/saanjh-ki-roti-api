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
