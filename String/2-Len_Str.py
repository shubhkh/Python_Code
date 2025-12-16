import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s - %(message)s"
)

s = "python"
count = 0

for ch in s:
    count += 1
    logging.debug(f"Counting: {count}")

logging.info(f"Length of String: {count}")
