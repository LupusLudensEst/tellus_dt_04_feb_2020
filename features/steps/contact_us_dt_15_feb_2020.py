from behave import *
from time import sleep


@then("Click on contact us button")
def clck_contct_us_bttn(context):
    context.app.contact_us_page.clck_contct_us_button()

@then('First Name {f_name}')
def frst_name_entrd(context, f_name):
    context.app.contact_us_page.frst_nm_entered(f_name)

@then('Last Name {l_name}')
def lst_name_entrd(context, l_name):
    context.app.contact_us_page.lst_nm_entered(l_name)

@then('Email Address {e_mail}')
def email_entrd(context, e_mail):
    context.app.contact_us_page.e_mail_entered(e_mail)

@then('Phone Number {p_nmbr}')
def phone_entrd(context, p_nmbr):
    context.app.contact_us_page.phone_entered(p_nmbr)

@then('Message {msg}')
def msg(context, msg):
    context.app.contact_us_page.message(msg)

@then("Click on Sumbit button")
def clck_sbmt_bttn(context):
    context.app.contact_us_page.clck_sbmt_button()
    sleep(4)

@then(
    'Verify {text_here} text is here')
def txt_is_hr(context, text_here):
    context.app.contact_us_page.txt_is_here(text_here)