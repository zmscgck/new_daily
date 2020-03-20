from django.shortcuts import render
from img_db.models import IMG
from img_db.forms import IMGForm
# Create your views here.


# @csrf_exempt
'''
def uploadImg(request):
    if request.method == 'POST':
        new_img = IMG(
            img=request.FILES.get('img'),
            name=request.FILES.get('img').name
        )
        new_img.save()
    return render(request, 'img_db/uploadimg.html')
'''


def uploadImg(request):
    # 上传图片
    if request.method != 'POST':
        # 未提交数据：I创建一个新表单
        form = IMGForm()
    else:
        # POST提交的数据，对数据进行处理
        form = IMGForm(data=request.POST)
        if form.is_valid():
            new_img = form.save(commit=False)
            new_img.owner = request.user
            new_img.save()
            # return HttpResponseRedirect(reverse('note:topics'))
    context = {'form': form}
    return render(request, 'img_db/uploadimg.html', context)


# @csrf_exempt
def showImg(request):
    imgs = IMG.objects.all()
    content = {
        'imgs': imgs,
    }
    for i in imgs:
        print(i.img.url)
    return render(request, 'img_db/showimg.html', content)
