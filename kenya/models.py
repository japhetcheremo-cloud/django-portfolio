from django.db import models


class Profile(models.Model):
    full_name = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    slogan = models.CharField(max_length=300)

    email = models.EmailField()
    phone = models.CharField(max_length=20)

    location = models.CharField(max_length=200)

    bio = models.TextField()

    profile_image = models.ImageField(upload_to="profile/")
    cover_image = models.ImageField(upload_to="cover/")

    cv = models.FileField(upload_to="cv/")

    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    whatsapp = models.CharField(max_length=20)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Skill(models.Model):
    CATEGORY = (
        ("Frontend", "Frontend"),
        ("Backend", "Backend"),
        ("Database", "Database"),
        ("Tools", "Tools"),
    )

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY)
    percentage = models.IntegerField()

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Project(models.Model):
    STATUS = (
        ("Completed", "Completed"),
        ("Ongoing", "Ongoing"),
        ("Archived", "Archived"),
    )

    title = models.CharField(max_length=200)

    image = models.ImageField(upload_to="projects/")

    description = models.TextField()

    technologies = models.CharField(max_length=300)

    github = models.URLField(blank=True)

    live_demo = models.URLField(blank=True)

    featured = models.BooleanField(default=False)

    status = models.CharField(max_length=20, choices=STATUS)

    created = models.DateField()

    def __str__(self):
        return self.title


class Education(models.Model):
    school = models.CharField(max_length=200)

    course = models.CharField(max_length=200)

    start_year = models.IntegerField()

    end_year = models.IntegerField()

    description = models.TextField()

    def __str__(self):
        return self.school


class Experience(models.Model):
    company = models.CharField(max_length=200)

    position = models.CharField(max_length=200)

    start_date = models.DateField()

    end_date = models.DateField()

    description = models.TextField()

    def __str__(self):
        return self.company


class Certificate(models.Model):
    title = models.CharField(max_length=200)

    issuer = models.CharField(max_length=200)

    issue_date = models.DateField()

    certificate = models.FileField(upload_to="certificates/")

    verification_link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=250)

    image = models.ImageField(upload_to="blog/")

    content = models.TextField()

    published = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=200)

    image = models.ImageField(upload_to="gallery/")

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=200)

    profession = models.CharField(max_length=200)

    photo = models.ImageField(upload_to="testimonials/")

    message = models.TextField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)

    email = models.EmailField()

    subject = models.CharField(max_length=200)

    message = models.TextField()

    sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=200)

    logo = models.ImageField(upload_to="logo/")

    favicon = models.ImageField(upload_to="favicon/")

    footer = models.TextField()

    primary_color = models.CharField(max_length=30, default="red")

    maintenance_mode = models.BooleanField(default=False)

    def __str__(self):
        return self.site_name