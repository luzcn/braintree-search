import braintree, os

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Production,
        merchant_id=os.getenv('BRAINTREE_MERCHANT_ID'),
        public_key=os.getenv('BRAINTREE_PUBLIC_KEY'),
        private_key=os.getenv('BRAINTREE_PRIVATE_KEY')
    )
)


def search(verification_id):
    collection = gateway.verification.search(
        braintree.CreditCardVerificationSearch.id == verification_id
    )

    for verification in collection.items:
        print(verification)


search("")
