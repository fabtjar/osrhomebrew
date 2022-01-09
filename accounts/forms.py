from allauth.account.forms import (
    SignupForm,
    LoginForm,
    ResetPasswordForm,
    ChangePasswordForm,
)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, HTML


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.add_input(
            Submit("submit", "Sign up", css_class="btn-success w-100")
        )


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["login"].label = False
        self.fields["password"].label = False
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div("login", "password", "remember"),
            Div(
                HTML(
                    """<p><a href="{% url 'account_reset_password' %}">Forgot password?</a></p>"""
                ),
                css_class="text-center",
            ),
            Submit("submit", "Sign in", css_class="btn-success w-100"),
        )


class CustomResetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

        self.helper.add_input(
            Submit("submit", "Reset my password", css_class="btn-success w-100")
        )


class CustomSetPasswordForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.add_input(
            Submit("submit", "Change password", css_class="btn-success w-100"),
        )
