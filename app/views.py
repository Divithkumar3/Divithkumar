from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

def portfolio_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f"New Contact Form Submission from {name}"
        message_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        from_email = 'your_email@gmail.com'  # Use the same email as EMAIL_HOST_USER
        recipient_list = ['your_email@gmail.com']  # Your email to receive messages

        try:
            send_mail(subject, message_body, from_email, recipient_list)
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, "Error sending message. Please try again.")

        return redirect('portfolio')  # Redirect after form submission

    return render(request, 'portfolio.html')  # Render portfolio page with form
