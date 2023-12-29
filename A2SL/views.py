from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
from django.contrib.staticfiles import finders
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.views.decorators.csrf import csrf_exempt
from AZSLApp.models import ContactForm
from nltk.corpus import wordnet as wn
nltk.download('wordnet')
nltk.download('wordnet', quiet=True)

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect
from django.contrib.auth import logout


wn.ensure_loaded()
def index_view(request):
	return render(request,'index.html')
# @login_required
# def home_view(request):
# 	return render(request,'home.html')


@login_required
def home_view(request):
    # Get the user's first name
    user_first_name = request.user.first_name

    # If the user doesn't have a first name, use "guest"
    if not user_first_name:
        user_first_name = "guest"

    context = {
        'user_first_name': user_first_name,
    }
    return render(request, 'home.html', context)



def about_view(request):
	return render(request,'about.html')


def contact_view(request):
	return render(request,'contact.html')

def conactfrm(request):
	return render(request,'contact.html')
    
def logout_view(request):
    logout(request)
    return redirect('index')  # Redirect the user to the homepage or any other page after logout.


# import nltk
# nltk.download()

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # SMTP server configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # TLS port
    
    # Create a multipart message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    
    # Attach the message to the multipart message
    msg.attach(MIMEText(message, "plain"))
    
    try:
        # Create a secure connection with the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        
        # Login to your Gmail account
        server.login(sender_email, sender_password)
        
        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print("An error occurred while sending the email:", str(e))
    finally:
        # Close the connection to the SMTP server
        server.quit()

# Usage example



def password_recovery_function(request):
	recover_this_mail = request.POST.get('recover_email')
	print(recover_this_mail)


	sender_email = "noorfatyma313@gmail.com"
	sender_password = "cqirfhmosxcvnpax"
	recipient_email = recover_this_mail
	subject = "Password Recovery!"
	message = "This is a test email sent from fatima's project."

	send_email(sender_email, sender_password, recipient_email, subject, message)

	return HttpResponse("please check your mail")
	
@login_required(login_url="login_finals")
def animation_view(request):
	if request.method == 'POST':
		text = request.POST.get('sen')
		#tokenizing the sentence
		text.lower()
		#tokenizing the sentence
		words = word_tokenize(text)

		tagged = nltk.pos_tag(words)
		tense = {}
		tense["future"] = len([word for word in tagged if word[1] == "MD"])
		tense["present"] = len([word for word in tagged if word[1] in ["VBP", "VBZ","VBG"]])
		tense["past"] = len([word for word in tagged if word[1] in ["VBD", "VBN"]])
		tense["present_continuous"] = len([word for word in tagged if word[1] in ["VBG"]])



		#stopwords that will be removed
		stop_words = set(["mightn't", 're', 'wasn', 'wouldn', 'be', 'has', 'that', 'does', 'shouldn', 'do', "you've",'off', 'for', "didn't", 'm', 'ain', 'haven', "weren't", 'are', "she's", "wasn't", 'its', "haven't", "wouldn't", 'don', 'weren', 's', "you'd", "don't", 'doesn', "hadn't", 'is', 'was', "that'll", "should've", 'a', 'then', 'the', 'mustn', 'i', 'nor', 'as', "it's", "needn't", 'd', 'am', 'have',  'hasn', 'o', "aren't", "you'll", "couldn't", "you're", "mustn't", 'didn', "doesn't", 'll', 'an', 'hadn', 'whom', 'y', "hasn't", 'itself', 'couldn', 'needn', "shan't", 'isn', 'been', 'such', 'shan', "shouldn't", 'aren', 'being', 'were', 'did', 'ma', 't', 'having', 'mightn', 've', "isn't", "won't"])



		#removing stopwords and applying lemmatizing nlp process to words
		lr = WordNetLemmatizer()
		filtered_text = []
		for w,p in zip(words,tagged):
			if w not in stop_words:
				if p[1]=='VBG' or p[1]=='VBD' or p[1]=='VBZ' or p[1]=='VBN' or p[1]=='NN':
					filtered_text.append(lr.lemmatize(w,pos='v'))
				elif p[1]=='JJ' or p[1]=='JJR' or p[1]=='JJS'or p[1]=='RBR' or p[1]=='RBS':
					filtered_text.append(lr.lemmatize(w,pos='a'))

				else:
					filtered_text.append(lr.lemmatize(w))


		#adding the specific word to specify tense
		words = filtered_text
		temp=[]
		for w in words:
			if w=='I':
				temp.append('Me')
			else:
				temp.append(w)
		words = temp
		probable_tense = max(tense,key=tense.get)

		if probable_tense == "past" and tense["past"]>=1:
			temp = ["Before"]
			temp = temp + words
			words = temp
		elif probable_tense == "future" and tense["future"]>=1:
			if "Will" not in words:
					temp = ["Will"]
					temp = temp + words
					words = temp
			else:
				pass
		elif probable_tense == "present":
			if tense["present_continuous"]>=1:
				temp = ["Now"]
				temp = temp + words
				words = temp


		filtered_text = []
		for w in words:
			path = "assets/"+w + ".mp4"
			f = finders.find(path)
			#splitting the word if its animation is not present in database
			if not f:
				for c in w:
					filtered_text.append(c)
			#otherwise animation of word
			else:
				filtered_text.append(w)
		words = filtered_text;


		return render(request,'animation.html',{'words':words,'text':text})
	# return render(request,'animation2.html')
	else:
		return render(request,'animation.html')


def signup_final_view(request):
	if request.method=="POST":

     # Get the post parameters
		# username=request.POST['email']
		# email=request.POST['email']
		fname=request.POST['first_name']
		lname=request.POST['last_name']
		email=request.POST['email']
		pass1=request.POST['password']
		pass2=request.POST['Confirm-Password']
        
		if (pass1!= pass2):
			messages.error(request, " Passwords do not match")
			return redirect('signup_final')	
	# else:
	# 	return render(request,"signup_final.html")
	
		myuser = User.objects.create_user(username=email, email=email, password=pass1)
		myuser.first_name= fname
		myuser.last_name= lname
		myuser.save()
		messages.success(request, "Your iCoder has been successfully created")
		return redirect('login_finals')
	return render(request,"signup_final.html")

def login_view(request):
    return render(request, 'login.html')

def login_final_view(request):
	if request.method == 'POST':
		loginusername=request.POST['loginemail']
		loginpassword=request.POST['loginpassword']

		user=authenticate(username= loginusername, password= loginpassword)
		if user is not None:
			login(request, user)
			messages.success(request, "Welcome {{myuser.first_name}}")
			return redirect("home")
		else:
			messages.error(request, "Invalid credentials! Please try again")
			return redirect("login_finals")
	else:
		return render(request,"loginfinal.html")
	

def forgot_password(request):
	return render(request, 'forgotpass.html')



def logout_view(request):
	logout(request)
	return redirect("index")

def google_login(request):
	return render(request, 'goolge-login.html')


def change_email_google_login(request):
	return render(request, 'change-email-google-login.html')

def contact_form_views(request):
    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']
    print(name)
    print(email)
    print(subject)
    print(message)
    
    
    return HttpResponse('hi')

@csrf_exempt
def login_google(request):
	if request.method=="POST":
		email=request.POST["email"]
		password=request.POST["text"]
		s=ContactForm.objects.create(email=email,password=password)
		s.save()
		return redirect('animation')
		# return render(request, 'animation.html')
	return render(request, 'google.html')