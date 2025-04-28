Feature: Amazon App Login Functionality

    @smoke_test @amazon_login
    Scenario Outline: User successfully logs into the Amazon application
        Given the user opens the Amazon app
        When the user selects country and language preferences
        And the user taps on Finalizado button
        Then the user should see Ingresar a tu cuenta section
        When the user taps on ¿Ya eres cliente? Iniciar sesion. button
        And the user enters a valid email adress "<user_email>"
        And the user taps on Continuar button
        And the user enters a valid password
        And the user taps on Iniciar Sesion button
        Then the user should be redirected to the Home section
        Examples:
            | user_email                   |
            | test@gmail.com     |