import spotify

ALBUM_URI: str = "spotify:album:1o7kL55w6IvIGz4mfWJjfu"
USER_URI: str = "spotify:user:4lml5veu8zto4kbph5b6toyp4"
CLIENT_ID: str = "6b437473db9b4770a42d3f29f5786137"
CLIENT_SECRET: str = "b0ca0af3a2634a349d3b4a574b3f831f"

async def user(user_uri: str) -> None:
    # Useful tip: use a context manager to handle
    # automatically closing any underlying http sessions
    async with spotify.Client(CLIENT_ID, CLIENT_SECRET) as client:
        u = await client.get_user(user_uri)
        return f"{u.display_name} with id {u.id} from {u.country}"

