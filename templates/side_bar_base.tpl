{% extends "base.tpl" %}

{% block carnel %}
    <div class="col-sm-3 sidenav">
        {% block sidebar %}{% endblock %}
    </div>
    <div class="col-sm-9 text-left">
    {% block content %}{% endblock %}
    </div>
{% endblock %}