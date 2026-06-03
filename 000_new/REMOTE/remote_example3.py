# windows 서버에 freeSSHd를 설치하시오

import paramiko

hostname = "your-hostname"
username = "your-username"
password = "your-password"
cmd = 'your-command'

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname,username=username,password=password)
    print("Connected to %s" % hostname)
except paramiko.AuthenticationException:
    print("Failed to connect to %s due to wrong username/password" %hostname)
    exit(1)
except Exception as e:
    print(e.message)
    exit(2)

try:
    stdin, stdout, stderr = ssh.exec_command(cmd)
except Exception as e:
    print(e.message)

err = ''.join(stderr.readlines())
out = ''.join(stdout.readlines())
final_output = str(out)+str(err)
print(final_output)