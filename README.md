# data_decrypted

when  a file encrypted by AES256/CTR method and know the IV value，you can use this function do the decrypted.



# for example：




```
fileList = ["test.txt", "test0k.txt", "test64k.txt", "test1m.txt", "test10m.txt", "test100m.txt", "test1g.txt",
		"test5g.txt", "test10g.txt", "1.mp4", "2.mp4", "3.mp4", "5.mp4", "powerdesigner1029.zip"]

iv = "12345678abcdefgh"
masterCryptoKey = "12345678123456781234567812345678"

for fileName in  fileList:
    DecryptedLocalfile(masterCryptoKey, iv,
                      "D:/Program Files (x86)/obsutil_windows_amd64_5.1.7.2/test-reliability/test-encryption/"+fileName,
                      "D:/Program Files (x86)/obsutil_windows_amd64_5.1.7.2/test-reliability/download/"+fileName)
                      
            
