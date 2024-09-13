# raise Exception("bad code")
# raise FileExistsError("file not found")

try:
    x=7/0
except Exception as e:
    print(e)
finally:
    raise Exception("bad code")