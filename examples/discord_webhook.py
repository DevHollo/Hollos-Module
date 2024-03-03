from hollosmodule import DiscordAPI

discord = DiscordAPI()

discord.webhook_send_msg("Hello World!", "https://discord.com/api/webhooks/123/abc123")