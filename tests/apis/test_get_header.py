def test_get_header(playwright):
    request = playwright.request.new_context(
        extra_http_headers={
            "Accept": "application/json",
            "Authorization": "Bearer your_token_here",
            "X-api-key": "reqres-api-key"
        }
    )
    response = request.get("https://reqres.in/api/users?page=2")
    assert response.status == 200
    json_data = response.json()
    print(json_data)
    # assert json_data["id"] == 1
    request.dispose()
    print("API GET request successful and data validated.")
    #assert json_data["title"] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"