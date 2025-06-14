# myapp/forms.py
from django import forms
# Ensure necessary models are imported
from .models import UploadedFile, Students, Course

# --- UploadForm Definition ---
# Needed if using views_yolo.py or other upload functionality
class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']
# --- End UploadForm Definition ---


# --- StudentForm Definition (with corrected validate_unique) ---
# Used by the formset in create_course_view
class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'roll_no', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'roll_no': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control-file', 'accept': 'image/*'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ensure required fields are set if not handled by model Meta naturally
        self.fields['roll_no'].required = True
        self.fields['name'].required = True

    def validate_unique(self):
        # Override to bypass form-level DB unique check for roll_no.
        # The view's logic handles existing records using get/create.
        pass
# --- End StudentForm Definition ---


# --- CourseForm Definition ---
# Used in create_course_view
class CourseForm(forms.ModelForm):
     instructor_name = forms.CharField(max_length=100, required=True)
     class Meta:
         model = Course
         fields = ['name']
         widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
         }
# --- End CourseForm Definition ---