import paramiko

hostname = input("Enter hostname: ")
port = input("Enter port (default is 22): ")
username = input("Enter username: ")
password = input("Emter password: ")

given_script = input("specify local shell script for remote execution (script.sh): ")
command = ("time ") + open(given_script).read()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)

err = ''.join(stderr.readlines())
out = ''.join(stdout.readlines())
final_output = str(out)+str(err)
print(final_output)
