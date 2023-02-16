from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.order import Order
from ...types import Response


def _get_kwargs(
    order_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/store/order/{orderId}".format(client.base_url, orderId=order_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, Order]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Order.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, Order]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    order_id: int,
    *,
    client: Client,
) -> Response[Union[Any, Order]]:
    """Find purchase order by ID

     For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.

    Args:
        order_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Order]]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    order_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, Order]]:
    """Find purchase order by ID

     For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.

    Args:
        order_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Order]]
    """

    return sync_detailed(
        order_id=order_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    order_id: int,
    *,
    client: Client,
) -> Response[Union[Any, Order]]:
    """Find purchase order by ID

     For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.

    Args:
        order_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Order]]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    order_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, Order]]:
    """Find purchase order by ID

     For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.

    Args:
        order_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Order]]
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            client=client,
        )
    ).parsed
