docker build . -t python:0.0.2
docker run -p 8000:8000 -t python:0.0.2 
docker run -p 8000:8000 -t python:0.0.2 -v /dockers:/app 

# Multiprocessing 
The start() function does not block, meaning it returns immediately.

We can explicitly wait for the new process to finish executing by calling the join() function.

bash 
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

