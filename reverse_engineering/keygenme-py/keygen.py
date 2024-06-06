import hashlib
from cryptography.fernet import Fernet
import base64



username_trial = b"FREEMAN"

part1 = hashlib.sha256(username_trial).hexdigest()[4]
part2 = hashlib.sha256(username_trial).hexdigest()[5]
part3 = hashlib.sha256(username_trial).hexdigest()[3]
part4 = hashlib.sha256(username_trial).hexdigest()[6]
part5 = hashlib.sha256(username_trial).hexdigest()[2]
part6 = hashlib.sha256(username_trial).hexdigest()[7]
part7 = hashlib.sha256(username_trial).hexdigest()[1]
part8 = hashlib.sha256(username_trial).hexdigest()[8]
print("\n")
print(part1 + part2 + part3 + part4 + part5 + part6 + part7 + part8)


