#!/bin/bash

filename='words.txt'
c=0
arr=( 0 1 2 3 4 5 6 7 8 9 )

while read line
do
	((c++))
	for password in "${arr[@]}" :
	do
		password+=$line	
	
		openssl enc -d -aes-192-cbc -md md5 -k $password -in cipher-task3-111 -out decoutcbc.txt -nopad -pbkdf2 -nosalt

		if [ "$(file decoutcbc.txt)" = "decoutcbc.txt: ASCII text" ]
		then
			echo "Passowrd: $password"
			break
		fi
	done
done < $filename


