from django import forms
from django.core.validators import RegexValidator
from.models import Person,BloodBank

class PersonForm(forms.Form):
    alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')
    numbers=RegexValidator(r'^[0-9]*$','only numbers allowed')
    GROUPS = (
            ('A+','A+'),
            ('O+','O+'),
            ('B+','B+'),
            ('AB+','AB+'),
            ('A-','A-'),
            ('O-','O-'),
            ('B-','B-'),
            ('AB-','AB-'),
    )
    name=forms.CharField(max_length=101,required=True,validators=[alphanumeric],widget=forms.TextInput(attrs={'placeholder':'Name','class':'form-control'}))
    age=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder':'Age','class':'form-control'}))
    email=forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder':'Email','class':'form-control'}))
    phonenumber=forms.CharField(max_length=10,required=True,widget=forms.TextInput(attrs={'placeholder':'Phonenumber','class':'form-control'}))
    city=forms.CharField(max_length=100,required=True,validators=[alphanumeric],widget=forms.TextInput(attrs={'placeholder':'City','class':'form-control'}))
    district=forms.CharField(max_length=100,required=True,validators=[alphanumeric],widget=forms.TextInput(attrs={'placeholder':'District','class':'form-control'}))
    state=forms.CharField(max_length=100,required=True,validators=[alphanumeric],widget=forms.TextInput(attrs={'placeholder':'State','class':'form-control'}))
    bloodgroup=forms.ChoiceField(choices=GROUPS,required=True,widget=forms.Select(attrs={'class':'form-control'}))
    
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if Person.objects.filter(email=email).exists():
            
            raise forms.ValidationError('Using this email already an account created,use another email')
                
        else:
            return email


    def clean_phonenumber(self):
        phonenumber=self.cleaned_data.get('phonenumber')
        if Person.objects.filter(phonenumber=phonenumber).exists():
            
            raise forms.ValidationError('Using this phonenumber already an account created,use another email')
                
        else:
            return phonenumber
    
    def create_person(self):
        p=Person(
            name=self.cleaned_data.get('name'),
            age=self.cleaned_data.get('age'),
            email=self.clean_email(),
            phonenumber=self.clean_phonenumber(),
            city=self.cleaned_data.get('city'),
            district=self.cleaned_data.get('district'),
            state=self.cleaned_data.get('state'),
            bloodgroup=self.cleaned_data.get('bloodgroup'),
            type_of_donor='Person'
        )
        p.save()
        return p

class BloodBankForm(forms.Form):
    alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')
    numbers=RegexValidator(r'^[0-9]*$','only numbers allowed')
    GROUPS = (
            ('A+','A+'),
            ('O+','O+'),
            ('B+','B+'),
            ('AB+','AB+'),
            ('A-','A-'),
            ('O-','O-'),
            ('B-','B-'),
            ('AB-','AB-'),
    )
    name=forms.CharField(max_length=101,required=True,validators=[alphanumeric],widget=forms.TextInput(attrs={'placeholder':'Name','class':'form-control'}))
    
    email=forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder':'Email','class':'form-control'}))
    phonenumber=forms.CharField(max_length=10,required=True,widget=forms.TextInput(attrs={'placeholder':'Phonenumber','class':'form-control'}))
    city=forms.CharField(max_length=100,required=True,validators=[alphanumeric],widget=forms.TextInput(attrs={'placeholder':'City','class':'form-control'}))
    district=forms.CharField(max_length=100,required=True,validators=[alphanumeric],widget=forms.TextInput(attrs={'placeholder':'District','class':'form-control'}))
    state=forms.CharField(max_length=100,required=True,validators=[alphanumeric],widget=forms.TextInput(attrs={'placeholder':'State','class':'form-control'}))
    bloodgroup=forms.MultipleChoiceField(choices=GROUPS,widget=forms.CheckboxSelectMultiple(attrs={'class':'list-inline'}))


    def clean_email(self):
        email=self.cleaned_data.get('email')
        if Person.objects.filter(email=email).exists():
            
            raise forms.ValidationError('Using this email already an account created,use another email')
                
        else:
            return email


    def clean_phonenumber(self):
        phonenumber=self.cleaned_data.get('phonenumber')
        if Person.objects.filter(phonenumber=phonenumber).exists():
            
            raise forms.ValidationError('Using this phonenumber already an account created,use another email')
                
        else:
            return phonenumber
    
    def create_bloodbank(self):
        p=BloodBank(
            name=self.cleaned_data.get('name'),
            
            email=self.clean_email(),
            phonenumber=self.clean_phonenumber(),
            city=self.cleaned_data.get('city'),
            district=self.cleaned_data.get('district'),
            state=self.cleaned_data.get('state'),
            bloodgroup=self.cleaned_data.get('bloodgroup'),
            type_of_donor='Blood Bank',
        )
        p.save()
        return p


class ContactForm(forms.Form):
    name=forms.CharField(max_length=100,min_length=5,required=True)
    email=forms.CharField(required=True)
    subject=forms.CharField(max_length=100,min_length=5,required=True)
    message=forms.CharField(required=True)