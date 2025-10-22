import json

json_string='{"ten":"Nguyễn Văn A","tuổi": 32,"công ty":"abc","chức vụ":"nhân viên"}'
python_string=json.loads(json_string)
print(python_string)