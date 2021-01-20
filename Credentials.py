class Credentials:
    
    def __init__(self,log="", password="", credentialsFilePath="cred.txt"):
        
        if(log != "" or password != ""):
            
            self.login = self.hash_nk(log)
            self.password = self.hash_nk(password)    
            
        else:
            
            tempCred = open(credentialsFilePath, "r")
            
            
            self.login = tempCred.readline()
            self.password = tempCred.readline()
            tempCred.close()
    
    #------------------------------------    
        
    def hash_nk(self, toHash):
        toHash = toHash.encode().hex()
        return toHash
    
    def dehash_nk(self, toDehash):
        return bytes.fromhex(toDehash).decode('utf-8')
    
    #------------------------------------
    
    def get_login(self):
        return self.dehash_nk(self.login)
    
    def get_password(self):
        return self.dehash_nk(self.password)




