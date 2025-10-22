import json

json_string='{"ten":"Nguyễn Văn A","tuổi": 32,"công ty":"abc","chức vụ":"nhân viên"}'
python_string=json.loads(json_string)

for key in sorted(python_string.keys()):
    print(f"    {key}: {python_string[key]}")

