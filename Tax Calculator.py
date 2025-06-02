# Make it so the user inputs the energy consumed into the program
units = int(input("Enter the number of energy units you have consumed: "))
# Starting tax
tax = 0
# Basically if the units are under 100 the tax is 0
if units <=100:
    tax = 0
# If the units is above 100 but under or equal to 200 then the units above 100 is 0.70 per unit    
elif units <= 200:
    tax = (units - 100) * 0.70
# Now do the same but this time make it so you add the amount that is above 100 + any units above 200 and multiple it by 0.70 per unit    
else:
    tax = (200-100) * 0.70 + (units - 200) * 0.70
# Print the text to tell the user the calculation of how much they need to pay. 
print(f"The tax to be paid for {units} units consumed is: {tax:.2f}")