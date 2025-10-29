from django import template
from datetime import datetime

register = template.Library()

@register.filter
def format_time(value):
    """
    Formats time string like '2025-10-29T17:00' into a more readable format
    """
    if not value:
        return ""
    
    try:
        # Parse the time string
        dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
        # Format it nicely (e.g., "October 29, 2025 at 5:00 PM")
        return dt.strftime("%B %d, %Y at %I:%M %p")
    except ValueError:
        # If parsing fails, return the original value
        return value

@register.filter
def format_time_short(value):
    """
    Formats time string like '2025-10-29T17:00' into a short format
    """
    if not value:
        return ""
    
    try:
        # Parse the time string
        dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
        # Format it in a short format (e.g., "Oct 29, 2025, 5:00 PM")
        return dt.strftime("%b %d, %Y, %I:%M %p")
    except ValueError:
        # If parsing fails, return the original value
        return value