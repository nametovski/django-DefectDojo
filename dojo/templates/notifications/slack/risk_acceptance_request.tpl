{% load i18n %}
{% load display_tags %}
{% blocktranslate trimmed with ra=risk_acceptance.name eng=engagement.name url=url|full_url %}
Risk acceptance "{{ ra }}" for engagement "{{ eng }}" requires approval: {{ url }}
{% endblocktranslate %}
{% if system_settings.disclaimer_notifications and system_settings.disclaimer_notifications.strip %}

    {% trans "Disclaimer" %}:
    {{ system_settings.disclaimer_notifications }}
{% endif %}

