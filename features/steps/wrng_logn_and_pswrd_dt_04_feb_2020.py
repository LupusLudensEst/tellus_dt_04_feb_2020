from behave import *

@given("Loginpage")
def open_homepage(context):
    context.app.main_page.open_page()


@then("Click on login button")
def clck_logn_bttn(context):
    context.app.main_page.click_login_button()

@then('Wrong login {login}')
def wrng_lgn(context, login):
    context.app.main_page.wrong_login(login)

@then('Wrong password {password}')
def wrng_psswrd(context, password):
    context.app.main_page.wrong_password(password)


@then("Click on login button after login and password are entered")
def clck_logn_bttn_aftr_lgn_pswd_entrd(context):
    context.app.main_page.click_login_button_aftr_entrd()


@then('Verify {invld_nm} sign is here')
def alrt_is_hr(context, invld_nm):
    context.app.main_page.alert_is_here(invld_nm)


