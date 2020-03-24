from django.shortcuts import render
from img_db.models import IMG
from img_db.forms import IMGForm
import django.utils.timezone as timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


# @csrf_exempt
def uploadImg(request):
    # 上传图片
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = IMGForm()
    else:
        # POST提交的数据，对数据进行处理
        form = IMGForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            new_img = form.save(commit=False)
            new_img.owner = request.user
            new_img.save()
            #form.save
            print(new_img.img.url)
            return HttpResponseRedirect(reverse('img_db:show'))
    context = {'form': form}
    return render(request, 'img_db/uploadimg.html', context)


# @csrf_exempt
def showImg(request):
    imgs = IMG.objects.all().filter(
        date_added=timezone.localtime().strftime("%F")
        ).order_by('-date_added')[0:7]
    content = {
        'imgs': imgs,
    }
    # for i in imgs:
    #    print(i.img.url)
    return render(request, 'img_db/showimg.html', content)
