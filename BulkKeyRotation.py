#!/usr/bin/python
import sys, subprocess

with open ("./usuarios.txt", "r") as myfile:
    usuarios=myfile.readlines()
    for i in usuarios:
        i = i.strip('\n')
        try:
            response=subprocess.check_output(["aws", "iam", "create-access-key", "--user-name", i], stderr=None)
            with open("./keys.log", "a") as log:
            	print >> log, response
        except:
            response=("The user {} either does not existe, or else it already has 2 access keys".format(i))
            with open("./errors.log", "a") as log:
                print >> log, response
    sys.exit(0)
