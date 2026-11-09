# Estimation
### WBS Tree
* Bend Bike Shop Rental System
    * Project Management
        * Planning and Scheduling (2, 4, 8)
        * Reporting (1, 3, 6)
    * Requirements and Design 
        * Requirements gathering (3, 6 12)
        * Prototyping (4, 8, 15)
        * Architecture and database design (3, 7, 14)
    * Kiosk Interface
        * Greeting screen (1, 2, 4)
        * Hardware Integration (5, 10 20)
        * Web integration(3, 6, 12)
    * Web Interface
        * Bike catalog page (2, 5, 10)
        * Individual bike Page (2, 4, 8)
        * Cart page (2, 5, 9)
    * Rental Logic Unit
        * Date validation (1, 3, 6)
        * Inventory state management (4, 8, 16)
        * Pricing Constraints (2, 5, 10)
    * Late Fee Calculator
        * Automatic late calculation (2, 4, 8)
        * Manual staff adjustment (1, 3, 6)
    * Payment Wrapper
        * Processor API Integration (3, 7, 14)
        * Card pre-authorization (2, 5, 10)
        * Execution of final, adjusted charges (2, 5, 10)
        * Automated Data Deletion (1, 3, 7)
    * Employee/Management Dashboards
        * Rental Tracking (3, 6, 12)
        * Bike availability settings (2, 4, 8)
        * Rate settings (1, 3, 6)
        * Refund Approval (2, 4, 8)
        * Summary Reports (3, 6, 12)
    * Testing
        * Automated Testing (e.g. github actions) (4, 8, 16)
        * Usability Testing (2, 5, 10)
        * Security Testing (3, 7, 10)
### Monte Carlo Simulation
p90 = ~ 78.2 days 
Assuming that the major development tasks run in parallel.

# Scheduling
### CPM Table
| Task ID | Task                                      | Duration | Dependencies                  | ES     | EF     | LS     | LF     | Slack  |
|---------|-------------------------------------------|----------|-------------------------------|--------|--------|--------|--------|--------|
| PM1     | Planning and Scheduling                   | 4.333    | —                             | 0.000  | 4.333  | 0.000  | 4.333  | 0.000  |
| RD1     | Requirements gathering                    | 6.500    | PM1                           | 4.333  | 10.833 | 4.333  | 10.833 | 0.000  |
| RD2     | Prototyping                               | 8.500    | RD1                           | 10.833 | 19.333 | 10.833 | 19.333 | 0.000  |
| RD3     | Architecture and database design          | 7.500    | RD2                           | 19.333 | 26.833 | 19.333 | 26.833 | 0.000  |
| KI1     | Greeting screen                           | 2.167    | RD3                           | 26.833 | 29.000 | 32.166 | 34.333 | 5.333  |
| KI2     | Hardware Integration                      | 10.833   | KI1                           | 29.000 | 39.833 | 34.333 | 45.166 | 5.333  |
| KI3     | Web integration                           | 6.500    | KI2                           | 39.833 | 46.333 | 45.166 | 51.666 | 5.333  |
| WI1     | Bike catalog page                         | 5.333    | RD3                           | 26.833 | 32.166 | 36.833 | 42.166 | 10.000 |
| WI2     | Individual bike Page                      | 4.333    | WI1                           | 32.166 | 36.499 | 42.166 | 46.499 | 10.000 |
| WI3     | Cart page                                 | 5.167    | WI2                           | 36.499 | 41.666 | 46.499 | 51.666 | 10.000 |
| RL1     | Date validation                           | 3.167    | RD3                           | 26.833 | 30.000 | 34.499 | 37.666 | 7.666  |
| RL2     | Inventory state management                | 8.667    | RL1                           | 30.000 | 38.667 | 37.666 | 46.333 | 7.666  |
| RL3     | Pricing Constraints                       | 5.333    | RL2                           | 38.667 | 44.000 | 46.333 | 51.666 | 7.666  |
| LF1     | Automatic late calculation                | 4.333    | RD3                           | 26.833 | 31.166 | 44.166 | 48.499 | 17.333 |
| LF2     | Manual staff adjustment                   | 3.167    | LF1                           | 31.166 | 34.333 | 48.499 | 51.666 | 17.333 |
| PW1     | Processor API Integration                 | 7.500    | RD3                           | 26.833 | 34.333 | 30.167 | 37.667 | 3.334  |
| PW2     | Card pre-authorization                    | 5.333    | PW1                           | 34.333 | 39.666 | 37.667 | 43.000 | 3.334  |
| PW3     | Execution of final, adjusted charges      | 5.333    | PW2                           | 39.666 | 44.999 | 43.000 | 48.333 | 3.334  |
| PW4     | Automated Data Deletion                   | 3.333    | PW3                           | 44.999 | 48.332 | 48.333 | 51.666 | 3.334  |
| ED1     | Rental Tracking                           | 6.500    | RD3                           | 26.833 | 33.333 | 26.833 | 33.333 | 0.000  |
| ED2     | Bike availability settings                | 4.333    | ED1                           | 33.333 | 37.666 | 33.333 | 37.666 | 0.000  |
| ED3     | Rate settings                             | 3.167    | ED2                           | 37.666 | 40.833 | 37.666 | 40.833 | 0.000  |
| ED4     | Refund Approval                           | 4.333    | ED3                           | 40.833 | 45.166 | 40.833 | 45.166 | 0.000  |
| ED5     | Summary Reports                           | 6.500    | ED4                           | 45.166 | 51.666 | 45.166 | 51.666 | 0.000  |
| T1      | Automated Testing                         | 8.667    | KI3, WI3, RL3, LF2, PW4, ED5  | 51.666 | 60.333 | 51.666 | 60.333 | 0.000  |
| T2      | Usability Testing                         | 5.333    | KI3, WI3, RL3, LF2, PW4, ED5  | 51.666 | 56.999 | 55.000 | 60.333 | 3.334  |
| T3      | Security Testing                          | 7.667    | KI3, WI3, RL3, LF2, PW4, ED5  | 51.666 | 59.333 | 52.666 | 60.333 | 1.000  |
| PM2     | Reporting                                 | 3.167    | ED5, T1, T2, T3               | 60.333 | 63.500 | 60.333 | 63.500 | 0.000  |
### Gantt Chart
```mermaid
gantt
    title Bike Shop Rental System – CPM Schedule
    dateFormat  YYYY-MM-DD
    axisFormat %b %d

    section Project Management
    Planning and Scheduling           :crit, pm1, 0, 4.333
    Reporting                         :crit, pm2, 60.333, 3.167

    section Requirements & Design
    Requirements gathering            :crit, rd1, 4.333, 6.500
    Prototyping                       :crit, rd2, 10.833, 8.500
    Architecture and database design  :crit, rd3, 19.333, 7.500

    section Kiosk Interface
    Greeting screen                   :ki1, 26.833, 2.167
    Hardware Integration              :ki2, 29.000, 10.833
    Web integration                   :ki3, 39.833, 6.500

    section Web Interface
    Bike catalog page                 :wi1, 26.833, 5.333
    Individual bike Page              :wi2, 32.166, 4.333
    Cart page                         :wi3, 36.499, 5.167

    section Rental Logic Unit
    Date validation                   :rl1, 26.833, 3.167
    Inventory state management        :rl2, 30.000, 8.667
    Pricing Constraints               :rl3, 38.667, 5.333

    section Late Fee Calculator
    Automatic late calculation        :lf1, 26.833, 4.333
    Manual staff adjustment           :lf2, 31.166, 3.167

    section Payment Wrapper
    Processor API Integration         :pw1, 26.833, 7.500
    Card pre-authorization            :pw2, 34.333, 5.333
    Execution of final charges        :pw3, 39.666, 5.333
    Automated Data Deletion           :pw4, 44.999, 3.333

    section Employee / Management Dashboards
    Rental Tracking                   :crit, ed1, 26.833, 6.500
    Bike availability settings        :crit, ed2, 33.333, 4.333
    Rate settings                     :crit, ed3, 37.666, 3.167
    Refund Approval                   :crit, ed4, 40.833, 4.333
    Summary Reports                   :crit, ed5, 45.166, 6.500

    section Testing
    Automated Testing                 :crit, t1, 51.666, 8.667
    Usability Testing                 :t2, 51.666, 5.333
    Security Testing                  :t3, 51.666, 7.667
```