from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    username: Union[Unset, None, str] = UNSET,
    password: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/user/login".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["username"] = username

    params["password"] = password

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, str]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(str, response.json())
        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    username: Union[Unset, None, str] = UNSET,
    password: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, str]]:
    """Logs user into the system

    Args:
        username (Union[Unset, None, str]):
        password (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, str]]
    """

    kwargs = _get_kwargs(
        client=client,
        username=username,
        password=password,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    username: Union[Unset, None, str] = UNSET,
    password: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, str]]:
    """Logs user into the system

    Args:
        username (Union[Unset, None, str]):
        password (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, str]]
    """

    return sync_detailed(
        client=client,
        username=username,
        password=password,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    username: Union[Unset, None, str] = UNSET,
    password: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, str]]:
    """Logs user into the system

    Args:
        username (Union[Unset, None, str]):
        password (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, str]]
    """

    kwargs = _get_kwargs(
        client=client,
        username=username,
        password=password,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    username: Union[Unset, None, str] = UNSET,
    password: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, str]]:
    """Logs user into the system

    Args:
        username (Union[Unset, None, str]):
        password (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, str]]
    """

    return (
        await asyncio_detailed(
            client=client,
            username=username,
            password=password,
        )
    ).parsed
