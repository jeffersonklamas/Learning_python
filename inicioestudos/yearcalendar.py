## Print calendar of any year.
# by @jeffersonklamas
# há  varias versões deste código.
# Print na tela o ano informado.
import calendar
def printcalendar(year):
    print(calendar.calendar(year))
year = int(input('Enter the year: '))
printcalendar(year)