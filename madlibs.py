def main():
	# write your code here
	print("Mad libs where libs get mad." "\nStart below:\n")
	time = 0
	while time < 1 or time > 12:
		time = int(input("Enter a number from 1 to 12: "))
	items = input("Enter a noun (plural): ")
	name = input("Enter a name: ")
	scream = input ("Enter any sentence: ")
	action = input("Enter a verb: ")

	print('\nThe story goes...\n\n'
	f'It was {time} o\'clock when I heard a knock at the door.\n'
	f'I opened the door and there was a box full of {items} with a note saying "From Mr. {" ".join([nameIs.capitalize() for nameIs in name.split()]) }."\n'
	f'Just as I closed the door I heard a scream "{scream.upper()}."\n'
	f'I froze in place and all I could do was {action}.')



if __name__ == '__main__':
	main()