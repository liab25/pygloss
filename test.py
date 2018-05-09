import requests
import json

while_def = requests.get('https://raw.githubusercontent.com/liab25/pygloss/master/while.md', auth=('liab_t@hotmail.com', 'Drift3r@30'))

print(while_def.text)
