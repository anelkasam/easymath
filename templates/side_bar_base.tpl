{% extends "base.tpl" %}

{% block carnel %}
    <div class="wrapper">
        <nav id="sidebar">
            {% block sidebar %}{% endblock %}
        </nav>
        <div id="content">
            {% block content %}{% endblock %}
        </div>
    </div>
{% endblock %}