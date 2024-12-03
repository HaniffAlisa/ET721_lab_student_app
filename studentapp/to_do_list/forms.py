from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'id': 'task',
                'class': 'todo_text',
                'placeholder': 'type your task...',
                'aria-label': 'Todo',
                'aria-describedby': 'add-btn'
            }
        )
    )