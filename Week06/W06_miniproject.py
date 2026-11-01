"""
RECORD CHECK  -  my version
===========================

Name  :  Teeman Doobary
Lane  :  IT
Date  :  1/11/2026

Run it:   python W06_miniproject.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================== LOAD
df = pd.read_csv("records_sample.csv")


# ================================================================= PROCESS
df["percent"] = (df["value"] / df["limit"]) * 100


df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK")
)


# ================================================================== OUTPUT
print(df)

not_ok = df[df["status"] != "OK"]
print("\n--- Not OK ---")
print(not_ok)


print("\n--- Count per status ---")
print(df["status"].value_counts())

df.to_csv("records_report.csv", index=False)

df["status"].value_counts().plot(kind="bar")
plt.title("Status counts")
plt.xlabel("Status")
plt.ylabel("Count")
plt.savefig("status_counts.png")
plt.show()
