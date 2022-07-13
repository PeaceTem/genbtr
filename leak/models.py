from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

"""
FSLeaks.com

The moderators will be given total control over which post goes out before they are out.
They will be given unrestricted access to post
They can see reported posts


Users can send friend request to each other.
friends share leaks and other things with eachother


there will be a trending page according to the demographic, language
    criteria for trending



users can submit request for categories

try to get the language of the user browser so as to serve him his preferred language.
each leaks will have discussions, ratings(upvote and down), demographic


users will be able to share posts to facebook, twitter, reddit, etc.

create an ad network by yourself. use in infoleaks, tothex, etc. Use adsterra

Users will be only allowed to post under each category

There will be sub categories
users can save leaks, sections, etc. as drafts and favorites
"""

Countries = (
   (_('Afghanistan'),_('Afghanistan')),
   (_('Albania'),_('Albania')),
   (_('Algeria'),_('Algeria')),
   (_('Andorra'),_('Andorra')),
   (_('Angola'),_('Angola')),
   (_('Antigua and Barbuda'),_('Antigua and Barbuda')),
   (_('Argentina'),_('Argentina')),
   (_('Armenia'),_('Armenia')),
   (_('Australia'),_('Australia')),
   (_('Austria'),_('Austria')),
   (_('Azerbaijan'),_('Azerbaijan')),
   (_('Bahamas'),_('Bahamas')),
   (_('Bahrain'),_('Bahrain')),
   (_('Bangladesh'),_('Bangladesh')),
   (_('Barbados'),_('Barbados')),
   (_('Belarus'),_('Belarus')),
   (_('Belgium'),_('Belgium')),
   (_('Belize'),_('Belize')),
   (_('Benin'),_('Benin')),
   (_('Bhutan'),_('Bhutan')),
   (_('Bolivia'),_('Bolivia')),
   (_('Bosnia and Herzegovina'),_('Bosnia and Herzegovina')),
   (_('Bostswana'),_('Bostswana')),
   (_('Brazil'),_('Brazil')),
   (_('Brunei'),_('Brunei')),
   (_('Bulgaria'),_('Bulgaria')),
   (_('Burnkina Faso'),_('Burnkina Faso')),
   (_('Burundi'),_('Burundi')),
   (_('Cote D\'Ivoire'),_('Cote D\'Ivoire')),
   (_('Cabo Verde'),_('Cabo Verde')),
   (_('Cambodia'),_('Cambodia')),
   (_('Cameroon'),_('Cameroon')),
   (_('Canada'),_('Canada')),
   (_('Central African Republic'),_('Central African Republic')),
   (_('Chad'),_('Chad')),
   (_('Chile'),_('Chile')),
   (_('China'),_('China')),
   (_('Colombia'),_('Colombia')),
   (_('Congo (Congo Brazzaville)'),_('Congo (Congo Brazzaville)')),
   (_('Costa Rica'),_('Costa Rica')),
   (_('Croatia'),_('Croatia')),
   (_('Cuba'),_('Cuba')),
   (_('Cyprus'),_('Cyprus')),
   (_('Czechnia (Czech Republic)'),_('Czechnia (Czech Republic)')),
   (_('Democratic Republic of the Congo'),_('Democratic Republic of the Congo')),
   (_('Denmark'),_('Denmark')),
   (_('Djibouti'),_('Djibouti')),
   (_('Dominica'),_('Dominica')),
   (_('Dominican Republic'),_('Dominican Republic')),
   (_('Ecuador'),_('Ecuador')),
   (_('Egypt'),_('Egypt')),
   (_('El Salvador'),_('El Salvador')),
   (_('Equatorial Guinea'),_('Equatorial Guinea')),
   (_('Eritrea'),_('Eritrea')),
   (_('Estonia'),_('Estonia')),
   (_('Eswatini'),_('Eswatini')),
   (_('Ethiopia'),_('Ethiopia')),
   (_('Fiji'),_('Fiji')),
   (_('Finland'),_('Finland')),
   (_('France'),_('France')),
   (_('Gabon'),_('Gabon')),
   (_('Gambia'),_('Gambia')),
   (_('Germany'),_('Germany')),
   (_('Ghana'),_('Ghana')),
   (_('Greece'),_('Greece')),
   (_('Grenada'),_('Grenada')),
   (_('Guetamala'),_('Guetamala')),
   (_('Guinea'),_('Guinea')),
   (_('Guinea-Bissau'),_('Guinea-Bissau')),
   (_('Haiti'),_('Haiti')),
   (_('Holy See'),_('Holy See')),
   (_('Honduras'),_('Honduras')),
)

Categories = (
    'Lifestyle',
    'Education',
    'Movies',
    'Politics',
    'Government',
    'Technology',
    'News',
    'Thoughts',
    'Gaming',
    'Wealth',
    'Debates',
    'History',
    'Comedy',
    'Transportation',
    'Tourism',
    'Business',
    'Podcasts',
    'Music',
    'Books',
    'Religion',
    'Lifestyle',
    'Celebrities',
    'Science',
    'Art',
    'Astronomy',
    'Computer Programming',
    'Learning',
    'Facts & Figures',
    'Magazines',
    'Personal Development',
    'Finance',
    'Family & Friends',
    'Natural Environment',
    'Health',
    'Career',
    'Emotion',
    'Fitness',
    'Leisure',
    'Love',
    'Mental Health',
    'Sport',
    'Food & Cooking',
    'Fashion',
    'Travel',
    'Ethical Hacking',
    'GIF & Memes',
    'Photography',
    'Picture',
    'Video',
    'Others',
)



# whenever a category is created there should be a subcategory created automatically with it. And the name of the subcategory will be all.
class Category(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name=_('title'))
    description = RichTextField(verbose_name=_('description'))
    number_of_leaks = models.PositiveIntegerField(default=0, verbose_name=_('number of leaks'))
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return f"{self.title}"





class Subcategory(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, related_name='category')
    title = models.CharField(max_length=100, verbose_name=_('title'))
    description = RichTextField(verbose_name=_('description'))
    number_of_leaks = models.PositiveIntegerField(default=0, verbose_name=_('number of leaks'))
    date = models.DateTimeField(auto_now_add=True)
    # moderators = models.ManyToManyField(User, blank=True, related_name='moderators')
    creator = models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='subcategory')

    class Meta:
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return f"{self.title}"





"""
Anything here should be replicated in the draft leak model
"""



class Leak(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('title'))
    story = RichTextField(verbose_name=_('story'), null=True) # try to change the verbose name and see what will happen 
    votes = models.IntegerField(default=0, verbose_name=_('votes'))
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='leak_category')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, blank=True, related_name='leak_subcategory')
    views = models.IntegerField(default=0)



    def __str__(self):
        return f"{self.title}"





class Image(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    image = models.ImageField(upload_to='leak/images/', verbose_name=_('image'))
    leak = models.ForeignKey(Leak, on_delete=models.CASCADE, blank=True, null=True, related_name='leak_image')


    def __str__(self):
        return f"{self.title}"






class Audio(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    audio = models.FileField(upload_to='leak/audios/', verbose_name=_('audio'))
    leak = models.ForeignKey(Leak, on_delete=models.CASCADE, blank=True, null=True, related_name='leak_audio')


    def __str__(self):
        return f"{self.title}"






class File(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    file = models.FileField(upload_to='leak/files/', verbose_name=_('file'))
    leak = models.ForeignKey(Leak, on_delete=models.CASCADE, blank=True, null=True, related_name='leak_file')



    def __str__(self):
        return f"{self.title}"







class Video(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    video = models.FileField(upload_to='leak/videos/', verbose_name=_('video'))
    leak = models.ForeignKey(Leak, on_delete=models.CASCADE, blank=True, null=True, related_name='leak_video')


    def __str__(self):
        return f"{self.title}"





# class Section(models.Model):
#     # use rich text field
#     header = models.CharField(max_length=100, verbose_name=_('header'))
#     text = RichTextField(verbose_name=_('text'))
#     images = models.ManyToManyField(Image, blank=True, related_name='images')
#     audios = models.ManyToManyField(Audio, blank=True, related_name='audios')
#     files = models.ManyToManyField(File, blank=True, related_name='files')
#     videos = models.ManyToManyField(Video, blank=True, related_name='videos')
#     index = models.PositiveSmallIntegerField(default=0)

#     def __str__(self):
#         return f"{self.header}"







class Comment(models.Model):
    comment = models.CharField(max_length=500, verbose_name=_('comment'))
    date = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)
    leak = models.ForeignKey(Leak, on_delete=models.CASCADE, blank=True, null=True, related_name='leak_comment')

    class Meta:
        ordering = ('votes',)

    def __str__(self):
        return f"{self.comment}"






"""
Learn how to design whatsapp comment form
"""
class Reply(models.Model):
    reply = models.CharField(max_length=500, verbose_name=_('reply'))
    votes = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True, related_name='leak_comment_reply')

    class Meta:
        verbose_name_plural = 'replies'
        ordering = ('votes',)

    def __str__(self):
        return f"{self.reply}"




