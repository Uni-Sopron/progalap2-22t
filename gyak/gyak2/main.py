import matplotlib.pyplot as plt
import csv
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator
from datetime import date

data = {}
countries = []
names = {}

with open('data.csv') as csvFile:
    reader = csv.reader(csvFile)
    for (country, code, d, cases) in reader:
        if code not in countries:
            countries.append(code)
            names[code] = country
            data[code] = {'date': [date.fromisoformat(d)], 'cases': [
                int(cases)]}
        else:
            data[code]['date'].append(date.fromisoformat(d))
            data[code]['cases'].append(int(cases))

selected = 'USA'

months = mdates.MonthLocator()
days = mdates.DayLocator()

fig, ax = plt.subplots(num=f'Daily COVID cases in {selected}')
ax.plot(data[selected]['date'], data[selected]['cases'])
ax.plot('date', 'cases', data=data[selected], label='Hungary')


sub = data[selected]

ym = sub['cases'][:2]
for i in range(2, len(sub['cases'])):
    current = sub['cases'][i]
    prev = sub['cases'][i-1]
    penu = sub['cases'][i-2]
    ym.append((current + prev + penu) / 3)

ax.plot(sub['date'], ym, label='Rolling average')

ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y.%m.%d.'))
ax.xaxis.set_minor_locator(days)

# ax.yaxis.set_major_locator(MultipleLocator(1000))
ax.yaxis.set_major_locator(MultipleLocator(100000))
# ax.yaxis.set_minor_locator(MultipleLocator(100))
ax.yaxis.set_minor_locator(MultipleLocator(10000))
ax.yaxis.set_major_formatter('{x:.0f}')


# for name in names:
#     ax.plot('date', 'cases', data=data[name], label=names[name])

fig.autofmt_xdate()
fig.suptitle(f'Daily COVID cases in {names[selected]}', fontsize=16)
fig.legend(fontsize='xx-small', loc='upper left', ncol=5)
fig.savefig('chart.png')

# plt.show()
