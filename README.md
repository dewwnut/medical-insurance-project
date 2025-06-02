# 🩺 Medical Insurance Project

A Python class to represent patient data and estimate insurance costs.

## Features

- Create patient profiles
- Update age and number of children
- Estimate insurance cost based on given formula
- View patient info as a dictionary

## Example

```python
from patient import Patient

john = Patient("John", 35, 1, 22.5, 2, 1)
john.estimated_insurance_cost()
john.update_age(36)
john.update_num_of_children(3)
print(john.patient_profile())
