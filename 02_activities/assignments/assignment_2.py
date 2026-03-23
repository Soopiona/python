# Assignment #2: Efficacy Analysis of a Hypothetical Arthritis Drug
#
# Objective: Evaluate the effectiveness of a fictional medication designed to
# reduce inflammation caused by arthritis flare-ups.
#
# Data: 12 CSV files, each with 60 patients (rows) x 40 days (columns).

import numpy as np
import os

# Resolve paths relative to this script's location
_base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../05_src/data/assignment_2_data")

all_paths = [os.path.join(_base, f"inflammation_{i:02d}.csv") for i in range(1, 13)]


# ── Part 1: Reading and Displaying Data from the First File ────────────────

with open(all_paths[0], 'r') as f:
    rows = f.readlines()
    for row in rows:
        print(row)


# ── Part 2: Data Summarization Function ───────────────────────────────────

def patient_summary(file_path, operation):
    """Return a per-patient summary (mean/max/min) over 40 days.

    Parameters
    ----------
    file_path : str  - path to a CSV file (60 patients x 40 days)
    operation : str  - one of 'mean', 'max', or 'min'

    Returns
    -------
    numpy array of length 60
    """
    data = np.loadtxt(fname=file_path, delimiter=',')
    ax = 1  # axis=1 → operate across columns (days) for each row (patient)

    if operation == 'mean':
        summary_values = np.mean(data, axis=ax)
    elif operation == 'max':
        summary_values = np.max(data, axis=ax)
    elif operation == 'min':
        summary_values = np.min(data, axis=ax)
    else:
        raise ValueError("Invalid operation. Please choose 'mean', 'max', or 'min'.")

    return summary_values


# Test: output should be 60
data_min = patient_summary(all_paths[0], 'min')
print(len(data_min))


# ── Helper Function ────────────────────────────────────────────────────────

def check_zeros(x):
    """Return True if any value in array x equals 0, else False."""
    flag = np.where(x == 0)[0]
    return len(flag) > 0


# ── Part 3: Error Detection in Patient Data ────────────────────────────────

def detect_problems(file_path):
    """Return True if any patient has a mean inflammation score of 0."""
    means = patient_summary(file_path, 'mean')
    return check_zeros(means)


# Test: output for the first file should be False
print(detect_problems(all_paths[0]))
