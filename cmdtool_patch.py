defender_path = "C:\\Program files\Shadow Defender\CmdTool.exe"

with open(defender_path, "rb") as reader:     
    defender_data = reader.read()
  
defender_data = defender_data.replace(b"\xC7\x84\x24\x6C\x04\x00\x00\x00\x00\x00\x00", b"\xC7\x84\x24\x6C\x04\x00\x00\x01\x00\x00\x00")

with open(defender_path, "wb") as writer:
    writer.write(defender_data)
