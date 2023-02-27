#icyx vm
source = "https://raw.githubusercontent.com/icyx0/PythonVM/main/vm-files/vm.py"
import urllib.request
exec(str(urllib.request.urlopen(source).read(),"utf-8").format(key="<YOUR-KEY-GOES-HERE>")) #use a random 256 bit hexadecimal for the key
