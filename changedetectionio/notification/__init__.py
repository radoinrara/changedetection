from changedetectionio.model import USE_SYSTEM_DEFAULT_NOTIFICATION_FORMAT_FOR_WATCH

default_notification_format = 'text'
default_notification_body = '\n---\n{{diff}}\n---\n'
default_notification_title = 'ChangeDetection - {{watch_title}}'

# The values (markdown etc) are from apprise NotifyFormat,
# But to avoid importing the whole heavy module just use the same strings here.
valid_notification_formats = {
    'text': 'Plain Text',
    'html': 'HTML',
    'htmlcolor': 'HTML Color',
    'markdown': 'Markdown to HTML',
    # Used only for editing a watch (not for global)
    USE_SYSTEM_DEFAULT_NOTIFICATION_FORMAT_FOR_WATCH: USE_SYSTEM_DEFAULT_NOTIFICATION_FORMAT_FOR_WATCH
}
