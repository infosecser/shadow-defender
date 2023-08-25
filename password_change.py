import hashlib
import winreg
import sys

# Получение значения из реестра
reg_type = winreg.HKEY_LOCAL_MACHINE
reg_dir = winreg.OpenKeyEx(reg_type, r"SYSTEM\\CurrentControlSet\\Services\\diskpt\\")
guid = winreg.QueryValueEx(reg_dir, 'GUID')[0]
winreg.CloseKey(reg_dir)

# Формирование значения
password = sys.argv[1]
data = "{}{}".format(guid, password)

# Получение хэша
hash_store = b''
for byte in data:
  hash_store += byte.encode() + b'\x00'
hash = hashlib.md5(hash_store).hexdigest()
line = "hash={}\n".format(hash)

# Чтение из файла конфигурации
with open(r"C:\\Program Files\\Shadow Defender\\user.dat", 'r') as file:
  data = file.readlines()

for ptr in range(len(data)):
  if "hash=" in data[ptr]:
    del data[ptr]
data.append(line)

# Запись в файл конфигурации
with open(r"C:\\Program Files\\Shadow Defender\\user.dat", 'w') as file:
  data = file.writelines(data)
