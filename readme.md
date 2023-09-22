# commands
docker build . -t python:0.0.2
docker run -p 8000:8000 -t python:0.0.2 
docker run -p 8000:8000 -t python:0.0.2 -v /dockers:/app 

docker-compose build
docker-compose up


# Multiprocessing 
The start() function does not block, meaning it returns immediately.

We can explicitly wait for the new process to finish executing by calling the join() function.

# Error Queue  
```sh
$ docker run -p 8000:8000 -t python:0.0.3 
INFO:     Will watch for changes in these directories: ['/app']
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [1] using StatReload
INFO:     Started server process [8]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     172.17.0.1:48346 - "GET /docs HTTP/1.1" 200 OK
INFO:     172.17.0.1:48346 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     172.17.0.1:48348 - "GET /version HTTP/1.1" 200 OK
INFO:     172.17.0.1:48354 - "GET /test HTTP/1.1" 200 OK
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/usr/local/lib/python3.10/multiprocessing/spawn.py", line 116, in spawn_main
    exitcode = _main(fd, parent_sentinel)
  File "/usr/local/lib/python3.10/multiprocessing/spawn.py", line 126, in _main
    self = reduction.pickle.load(from_parent)
  File "/usr/local/lib/python3.10/multiprocessing/synchronize.py", line 110, in __setstate__
    self._semlock = _multiprocessing.SemLock._rebuild(*state)
FileNotFoundError: [Errno 2] No such file or directory
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/usr/local/lib/python3.10/multiprocessing/spawn.py", line 116, in spawn_main
    exitcode = _main(fd, parent_sentinel)
  File "/usr/local/lib/python3.10/multiprocessing/spawn.py", line 126, in _main
    self = reduction.pickle.load(from_parent)
  File "/usr/local/lib/python3.10/multiprocessing/synchronize.py", line 110, in __setstate__
    self._semlock = _multiprocessing.SemLock._rebuild(*state)
FileNotFoundError: [Errno 2] No such file or directory
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/usr/local/lib/python3.10/multiprocessing/spawn.py", line 116, in spawn_main
    exitcode = _main(fd, parent_sentinel)
  File "/usr/local/lib/python3.10/multiprocessing/spawn.py", line 126, in _main
    self = reduction.pickle.load(from_parent)
  File "/usr/local/lib/python3.10/multiprocessing/synchronize.py", line 110, in __setstate__
    self._semlock = _multiprocessing.SemLock._rebuild(*state)
FileNotFoundError: [Errno 2] No such file or directory
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [8]
INFO:     Stopping reloader process [1]
```

# Error Pipe 
```bash
$ docker run -p 8000:8000 -t python:0.0.3 
INFO:     Will watch for changes in these directories: ['/app']
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [1] using StatReload
INFO:     Started server process [8]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     172.17.0.1:48362 - "GET /version HTTP/1.1" 200 OK
~~~ test_func: one
~~~ test_func: two
~~~ test_func: three
Received in process two: Message from two
Process Process-1:2:
Process Process-1:1:
Traceback (most recent call last):
Traceback (most recent call last):
  File "/usr/local/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap     
    self.run()
  File "/usr/local/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap     
    self.run()
  File "/usr/local/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/app/tmp.py", line 15, in worker_function
    conn.recv()  # Espera a recibir una respuesta
  File "/app/tmp.py", line 15, in worker_function
    conn.recv()  # Espera a recibir una respuesta
  File "/usr/local/lib/python3.10/multiprocessing/connection.py", line 250, in recv        
    buf = self._recv_bytes()
  File "/usr/local/lib/python3.10/multiprocessing/connection.py", line 250, in recv        
    buf = self._recv_bytes()
  File "/usr/local/lib/python3.10/multiprocessing/connection.py", line 414, in _recv_bytes 
    buf = self._recv(4)
  File "/usr/local/lib/python3.10/multiprocessing/connection.py", line 414, in _recv_bytes 
    buf = self._recv(4)
  File "/usr/local/lib/python3.10/multiprocessing/connection.py", line 383, in _recv       
    raise EOFError
  File "/usr/local/lib/python3.10/multiprocessing/connection.py", line 379, in _recv       
    chunk = read(handle, remaining)
EOFError
ConnectionResetError: [Errno 104] Connection reset by peer
INFO:     172.17.0.1:48362 - "GET /test HTTP/1.1" 200 OK
Process Process-1:3:
Traceback (most recent call last):
  File "/usr/local/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap     
    self.run()
  File "/usr/local/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/app/tmp.py", line 14, in worker_function
    conn.send(f"Message from {s}")  # Envía un mensaje al otro proceso
  File "/usr/local/lib/python3.10/multiprocessing/connection.py", line 206, in send        
    self._send_bytes(_ForkingPickler.dumps(obj))
  File "/usr/local/lib/python3.10/multiprocessing/connection.py", line 411, in _send_bytes 
    self._send(header + buf)
  File "/usr/local/lib/python3.10/multiprocessing/connection.py", line 368, in _send       
    n = write(self._handle, buf)
BrokenPipeError: [Errno 32] Broken pipe
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [8]
INFO:     Stopping reloader process [1]
```