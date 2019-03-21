import os
import datetime

# Get current year with now.year
now = datetime.datetime.now()

# Current Working folder
file_path = os.getcwd()

months = [
          "1. Januari", "2. Februari", "3. Maart", 
          "4. April", "5. Mei", "6. Juni",
          "7. Juli", "8. Augustus", "9. September",
          "10. Oktober", "11. November", "12. December"
          ]


try:
    for month in months:
        os.makedirs(f"{file_path}/{now.year}/{month}")
except OSError:
    print ("Creation of the directory's failed")
else:
    print ("Successfully created the directory's")
