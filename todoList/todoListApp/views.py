from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .models import toDoApp

# Create your views here.
def todo_list(request):
	allData = {'toDoList':toDoApp.objects.all()}
	return render(request ,'todoListApp/todo_list.html',allData)

def insert_todo(request:HttpRequest):
	#database ထဲ data လှမ်းထည့်ပေးရမယ် model ကနေတစ်ဆင့်
	todo =toDoApp(content = request.POST['content'])#database model ကိုအသုံးပြုပြီး data လှမ်းယူတာ
	todo.save()
	return redirect('/todo/list')

def delete_todoItem(request,todo_id):
	delete_id = toDoApp.objects.get(id=todo_id)
	delete_id.delete()
	return redirect('/todo/list')
 
	
 
