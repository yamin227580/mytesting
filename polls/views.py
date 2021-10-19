from .models import Post 
from .forms import PostForm,GForm
from django.shortcuts import HttpResponse, render, redirect 
    
def home(request): 
  
    # check if the request is post  
    if request.method =='POST':   
  
        # Pass the form data to the form class 
        details = PostForm(request.POST) 
  
        # In the 'form' class the clean function  
        # is defined, if all the data is correct  
        # as per the clean function, it returns true 
        if details.is_valid():   
  
            # Temporarily make an object to be add some 
            # logic into the data if there is such a need 
            # before writing to the database    
            post = details.save(commit = False) 
  
            # Finally write the changes into database 
            post.save()   
  
            # redirect it to some another page indicating data 
            # was inserted successfully 
            return redirect('/detail') 
              
        else: 
          
            # Redirect back to the same page if the data 
            # was invalid 
            return render(request, "home.html", {'form':details})   
    else: 
  
        # If the request is a GET request then, 
        # create an empty form object and  
        # render it into the page 
        form = PostForm(None)    
        return render(request, 'home.html', {'form':form}) 

def detail(request):

	data = Post.objects.all()

	return render(request,'detail.html',{'data':data})

def gmailform(request):
	if request.method =='POST':
		form = GForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/detail') 
		
		else:
			return render(request, "gmail.html", {'form':form}) 
	else:
		form = GForm(None)
	return render(request, 'gmail.html', {'form': form})

