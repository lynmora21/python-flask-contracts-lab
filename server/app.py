#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}
]

customers = ["bob", "bill", "john", "sarah"]

app = Flask(__name__)


@app.route('/contract/<int:id>')
def get_contract(id):
    # Search the contracts list for a contract with the requested ID.
    for contract in contracts:
        if contract["id"] == id:
            # Return the contract information with a 200 status code.
            return contract, 200

    # Return a 404 if no contract matches the requested ID.
    return "Contract not found", 404


@app.route('/customer/<customer_name>')
def get_customer(customer_name):
    # Check whether the requested customer exists.
    if customer_name in customers:
        # Customer information is sensitive, so return an empty body.
        return "", 204

    # Return a 404 if the customer does not exist.
    return "Customer not found", 404


if __name__ == '__main__':
    app.run(port=5555, debug=True)
