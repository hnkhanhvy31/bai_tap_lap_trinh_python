import json

python_string={'ten': 'Nguyễn Văn A', 'tuổi': 32, 'công ty': 'abc', 'chức vụ': 'nhân viên'}

json_string=json.dumps(python_string,skipkeys=False,ensure_ascii=False,check_circular=True,allow_nan=True,cls=None,indent=4,separators=None,default=None,sort_keys=False)
print(json_string)
