import json
import random

male_names = ["Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Reyansh", "Krishna", "Ishaan", "Shaurya",
              "Ravi", "Rohan", "Amit", "Rahul", "Vikram", "Sanjay", "Pradeep", "Suresh", "Rajesh", "Manoj",
              "Karan", "Nikhil", "Akash", "Varun", "Dev", "Kabir", "Aryan", "Yash", "Harsh",
              "Anil", "Sunil", "Mohan", "Gopal", "Ramesh", "Dinesh", "Mahesh", "Prakash", "Ajay", "Vijay",
              "Siddharth", "Adrian", "Dhruv", "Kunal", "Lakshya", "Manan", "Neel", "Omkar", "Parth"]

female_names = ["Ananya", "Sneha", "Neha", "Priya", "Aisha", "Diya", "Anika", "Ira", "Kiara", "Myra",
                "Pooja", "Riya", "Simran", "Tanvi", "Kavya", "Nisha", "Meera", "Divya", "Swati", "Anjali",
                "Aarti", "Sunita", "Kavita", "Rekha", "Suman", "Geeta", "Lata", "Usha", "Vandana", "Nidhi",
                "Shreya", "Ishita", "Aaradhya", "Anvi", "Avni", "Charu", "Drishya", "Elina", "Gracy", "Hansika",
                "Jhanvi", "Kiyara", "Lavanya", "Mira", "Naima", "Prisha", "Saanvi", "Tara", "Vanya"]

last_names = ["Verma", "Mehta", "Kulkarni", "Sinha", "Sharma", "Patel", "Singh", "Kumar", "Gupta", "Joshi",
              "Reddy", "Nair", "Iyer", "Rao", "Desai", "Chopra", "Malhotra", "Kapoor", "Bose", "Das",
              "Mukherjee", "Banerjee", "Chatterjee", "Ghosh", "Pillai", "Menon", "Chauhan", "Thakur", "Yadav", "Mishra",
              "Agarwal", "Jain", "Saxena", "Tiwari", "Dubey", "Pandey", "Tripathi", "Srivastava", "Chandra", "Varma"]

cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Lucknow",
          "Kanpur", "Nagpur", "Indore", "Thane", "Bhopal", "Visakhapatnam", "Patna", "Vadodara", "Ghaziabad", "Ludhiana",
          "Agra", "Nashik", "Faridabad", "Meerut", "Rajkot", "Varanasi", "Srinagar", "Aurangabad", "Dhanbad", "Amritsar",
          "Allahabad", "Ranchi", "Howrah", "Coimbatore", "Jabalpur", "Gwalior", "Vijayawada", "Jodhpur", "Madurai", "Raipur",
          "Guwahati", "Chandigarh", "Thiruvananthapuram", "Solapur", "Hubli", "Mysore", "Tiruchirappalli", "Bareilly", "Mangalore"]

def get_verdict(bmi):
    if bmi < 18.5: return "Underweight"
    elif bmi < 25: return "Normal"
    elif bmi < 30: return "Overweight"
    else: return "Obese"

random.seed(42)
data = {}

for i in range(1, 501):
    pid = f"P{i:03d}"
    gender = random.choice(["male", "female"])
    name = f"{random.choice(male_names if gender == 'male' else female_names)} {random.choice(last_names)}"
    city = random.choice(cities)
    age = random.randint(18, 65)
    height = round(random.uniform(1.45, 1.95), 2)
    weight = round(random.uniform(38, 125), 1)
    bmi = round(weight / (height ** 2), 2)
    
    data[pid] = {
        "name": name, "city": city, "age": age, "gender": gender,
        "height": height, "weight": weight, "bmi": bmi, "verdict": get_verdict(bmi)
    }

with open('patients_data.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✅ Generated {len(data)} records in patients_data.json")