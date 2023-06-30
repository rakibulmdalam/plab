import schemathesis

schema = schemathesis.from_uri("http://localhost:5000/swagger.json")


@schema.parametrize()
def test_api(case):
    case.call_and_validate()
