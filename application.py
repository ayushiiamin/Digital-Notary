import os
import subprocess
from subprocess import call
import sys

def record():
	

	if len(sys.argv) == 4:
		mode = 1
	elif len(sys.argv) == 3:
		mode = 2
	else :
		print("wrong number of arguments")
	

	if mode == 1:
	
		doc = sys.argv[2]		
		key = sys.argv[3]
		
		call(['openssl', 'dgst', '-sha256', '-sign', key, '-out','signedDoc.txt.sha256' , doc])
	
	elif mode == 2:

		doc = sys.argv[2]

		print("Please enter recipient's email address:")
		emailid = input()
		encrypt = "gpg --encrypt --recipient "+emailid+" "+doc 
		os.system(encrypt)

	elif mode != 1 or mode != 2 :
		print("Invalid syntax")
		quit()
		

def verify():
	

	if len(sys.argv) == 5:
		mode = 1
	elif len(sys.argv) == 3:
		mode = 2
	else :
		print("wrong number of arguments")
	

	if mode == 1:
	
		signedDoc = sys.argv[2]
		doc = sys.argv[3]
		cert = sys.argv[4]

		pubKey = "openssl x509 -in "+cert+" -pubkey -out public_key.pem"
		os.system(pubKey)

		verify = "openssl dgst -sha256 -verify public_key.pem -signature "+ signedDoc+" "+doc
	
		os.system(verify)

	elif mode == 2:
		encryptedFile = sys.argv[2]

		decrypt = "gpg --output text.txt --decrypt "+encryptedFile
		os.system(decrypt)

	elif mode != 1 or mode != 2 :
		print("Invalid syntax")
		quit()
	
	

def main():
	
	if len(sys.argv)<2:
		print("Invalid Syntax")	
		quit()
	elif sys.argv[1] == "record":
		record()
	elif sys.argv[1] == "verify":
		verify()
	else :
		print("Invalid/Missing mode")
		quit()
	



if __name__ == "__main__":
	main()
