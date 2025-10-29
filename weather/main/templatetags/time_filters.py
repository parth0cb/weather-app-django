from django import template
from datetime import datetime
from django.utils import timezone
import pytz

register = template.Library()

@register.filter
def format_time(value):
    """
    Formats time string like '2025-10-29T17:00' into a more readable format
    """
    if not value:
        return ""
    
    try:
        # Open-Meteo API returns time in ISO format like '2025-10-29T17:00'
        # This represents local time for the location
        if 'T' in value and '+' not in value and 'Z' not in value:
            # Format is like '2025-10-29T17:00' without timezone info
            # This represents local time from the API
            date_str, time_str = value.split('T')
            year, month, day = map(int, date_str.split('-'))
            hour, minute = map(int, time_str.split(':'))
            
            # Create datetime object - this assumes the API returns local time
            dt = datetime(year, month, day, hour, minute)
        else:
            # Handle formats with timezone info
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
        # Open-Meteo API returns time in ISO format like '2025-10-29T17:00'
        # This represents local time for the location
        if 'T' in value and '+' not in value and 'Z' not in value:
            # Format is like '2025-10-29T17:00' without timezone info
            # This represents local time from the API
            date_str, time_str = value.split('T')
            year, month, day = map(int, date_str.split('-'))
            hour, minute = map(int, time_str.split(':'))
            
            # Create datetime object - this assumes the API returns local time
            dt = datetime(year, month, day, hour, minute)
        else:
            # Handle formats with timezone info
            dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
        
        # Format it in a short format (e.g., "Oct 29, 2025, 5:00 PM")
        return dt.strftime("%b %d, %Y, %I:%M %p")
    except ValueError:
        # If parsing fails, return the original value
        return value