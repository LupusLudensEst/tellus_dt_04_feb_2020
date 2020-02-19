from behave import *
from time import sleep


@then("Click on forgot password button")
def frgt_pswd_btn(context):
    """
    click forgot password button
    """
    context.app.restore_password_page.clck_frgt_pswd_button()

@then("Enter user name {usr_nm}")
def entr_usr_nm(context, usr_nm):
    """
    enter user name
    """
    context.app.restore_password_page.entr_usr_name(usr_nm)

@then("Click on reset password button")
def clck_rst_pswd_btn(context):
    """
    click on reset password button
    """
    context.app.restore_password_page.clck_rst_pswd_button()

@then("Verify page has a text {usr_nt_fnd}")
def txt_s_hr(context, usr_nt_fnd):
    """
    verify page has a text 'User not found'
    """
    context.app.restore_password_page.txt_s_here(usr_nt_fnd)

