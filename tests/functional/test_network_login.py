from playwright.sync_api import Playwright

credentials = {"userEmail": "rahulshetty@gmail.com", "userPassword": "Iamking@000"}


def test_login_thorugh_api(playwright: Playwright):
    request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
    post_data = request_context.post(url="api/ecom/auth/login", headers={"content-type": "application/json"},
                         data=credentials)

    response = post_data.json()
    print(response['token'])
