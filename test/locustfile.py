from locust import HttpUser, task, between

class LoginUser(HttpUser):
    wait_time = between(2, 5)
    
    def on_star(self):
        self.client.post("/login", json={"username": "Ale", "password": "1234"})
        
    @task(3)
    def view_users(self):
        self.client.get("/users")
        
    @task(2)
    def view_images(self):
        self.client.get("/images")