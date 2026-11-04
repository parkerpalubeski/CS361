# Design Doc (AI)
## Overview
The Bend Bike shop is a store that rents bikes out to customers. They are looking to create a web-based software interface where customers can reserve bike rentals, either online (such as through a browser) or through a kiosk in the store, backed by a centralized relational database and secure payment processor integration.

## Actors
- **Customer**
- Queries bike catalog via web browser or kiosk interface
- Filters inventory by size, category, and date range
- Selects and reserves bikes
- Enters contact and payment card information
- Swipes card at kiosk or saves tokenized card online
- Modifies reservations (subject to time-window rules)
- **Employee**
- Authenticates via employee dashboard
- Views active rentals and late return alerts
- Marks bikes as returned and triggers condition inspection status
- Manually adjusts late fees and handles cash transactions
- **Management**
- Accesses admin portal / management dashboard
- Approves or declines refund requests
- Updates rate management settings (e.g., seasonal/holiday pricing by category)
- Views summary reports and analytics
- **Payment Processor (external)**
- Verifies card information via secure API gateway
- Conducts pre-authorization holds without immediate capture
- Executes final post-return charges and refund transactions

## Goals/Non-Goals
### Goals
- Display real-time available bike inventory filtered by category and attributes (e.g., size, type)
- Allow bikes to be reserved and rented, marking them as unavailable/occupied in the database
- Allow bikes to be added, removed, or marked unavailable manually by employees
- Support flexible rental time intervals and seasonal rate adjustments via an admin portal
- Allow employees to assess and manually adjust late fees
- Pre-authorize user payment cards to ensure validity and prevent declines upon return
- Support online reservation modifications (date/time shifts) outside of a 24-hour cutoff window without penalty
- Handle multi-day billing rules capped at a maximum of 12 hours per calendar day

### Non-goals
- The system does *not* include functionality for purchasing a bike or gear. Rentals only
- The system should *not* include advertisements within the app, or outside of the app (as that is outside of our parameters)
- The system does not need to include automatic discount systems
- The system will not require automated blacklisting of individuals. That process is manual
- Automated cancellation of future rentals due to limited stock is *not* necessary at least according to the client

## Constraints
- Payment must be captured *after* the bike is returned (following pre-authorization at checkout)
- A late fee is assessed automatically by the system when a bike exceeds its scheduled return window
- Adjustments to late fees can be manually overridden by authorized employees
- Rental time periods operate on 4-hour increments (4 hours, 8 hours, 12 hours, etc.)
- Multi-day billing rule: Users are billed for a maximum of 12 hours per calendar day (e.g., a 2-day rental equates to 24 hours of billed time)
- Reservation modifications made outside of a 24-hour cutoff window incur no penalty fees

## Assumptions
- The external payment processor API maintains high availability with negligible downtime
- All monetary transactions are processed in USD
- Cash payment workflows are supported for local checkout, requiring manual reconciliation by staff
- In-store kiosks maintain a stable network connection (with fallback workflows for offline states)
- Payment card pre-authorization holds do not trigger unintended transaction fees for the business or customer

## Non-functional requirements
- **Performance:** The bike catalog page must query the database and render available inventory in under 2 seconds under normal network conditions
- **Reliability:** The web application and backend services must maintain $\ge 99\%$ uptime; kiosks must remain operational during store business hours
- **Security:** Payment card data must comply with PCI-DSS standards; raw card details must be promptly tokenized and purged upon transaction completion
- **Scalability:** The server infrastructure must simultaneously handle concurrent traffic from the public web app and multiple in-store kiosks without performance degradation
- **Fallback:** If an in-store kiosk loses network connectivity, the interface must gracefully prompt the user to complete their transaction with an employee at the counter

## Components
| Component          |  Description                                                                                         |
|--------------------|------------------------------------------------------------------------------------------------------|
|Kiosk interface     | A specialized interface that includes touch screen capability and hardware integration (card readers)|
|Web dashboard       | An interface for users connecting on PC or phone.                                                    |
|Admin Portal / Management Dashboard | Interface for management to configure seasonal/holiday pricing, view summary reports, and issue refunds |
|Bike Catalog Page   | Displays bikes from the database with category, size, and attribute filters                          |
|Bike Database       | Stores relational data on inventory, rates, active rentals, and customer reservation history         |
|Rental logic unit   | Logical unit that enforces pricing constraints, time increments (4-hr blocks), 12-hr multi-day billing rules, and inventory locking |
|Payment processor   | External API that processes secure transactions and pre-authorization holds                          |
|Payment Wrapper     | Logical unit that determines transaction types, interfaces with tokenization, and handles charge capture/refunds |
|Employee dashboard  | Displays active rentals, late return alerts, condition inspection prompts, and manual fee adjustment controls |
|Late Fee Calculator | Automatically computes fees when bikes exceed scheduled return windows subject to employee overrides |
|Reservation Manager | Enforces the 24-hour modification cutoff window and processes customer-initiated schedule changes    |

## Diagram
```mermaid
    flowchart TD
        WD[Web Dashboard]
        KI[Kiosk Interface]
        AP[Admin Portal / Mgmt. Dashboard]
        BCP[Bike Catalog Page]
        BD[(Bike Database)]
        RLU[Rental Logic Unit]
        PP[External Payment Processor]
        PW[Payment Wrapper / Tokenizer]
        ED[Employee Dashboard]
        LFC[Late Fee Calculator]
        RM[Reservation Manager]

        WD -->|Navigates / Searches| BCP
        KI -->|Navigates / Searches| BCP
        AP -->|Updates rates & views reports| BD
        BCP -->|Queries inventory & rates| BD
        BD -->|Returns inventory data| BCP
        BCP -->|Submits reservation| RLU
        
        WD -->|Requests modification (>24h window)| RM
        RM -->|Validates & updates schedule| RLU
        
        RLU -->|Requests pre-authorization| PW
        RLU -->|Marks bike unavailable| BD
        
        BD -->|Fetches active rentals| ED
        ED -->|Marks bike returned / available| BD
        LFC -->|Computes automatic late fee| ED
        ED -->|Submits manual fee adjustments| LFC
        ED -->|Triggers final charge capture| PW
        
        AP -->|Issues refund request| PW
        
        PW <-->|API Calls / Secure Handshake| PP
```