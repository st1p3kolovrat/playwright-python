class UserCredentials:
    PASSWORD = "secret_sauce"
    STANDARD_USER = "standard_user"
    LOCKED_OUT_USER = "locked_out_user"
    PERFORMANCE_GLITCH_USER = "performance_glitch_user"


class ErrorMsg:
    LOGIN_ERR_LOCKED_OUT = "Epic sadface: Sorry, this user has been locked out."
    LOGIN_ERR_INVALID_CREDS = "Epic sadface: Username and password do not match any user in this service"
    LOGIN_ERR_USERNAME_MISSING = "Epic sadface: Username is required"
    LOGIN_ERR_PWD_MISSING = "Epic sadface: Password is required"
