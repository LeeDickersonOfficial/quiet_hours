from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.restore_state import RestoreEntity

from .const import CONF_MEDIA_PLAYERS, DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([QuietHoursSwitch(hass, entry)])


class QuietHoursSwitch(SwitchEntity, RestoreEntity):
    _attr_name = "Quiet Hours"
    _attr_icon = "mdi:weather-night"

    def __init__(self, hass, entry):
        self.hass = hass
        self.entry = entry
        self._state = False
        self._players = entry.data.get(CONF_MEDIA_PLAYERS, [])
        self._previous_states: dict[str, bool | None] = {}

        # Required for entity registry
        self._attr_unique_id = f"{entry.entry_id}_quiet_hours"

    @property
    def is_on(self):
        return self._state

    async def async_added_to_hass(self):
        last_state = await self.async_get_last_state()
        if last_state:
            self._state = last_state.state == "on"

    async def async_turn_on(self, **kwargs):
        if self._state:
            return

        self._state = True
        self._previous_states.clear()
        await self._mute_players()
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs):
        if not self._state:
            return

        self._state = False
        await self._restore_players()
        self._previous_states.clear()
        self.async_write_ha_state()

    async def _mute_players(self):
        for entity_id in self._players:
            state = self.hass.states.get(entity_id)
            if state:
                self._previous_states[entity_id] = state.attributes.get(
                    "is_volume_muted"
                )

        if self._players:
            await self.hass.services.async_call(
                "media_player",
                "volume_mute",
                {
                    "entity_id": self._players,
                    "is_volume_muted": True,
                },
                blocking=False,
            )

    async def _restore_players(self):
        for entity_id, was_muted in self._previous_states.items():
            if was_muted is False:
                await self.hass.services.async_call(
                    "media_player",
                    "volume_mute",
                    {
                        "entity_id": entity_id,
                        "is_volume_muted": False,
                    },
                    blocking=False,
                )
