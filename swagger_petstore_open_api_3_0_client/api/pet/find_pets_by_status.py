from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.find_pets_by_status_status import FindPetsByStatusStatus
from ...models.pet import Pet
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    status: Union[Unset, None, FindPetsByStatusStatus] = FindPetsByStatusStatus.AVAILABLE,
) -> Dict[str, Any]:
    url = "{}/pet/findByStatus".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_status: Union[Unset, None, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value if status else None

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, List["Pet"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Pet.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, List["Pet"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    status: Union[Unset, None, FindPetsByStatusStatus] = FindPetsByStatusStatus.AVAILABLE,
) -> Response[Union[Any, List["Pet"]]]:
    """Finds Pets by status

     Multiple status values can be provided with comma separated strings

    Args:
        status (Union[Unset, None, FindPetsByStatusStatus]):  Default:
            FindPetsByStatusStatus.AVAILABLE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['Pet']]]
    """

    kwargs = _get_kwargs(
        client=client,
        status=status,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    status: Union[Unset, None, FindPetsByStatusStatus] = FindPetsByStatusStatus.AVAILABLE,
) -> Optional[Union[Any, List["Pet"]]]:
    """Finds Pets by status

     Multiple status values can be provided with comma separated strings

    Args:
        status (Union[Unset, None, FindPetsByStatusStatus]):  Default:
            FindPetsByStatusStatus.AVAILABLE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['Pet']]]
    """

    return sync_detailed(
        client=client,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    status: Union[Unset, None, FindPetsByStatusStatus] = FindPetsByStatusStatus.AVAILABLE,
) -> Response[Union[Any, List["Pet"]]]:
    """Finds Pets by status

     Multiple status values can be provided with comma separated strings

    Args:
        status (Union[Unset, None, FindPetsByStatusStatus]):  Default:
            FindPetsByStatusStatus.AVAILABLE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['Pet']]]
    """

    kwargs = _get_kwargs(
        client=client,
        status=status,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    status: Union[Unset, None, FindPetsByStatusStatus] = FindPetsByStatusStatus.AVAILABLE,
) -> Optional[Union[Any, List["Pet"]]]:
    """Finds Pets by status

     Multiple status values can be provided with comma separated strings

    Args:
        status (Union[Unset, None, FindPetsByStatusStatus]):  Default:
            FindPetsByStatusStatus.AVAILABLE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['Pet']]]
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
        )
    ).parsed
