from pathlib import Path
import requests



# now_path = Path.cwd()
p = Path('.')
r = requests.get(r'https://gitee.com/pscly/my_y1/raw/master/configs/config.yaml')
print()

