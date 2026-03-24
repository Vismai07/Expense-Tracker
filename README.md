# Expense Tracker with Category-wise Analytics
Overview

This project models personal financial transactions as a structured data pipeline:

$$
\text{Input} \rightarrow \text{Storage} \rightarrow \text{Organization} \rightarrow \text{Aggregation} \rightarrow \text{Insight}
$$

# Mathematical Model

Each transaction is represented as:

$$
e_i = (a_i, c_i, t_i)
$$

Where:
	•	a_i: amount
	•	c_i: category
	•	t_i: timestamp


# Core Components

Data Structures

	•	Class (Expense): Represents a single transaction (analogous to a row in a database)
	•	List (expenses): Stores all transaction records
	•	defaultdict: Enables efficient aggregation


### Why defaultdict?

A normal dictionary requires manual 
initialization:

d = {}

d["food"] = 0

d["food"] += 

Without initialization:

d["food"] += 100  # KeyError

Using defaultdict:

from collections import defaultdict

d = defaultdict(float)

d["food"] += 100  # Automatically 

initializes to 0.0

# Aggregation Logic

***Monthly Aggregation***

$$
S_m = \sum_{i : t_i \in m} a_i
$$

month = e.date.strftime("%Y-%m")

summary[month] += e.amount

***Category-wise Aggregation***

$$
S_c = \sum_{i : c_i = c} a_i
$$

breakdown[e.category] += e.amount

### System Pipeline

	•	Input → input()
	•	Validation → get_valid_date()
	•	Storage → expenses.append()
	•	Aggregation → summary functions
	•	Output → print()

### Complexity Analysis

	•	Time Complexity: O(n)

	•	Space Complexity: O(k)
### Future Work

	•	Time-series forecasting of expenses
	•	Anomaly detection in spending patterns
	•	Budget optimization models
	•	Integration with machine learning pipelines
