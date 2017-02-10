import subprocess

# p = subprocess.Popen(['python','main.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
# stdout,stderr = p.communicate()
# print 'stdout : ',stdout
# print 'stderr : ',stder


# import subprocess
# p = subprocess.Popen(['python','main.py'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=False)

# stdout,stderr = p.communicate()
# print 'stdout : ',stdout
# print 'stderr : ',stderr


p = subprocess.Popen("python main.py", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
returncode = p.poll()
while returncode is None:
        line = p.stdout.readline()
        returncode = p.poll()
        line = line.strip()
        print line
print returncode