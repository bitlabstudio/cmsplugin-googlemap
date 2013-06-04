"""Models for the ``cmsplugin_googlemap`` app."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin


ZOOM_LEVELS = map(lambda c: (c, str(c)), range(22))


class GoogleMap(CMSPlugin):
    """
    A google maps integration

    """
    title = models.CharField(
        verbose_name=_("map title"),
        max_length=100,
        blank=True,
    )

    address = models.CharField(
        verbose_name=_("address"),
        max_length=150,
        blank=True,
    )

    zipcode = models.CharField(
        verbose_name=_("zip code"),
        max_length=30,
        blank=True,
    )

    city = models.CharField(
        verbose_name=_("city"),
        max_length=100,
    )

    content = models.CharField(
        verbose_name=_("additional content"),
        max_length=255,
        blank=True,
        help_text=_('Displayed under address in the bubble.'),
    )

    zoom = models.PositiveSmallIntegerField(
        verbose_name=_("zoom level"),
        choices=ZOOM_LEVELS,
        default=13,
    )

    lat = models.DecimalField(
        verbose_name=_('latitude'),
        max_digits=10,
        decimal_places=6,
        null=True, blank=True,
        help_text=_('Use latitude & longitude to fine tune the map position.'),
    )

    lng = models.DecimalField(
        verbose_name=_('longitude'),
        max_digits=10,
        decimal_places=6,
        null=True, blank=True,
    )

    route_planer_title = models.CharField(
        verbose_name=_("route planer title"),
        max_length=150,
        blank=True,
        null=True,
        default=_('Calculate your fastest way to here'),
    )

    route_planer = models.BooleanField(
        verbose_name=_("route planer"),
        default=False,
    )

    width = models.CharField(
        verbose_name=_('width'),
        max_length=6,
        default='100%',
        help_text=_('Plugin width (in pixels or percent).')
    )
    height = models.CharField(
        verbose_name=_('height'),
        max_length=6,
        default='400px',
        help_text=_('Plugin height (in pixels).'),
    )

    def __unicode__(self):
        return u"%s (%s, %s %s)" % (self.get_title(), self.address,
                                    self.zipcode, self.city,)

    def get_title(self):
        if self.title is None:
            return _("Map")
        return self.title

    def get_lat_lng(self):
        if self.lat and self.lng:
            return (self.lat, self.lng)
