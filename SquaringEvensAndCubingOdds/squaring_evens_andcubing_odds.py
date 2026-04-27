import time

class NumberTransformer:
    def __init__(self, source_file):
        self.source_file = source_file

    def process_integers(self):
        try:
            with open(self.source_file, "r") as file:
                numbers = file.readlines()
                
            with open("double.txt", "w") as double_f, open("triple.txt", "w") as triple_f:
                print("Processing data...")
                for idx, num_str in enumerate(numbers):
                    num = int(num_str.strip())
                    
                    time.sleep(0.05) 
                    print(f"Transforming item {idx+1}/{len(numbers)}...", end="\r")
                    
                    if num % 2 == 0:
                        double_f.write(f"{num**2}\n")
                    else:
                        triple_f.write(f"{num**3}\n")
                        
            print("\nSuccessfully created double.txt and triple.txt!")
            
        except FileNotFoundError:
            print(f"Error: '{self.source_file}' not found. Please create it first.")

if __name__ == "__main__":
    transformer = NumberTransformer("integers.txt")
    transformer.process_integers()