from behave import *
from hola_mundo import hola_mundo


@given("No name is given")
def step_impl(context):
    context.name = ""


@when("the function is called")
def step_impl(context):
    pass


@then("return 'Hello World!'")
def step_impl(context):
    assert hola_mundo() == "Hello World!"


@given("Nicolas is given")
def step_impl(context):
    context.name = "Nicolas"


@given("Juan is given")
def step_impl(context):
    context.name = "Juan"


@then("return 'Hello Nicolas!'")
def step_impl(context):
    assert hola_mundo(context.name) == "Hello Nicolas!"


@then("do not return 'Hello Nicolas!'")
def step_impl(context):
    assert hola_mundo(context.name) != "Hello Nicolas!"
