#Email: abc5885@psu.edu

#Input how many people will be sharing the pizza and how many pizzas will be order
people = int(input("How many people will be sharing the pizza? "))
pizza = int(input("How many pizzas will be ordered? "))


#Input if anyone only wants two slices of pizza
limitSlices = int(input("How many people will limit themselves to TWO slices? "))


#Slices per pizza
pizzaSlices = 8


#Algorithm to determine how many will distrubted to people eating
#Determines how many slices will be purchased when certian amount of pizza is ordered
#Also determines how many slices are left if anyone ops for only 2 slices
sliceCount = pizza * pizzaSlices
recountPeople = people - limitSlices
limitSliceCount = sliceCount - limitSlices * 2
#Determines how the groups will split up for distrubtion of pizza slices
secondGroup = limitSliceCount % recountPeople
firstGroup = recountPeople - secondGroup
#Determine how many slices each person gets and how many remaining slices are left
slicesPerPerson = limitSliceCount // recountPeople
slicesRemaining = limitSliceCount % recountPeople
#Determines how the remaining slices are distrubted to group two 
extraSlices = slicesPerPerson + slicesRemaining//secondGroup


#End Results
print("You will divide", sliceCount, "slices between", people, "people.")
print(limitSlices, "person(s) will have 2 slices.")

print(firstGroup,"will receive",slicesPerPerson,"slice(s),",
      secondGroup,"will recieve",extraSlices,"slice(s).")

