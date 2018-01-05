{% extends "library/side_bar_base.tpl" %}

{% block content %}
    <h3 style="text-align: center">Означення</h3>
    <ul class="cont">
    {% for obj in definitions %}
        <li class="cont">
            <a class="definition" onclick="ShowHide({{ forloop.counter }})"><b>{{ obj.name }}</b></a>
            <span class="myDIV" id="{{ forloop.counter }}" style="display: none">{{ obj.text|safe }}</span>
        </li>
    {% endfor %}
    </ul>


    <script>
    function ShowHide(spanid) {
        var x = document.getElementById(spanid);
        if (x.style.display == "none") {
            x.style.display = "block";
        } else {
            x.style.display = "none";
        }
    }
    </script>
{% endblock %}
