import braintree
import os
import requests


class Core:
    def __init__(self):
        self.gateway = braintree.BraintreeGateway(
            braintree.Configuration(
                braintree.Environment.Production,
                merchant_id=os.getenv('BRAINTREE_MERCHANT_ID'),
                public_key=os.getenv('BRAINTREE_PUBLIC_KEY'),
                private_key=os.getenv('BRAINTREE_PRIVATE_KEY')
            )
        )
        self.kount_url = os.getenv('KOUNT_URL')
        self.kount_api_key = os.getenv('KOUNT_API_KEY')

    # query the Kount service
    def get_kount(self, trx_id):
        if not trx_id:
            return

        path = '/rpc/v1/orders/detail.json'
        response = requests.get(self.kount_url + path,
                                params={'trid': trx_id},
                                headers={'x-kount-api-key': self.kount_api_key})

        if response.status_code != 200:
            return

        data = response.json()
        return data['result']

    def search(self, verification_id):
        if not verification_id:
            return []

        collection = self.gateway.verification.search(
            braintree.CreditCardVerificationSearch.id == verification_id
        )

        res = []
        for verification in collection.items:
            if verification.risk_data:
                kount = self.get_kount(verification.risk_data.id)

                res.append({'status': verification.status,
                            'created_at': verification.created_at,
                            'risk_data': {'id': verification.risk_data.id,
                                          'decision': verification.risk_data.decision},
                            'kount': kount
                            })
            else:
                res.append({'status': verification.status,
                            'created_at': verification.created_at,
                            'risk_data': 'null'})

        return res


def query(id):
    s = Core()
    return s.search(id)
