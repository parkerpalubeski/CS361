# Design Document Review & Critique

This review evaluates the partial design document for the Bend Bike Shop rental system as a **Professional System Design Specification** (target audience: software engineering team, product managers, and stakeholders; goal: provide a robust, consistent, and implementable architecture blueprint). 

**Overall Assessment:** **Developing**
The document shows strong foundational work—particularly in defining actors, setting clear non-goals, outlining Mermaid diagrams, and providing F# signature examples. However, it suffers from several critical logical contradictions, structural inconsistencies between the components and data models, and mismatched signature definitions that need resolution before development can begin.

---

## Evaluation & Feedback

### 1. Logical Inconsistencies & Constraint Violations
*   **Constraint vs. Flow Mismatch (Payment Timing):** The constraints state that *"Payment must be charged after the bike is returned,"* but the Goals section mentions, *"Pre-authorize users to ensure their card won't decline,"* and the Component Diagram shows `RLU` calling `PW` for a pre-authorization during the rental phase. While pre-authorization holds funds rather than capturing them, the interface definitions (`executeCharge()`, `createReservation()`) do not explicitly model a two-step auth/capture workflow. 
    *   *Action:* Clarify how pre-authorization and final settlement interact in the `Card` class and interface definitions so that payment capture strictly occurs post-return.
*   **Rental Duration Logic Conflict:** Under Constraints, it notes: *"Rental time periods are on 4 hour increments (4 hours, 8 hours, 12 hours, etc.)"* and *"When users pay for multiple days, they only pay for 12 hours each day."* However, the ER and Class diagrams model `Order` with a simple integer `duration` field without units or fractional day handling, and the reservation interface accepts a `DateRange` rather than hourly increments. 
    *   *Action:* Reconcile how hourly increments vs. multi-day caps are calculated and passed into the data model.

### 2. Structural & Interface Mismatches
*   **F# Type Signature Typos and Inconsistencies:** 
    *   In `searchInventory`, the parameter is typed as `DateRangee` (with a double `ee`), whereas the type definition earlier is `DateRange`.
    *   In `adjustLateFee`, the parameter `orderId` is typed as `OrderIDd` instead of `OrderId`.
    *   In `updateRentalRates`, `managerId` uses `ManagerID` instead of `ManagerId`.
    *   *Action:* Standardize type names across all F# code snippets to prevent compilation and parsing confusion.
*   **Missing Payment Wrapper in Sequence/Component Flow:** The Component Description lists a "Payment Wrapper" component, but the Mermaid flowchart shows `RLU` directly calling `PW`, and the Class diagram has `Card` methods (`preAuthorize`, `executeCharge`) directly on the `Card` class. 
    *   *Action:* Unify the payment abstraction layer across the component description, flowchart, and class diagram.

### 3. Missing Specifications & Ambiguities
*   **Cash Payment Handling Gap:** The Actor section states that Employees handle cash payments, and Assumptions note some customers pay in cash, but cash handling is entirely absent from the Data Model, Component flows, and F# interfaces (which focus strictly on electronic card flows).
    *   *Action:* Add a cash transaction handling flow or method to the Employee components and Order data models.
*   **Kiosk Offline Fallback Details:** The Non-Functional Requirements and Failure Modes mention prompting the user to see an employee if the kiosk loses connection. However, the system state handling for half-completed local kiosk transactions is underspecified.
    *   *Action:* Define how partial reservation states are synced or discarded when a kiosk reconnects or fails over to an employee.

---

## Suggested Edits

<comment-tag>Consider updating the `duration` field in the `Order` class to an explicit unit (e.g., `hours: Integer`) to support the 4-hour increment constraint.</comment-tag>

<comment-tag>Fix the typo `DateRangee` in the `searchInventory` function signature to match `DateRange`.</comment-tag>

---
