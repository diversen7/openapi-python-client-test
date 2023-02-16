from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pet import Pet
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    form_data: Pet,
    json_body: Pet,
) -> Dict[str, Any]:
    url = "{}/pet".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": form_data.to_dict(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, Pet]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Pet.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.METHOD_NOT_ALLOWED:
        response_405 = cast(Any, None)
        return response_405
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, Pet]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: Pet,
    json_body: Pet,
) -> Response[Union[Any, Pet]]:
    """Update an existing pet

     Update an existing pet by Id

    Args:
        json_body (Pet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Pet]]
    """

    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    form_data: Pet,
    json_body: Pet,
) -> Optional[Union[Any, Pet]]:
    """Update an existing pet

     Update an existing pet by Id

    Args:
        json_body (Pet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Pet]]
    """

    return sync_detailed(
        client=client,
        form_data=form_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    form_data: Pet,
    json_body: Pet,
) -> Response[Union[Any, Pet]]:
    """Update an existing pet

     Update an existing pet by Id

    Args:
        json_body (Pet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Pet]]
    """

    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    form_data: Pet,
    json_body: Pet,
) -> Optional[Union[Any, Pet]]:
    """Update an existing pet

     Update an existing pet by Id

    Args:
        json_body (Pet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Pet]]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            json_body=json_body,
        )
    ).parsed
