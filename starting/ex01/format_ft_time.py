import time
import datetime

seconds = time.time()
today = datetime.datetime.today()

print(f"Seconds since January 1, 1970: {seconds:.4f} or {seconds:.2e}  in scientific notation")
print(today.strftime("%b %d %Y"))