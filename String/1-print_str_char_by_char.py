'''Print a string character by character'''

import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

s= ' Python'

for ch in s:
    logging.info(f"Character: {ch}")