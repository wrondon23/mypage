from venv import create
from django.db import models
import uuid

#create model project
#-------------------------------------------------------------------------------------------

class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=200, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title

#create model Review
#-------------------------------------------------------------------------------------------

class Review(models.Model):
    VOTE_TYPE =(
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
        
    )
    
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE )
    #owner
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.value
    
#create model Tag
#-------------------------------------------------------------------------------------------

class Tag(models.Model):
    
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    name = models.CharField(max_length=200) 
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name