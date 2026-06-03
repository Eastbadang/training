# pip install pywinrm requests_kerberos

#! /usr/bin/env python
import winrm

# Create winrm connection.
sess = winrm.Session('https://ip', auth=('username','password'), transport='kerberos')
result = sess.run_cmd('ipconfig', ['/all'])