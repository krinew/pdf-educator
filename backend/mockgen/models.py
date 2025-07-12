from django.db import models

# Create your models here.

class SourceDocument(models.Model):
    DOC_TYPE_CHOICES = [
        ('PDF', 'PDF Document'),
        ('PPT', 'PowerPoint Slides'),
        ('DOC', 'Word Document'),
        ('IMG', 'Scanned Image'),
    ]

    name        = models.CharField(max_length=255, help_text="Original file name")
    doc_type    = models.CharField(max_length=10, choices=DOC_TYPE_CHOICES)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed   = models.BooleanField(default=False)
    notes       = models.TextField(blank=True, help_text="Optional comments or parse issues")

    # NEW: store the actual file
    file        = models.FileField(
        upload_to='source_docs/%Y/%m/%d/',
        help_text="Upload the original document here"
    )

    def __str__(self):
        return f"{self.name} ({self.doc_type})"
    
    
class Question(models.Model):
    COURSE_CHOICES = [
        ('CS101', 'Intro to Computer Science'),
        ('CS202', 'Data Structures'),
    ]
    
    QUESTION_TYPE_CHOICES = [
        ('MCQ', 'Multiple Choice Question'),
        ('SUBJECTIVE', 'Subjective'),
        ('MISCELLANEOUS', 'Miscellaneous'),
    ]
    
    source = models.ForeignKey(
        SourceDocument,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='questions',
        help_text="The document this question was extracted from"
    )

    course_code = models.CharField(
        max_length=10,
        choices=COURSE_CHOICES,
        default='CS101',
        help_text="Identifier for the course"
    )
    year        = models.PositiveSmallIntegerField(
        help_text="Exam year of this past question"
    )
    question_type = models.CharField(
        max_length=15,
        choices=QUESTION_TYPE_CHOICES,
        default='MCQ',
        help_text="Type of question (MCQ, Subjective, or Miscellaneous)"
    )
    text        = models.TextField(
        help_text="The full question text"
    )
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course_code} ({self.year}) - {self.question_type}: {self.text[:50]}…"
    
    
    
