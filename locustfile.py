from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):

    def on_start(self):
        """On start, log in the user."""
        self.login()

    def login(self):
        self.client.post("/login", {
            "email": "test@example.com",
            "password": "password"
        })

    @task(1)
    def upload_file(self):
        """Simulate file upload."""
        with open("sample.pdf", "rb") as file:
            self.client.post("/upload", files={"file": file})

    @task(2)
    def text_input(self):
        """Simulate text input and conversion."""
        self.client.post("/convert", {
            "content": "This is a test input.",
            "conversion_type": "funny_statement"
        })

    @task(3)
    def voice_input(self):
        """Simulate voice input by sending pre-recorded text."""
        self.client.post("/convert", {
            "content": "Voice input test.",
            "conversion_type": "song"
        })

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)

