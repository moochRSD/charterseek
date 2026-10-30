import openpyxl
import json
import os
wb = openpyxl.load_workbook('/tmp/part135_latest.xlsx', read_only=True, data_only=True)
ws = wb[wb.sheetnames[0]]
operators = {}
for row in ws.iter_rows(min_row=2, values_only=True):
    cfr, chdo, dsgn, name, aircraft, reg, serial = row
    if not name or '135' not in str(cfr): continue
    if name not in operators: operators[name] = {'cfr': cfr, 'chdo': chdo, 'designator': dsgn, 'aircraft': []}
    operators[name]['aircraft'].append({'model': aircraft, 'registration': reg, 'serial': serial})
os.makedirs('charterseek/data', exist_ok=True)
summary = []
for name, data in sorted(operators.items()):
    summary.append({'name': name, 'cfr': data['cfr'], 'chdo': data['chdo'], 'designator': data['designator'], 'aircraft_count': len(data['aircraft']), 'aircraft_models': list(set(a['model'] for a in data['aircraft'] if a['model']))})
with open('charterseek/data/operators.json', 'w') as f: json.dump(summary, f, indent=2)
print(f'Total operators: {len(operators)}')