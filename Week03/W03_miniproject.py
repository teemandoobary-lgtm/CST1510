"""
RECORD CHECK  -  my version
===========================

Name  : Teeman Doobary
Lane  :  IT      
Date  : 09/10/2026

Run it:   python W03_miniproject.py

"""

# =================================================================== FUNCTIONS

def status_of(percent, warning_at=90):
    """Return 'OVER LIMIT', 'WARNING', or 'OK' for a percentage."""

    if percent >= 100:
        return "OVER LIMIT"
        
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"



def check_value(value, limit):
    """Return the amount of free space and the percentage as two values"""
    
    free_space = limit - value
    percentage = (value / limit) * 100
    return free_space, percentage

def print_report(label, value, limit, free_space, percent, status):
    """Print a bordered report for one record check."""
            
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"  Used              : {value:>10.2f} GB")
    print(f"  Limit             : {limit:>10.2f} GB")
    print(f"  Free              : {free_space:>+10.2f} GB")
    print(f"  Percent           : {percent:>10.2f} %")
    print(f"  Status            : {status:>10}")
    print("=" * 34)



# ==================================================================== INPUT

over_limit_count = 0

while True:
    
    hostname = input("Enter a hostname (or 'quit' to stop): ")
    if hostname.lower() == "quit":
        break

    gb_used = float(input("Enter the amount of GB used: "))
    gb_total = float(input("Enter the amount of GB total: "))

    if gb_total <= 0:
        print("Total must be greater than 0. Try again.")
        continue

# ============================================================== PROCESS

    free_space, percent = check_value(gb_used, gb_total)
    status = status_of(percent)

    

# =============================================================== OUTPUT

    print_report(hostname, gb_used, gb_total, free_space, percent, status)
    if status == "OVER LIMIT":
        over_limit_count += 1
print()
print(f"Records over limit: {over_limit_count}")

