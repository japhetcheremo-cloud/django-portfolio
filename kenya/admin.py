from django.contrib import admin
from .models import (
    Profile,
    Skill,
    Service,
    Project,
    Education,
    Experience,
    Certificate,
    Blog,
    Gallery,
    Testimonial,
    Contact,
    SiteSettings
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "profession", "email", "phone")
    search_fields = ("full_name", "profession", "email")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "percentage")
    list_filter = ("category",)
    search_fields = ("name",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "featured",
        "created"
    )
    list_filter = ("status", "featured")
    search_fields = ("title", "technologies")


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        "school",
        "course",
        "start_year",
        "end_year"
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "company",
        "position",
        "start_date",
        "end_date"
    )


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "issuer",
        "issue_date"
    )


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "published"
    )
    search_fields = ("title",)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "profession"
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "subject",
        "sent"
    )
    readonly_fields = ("sent",)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = (
        "site_name",
        "maintenance_mode"
    )