# Design Document Review: The Bend Bike Shop Rental System (WIP)

## Executive Summary
This design document provides a solid foundation for the Bend Bike shop rental system, establishing clear boundaries (goals vs. non-goals) and capturing core actors and constraints. However, there are several logical contradictions, architectural gaps, and workflow ambiguities between the **Constraints**, **Actors**, **Assumptions**, and the **Mermaid diagram**. 

The findings below are categorized by severity and impact to help refine the document before implementation.

---

## 1. Critical Logical & Constraint Conflicts

### A. Pre-Authorization vs. Payment Timing
* **Conflict:** The **Constraints** state: *"Payment must be charged **after** the bike is returned."* However, the **Goals** state: *"Pre-authorize users to ensure their card won't decline,"* and the **Assumptions** state: *"The pre-authorization from the payment processor doesn't result in a nonzero charge..."*
* **Issue:** While credit card pre-authorizations are common in rentals (holding a temporary pending amount), the document lacks clarity on *when* this pre-auth occurs (presumably at the start of the rental) versus when the actual capture/charge happens (after return). 
* **Recommendation:** Clarify the payment lifecycle explicitly: 
  1. Pre-authorization at rental creation.
  2. Final charge captured upon return (including base rental + late fees).

### B. Cash Payment Workflow Gap
* **Conflict:** The **Actors** and **Assumptions** note that employees can handle cash payments ("Handles cash payments", "Some customers may pay in cash"). However, the **Component Diagram** and description do not account for cash handling, cash drawers, or bypassing the `Payment Wrapper` / `Payment Processor` for cash transactions.
* **Recommendation:** Update the `Payment Wrapper` or add a component/flow to handle cash transactions where no external API call is made, marking the rental as paid via cash in the database.

### C. Multi-Day Pricing Rule Ambiguity
* **Constraint:** *"When users pay for multiple days, they only pay for 12 hours each day (2 days is 24 hours of time paid)"*
* **Issue:** This pricing logic is highly specific and unconventional. It implies a daily cap or discounted tier. However, it contradicts the constraint that *"Rental time periods are on 4 hour increments (4 hours, 8 hours, 12 hours, etc.)"* and there is no mention of how the `Rental Logic Unit` or pricing engine calculates this.
* **Recommendation:** Explicitly define the formula for multi-day rentals and rate structures (e.g., *“Hourly rate applies up to 12 hours per calendar day, after which the daily cap is reached”*).

---

## 2. Architectural & Diagram Discrepancies

### A. Missing Cash Path in Flowchart
* **Issue:** In the Mermaid diagram, the `Employee Dashboard` connects directly to `Payment Wrapper`. If an employee accepts cash, the flow incorrectly forces a route through the `Payment Wrapper` / `Payment Processor`.
* **Recommendation:** Split or branch the `Employee Dashboard` flow to show cash payments resolving locally via the database/logic unit, while card payments route through the `Payment Wrapper`.

### B. Kiosk Payment & Card Swiping Flow
* **Issue:** The `Kiosk Interface` allows customers to "Swipe card" and "Enter card information", but the Mermaid diagram does not show how the `Kiosk Interface` connects to the `Payment Wrapper` or `Payment Processor`. Currently, it only navigates to the `Bike Catalog Page`.
* **Recommendation:** Add connection paths from the `Kiosk Interface` (and `Web Dashboard`) to the `Payment Wrapper` during the checkout/rental phase.

### C. Late Fee Calculation Loop
* **Issue:** The Mermaid diagram shows `ED <-->|IF LATE: Adjusts fee| LFC`. However, the `Late Fee Calculator` component description says *"Adjusts the amount due automatically when the bike is late,"* while the actor/constraints state employees adjust it manually. 
* **Recommendation:** Clarify the division of labor: Does the `Late Fee Calculator` automatically compute the accrued fee, and the employee *reviews/adjusts* it before final charge? Update the diagram arrow to reflect this unidirectional or supervisory relationship.

---

## 3. Edge Cases & Missing Non-Functional Requirements

### A. Kiosk Offline Fallback Execution
* **Fallback Requirement:** *"If the kiosk loses connection, it should prompt the user to complete their transaction with an employee"*
* **Issue:** If a kiosk loses connection mid-transaction or right before payment, how is state handled? Does the partial reservation persist so the employee can pull it up, or is the user forced to start over?
* **Recommendation:** Specify a synchronization or local session-cache mechanism for offline kiosk states.

### B. Security & PII Scope
* **Security Requirement:** *"Any payment information is promptly deleted upon the transaction being completed"*
* **Issue:** PCI-DSS compliance dictates that card data should generally not even touch application servers unless strictly necessary (tokenization via the payment processor is standard). Storing and then deleting card data opens up unnecessary compliance overhead.
* **Recommendation:** Specify the use of tokenization (e.g., Stripe/Payment Processor tokens) rather than raw card data handling, satisfying the intent of not retaining sensitive payment data.

---

## 4. Suggested Document Structure Additions
To make this a complete production-ready design doc, consider adding:
1. **Data Models / Schema Outline:** Basic entities for `User`, `Bike`, `Rental`, `Transaction`, and `LateFee`.
2. **State Machine:** A clear state diagram for a `Bike` (Available -> Reserved -> Rented -> Late -> Maintenance/Returned).