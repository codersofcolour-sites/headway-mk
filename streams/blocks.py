""" SteamFields live in here"""

from wagtail.core import blocks
from wagtail.core.blocks.struct_block import StructBlock 
from wagtail.images.blocks import ImageChooserBlock


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


class TeamCards(blocks.StructBlock):
    title = blocks.CharBlock(required=False, max_length=50, help_text="Add your title")
    subtitle = blocks.CharBlock(required=False, max_length=50, help_text="Add your subtitle")

    team = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("name", blocks.CharBlock(required=True, max_length=40)),
                ("position", blocks.CharBlock(required=True, max_length=40)),
            ], icon='user'
        )
    )

    class Meta:
        template = "streams/teamcard_block.html"
        icon = "user"
        label = "Team Cards"


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

    # class ColumnBlock(blocks.StreamBlock):
    #     heading = blocks.CharBlock(classname="full title")
    #     paragraph = blocks.RichTextBlock()
    #     image = ImageChooserBlock()

    #     class Meta:
    #         template = 'blog/blocks/column.html'


    # class TwoColumnBlock(blocks.StructBlock):

    #     left_column = ColumnBlock(icon='arrow-right', label='Left column content')
    #     right_column = ColumnBlock(icon='arrow-right', label='Right column content')

    #     class Meta:
    #         template = 'blog/blocks/two_column_block.html'
    #         icon = 'placeholder'
    #         label = 'Two Columns'

    # class AlignedParagraphBlock(blocks.StructBlock):
    #     alignment = blocks.ChoiceBlock([('left', 'Left'), ('center', 'Center'), ('right', 'Right')])
    #     paragraph = blocks.RichTextBlock()

    #     class Meta:
    #         template = 'blocks/aligned_paragraph.html'
        