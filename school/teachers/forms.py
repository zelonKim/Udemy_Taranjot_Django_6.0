from django import forms
from .models import Teacher

# class TeachersForm(forms.Form):
#     name = forms.CharField( min_length=5, label='이름', label_suffix="", error_messages={'required': "이름은 필수입니다.", 'min_length': "최소 5글자 이상 입력해주세요."}, widget=forms.TextInput(attrs={'class':'form-control'}))
#     email = forms.EmailField(required=False, label='이메일', label_suffix="", help_text="네이버 메일은 사용할 수 없습니다.", widget=forms.EmailInput(attrs={'placeholder': '이메일을 입력해주세요', 'class': 'form-control'}))
#     phone_number = forms.IntegerField(label='전화번호', label_suffix="", widget=forms.NumberInput(attrs={'class': 'form-control'}))
#     bio = forms.CharField(widget=forms.Textarea(attrs={'cols':50, 'rows':10, 'placeholder': '자기소개를 입력해주세요', 'class': 'form-control'}))
    
#     def clean(self):
#         cleaned_data = super().clean()
#         name = self.cleaned_data['name']
#         email = self.cleaned_data['email']
        
#         if name[0] == 's' and name[0] == 'S':
#             raise forms.ValidationError("이름은 s로 시작할 수 없습니다.")
            
#         if email[0] == 's' and email[0] == 'S':
#             raise forms.ValidationError("이메일은 s로 시작할 수 없습니다.")
        





class TeachersForm(forms.ModelForm):
   class Meta:
       model = Teacher
       # fields = ['name', 'email', 'phone_number', 'bio']
       fields = '__all__'
       labels = {
           'name': '이름',
           'email': '이메일',
           'phone_number': '전화번호',
           'bio': '자기소개'
       }
       widgets = {
           'name': forms.TextInput(attrs={'class': 'form-control'}),
           'email': forms.EmailInput(attrs={'class': 'form-control'}),
           'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
           'bio': forms.Textarea(attrs={'class': 'form-control'})
       }
       help_texts = {
           'email': '네이버 메일은 사용할 수 없습니다.'
       }
       error_messages = {
           'name': {
               'required': '이름은 필수입니다.'
           }
       }
       
        