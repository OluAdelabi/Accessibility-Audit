import paramiko
pkey = paramiko.RSAKey.from_private_key_file('/Users/fw7424/.ssh/docs')
# transport = paramiko.Transport(('localhost', 3373))
# transport.connect(username='admin', password='admin', pkey=pkey)
# sftp = paramiko.SFTPClient.from_transport(transport)
# sftp.listdir('.')
# ['loop.py', 'stub_sftp.py']