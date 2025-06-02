class Patient:
    def __init__(self, name, age, sex, bmi, num_of_children, smoker):
        """
        sex: 0 for female, 1 for male
        smoker: 0 for non-smoker, 1 for smoker
        """
        self.name = name
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.num_of_children = num_of_children
        self.smoker = smoker
        
    def estimated_insurance_cost(self):
        estimated_cost = (
            250 * self.age
            - 128 * self.sex
            + 370 * self.bmi
            + 425 * self.num_of_children
            + 24000 * self.smoker
            - 12500
        )
        print(f"{self.name}'s estimated insurance cost is ${estimated_cost:.2f}.")
        return estimated_cost
        
    def update_age(self, new_age):
        self.age = new_age
        print(f"{self.name} is now {self.age} years old.")
        self.estimated_insurance_cost()
        
    def update_num_of_children(self, new_num_children):
        self.num_of_children = new_num_children
        child_word = "child" if self.num_of_children == 1 else "children"
        print(f"{self.name} has {self.num_of_children} {child_word}.")
        self.estimated_insurance_cost()
        
    def patient_profile(self):
        return {
            "Name": self.name,
            "Age": self.age,
            "Sex": self.sex,
            "BMI": self.bmi,
            "Number of Children": self.num_of_children,
            "Smoker": self.smoker,
        }
