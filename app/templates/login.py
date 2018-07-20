{% extends "base.html" %}

{% block content %}
	<h1>Sign In</h1>
	<form action="" method="post" novalidate>
		{{ form.hidden_tag() }}
		<p>
			{{ form.username.label }}<br>
			{{ form.username(size=32) }}
		</p>
		<p>
			{{ form.password.label }}<br>
			{{ form.password(size=32) }}
		</p>
		<p>{{ form.remember_me() }} {{ form.remember_me.label }}</p>
		<p>{{ form.submit() }}</p>
	</form>
{% endblock %}