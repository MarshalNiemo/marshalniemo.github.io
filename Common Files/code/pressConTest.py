import pressure_converter as pc

pressure = 200
units = ['Pa',
         'kPa',
         'MPa',
         'atm',
         'psi',
         'lbf/ft2',
         'torr',
         'inHg',
         'mmHg',
         'K']

print('Input Unit\t\tOutput Unit\tValue')

for input_unit in unts:
    for output_unit in units:
        message = input_unit + '\t' + output_unit + '\t'
        message += str(pc.pressCon(pressure, input_unit, output_unit))
        print(message)