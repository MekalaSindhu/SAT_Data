import json

# hatchling: code generated with LLM assistance

class SATResultsSystem:
    def __init__(this):
        this.dict = {}  # key: Name, value: dict of student details
        this.file_name = "SAT-Results.json"

    def insert_data(this):
        name = input("Enter Student Name (unique): ").strip()
        if name in this.dict:
            print("Student Name already exists. Try updating instead.")
            return

        address = input("Enter Address: ").strip()
        city = input("Enter City: ").strip()
        country = input("Enter Country: ").strip()
        pincode = input("Enter Pincode: ").strip()
        try:
            score = float(input("Enter SAT Score: ").strip())
        except ValueError:
            print("Invalid score. Please enter a numeric value.")
            return

        passed = "Pass" if score > 30 else "Fail"  # 30% cutoff9==6-55555555
        this.dict[name] = {
            "Name": name,
            "Address": address,
            "City": city,
            "Country": country,
            "Pincode": pincode,
            "SAT Score": score,
            "Status": passed
        }
        print("Record inserted successfully.")
        this._save_to_file()

    def view_all_data(this):
        if not this.dict:
            print("No dict found.")
            return
        print(json.dumps(list(this.dict.values()), indent=4))

    def get_rank(this):
        if not this.dict:
            print("No dict found.")
            return
        name = input("Enter Name to get rank: ").strip()
        if name not in this.dict:
            print("Student name not listed.")
            return
        # Sort by SAT score in descending order
        sorted_dict = sorted(this.dict.values(), key=lambda x: x["SAT Score"], reverse=True)
        for rank, record in enumerate(sorted_dict, start=1):
            if record["Name"] == name:
                print(f"{name}'s rank is {rank}")
                return

    def update_score(this):
        name = input("Enter Name to update score: ").strip()
        if name not in this.dict:
            print("No update score not found.")
            return
        try:
            new_score = float(input("Enter new SAT Score: ").strip())
        except ValueError:
            print("Invalid score.")
            return
        this.dict[name]["SAT Score"] = new_score
        this.dict[name]["Status"] = "Pass" if new_score > 30 else "Fail"
        print(" student Score updated successfully.")
        this._save_to_file()

    def delete_record(this):
        name = input("Enter Name to delete: ").strip()
        if name not in this.dict:
            print("Name not found.")
            return
        del this.dict[name]
        print("student Record deleted successfully.")
        this._save_to_file()

    def calculate_average_score(this):
        if not this.dict:
            print("No dict to calculate average.")
            return
        avg_score = sum(r["SAT Score"] for r in this.dict.values()) / len(this.dict)
        print(f"Average SAT Score: {avg_score:.2f}")

    def filter_by_status(this):
        status = input("Enter status to filter by (Pass/Fail): ").strip().capitalize()
        if status not in ["Pass", "Fail"]:
            print("Invalid status. Enter Pass or Fail.")
            return
        filtered = [r for r in this.dict.values() if r["Status"] == status]
        if not filtered:
            print(f"No dict with status {status}.")
        else:
            print(json.dumps(filtered, indent=4))

    def _save_to_file(this):
        with open(this.file_name, "w") as f:
            json.dump(list(this.dict.values()), f, indent=4)


def main():
    system = SATResultsSystem()
    menu = """
---- SAT Results Menu ----
1. Insert data
2. View all data
3. Get rank
4. Update score
5. Delete one record
6. Calculate Average SAT Score
7. Filter records by Pass/Fail Status
8. Put the inserted data in json format in a file.

---------------------------
"""
    while True:
        print(menu)
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            system.insert_data()
        elif choice == "2":
            system.view_all_data()
        elif choice == "3":
            system.get_rank()
        elif choice == "4":
            system.update_score()
        elif choice == "5":
            system.delete_record()
        elif choice == "6":
            system.calculate_average_score()
        elif choice == "7":
            system.filter_by_status()
        elif choice == "8":
            print("Put the inserted data in json format in a file...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
