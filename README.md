# serial

## A python serial port utility

This is a cli serial port utility.

Just running
```bash
ser.py
```
will give you gui prompts to enter port and baud rate.


To avoid gui run
```bash
ser.py [port] [baud]
```

There is also a third option for line ending of sent strings.
```bash
ser.py [port] [baud] [ending]
```
Options are 'lf' / 'cr' / 'crlf'. Default is 'lf'.
