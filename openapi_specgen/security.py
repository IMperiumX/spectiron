from dataclasses import dataclass
from typing import Protocol
from typing import Union


@dataclass
class BasicAuth:
    protocol_type: Protocol = "http"
    scheme: str = "basic"

    def as_dict(self):
        return {"type": self.protocol_type, "scheme": self.scheme}


@dataclass
class BearerAuth:
    protocol_type: Protocol = "http"
    scheme: str = "bearer"

    def as_dict(self):
        return {"type": self.protocol_type, "scheme": self.scheme}


@dataclass
class ApiKeyAuth:
    protocol_type: Protocol = "apiKey"
    in_location: str = "header"
    name: str = "X-API-Key"

    def as_dict(self):
        return {
            "type": self.protocol_type,
            "in": self.in_location,
            "name": self.name
        }


@dataclass
class OpenApiSecurity:
    basic_auth: Union[BasicAuth, None] = None
    bearer_auth: Union[BearerAuth, None] = None
    api_key_auth: Union[ApiKeyAuth, None] = None

    def as_dict(self):
        auth_options = dict()
        self._auth_handler(
            auth_options,
            self.basic_auth,
            self.basic_auth.__class__.__name__,
        )
        self._auth_handler(
            auth_options,
            self.bearer_auth,
            self.bearer_auth.__class__.__name__,
        )
        self._auth_handler(
            auth_options,
            self.api_key_auth,
            self.api_key_auth.__class__.__name__,
        )

        return auth_options

    def get_security_reference(self):
        """Returns reference to configured openapi schemas"""
        auth_ref = []
        self._auth_ref_handler(auth_ref, self.api_key_auth, "ApiKeyAuth")
        self._auth_ref_handler(auth_ref, self.basic_auth, "BasicAuth")
        self._auth_ref_handler(auth_ref, self.bearer_auth, "BearerAuth")
        return auth_ref

    def _auth_ref_handler(self, auth_ref, prop, key):
        if prop:
            auth_ref.append({key: []})

    def _auth_handler(self, auth_options, prop, key):
        if prop:
            auth_options[key] = prop.as_dict()
