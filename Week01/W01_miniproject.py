"""
RECORD CHECK  -  my version
===========================

Name  : Teeman Doobary
Lane  : IT      
Date  : 23/09/2026

Run it:   python W01_miniproject.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
#
#    Remember: input() always gives back text.

server = input("Enter a hostname: ")          # : replace with an input() call
gb_used = float(input("Enter the amount of GB used: "))     # : replace with an input() call, converted
gb_total = float(input("Enter the amount of GB total: "))    # : replace with an input() call, converted


# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#    - difference : how far the first is from the second
#    - percent    : the first as a percentage of the second
#
#    Do not type the answers. Calculate them.

gb_free =  gb_total - gb_used           # 
percent = (gb_used / gb_total) * 100      # 

#IT ops set aside 10% as a safety buffer first. Only what's left over counts.
safety_buffer = gb_total * 0.10
usable_free_gb   = gb_free - safety_buffer


# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {server}")
print("=" * 34)

# : your report lines go here

print(f"Used            : {gb_used:>10.2f} GB")
print(f"Total           : {gb_total:>10.2f} GB")
print(f"Free            : {gb_free:>+10.2f} GB")
print(f"Percent         : {percent:>10.2f} %")
print(f"Usable free     : {usable_free_gb:>+10.2f} GB")
print("=" * 34)

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
