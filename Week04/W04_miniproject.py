"""
RECORD CHECK - Mini-project
===========================
Name  : Teeman Doobary
Lane  : IT
Date  : 18/10/2026

Run it: python W04_miniproject.py
"""

# =================================================================== FUNCTIONS

def check_record(value, limit):
    """Calculates difference, percent, and status of a record."""
    difference = value - limit
    # Prevent division by zero error just in case total is 0
    percent = (value / limit) * 100 if limit != 0 else 0.0
    
    if value >= limit:
        status = "OVER LIMIT"
    else:
        status = "OK"
        
    return difference, percent, status

def print_report(label, value, limit, difference, percent, status):
    """Prints a formatted report for a single record."""
    
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"Used        : {value:>10.2f} GB")
    print(f"Total       : {limit:>10.2f} GB")
    print(f"Diff        : {difference:>+10.2f} GB")
    print(f"Percent     : {percent:>10.2f} %")
    print(f"Status      : {status:>10}")
    print("=" * 34)


# ====================================================================== STORE

def load_records(path):
    """Reads a file and returns a list of dicts representing the records."""
    records = []
    try:
        with open(path, 'r') as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    records.append({
                        "label": parts[0],
                        "value": float(parts[1]),
                        "limit": float(parts[2])
                    })
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found. Starting with an empty list.")
        return []
        
    return records


# =============================================================== PROCESS + OUTPUT

# Load the data 
file_path = "it_records.txt"
records = load_records(file_path)

over_limit_count = 0

# Open a new file to write results
with open("results.txt", "w") as out_file:

    for record in records:
        # Extract data for readability
        label = record["label"]
        value = record["value"]
        limit = record["limit"]
        
        # Call functions
        diff, percent, status = check_record(value, limit)
        print_report(label, value, limit, diff, percent, status)
        
        # Track over limit count
        if status == "OVER LIMIT":
            over_limit_count += 1
            
        # Write to file
        out_file.write(f"{label},{status}\n")

# Print final summary after the loop
print(f"SUMMARY: {len(records)} records processed.")
print(f"{over_limit_count} record(s) were OVER LIMIT.")
