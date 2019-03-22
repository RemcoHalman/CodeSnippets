import xlsxwriter
import sys
import datetime
import calendar
import os

FirstName = sys.argv[1]
LastName = sys.argv[2]
Car = sys.argv[3]

now = datetime.datetime.now()
cal = calendar.Calendar()
current_year = now.year
current_month = now.month

file_path = os.getcwd()
folder_name = "Mileage_expenses"

# Folder creation
if os.path.exists(folder_name):
    pass
else:
    os.mkdir(folder_name)

months = (
          ["1. Januari", 1],["2. Februari", 2],["3. Maart", 3], ["4. April", 4],
          ["5. Mei", 5],["6. Juni", 6], ["7. Juli", 7],["8. Augustus", 8],
          ["9. September", 9],["10. Oktober", 10],["11. November", 11],["12. December", 12]
          )

start_row = 6
column = 0

def SetData():
    bold = workbook.add_format({'bold': True})
    worksheet.write('A1', "Kilometer Registratie", bold)
    worksheet.write('H1', month[0], bold)
    worksheet.write('H2', current_year)
    worksheet.write('A2', (FirstName + " " + LastName))
    worksheet.write('A3', Car)
    worksheet.write('A5', "Datum")
    worksheet.write('B5', "Heen")
    worksheet.write('D5', "Terug")
    worksheet.write('F5', "Via")
    worksheet.write('I5', "Totaal")

    worksheet.write('B6', "Van")
    worksheet.write('C6', "Naar")
    worksheet.write('D6', "Van")
    worksheet.write('E6', "Naar")
    worksheet.write('G6', "Heen")
    worksheet.write('H6', "Terug")

    worksheet.write('C38', 'kilometer vergoeding * 0,19')
    worksheet.write('F38', '=SUM(I38*0.19)', bold)
    worksheet.write('G38', 'Gereden Kilometers')
    worksheet.write('I38', '=SUM(I7:I37)', bold)
    # worksheet.write('I7', '=SUM(G7+H7)', bold)
    for i in range(7,38):
        set_row = i
        worksheet.write(f'I{set_row}', f'=SUM(G{set_row}+H{set_row})', bold)



try:

    for month in months:
        # Creating the excel sheets and setting basic data
        workbook = xlsxwriter.Workbook(f'{file_path}/{folder_name}/{month[0]}.xlsx')
        worksheet = workbook.add_worksheet()
        SetData()
        # Adding all days of the month to the sheet
        for day in cal.itermonthdays(current_year, month[1]):
            if day > 0:
                 worksheet.write(start_row, column, day)
                 start_row += 1
                 day += 1
                 # Check if the end of the month has been reached and start at row 6 again
                 if day > calendar.monthrange(current_year, month[1])[1]:
                     start_row = 6
        workbook.close()

except Exception as e:
    print(e)
