from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import *
from .mpesa import stk_push

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from openai import OpenAI

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def home(request):

    context = {
        "profile": Profile.objects.first(),
        "skills": Skill.objects.all(),
        "projects": Project.objects.all(),
        "services": Service.objects.all(),
        "testimonials": Testimonial.objects.all(),
        "settings": SiteSettings.objects.first(),
    }

    return render(request, "kenya/index.html", context)



def about(request):

    context = {
        "profile": Profile.objects.first(),
        "education": Education.objects.all(),
        "experience": Experience.objects.all(),
        "certificates": Certificate.objects.all(),
        "settings": SiteSettings.objects.first(),
    }

    return render(request, "kenya/about.html", context)



def projects(request):

    context = {
        "projects": Project.objects.all().order_by("-created"),
        "settings": SiteSettings.objects.first(),
    }

    return render(request, "kenya/projects.html", context)



def blog(request):

    context = {
        "blogs": Blog.objects.all().order_by("-published"),
        "settings": SiteSettings.objects.first(),
    }

    return render(request, "kenya/blog.html", context)



def contact(request):

    profile = Profile.objects.first()

    if request.method == "POST":

        Contact.objects.create(
            name=request.POST.get("name", ""),
            email=request.POST.get("email", ""),
            subject=request.POST.get("subject", ""),
            message=request.POST.get("message", "")
        )

        return redirect("contact")


    context = {
        "profile": profile,
        "settings": SiteSettings.objects.first(),
    }

    return render(request, "kenya/contact.html", context)



# ==========================
# MPESA STK PUSH
# ==========================


@require_POST
def pay_mpesa(request):

    try:

        phone = request.POST.get("phone")
        amount = int(request.POST.get("amount"))


        response = stk_push(
            phone,
            amount
        )


        MpesaPayment.objects.create(

            phone=phone,

            amount=amount,

            checkout_request_id=response.get(
                "CheckoutRequestID"
            ),

            merchant_request_id=response.get(
                "MerchantRequestID"
            ),

        )


        return JsonResponse(response)


    except Exception as e:

        return JsonResponse(
            {
                "error": str(e)
            },
            status=400
        )



def mpesa_callback(request):

    print(request.body)


    return JsonResponse(
        {
            "ResultCode": 0,
            "ResultDesc": "Accepted"
        }
    )
@csrf_exempt
def chatbot(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required"}, status=405)

    if client is None:
        return JsonResponse({
            "reply": "The AI chatbot is temporarily unavailable because the API key has not been configured."
        })

    try:
        data = json.loads(request.body)
        message = data.get("message", "")

        response = client.responses.create(
            model="gpt-5",
            input=message,
        )

        return JsonResponse({
            "reply": response.output_text
        })

    except Exception as e:
        return JsonResponse({
            "reply": f"Error: {str(e)}"
        }, status=500)