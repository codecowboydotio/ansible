#!/usr/bin/expect -f
spawn ssh-copy-id localhost
expect "Are you sure you want to continue connecting (yes/no)?" 
send "yes\r"
expect "password:"
send "password\n"
expect eof
#expect -timeout 10 "Are you sure you want to continue connecting (yes/no)?" {send "yes\r"; exp_continue}
#expect -timeout 10 "password:" {send "password\n"; exp_continue}
expect eof

