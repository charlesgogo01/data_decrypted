# data_decrypted

when  a file encrypted by AES256/CTR method and know the IV value，you can use this function do the decrypted.



# for example：


```
iv = "12345678abcdefgh"
masterCryptoKey = "12345678123456781234567812345678"

for fileName in  fileList:
    DecryptedLocalile(masterCryptoKey, iv,
                      "D:/Program Files (x86)/obsutil_windows_amd64_5.1.7.2/test-reliability/test-encryption/"+fileName,
                      "D:/Program Files (x86)/obsutil_windows_amd64_5.1.7.2/test-reliability/download/"+fileName)
                      
            
