from django.db import models

# Create your models here.


class BuyerAzPackageManager(models.Manager):
    def get_queryset(self):
        return super(BuyerAzPackageManager, self).get_queryset().filter(user_type='buyer', is_active=1)


class SellerAzPackageManager(models.Manager):
    def get_queryset(self):
        return super(SellerAzPackageManager, self).get_queryset().filter(user_type='seller', is_active=1)


class AzPackage(models.Model):
    TYPE_OF_USER = (
        ('seller', 'seller'),
        ('buyer', 'buyer'),
    )
    user_type = models.CharField(max_length=6, choices=TYPE_OF_USER, default='seller')
    package_name = models.CharField(max_length=200, blank=True, null=True, unique=True)
    package_code = models.CharField(max_length=25, blank=True, null=True, unique=True)
    description = models.TextField()
    is_active = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    objects = models.Manager()
    buyer_objects = BuyerAzPackageManager()
    seller_objects = SellerAzPackageManager()


    class Meta:
        verbose_name = "Package"
        verbose_name_plural = "Packages"

    def __str__(self):
        return 'Package ' + str(self.package_name)


class BuyerAzCountryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=1)


class SellerAzCountryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=1)


class AzCountry(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=200, blank=True, null=True, unique=True)
    country_code = models.CharField(max_length=25, blank=True, null=True, unique=True)
    is_active = models.IntegerField(default=0)
    currency = models.CharField(max_length=25, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    objects = models.Manager()
    buyer_objects = BuyerAzCountryManager()
    seller_objects = SellerAzCountryManager()

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return 'Country ' + str(self.country_name)


class BuyerAzStateManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=1)


class SellerAzStateManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=1)


class AzState(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=200, blank=True, null=True, unique=True)
    state_code = models.CharField(max_length=50, blank=True, null=True, unique=True)
    country = models.ForeignKey(AzCountry, on_delete=models.SET_NULL, blank=True, null=True)
    is_active = models.IntegerField(default=0)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    objects = models.Manager()
    buyer_objects = BuyerAzStateManager()
    seller_objects = SellerAzStateManager()

    class Meta:
        verbose_name = "State "
        verbose_name_plural = "States"

    def __str__(self):
        return 'State ' + str(self.state_name)


class BuyerAzCityManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=1)


class SellerAzCityManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=1)


class AzCity(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=200, blank=True, null=True, unique=True)
    city_code = models.CharField(max_length=50, blank=True, null=True, unique=True)
    state = models.ForeignKey('AzState', on_delete=models.SET_NULL, blank=True, null=True)
    is_active = models.IntegerField(default=0)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    objects = models.Manager()
    buyer_objects = BuyerAzCityManager()
    seller_objects = SellerAzCityManager()

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return 'City ' + str(self.city_name)


class BuyerMeasureUnitManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=1)


class SellerMeasureUnitManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=1)


# store measure unit
class MeasureUnit(models.Model):
    unit = models.CharField(max_length=150, unique=True)
    code = models.CharField(max_length=50, unique=True)
    is_active = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    objects = models.Manager()
    buyer_objects = BuyerMeasureUnitManager()
    seller_objects = SellerMeasureUnitManager()

    class Meta:
        verbose_name_plural = "Measure Units"

    def __str__(self):
        return 'Measure unit ' + str(self.unit)


class BuyerTimeUnitManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=1)


class SellerTimeUnitManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=1)


# store time unit
class TimeUnit(models.Model):
    unit = models.CharField(max_length=150, unique=True)
    code = models.CharField(max_length=50, unique=True)
    is_active = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    objects = models.Manager()
    buyer_objects = BuyerTimeUnitManager()
    seller_objects = SellerTimeUnitManager()

    class Meta:
        ordering = ['-created_by']
        verbose_name_plural = "Time Units"

    def __str__(self):
        return 'Time unit -> ' + str(self.unit)


class AuthorizationType(models.Model):
    name = models.CharField(max_length=250, unique=True)
    code = models.CharField(max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['-created_by']
        verbose_name_plural = "Types of Authorization"

    def __str__(self):
        return 'Authorization type -> ' + str(self.id)


class Authorization(models.Model):
    type = models.ForeignKey(AuthorizationType, related_name="authorization_authorization_type", on_delete=models.CASCADE)
    is_active = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['-created_by']
        verbose_name_plural = "Time Units"

    def __str__(self):
        return 'Authorization -> ' + str(self.id)
