from django import forms

from learning_logs.models import Topic, Entry


class TopicForm(forms.ModelForm):  # 继承forms.ModelForm
    class Meta:
        model = Topic  # 根据哪个模型创建表单
        fields = ['text']  # 表单只包含字段text
        labels = {'text': ''}  # 不为字段text生成标签


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry'}
        # 小部件(widget)是一个HTML表单元素，如单行文本框、多行文本区域或下拉列表。通过设置属性widgets，可覆盖Django选择的默认小部件。通过让Django使用forms.Textarea，我们定制了字段
        # 'text'的输入小部件，将文本区域的宽度设置为80列，而不是默认的40列
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
