from django import template
import markdown

register = template.Library()

@register.filter(name='renderMarkdown')
def renderMarkdown(value):
	return markdown.markdown(value)