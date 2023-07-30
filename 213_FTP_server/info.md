# Simple FTP Server

- Run main.py
- Open CMD

```cmd
PS C:\Users\anura> ftp
ftp> open 127.0.0.1
Connected to 127.0.0.1.
220 Twisted 22.10.0 FTP Server
530 Please login with USER and PASS.
User (127.0.0.1:(none)): anonymous
331 Guest login ok, type your email address as password.
Password:
230 Anonymous login ok, access restrictions apply.
ftp> ls .
200 PORT OK
125 Data connection already open, starting transfer
somefile.txt
226 Transfer Complete.
ftp: 17 bytes received in 0.00Seconds 17.00Kbytes/sec.
ftp> get somefile.txt
200 PORT OK
125 Data connection already open, starting transfer
226 Transfer Complete.
ftp: 242 bytes received in 0.00Seconds 242000.00Kbytes/sec.
ftp>
```

- Check transferred file in ```C:\Users\anura```


## FTP Client-side Operations

- List directory
- Upload/ Download files to/from FTP server
- CRUD operations on files in FTP server
