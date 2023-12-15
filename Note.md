- String format:

```
  value = x
  txt = "(text){para:.4f}(text)".format(para=value)
  print(txt) -> (text)(value formatted)(text)
  
  code = 'C' + str(run).zfill(3)
```

- chr(): convert ascii code into its corresponding character
- in theo list: " ".join(list)
- sắp xếp tùy chọn dùng lamda (VD PY04016)
  ```doctest
  ds.sort(key=lambda x: (-x.total))
  # x có thể là một đối tượng, phía sau lấy các thuộc tính
  # cần sắp xếp theo thứ tự ưu tiên
  ```
- chú ý những bài nhập xâu liền thì strip() cho chắc chắn

## Note

### Nhập xuất:

- PYKT089
  ```doctest
  e = []
  while True:
      try:
          e.extend(map(int, input().split()))
      except:
          break
  ```
- Nhập xuất tràn time, cần xử lí kiểu khác

```doctest
#Nhập bằng stdin
from sys import  stdin
```

- Nhập đến khi EOF
  ```doctest
  while True:
      try:
          full_text += input()
      except EOFError:
          break
  
  ```

### Đầu bài khó hiểu

- PY04019: Đầu bài cho TS tăng nhưng thực chất phải TS0 + số thứ tự
    ```doctest
    "TS0{}".format(str(run))
    ```
- PY04005: Nhập xuất phải nhập theo kiểu nhập hết testcase mới được xử lí

### Chú ý

- PY04014: `Decimal(x)` ảo ma vcl vì phép chia trong python sai số vcl
- PY04013

# Support Libraries

- datetime: hỗ trợ chuyển đổi thời gian theo format sẵn
    - Với các phương thức hỗ trợ lấy days, seconds, từ đây ta có thể dùng phép cộng trừ với ngày, với giây phút như bình
      thường

  ```doctest
  from datetime import datetime
  # format giờ phút hh:mm
  time = datetime.strptime(stringtime,__format="%H:%M").seconds
  # format ngày tháng năm  dd/mm/YYYY
  datetime.strptime(stringtime, "%d/%m/%Y").days
  ```
- re: regex trong bài PY03004 (!!!!!!Đầu bài điên)

  ```doctest
  import re
  arr = re.split("[^a-z0-9]", input().lower())
  # lấy các từ có kí tự a-z 0-9
  ```

# Vào ra File

PYKT069, PYKT070

```doctest
f = open("file_nam", mode) 
# rồi đọc bằng readline() như bình thường
```

# Note

PYKT2053