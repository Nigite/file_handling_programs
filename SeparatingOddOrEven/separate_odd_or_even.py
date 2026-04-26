class NumberSeparator:
    def __init__(self, input_file, even_file, odd_file):
        self.input_file = input_file
        self.even_file = even_file
        self.odd_file = odd_file

    def separate_numbers(self):
        even_count, odd_count = 0, 0
        try:
            with open(self.input_file, "r") as file:
                numbers = file.readlines()
            
            with open(self.even_file, "w") as even_f, open(self.odd_file, "w") as odd_f:
                for num_str in numbers:
                    num = int(num_str.strip())
                    if num % 2 == 0:
                        even_f.write(f"{num}\n")
                        even_count += 1
                    else:
                        odd_f.write(f"{num}\n")
                        odd_count += 1
                        
            print(f"Successfully sorted the numbers in the file! Sorted {even_count} even numbers and {odd_count} odd numbers.")
        except FileNotFoundError:
            print(f"Error: Could not find {self.input_file}.")

if __name__ == "__main__":
    separator = NumberSeparator("numbers.txt", "even.txt", "odd.txt")
    separator.separate_numbers()