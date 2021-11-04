# serial

## Description

This is a cli serial port utility. It displays the output of chosen serial port to stdout and sends stdin back.

If the specified serial port is not available it will try to reconnect every few seconds until it is. If disconnected it will try to reconnect every few seconds.

## CLI options

Just running
```fish
ser.py
```
will give you gui prompts to enter port and baud rate.


To avoid gui run
```fish
ser.py [port] [baud]
```

There is also a third option for line ending of sent strings.
```fish
ser.py [port] [baud] [ending]
```
Options are 'lf' / 'cr' / 'crlf'. Default is 'lf'.
