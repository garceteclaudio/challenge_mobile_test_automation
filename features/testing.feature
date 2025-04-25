Feature: Tesintg

    Testing Feature
    
    @test12345
    Scenario Outline: Scenario Outline Testing
        Given El usuario abre la app "<app_name>"
        Examples:
            | usuario           | app_name  |
            | DebitosAutomatico | ebay      |
        