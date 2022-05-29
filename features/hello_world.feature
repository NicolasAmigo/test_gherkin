Feature: Welcoming the user

    Scenario: Welcome without name
        Given No name is given
        When the function is called
        Then return 'Hello World!'

    Scenario: Welcome with name
        Given Nicolas is given
        When the function is called
        Then return 'Hello Nicolas!'

    Scenario: Welcome with correct name
        Given Juan is given
        When the function is called
        Then do not return 'Hello Nicolas!'