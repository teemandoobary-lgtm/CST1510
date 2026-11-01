"""
RECORD CHECK  -  my version
===========================

Name  : Teeman Doobary
Lane  : IT 
Date  : 21/10/2026

Run it:   python W05_miniproject.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

# your class goes here
class Record:
    # Class-level attribute to keep track of total over-limit records
    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Stores the label, value, and limit as attributes."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Returns OVER LIMIT, WARNING, or OK based on value and limit."""
        percentage = (self.value / self.limit) * 100
        
        if percentage >= 100:
            # Increment the class-level running total if it's over limit
            Record.over_limit_count += 1
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"

# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.

#records = []    replace with your code
def load_records(path):
    """Reads a file and returns a list of Record objects."""
    records_list = []
    try:
        with open(path, 'r') as file:
            for line in file:
                # Skip empty lines
                if not line.strip():
                    continue
                
                # Split the line by commas (assuming csv format)
                parts = line.strip().split(',')
                
                # Unpack the 3 parts
                label = parts[0].strip()
                value = float(parts[1].strip())
                limit = float(parts[2].strip())
                
                # Create the Record object and add it to the list
                records_list.append(Record(label, value, limit))
                
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        
    return records_list

records = load_records("records_sample.txt")

# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    # Report lines
    print(f"  Value : {record.value}")
    print(f"  Limit : {record.limit}")
    print(f"  Status: {record.status()}")
    
    print("=" * 34)

# Print the final summary using the class-level counter
print(f"\nTotal records OVER LIMIT: {Record.over_limit_count}")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
