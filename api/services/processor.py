# services/processor.py

import subprocess
import threading
from config import (
    GRADLE_COMMAND,
    CODE_DIR,
    COMMAND_TIMEOUT_SECONDS,
    ALLOW_CONCURRENT_JOBS,
)

# Global lock to ensure single execution
_processing_lock = threading.Lock()


class ProcessingAlreadyRunning(Exception):
    pass



"""
    TEST-ONLY:
    IMPORTS.
"""
import time
import os
import csv
from config import FLOW_DIR, ALLOW_CONCURRENT_JOBS


def _generate_dummy_csvs():
    """
    TEST-ONLY:
    Generates dummy CSV files in /flow directory.
    """

    os.makedirs(FLOW_DIR, exist_ok=True)

    for i in range(3):  # generate 3 CSV files
        file_path = os.path.join(FLOW_DIR, f"dummy_{i}.csv")
        with open(file_path, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "value"])
            for j in range(5):
                writer.writerow([j, f"value_{j}"])




def run_processing_command():
    """
    Runs the Gradle command in a blocking way.
    """

    if not ALLOW_CONCURRENT_JOBS:
        if not _processing_lock.acquire(blocking=False):
            raise ProcessingAlreadyRunning()

    try:
        subprocess.run(
            GRADLE_COMMAND,
            cwd=CODE_DIR,                 # IMPORTANT
            check=True,                   # Raise error if command fails
            timeout=COMMAND_TIMEOUT_SECONDS,
        )
    finally:
        if not ALLOW_CONCURRENT_JOBS:
            _processing_lock.release()


    """
    TEST-ONLY:
    Simulates processing by sleeping and generating CSV files.
    """

    # if not ALLOW_CONCURRENT_JOBS:
    #     if not _processing_lock.acquire(blocking=False):
    #         raise ProcessingAlreadyRunning()

    # try:
    #     # TEST-ONLY: simulate long processing
    #     time.sleep(5)

    #     # TEST-ONLY: generate dummy CSV output
    #     _generate_dummy_csvs()

    # finally:
    #     if not ALLOW_CONCURRENT_JOBS:
    #         _processing_lock.release()

    
