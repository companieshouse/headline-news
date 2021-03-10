# %%
import os

# Load environment variables for the `data` folder, and its sub-folders
DIR_DATA = os.getenv("DIR_DATA")
DIR_DATA_EXTERNAL = os.getenv("DIR_DATA_EXTERNAL")
DIR_DATA_EXTERNAL_URLS = os.getenv("DIR_DATA_EXTERNAL_URLS")
DIR_DATA_RAW = os.getenv("DIR_DATA_RAW")
DIR_DATA_INTERIM = os.getenv("DIR_DATA_INTERIM")
DIR_DATA_PROCESSED = os.getenv("DIR_DATA_PROCESSED")

# %%
with open(DIR_DATA_EXTERNAL_URLS + "/politics.txt") as file:
    lines = [line.strip() for line in file]

print(DIR_DATA_EXTERNAL_URLS)
# %%
