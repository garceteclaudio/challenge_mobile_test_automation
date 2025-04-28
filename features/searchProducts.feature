Feature: Amazon App Login Functionality

    @smoke_test @search_products
    Scenario Outline: User successfully search product
        Given the user opens the Amazon app
        When the user selects country and language preferences
        And the user taps on Finalizado button
        Then the user should see Ingresar a tu cuenta section
        When the user taps on Omitir inicio de sesion button
        Then the user should be redirected to the Home section
        When the user search a product "<product_name>"
        Then the user should see a list of products
        Examples:
            | product_name       |
            | super nintendo console    |