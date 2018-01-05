{% extends "base.tpl" %}

{% block carnel %}
    <div class="col-sm-2 sidenav">
        {% block sidebar %}{% endblock %}
    </div>
    <div class="col-sm-10 text-left">
    {% block content %}{% endblock %}
    </div>
{% endblock %}