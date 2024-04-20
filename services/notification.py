from typing import Annotated

from fastapi import BackgroundTasks


class NotifyService(object):
    __instance = None

    def __init__(self) -> None:
        pass

    @staticmethod
    def write_log(message: str):
        with open("log.txt", mode="a") as log:
            log.write(message)

    @staticmethod
    async def send_notification(
            self,
            email: str, background_tasks: BackgroundTasks
    ):
        message = f"message to {email}\n"
        background_tasks.add_task(self.write_log, message)
        return {"message": "Message sent"}
