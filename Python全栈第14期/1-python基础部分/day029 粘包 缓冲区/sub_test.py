import subprocess

sub_obj = subprocess.Popen('dir',stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)

print(sub_obj.stdout.read().decode('gbk'))







