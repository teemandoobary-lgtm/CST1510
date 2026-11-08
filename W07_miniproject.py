"""
RECORD CHECK  -  my version
===========================

Name  :  Teeman Doobary
Lane  :  IT
Date  :  07/11/2026

Run it:   python W07_miniproject.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
def parse_line(raw_line):
    """Clean one messy IT line into a dict with a hostname and numeric fields."""
    cleaned = raw_line.strip()
    hostname_part, rest = cleaned.split(",", 1)
    record = {"hostname": hostname_part.strip().lower()}
    for piece in rest.split(","):
        key, value = piece.split("=")
        record[key.strip().lower()] = float(value.strip())
    return record


def status_of(record):
    """Return OVER LIMIT / WARNING / OK for one cleaned IT record."""
    pct = record["used"] / record["total"] * 100
    if pct >= 100:
        return "OVER LIMIT"
    if pct >= 90:
        return "WARNING"
    return "OK"


# ====================================================================== INPUT
raw_records = ["Srv-01 , used=87 , total=100",
               "SRV-02,used=120,total=100",
               "srv-03,used=45 ,total=100",
               "Srv-04 , used = 93 , total=100",
               "sRv-05,USED=100,total=100"]


# =============================================================== PROCESS + OUTPUT
total_count = 0
flagged_count = 0

for raw_record in raw_records:
    if not raw_record.strip():
        continue
    record = parse_line(raw_record)
    status = status_of(record)
    print(f"{record}  ->  {status}")
    total_count += 1
    if status != "OK":
        flagged_count += 1

print(f"\n{total_count} records, {flagged_count} flagged.")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
