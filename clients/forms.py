from django import forms
from .models import Comment , VechicleByCust


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)

class VechicleForm ( forms.ModelForm ) :
    class Meta :
         model = VechicleByCust
         fields = ('client' , 'make' , 'model' , 'vin_number' , 'Date_Of_Purchase' ,
                          'Date_Of_LastService')

         widgets = {
            'Date_Of_Purchase' : DateInput(),
             'Date_Of_LastService' :DateInput(),
         }

    def __init__ ( self , *args , **kwargs ) :
        super ( VechicleForm , self ).__init__ ( *args , **kwargs )
        self.fields['client'].disabled = True
       # self.fields['Date_Of_Purchase'].widget = DateInput ( )
       # self.fields['Date_Of_LastService'].widget = DateInput ( )

class VechicleCreateForm ( forms.ModelForm ) :
    class Meta :
         model = VechicleByCust
         fields = ('make' , 'model' , 'vin_number' , 'Date_Of_Purchase' ,
                          'Date_Of_LastService')
         widgets = {
             'Date_Of_Purchase' : DateInput ( attrs={'type' : 'datetime-local'} , format='%Y-%m-%d' ) ,
             'Date_Of_LastService' : DateInput ( attrs={'type' : 'datetime-local'} , format='%Y-%m-%d' )
         }

    def __init__ ( self , *args , **kwargs ) :
        super ( VechicleCreateForm , self ).__init__ ( *args , **kwargs )
        self.fields['Date_Of_Purchase'].widget = DateInput ( )
        self.fields['Date_Of_LastService'].widget = DateInput ( )


