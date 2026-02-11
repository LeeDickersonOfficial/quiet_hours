from homeassistant import config_entries
from homeassistant.helpers import selector

from .const import DOMAIN, CONF_MEDIA_PLAYERS

class QuietHoursConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(
                title="Quiet Hours",
                data=user_input
            )

        schema = {
            CONF_MEDIA_PLAYERS: selector.EntitySelector(
                selector.EntitySelectorConfig(
                    domain="media_player",
                    multiple=True
                )
            )
        }

        return self.async_show_form(
            step_id="user",
            data_schema=schema
        )
