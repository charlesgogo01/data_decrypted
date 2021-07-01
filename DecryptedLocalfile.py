from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Util.number import bytes_to_long
import traceback
import os
import binascii


def DecryptedLocalfile(masterCryptoKey, initializationVector, encryptedFileName, plainFileName):
    if masterCryptoKey == "" or initializationVector == "" or encryptedFileName == "" or plainFileName == "":
        print("Invalid Input parameter.")
        return

    if not os.path.exists(encryptedFileName):
        print("The source file does not exist.")

    ctr = Counter.new(128, initial_value=bytes_to_long(initializationVector))
    aesCtrCrypter = AES.new(binascii.a2b_hex(masterCryptoKey), mode=AES.MODE_CTR, counter=ctr)

    try:
        totalCount = 0
        with open(plainFileName, "wb") as wfd:
            with open(encryptedFileName, "rb") as fd:
                while True:
                    data = fd.read(65536)
                    if not data:
                        break
                    totalCount += len(data)
                    plaintext = aesCtrCrypter.decrypt(data)
                    wfd.write(plaintext)
        print("Successfully decrypt file [%s] to [%s]" % (encryptedFileName, plainFileName))
        print("Total count is %d." % (totalCount))
    except Exception:
        print(traceback.format_exc())

fileList = ["test.txt", "test0k.txt", "test64k.txt", "test1m.txt", "test10m.txt", "test100m.txt", "test1g.txt",
		"test5g.txt", "test10g.txt", "1.mp4", "2.mp4", "3.mp4", "5.mp4", "powerdesigner1029.zip"]

iv = "12345678abcdefgh"
masterCryptoKey = "12345678123456781234567812345678"

# for example：
for fileName in  fileList:
    DecryptedLocalfile(masterCryptoKey, iv,
                      "D:/Program Files (x86)/obsutil_windows_amd64_5.1.7.2/test-reliability/test-encryption/"+fileName,
                      "D:/Program Files (x86)/obsutil_windows_amd64_5.1.7.2/test-reliability/download/"+fileName)
