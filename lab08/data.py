import json
cases = [
    {
        "origin": f"IMG_{str(i).zfill(3)}_O.png",
        "puzzle": f"IMG_{str(i).zfill(3)}_P.png",
        "position": [0, 0]
    }
    for i in range(0, 100)  
]

# 构建整个字典结构
data = {
    "tests": {
        "name": "Trick Test",
        "path": "trick_test",
        "error_tolerance": 5,
        "cases": cases
    }
}

# 输出到 JSON 文件
with open('output.json', 'w') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)