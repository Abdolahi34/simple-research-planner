from django.shortcuts import render
from .forms import ResearchForm


def home(request):
    if request.method == 'POST':
        form = ResearchForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            method = form.cleaned_data['method']

            context = generate_template(topic, method)
            return render(request, 'result.html', context)
    else:
        form = ResearchForm()

    return render(request, 'home.html', {'form': form})


def generate_template(topic, method):
    if method == 'quant':
        return {
            'topic': topic,
            'research_type': 'کمی',
            'goal': f'هدف این تحقیق بررسی رابطه بین متغیرهای مرتبط با {topic} است.',
            'question': f'آیا متغیرهای مرتبط با {topic} تأثیر معناداری دارند؟',
            'data_tool': 'داده‌های کمی (پرسشنامه یا داده‌های ثانویه)',
            'analysis': 'روش‌های آماری متداول مانند رگرسیون'
        }
    else:
        return {
            'topic': topic,
            'research_type': 'کیفی',
            'goal': f'هدف این تحقیق شناسایی و تحلیل ابعاد مختلف {topic} است.',
            'question': f'{topic} چگونه تبیین می‌شود؟',
            'data_tool': 'مصاحبه یا مشاهده',
            'analysis': 'تحلیل محتوا'
        }
