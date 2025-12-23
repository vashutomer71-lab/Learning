def auth_headers(token: str) -> dict:
    """Return default headers with Bearer token."""
    return {
        "Content-Type": "application/json",   # ✅ json (without 's')
        "Authorization": f"Bearer {token}",
    }

JSON_HEADERS = {
    "Content-Type": "application/json"
}
