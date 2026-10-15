# Local Web Server Lab

## Goal
Run a local web server and investigate how its folder, running state,
and port affect browser access.

## Environment
Windows PowerShell, Python and a web browser.
This lab ran on my laptop, not in Azure.

## Command
From the python-basics folder, I ran:

```powershell
py -m http.server 8000 --bind 127.0.0.1
```

## Observations
- Starting the server in my user folder displayed that folder's contents.
- Starting it in python-basics displayed README.md and stock_checker.py.
- Stopping the server with Ctrl+C caused ERR_CONNECTION_REFUSED on refresh.
- Restarting the server restored access.
- Port 9000 was unreachable while port 8000 still worked.

## What I learned
- A server must be running to answer requests.
- The browser must connect to the correct port.
- 127.0.0.1 points to the computer making the request.
- This server serves files from its current folder.
- Serving a Python file does not execute it.

## TCP port checks

I tested connectivity using PowerShell:

- Server running, port 8000: TcpTestSucceeded was True.
- Server stopped, port 8000: connection failed.
- Server running on 8000, testing port 9000: connection failed.

A successful TCP test confirms a connection to the port.
It does not prove the application works correctly.
A failed test alone does not identify the cause.