""" SteamFields live in here"""

from wagtail.core import blocks
from wagtail.core.blocks.struct_block import StructBlock 
from wagtail.images.blocks import ImageChooserBlock
from blog.models import BlogPage

class CarouselBlock(blocks.StreamBlock):
    carousel_item = blocks.StructBlock([
                ("image", ImageChooserBlock(required=True)),
                ("header", blocks.CharBlock(required=False, max_length=40)),
                ("text", blocks.TextBlock(required=False, max_length=200, help_text = 'Add additional text')),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")),
            ], icon='image')

    class Meta:
        template = "streams/carousel_block.html"
        label = "Carousel Image"

class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()

    class Meta:
        icon="image"
        template = "streams/image_block.html"
        label = "Image"

class ActionAreaBlock(blocks.StructBlock):
    text = blocks.CharBlock(required = True, help_text ='Add your title')
    image = ImageChooserBlock(required=False)
    button_page= blocks.PageChooserBlock(required=False)
    button_url= blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")
    button_text = blocks.CharBlock(required=False, default='Learn More', max_length=18)

    class Meta:
        template = "streams/action_area_block.html"
        icon = "doc-full-inverse"
        label = "Jumbotron - Text & Button"

class LatestBlogPosts(blocks.StructBlock):
    static = blocks.StaticBlock(admin_text='Latest blog posts: no configuration needed.',)

    def get_context(self, request, *args, **kwargs):
        context = super(LatestBlogPosts, self).get_context(request, *args, **kwargs)
        context['blog'] = BlogPage.objects.all().order_by('-first_published_at').live()[:3]
        return context

    class Meta:
        icon = 'radio-full'
        label = 'LatestBlogPosts'
        template = 'streams/latest_posts.html'



class TitleAndTextBlock(blocks.StructBlock):
    """ Title and text and nothing else"""

    title = blocks.CharBlock(required = True, help_text ='Add your title')
    text = blocks.TextBlock(required = True, help_text = 'Add additional text')

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"

class RichtextBlock(blocks.RichTextBlock):
    """Richtext with all the features."""

    class Meta: 
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"

class CardBlock(blocks.StructBlock):
    subtitle = blocks.CharBlock(required=False, max_length=50, help_text="Add your subtitle")
    title = blocks.CharBlock(required=False, max_length=50, help_text="Add your title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")),
            ], icon='list-ul'
        )
    )

    class Meta:
        template = "streams/card_block.html"
        icon = "form"
        label = "Cards"


class SimpleRichtextBlock(blocks.RichTextBlock):
    """Richtext without (limited) all the features."""

    def __init__(
        self, required=True, help_text=None, editor="default", features=None, **kwargs
    ): 
        super().__init__(**kwargs)
        self.features = ["h1","h2","h3","h4",'ol','ul',"bold", "italic", "link",'image',"embed"]

    class Meta: 
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Content RichText"
    
class CTABlock(blocks.StructBlock):
    """A simple call to action section."""

    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.RichTextBlock(required=True, features=["bold", "italic"])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default='Learn More', max_length=40)

    class Meta:  # noqa
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "Call to Action"
