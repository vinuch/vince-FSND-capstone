from functools import wraps
from flask import session
from urllib.request import urlopen
import json
from jose import jwt


AUTH0_DOMAIN = 'dev-vince.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'casting_agency'


def verify_decode_jwt(token):
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}
    if 'kid' not in unverified_header:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization malformed.'
        }, 401)

    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://' + AUTH0_DOMAIN + '/'
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'token_expired',
                'description': 'Token expired.'
            }, 401)

        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'invalid_claims',
                'description': 'Incorrect claims. Please, check the audience and issuer.'
            }, 401)
        except Exception:
            raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to parse authentication token.'
            }, 401)
    raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to find the appropriate key.'
            }, 401)
    raise Exception('Not Implemented')

def check_permissions(permission, payload):
    if 'permissions' not in payload:
        AuthError({
            'code': 'No_Permissions',
            'description': 'Permissions was expected as part of jwt payload '
        }, 401)
    
    elif permission not in payload['permissions']:
        AuthError({
            'code': 'requested_permission_unavailable',
            'description': 'the requested permission is not availabe for this useer'
        }, 401)
    else:
        return True
        