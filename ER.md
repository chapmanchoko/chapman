+------------------------+
|       User Service     |
|------------------------|
| - id (PK)              |
| - username             |
| - email                |
| - password             |
|                        |
| Django User Model      |
+------------------------+
           |
           | (One-to-Many)
           ↓
+-------------------------+
|   Transaction Service   |
|-------------------------|
| - id (PK)               |
| - user_id (FK → User)   |
| - type (income/expense)|
| - category              |
| - amount                |
| - date                  |
| - description (nullable)|
+-------------------------+

           |
           ↓
+-------------------------+
|     Budget Service      |
|-------------------------|
| - id (PK)               |
| - user_id (FK → User)   |
| - category              |
| - limit                 |
| - start_date            |
| - end_date              |
+-------------------------+

           |
           ↓
+------------------------------+
| RecurringTransaction Service |
|------------------------------|
| - id (PK)                    |
| - user_id (FK → User)        |
| - type (income/expense)      |
| - category                   |
| - amount                     |
| - frequency (e.g. weekly)    |
| - next_date                  |
+------------------------------+

           |
           ↓
+------------------------+
|  SavingsGoal Service   |
|------------------------|
| - id (PK)              |
| - user_id (FK → User)  |
| - name                 |
| - target_amount        |
| - current_amount       |
| - deadline             |
+------------------------+

SHARED BACKEND INFRASTRUCTURE:
+------------------------+
|  PostgreSQL Database   |
|  (общая база для всех) |
+------------------------+

+------------------------+
|     Django Backend     |
| (все сервисы как модули)|
+------------------------+

