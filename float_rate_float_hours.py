class Worker:
     def __init__(self, hours, rate):
          self.hours = hours
          self.rate = rate

     def calculate_pay(self):
          overtime_rate = self.rate * 1.5
          regular_hours = min (self.hours, 40)
          overtime_hours = max (self.hours - 40, 0)

          if self.hours > 40:
                print("Overtime hours: ", overtime_hours)
          else:
                print("Regular hours: ", regular_hours)
    
          amount_paid = (regular_hours * self.rate) + (overtime_hours * overtime_rate)
          return amount_paid

class SalariedWorker(Worker):
     def calculate_tax(self):
         tax_rate = 0.15
         pay = self.calculate_pay()
         tax_amount = pay * tax_rate
         net_pay = pay - tax_amount
         return net_pay
     
class Contractor(Worker):
     def calculate_tax(self):
         tax_rate = 0.3
         pay = self.calculate_pay()
         tax_amount = pay * tax_rate
         net_pay = pay - tax_amount
         return net_pay

string_hours = input ("Enter your hours for this week:")
string_rate = input ("Enter the rate at which you contracted: ")

try: 
    float_hours = float(string_hours)
    float_rate = float(string_rate)
    overtime_rate = float_rate * 1.5
    worker_type = input("Enter your current worker type (salaried/contractor): ")

    if worker_type.lower() == "salaried":
        worker = SalariedWorker(float_hours, float_rate)
    elif worker_type.lower() == "contractor":
         worker = Contractor (float_hours, float_rate)
    else: 
         print("Invalid worker type. Please enter either contractor or salaried.")
         exit()
    
    amount_paid = worker.calculate_pay()
    net_pay = worker.calculate_tax()

    print("Your pay is: ", amount_paid)
    print("Your net pay after tax is: ",net_pay)

except ValueError:
    print("Invalid input. Please enter numerical values for both hours and rates.")