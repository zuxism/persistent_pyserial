# Persistent Py Serial

## Description

This is a cli serial port utility. It displays the output of chosen serial port to stdout and sends stdin back.

## Persistency

If the specified serial port is not available it will try to reconnect every few seconds until it is.

If disconnected it will, again, try to reconnect every few seconds.

## CLI options

Running
```bash
ser.py
```
will prompt for port and baud rate.

---

To avoid prompts run
```bash
ser.py [port] [baud]
```

---

There is also a third option for line ending of sent strings.
```bash
ser.py [port] [baud] [ending]
```
Options are 'lf', 'cr', 'crlf'. Default is 'lf'.
