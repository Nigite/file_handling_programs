class GWAAnalyzer:
    def __init__(self, file_name):
        self.file_name = file_name

    def find_top_student(self):
        try:
            lowest_gwa = 5.0 
            top_students = []
            total_students = 0
            
            with open(self.file_name, "r") as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 2:
                        total_students += 1
                        name = parts[0].strip()
                        gwa = float(parts[1].strip())
                        
                        if gwa < lowest_gwa:
                            lowest_gwa = gwa
                            top_students = [name]
                        elif gwa == lowest_gwa:
                            top_students.append(name)
                            
            print(f"--- Class Analysis ({total_students} students) ---")
            print(f"Highest GWA Achieved: {lowest_gwa}")
            print(f"Top Student(s): {', '.join(top_students)}")
            print("-----------------------------")
                
        except FileNotFoundError:
            print(f"Error: {self.file_name} not found.")

if __name__ == "__main__":
    analyzer = GWAAnalyzer("students.txt")
    analyzer.find_top_student()