import base64
mypass=base64.b64encode(b'INTgsm7!7')
print(mypass)
print(base64.b64decode(mypass))