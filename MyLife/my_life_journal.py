import datetime

class JournalWriter:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_entries(self):
        with open(self.file_name, "a") as file: 
            print("--- Journal Entry Mode Started ---")
            while True:
                line = input("Enter line: ")
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"[{timestamp}] {line}\n")
                
                more = input("Are there more lines y/n? ").strip().lower()
                if more != 'y':
                    break 
                    
        print(f"\nJournal successfully updated in {self.file_name}")

if __name__ == "__main__":
    journal = JournalWriter("mylife.txt")
    journal.write_entries()