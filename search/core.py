import braintree, os, json

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Production,
        merchant_id=os.getenv('BRAINTREE_MERCHANT_ID'),
        public_key=os.getenv('BRAINTREE_PUBLIC_KEY'),
        private_key=os.getenv('BRAINTREE_PRIVATE_KEY')
    )
)


def search(verification_id):
    if verification_id is None:
        return []

    collection = gateway.verification.search(
        braintree.CreditCardVerificationSearch.id == verification_id
    )

    res = []
    for verification in collection.items:
        if verification.risk_data:
            res.append({'status': verification.status,
                        'risk_data': {'id': verification.risk_data.id,
                                      'decision': verification.risk_data.decision}
                        })
        else:
            res.append({'status': verification.status})

    return res
