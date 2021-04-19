## Print calendar of any year.
# Print na tela o ano informado.
import calendar
def printcalendar(year):
    print(calendar.calendar(year))
year = int(input('Enter the year: '))
printcalendar(year)