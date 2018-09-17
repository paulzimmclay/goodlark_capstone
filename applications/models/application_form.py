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

WORK_TYPES = (
    ('full_time','Full time'),
    ('part_time','Part time'),
    ('work_study','Work/Study'),
    )


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
    currently_employed = models.CharField(blank=True, choices=YES_NO, max_length=20, verbose_name='Are you currently employed?')
    type_of_work = models.CharField(blank=True, max_length=100, verbose_name='If so, where and what type of work?')
    hours_per_week = models.CharField(blank=True, max_length=100, verbose_name='How many hours per week?')
    pay_per_hour = models.CharField(blank=True, max_length=100, verbose_name='Pay per hour?')
    plan_to_work_in_college = models.CharField(blank=True, choices=YES_NO, max_length=20, verbose_name='Do you plan to work in college?')
    expense_payer = MultiSelectField(blank=True, choices=WORK_TYPES, max_length=20, verbose_name='What type of work?')
    clubs_and_activities = models.TextField(blank=True, max_length=500, verbose_name='List school clubs and activities in which you have participated')
    volunteer_activities = models.TextField(blank=True, max_length=500, verbose_name='List community/volunteer activities in which you have participated')
    honors_and_awards = models.TextField(blank=True, max_length=500, verbose_name='List honors and awards which you have received')
    untaxed_yes_no = models.CharField(blank=True, choices=YES_NO, max_length=20, verbose_name='Do you or your parents receive any of the following untaxed income? If yes, please give the yearly totals.')
    social_security = models.CharField(blank=True, max_length=100, verbose_name='Social Security Benefits')
    child_support = models.CharField(blank=True, max_length=100, verbose_name='Child Support')
    afdc = models.CharField(blank=True, max_length=100, verbose_name='AFDC')
    food_stamps = models.CharField(blank=True, max_length=100, verbose_name='Food Stamps')
    other_untaxed = models.CharField(blank=True, max_length=100, verbose_name='Other')
    savings_yes_no = models.CharField(blank=True, choices=YES_NO, max_length=20, verbose_name='Do you or your parents/guardiance have over $5,000 in combined bank savings, checking and other investments such as annuities, certificates of deposit, or stocks?')
    savings_description = models.TextField(blank=True, max_length=300, verbose_name='If yes, please describe')
    family_contribution = models.CharField(blank=True, max_length=100, verbose_name='How much can you and your family contribute to your education this year?')
    essay = models.TextField(blank=True, max_length=500, verbose_name='Our scholarship funds are limited. Please explain why you should receive a Goodlark scholarship.')
    federal_pell_grant = models.CharField(blank=True, max_length=100, verbose_name='Federal Pell Grant')
    fseog_grant = models.CharField(blank=True, max_length=100, verbose_name='FSEOG (Grant)')
    academic_competitiveness_grant = models.CharField(blank=True, max_length=100, verbose_name='Academic Competitiveness Grant')
    national_smart_grant = models.CharField(blank=True, max_length=100, verbose_name='National SMART Grant')
    federal_work_study = models.CharField(blank=True, max_length=100, verbose_name='Federal Work-Study')
    other_federal_aid = models.CharField(blank=True, max_length=100, verbose_name='Other')
    tsaa = models.CharField(blank=True, max_length=100, verbose_name='TN Student ASsistance Award (TSAA)')
    tn_hope = models.CharField(blank=True, max_length=100, verbose_name='TN HOPE Sholarship (Lottery Scholarship')
    tn_hope_general_assembly = models.CharField(blank=True, max_length=100, verbose_name='General Assembly Merit Scholarship (supplement)')
    tn_hope_aspire_award = models.CharField(blank=True, max_length=100, verbose_name='ASPIRE Award (supplement)')
    tn_hope_access_grant = models.CharField(blank=True, max_length=100, verbose_name='TN HOPE Access Grant')
    tn_hope_foster_child_tuition_grant = models.CharField(blank=True, max_length=100, verbose_name='TN HOPE Foster Child Tuition Grant')
    tn_promise = models.CharField(blank=True, max_length=100, verbose_name='TN Promise')
    wilder_naifeh_technical_skills = models.CharField(blank=True, max_length=100, verbose_name='Wilder-Naifeh Technical Skills Grant')
    other_state_aid = models.CharField(blank=True, max_length=100, verbose_name='Other')