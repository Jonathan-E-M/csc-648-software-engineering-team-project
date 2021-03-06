document.write(
   ' <nav class="navbar navbar-expand-lg navbar-dark bg-dark">\
    <a class="navbar-brand" href="{% url 'landing' %}">Ceres</a>\
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">\
    <span class="navbar-toggler-icon"></span>\
    </button>\

    <div class="collapse navbar-collapse" id="navbarSupportedContent">\
        <ul class="navbar-nav mr-auto">\
            <li class="nav-item">\
                <a class="nav-link" href="{% url 'about' %}">About us</a>\
            </li>\
            <li class="nav-item">\
                    <a class="nav-link" href="{% url 'landing' %}">Landing</a>\
                </li>\
        </ul>\
        <ul class="nav navbar-nav ml-auto">\
            {% if user.is_authenticated %}\
                <li class="nav-item">\
                    <a class="nav-link" href="{% url 'signout' %}">Log out</a>\
                </li>\
            {% else %}\
                <li class="nav-item">\
                    <a class="nav-link" href="{% url 'signin' %}">Sign in</a>\
                </li>\
                <li class="nav-item">\
                    <a class="nav-link" href="{% url 'signup' %}">Sign up</a>\
                </li>\
            {% endif %}\
        </ul>\
        <form class="form-inline my-2 my-lg-0">\
        </form>\
    </div>\
</nav> '
);