{% extends "library/side_bar_base.tpl" %}

{% block content %}
    <h3 style="text-align: center">Статті</h3>
    <ul class="content">
    {% for obj in articles %}
        <li><a href="#">{{ obj.title }}</a></li>
    {% endfor %}
    </ul>
{% endblock %}
