from django.shortcuts import render,HttpResponse


# Create your views here.
def home(request):
   khabar=[
      {"onvan":"عنوان خبر اول","matn":"متن خبر اول"},
      {"onvan":"عنوان خبر دوم","matn":"متن خبر دوم"},
      {"onvan":"عنوان خبر سوم","matn":"متن خبر سوم"}, 
      {"onvan":"عنوان خبر چهارم","matn":"متن خبر چهارم"},
      {"onvan":"عنوان خبر پنجم","matn":"متن خبر پنجم"},

   ]
   return render(request,"news\index.html",context={"meno":"khabar"})