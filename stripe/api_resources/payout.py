# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import api_requestor
from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class Payout(
    CreateableAPIResource, ListableAPIResource, UpdateableAPIResource
):
    OBJECT_NAME = "payout"

    @classmethod
    def _cls_cancel(
        cls,
        payout,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        requestor = api_requestor.APIRequestor(
            api_key, api_version=stripe_version, account=stripe_account
        )
        url = "/v1/payouts/{payout}/cancel".format(
            payout=util.sanitize_id(payout)
        )
        response, api_key = requestor.request("post", url, params)
        stripe_object = util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account
        )
        return stripe_object

    @util.class_method_variant("_cls_cancel")
    def cancel(self, idempotency_key=None, **params):
        url = "/v1/payouts/{payout}/cancel".format(
            payout=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    @classmethod
    def _cls_reverse(
        cls,
        payout,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        requestor = api_requestor.APIRequestor(
            api_key, api_version=stripe_version, account=stripe_account
        )
        url = "/v1/payouts/{payout}/reverse".format(
            payout=util.sanitize_id(payout)
        )
        response, api_key = requestor.request("post", url, params)
        stripe_object = util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account
        )
        return stripe_object

    @util.class_method_variant("_cls_reverse")
    def reverse(self, idempotency_key=None, **params):
        url = "/v1/payouts/{payout}/reverse".format(
            payout=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self
