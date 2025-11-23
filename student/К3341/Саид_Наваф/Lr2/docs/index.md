# Laboratory Work #2 - Racing Winners Board

## Student Information
- **Name**: Саид Наваф
- **Group**: K3341
- **Variant**: #6 - Табло победителей автогонок (Racing Winners Board)

## Project Overview
A complete racing management system built with Django that allows users to register as racers, participate in races, and manage racing teams and cars.

## Features Implemented

### Core Requirements ✅
- User registration with extended fields
- Race registration with CRUD operations
- Comment system with ratings (1-10) and types
- Admin panel for race result management
- Results table for last 30 days

### Advanced Features ✅
- Bootstrap navigation menu
- Pagination on all list views
- Search functionality across all models
- Responsive design
- Custom user model

## Technical Implementation

### Models
```python
class User(AbstractUser):
    passport_number = models.CharField(max_length=20)
    home_address = models.TextField()
    nationality = models.CharField(max_length=50)
    racing_experience = models.IntegerField(default=0)
    racing_class = models.CharField(max_length=50)