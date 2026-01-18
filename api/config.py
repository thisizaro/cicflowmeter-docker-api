# config.py

# ASSUMED FOR NOW:
# These directories already exist and are mounted into the container
PCAP_DIR = "/pcap"
FLOW_DIR = "/flow"
CODE_DIR = "/code"

# ASSUMED FOR NOW:
# Only one job at a time, blocking execution
ALLOW_CONCURRENT_JOBS = False

# ASSUMED FOR NOW:
# This command is correct and blocking
GRADLE_COMMAND = [
    "gradle",
    "--no-daemon",
    "-Pcmdargs=/pcap:/flow",
    "runcmd"
]

# Optional safety (can tune later)
COMMAND_TIMEOUT_SECONDS = None  # None = wait forever


# ASSUMED FOR NOW:
# Dummy processing mode enabled (no Gradle execution)
DUMMY_PROCESSING_MODE = True

