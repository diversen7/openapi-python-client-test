from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import ApiResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pet_id: int,
    *,
    client: AuthenticatedClient,
    additional_metadata: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/pet/{petId}/uploadImage".format(client.base_url, petId=pet_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["additionalMetadata"] = additional_metadata

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[ApiResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[ApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pet_id: int,
    *,
    client: AuthenticatedClient,
    additional_metadata: Union[Unset, None, str] = UNSET,
) -> Response[ApiResponse]:
    """uploads an image

    Args:
        pet_id (int):
        additional_metadata (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiResponse]
    """

    kwargs = _get_kwargs(
        pet_id=pet_id,
        client=client,
        additional_metadata=additional_metadata,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pet_id: int,
    *,
    client: AuthenticatedClient,
    additional_metadata: Union[Unset, None, str] = UNSET,
) -> Optional[ApiResponse]:
    """uploads an image

    Args:
        pet_id (int):
        additional_metadata (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiResponse]
    """

    return sync_detailed(
        pet_id=pet_id,
        client=client,
        additional_metadata=additional_metadata,
    ).parsed


async def asyncio_detailed(
    pet_id: int,
    *,
    client: AuthenticatedClient,
    additional_metadata: Union[Unset, None, str] = UNSET,
) -> Response[ApiResponse]:
    """uploads an image

    Args:
        pet_id (int):
        additional_metadata (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiResponse]
    """

    kwargs = _get_kwargs(
        pet_id=pet_id,
        client=client,
        additional_metadata=additional_metadata,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pet_id: int,
    *,
    client: AuthenticatedClient,
    additional_metadata: Union[Unset, None, str] = UNSET,
) -> Optional[ApiResponse]:
    """uploads an image

    Args:
        pet_id (int):
        additional_metadata (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiResponse]
    """

    return (
        await asyncio_detailed(
            pet_id=pet_id,
            client=client,
            additional_metadata=additional_metadata,
        )
    ).parsed
