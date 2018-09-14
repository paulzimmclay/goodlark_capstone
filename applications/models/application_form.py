from django.contrib.auth.models import User
from django.db import models

from multiselectfield import MultiSelectField

# ...

ASSISTANCE_FOR = (('graduate_program', 'Graduate program'),
                  ('four_year_undergraduate', 'Four year undergraduate college program'),
                  ('two_year_associate', 'Two year associate program'),
                  ('certificate_program', 'Certificate program'),)

PAYER = (('mother', 'Mother'),
         ('father', 'Father'),
         ('step-parent', 'Step-parent'),
         ('guardian', 'Guardian'),
         ('spouse', 'Spouse'),
         ('self', 'Self'),)

YES_NO = (('yes', 'Yes'),
          ('no', 'No'),)


class ApplicationFormModel(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    assistance_for = models.CharField(blank=True, choices=ASSISTANCE_FOR, max_length=20, verbose_name='I am applying for Goodlark Scholarship assistance for:')
    mailing_address = models.CharField(blank=True, max_length=100, help_text='your street address')
    city = models.CharField(blank=True, max_length=100)
    zip_code = models.CharField(blank=True, max_length=12)
    county = models.CharField(blank=True, max_length=100)
    length_of_residence_in_county = models.CharField(blank=True, max_length=100, verbose_name='How long have you lived in this county?')
    phone = models.CharField(blank=True, max_length=100)
    cell = models.CharField(blank=True, max_length=100)
    high_school = models.CharField(blank=True, max_length=100)
    graduation_year = models.CharField(blank=True, max_length=100)
    high_school_gpa = models.CharField(blank=True, max_length=100, verbose_name='High School GPA')
    act = models.CharField(blank=True, max_length=100, verbose_name='ACT')
    college_to_receive_scholarship = models.CharField(blank=True, max_length=100)
    student_id = models.CharField(blank=True, max_length=100)
    college_gpa = models.CharField(blank=True, max_length=100, verbose_name='College GPA (if already attending)')
    expected_major = models.CharField(blank=True, max_length=100, verbose_name='Expected major and degree')
    graduation_year = models.CharField(blank=True, max_length=100, verbose_name='Expected year of graduation')
    current_school = models.CharField(blank=True, max_length=100, verbose_name='Current school, if different from above')
    mother_name = models.CharField(blank=True, max_length=100, verbose_name='Mother\'s name')
    mother_occupation = models.CharField(blank=True, max_length=100, verbose_name='Mother\'s occupation')
    mother_place_of_employment = models.CharField(blank=True, max_length=100, verbose_name='Mother\'s place of employment')
    father_name = models.CharField(blank=True, max_length=100, verbose_name='Father\'s name')
    father_occupation = models.CharField(blank=True, max_length=100, verbose_name='Father\'s occupation')
    father_place_of_employment = models.CharField(blank=True, max_length=100, verbose_name='Father\'s place of employment')
    expense_payer = MultiSelectField(blank=True, choices=PAYER, max_length=20, verbose_name='Who will pay for your college expenses? (Please mark all who will contribute)')
    already_accumulated_debt = models.CharField(blank=True, choices=YES_NO, max_length=20, verbose_name='Have you already accumulated school debt?')
    amount_of_debt = models.CharField(blank=True, max_length=100, verbose_name='If so, how much?')
    siblings_enrolled = models.CharField(blank=True, max_length=100, verbose_name='Number of brothers or sisters enrolled in college next year')
    parents_enrolled = models.CharField(blank=True, max_length=100, verbose_name='Number of parents enrolled in college next year')
    previously_received_goodlark = models.CharField(blank=True, choices=YES_NO, max_length=20, verbose_name='Have you previously received a Goodlark Scholarship?')
    year_previously_received = models.CharField(blank=True, max_length=100, verbose_name='If so, what year(s)?')
    family_received_scholarship = models.CharField(blank=True, choices=YES_NO, max_length=20, verbose_name='Has anyone in your family ever received a Goodlark Scholarship?')
    family_member_that_received = models.CharField(blank=True, max_length=100, verbose_name='If so, please list names')
    