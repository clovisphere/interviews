import random
from typing import Dict
from locust import HttpUser, task, between


def generate_todo() -> Dict:
    return dict(
        id=random.randint(1, 100),
        todo=f"Todo #{random.randint(1, 100)}",
        status="open"
    )


class UserTask(HttpUser):
    wait_time = between(1, 2)

    @task(5)
    def add_todo(self):
        self.client.post("/todos", json=generate_todo())

    @task(1)
    def view_todo(self):
        self.client.get("/todos")

    @task(3)
    def edit_todo(self):
        self.client.post(
            "/edit-todos",
            json=dict(id=random.randint(1, 100), status=random.choice(["closed", "in progress"]))
        )

    @task(2)
    def delete_todo(self):
        self.client.post("/del-todos", json=dict(id=random.randint(1, 100)))

    def on_start(self):
        self.client.post("/todos", json=generate_todo())
