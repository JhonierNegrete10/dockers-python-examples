
from multiprocessing import Process, Queue, JoinableQueue, Event
from multiprocessing.synchronize import Event as EventClass
import time
import random


class Camera:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.queue_data = JoinableQueue()
        self.flag_stop: EventClass = Event()
        self.data_process = Process(
            target=self.camera_conection,
            args=(self.queue_data, self.flag_stop),
            name="camera generate data process",
        )

        self.put_database = Process(
            target=self.put_data_database,
            args=(self.queue_data, self.flag_stop),
            name="insert data in database",
        )

    def camera_conection(self, queue: Queue, flag_stop: EventClass):
        while not flag_stop.is_set():
            try:
                data = {"data": str(10 + random.randint(-2, 2))}
                queue.put((data))
                print(f"inter the process, {data}")
                time.sleep(2 + random.randint(0, 1))

            except:
                print("An exception occurred sending the mssg")
                break

    def put_data_database(self, queue: Queue, flag_stop: EventClass):
        count = 0
        while not flag_stop.is_set():
            try:
                if queue.qsize() == 0:
                    if count == 0:
                        print("empty")
                    count += 1
                    continue
                else:
                    data = queue.get()
                    print(data)
            except:
                print("An exception occurred")
                break
