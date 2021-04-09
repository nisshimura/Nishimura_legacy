import nfc
import binascii

clf = nfc.ContactlessFrontend('usb')
print('touch card:')
tag = clf.connect(rdwr={'on-connect': lambda tag: False})
clf.close()
idm = binascii.hexlify(tag.idm)
print(idm)
print('please released card')
