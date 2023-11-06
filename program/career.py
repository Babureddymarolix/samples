class CareerPage:
    def _init_(self):
        self.job_posts = []
        self.applications = []

    def add_job_post(self, job_post):
        self.job_posts.append(job_post)

    def view_job_posts(self):
        for job_post in self.job_posts:
            print(job_post)

    def view_applications(self):
        for application in self.applications:
            print(application)

class Admin:
    def _init_(self, username, password):
        self.username = username
        self.password = password

    def add_job_post(self, career_page, job_post):
        if self.is_authenticated():
            career_page.add_job_post(job_post)
            print("Job post added successfully.")
        else:
            print("Authentication failed. Admin credentials are incorrect.")

    def view_applications(self, career_page):
        if self.is_authenticated():
            career_page.view_applications()
        else:
            print("Authentication failed. Admin credentials are incorrect.")

    def is_authenticated(self):
        return True

class User:
    def _init_(self, username):
        self.username = username

    def view_job_posts(self, career_page):
        career_page.view_job_posts()

    def apply_for_job(self, career_page, job_post):
        career_page.applications.append(f"User: {self.username} applied for Job: {job_post}")


career_page = CareerPage()
admin = Admin("admin_username", "admin_password")
user1 = User("user1")
user2 = User("user2")

job_post1 = "Software Engineer at Company A"
job_post2 = "Data Analyst at Company B"

admin.add_job_post(career_page, job_post1)
admin.add_job_post(career_page, job_post2)

user1.view_job_posts(career_page)
user1.apply_for_job(career_page, job_post1)
user2.view_job_posts(career_page)
user2.apply_for_job(career_page, job_post2)

admin.view_applications(career_page)

