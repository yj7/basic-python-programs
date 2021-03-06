import sys, random

# variable declaration:

num = random.randint(1, 100) #generates a random number between 1 and 100 (both inclusive)
prev_inp = 0
count = 1
for_more = {
	5: "Wow, you're REALLY close. Try entering a slightly smaller number",
	10: "Ooh, you're close. But your number is still large",
	30: "The number you entered is large! Try entering a smaller one",
	50: "Your number is waaay too large. Try entering a smaller one",
	99: "Your number is w-a-a-a-y too large. Try entering a smaller one"	
}

for_less = {
	5: "Wow, you're REALLY close. Try entering a slightly larger number",
	10: "Ooh, you're close. But your number is still small",
	30: "The number you entered is small! Try entering a larger one",
	50: "Your number is waaay too small. Try entering a larger one",
	99: "Your number is w-a-a-a-y too small. Try entering a larger one"
}

# input:

print("So here's the deal: we have a number with us. It's between 1 to 100, pinky promise!")
print("Let's see how many tries it takes for you to guess it ;)")
print("All the best (y)")
print("P.S: if you feel like quiting, just enter 101. But don't give up!")
# 4 prints being more readable than 1 long one

# logic:

while True:
	try:
		inp = int(input())

	except:
		print("Lol, you have to enter a number idiot! Try again :P")
		continue

	if(inp == 101):
		print("Aww, you gave up :(")
		print("Try again soon!")
		sys.exit()

	elif(inp < 1 or inp > 100):
		print("Are you like nuts!? We already told you the number is between 1 to 100 for heaven's sakes! :P")

	elif(inp == prev_inp):
		print("Oops, looks like you entered the same number again. Don't worry though, this try won't be counted! :)")

	elif(inp == num):
		print("Woohoo! You've done it! You guessed the number perfectly correct :D")
		print("It took you", count, "try" if (count==1) else "tries", "to guess it right!")
		sys.exit()

	elif(inp < num):
		count += 1
		for key, value in sorted(for_less.items()):
			if(inp < num and inp >= num - key):
				print(value)
				break
				
	elif(inp > num):
		count += 1
		for key, value in sorted(for_more.items()):
			if(inp > num and inp <= num + key):
				print(value)
				break

	prev_inp = inp