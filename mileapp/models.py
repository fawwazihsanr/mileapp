from django.db import models


# Create your models here.
from django.utils import timezone


class ModelWithAutoTimestamp(models.Model):
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Mileapp(models.Model):
    transaction_id = models.TextField(blank=True, null=True)
    customer_name = models.TextField(blank=True, null=True)
    customer_code = models.IntegerField(blank=True, null=True)
    transaction_amount = models.IntegerField(blank=True, null=True)
    transaction_discount = models.IntegerField(blank=True, null=True)
    transaction_additional_field = models.IntegerField(blank=True, null=True)
    transaction_payment_type = models.IntegerField(blank=True, null=True)
    transaction_state = models.TextField(blank=True, null=True)
    transaction_code = models.TextField(blank=True, null=True)
    transaction_order = models.IntegerField(blank=True, null=True)
    location_id = models.TextField(blank=True, null=True)
    organization_id = models.IntegerField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    updated_at = models.TextField(blank=True, null=True)
    transaction_payment_type_name = models.TextField(blank=True, null=True)
    transaction_cash_amount = models.IntegerField(blank=True, null=True)
    transaction_cash_change = models.IntegerField(blank=True, null=True)
    customer_attribute_nama_sales = models.TextField(db_column='customer_attribute_Nama_Sales', blank=True,
                                                     null=True)  # Field name made lowercase.
    customer_attribute_top = models.TextField(db_column='customer_attribute_TOP', blank=True,
                                              null=True)  # Field name made lowercase.
    customer_attribute_jenis_pelanggan = models.TextField(db_column='customer_attribute_Jenis_Pelanggan', blank=True,
                                                          null=True)  # Field name made lowercase.
    connote_connote_id = models.TextField(blank=True, null=True)
    connote_connote_number = models.IntegerField(blank=True, null=True)
    connote_connote_service = models.TextField(blank=True, null=True)
    connote_connote_service_price = models.IntegerField(blank=True, null=True)
    connote_connote_amount = models.IntegerField(blank=True, null=True)
    connote_connote_code = models.TextField(blank=True, null=True)
    connote_connote_booking_code = models.IntegerField(blank=True, null=True)
    connote_connote_order = models.IntegerField(blank=True, null=True)
    connote_connote_state = models.TextField(blank=True, null=True)
    connote_connote_state_id = models.IntegerField(blank=True, null=True)
    connote_zone_code_from = models.TextField(blank=True, null=True)
    connote_zone_code_to = models.TextField(blank=True, null=True)
    connote_surcharge_amount = models.IntegerField(blank=True, null=True)
    connote_transaction_id = models.TextField(blank=True, null=True)
    connote_actual_weight = models.IntegerField(blank=True, null=True)
    connote_volume_weight = models.IntegerField(blank=True, null=True)
    connote_chargeable_weight = models.IntegerField(blank=True, null=True)
    connote_created_at = models.TextField(blank=True, null=True)
    connote_updated_at = models.TextField(blank=True, null=True)
    connote_organization_id = models.IntegerField(blank=True, null=True)
    connote_location_id = models.TextField(blank=True, null=True)
    connote_connote_total_package = models.IntegerField(blank=True, null=True)
    connote_connote_surcharge_amount = models.IntegerField(blank=True, null=True)
    connote_connote_sla_day = models.IntegerField(blank=True, null=True)
    connote_location_name = models.TextField(blank=True, null=True)
    connote_location_type = models.TextField(blank=True, null=True)
    connote_source_tariff_db = models.TextField(blank=True, null=True)
    connote_id_source_tariff = models.IntegerField(blank=True, null=True)
    connote_pod = models.IntegerField(blank=True, null=True)
    connote_id = models.TextField(blank=True, null=True)
    origin_data_customer_name = models.TextField(blank=True, null=True)
    origin_data_customer_address = models.TextField(blank=True, null=True)
    origin_data_customer_email = models.TextField(blank=True, null=True)
    origin_data_customer_phone = models.TextField(blank=True, null=True)
    origin_data_customer_address_detail = models.IntegerField(blank=True, null=True)
    origin_data_customer_zip_code = models.IntegerField(blank=True, null=True)
    origin_data_zone_code = models.TextField(blank=True, null=True)
    origin_data_organization_id = models.IntegerField(blank=True, null=True)
    origin_data_location_id = models.TextField(blank=True, null=True)
    destination_data_customer_name = models.TextField(blank=True, null=True)
    destination_data_customer_address = models.TextField(blank=True, null=True)
    destination_data_customer_email = models.IntegerField(blank=True, null=True)
    destination_data_customer_phone = models.IntegerField(blank=True, null=True)
    destination_data_customer_address_detail = models.TextField(blank=True, null=True)
    destination_data_customer_zip_code = models.IntegerField(blank=True, null=True)
    destination_data_zone_code = models.TextField(blank=True, null=True)
    destination_data_organization_id = models.IntegerField(blank=True, null=True)
    destination_data_location_id = models.TextField(blank=True, null=True)
    koli_data_koli_length = models.IntegerField(blank=True, null=True)
    koli_data_awb_url = models.TextField(blank=True, null=True)
    koli_data_created_at = models.DateTimeField(blank=True, null=True)
    koli_data_koli_chargeable_weight = models.IntegerField(blank=True, null=True)
    koli_data_koli_width = models.IntegerField(blank=True, null=True)
    koli_data_koli_height = models.IntegerField(blank=True, null=True)
    koli_data_updated_at = models.DateTimeField(blank=True, null=True)
    koli_data_koli_description = models.TextField(blank=True, null=True)
    koli_data_koli_formula_id = models.IntegerField(blank=True, null=True)
    koli_data_connote_id = models.TextField(blank=True, null=True)
    koli_data_koli_volume = models.IntegerField(blank=True, null=True)
    koli_data_koli_weight = models.IntegerField(blank=True, null=True)
    koli_data_koli_id = models.TextField(blank=True, null=True)
    koli_data_koli_custom_field_awb_sicepat = models.IntegerField(blank=True, null=True)
    koli_data_koli_custom_field_harga_barang = models.IntegerField(blank=True, null=True)
    koli_data_koli_code = models.TextField(blank=True, null=True)
    custom_field_catatan_tambahan = models.TextField(blank=True, null=True)
    currentlocation_name = models.TextField(db_column='currentLocation_name', blank=True,
                                            null=True)  # Field name made lowercase.
    currentlocation_code = models.TextField(db_column='currentLocation_code', blank=True,
                                            null=True)  # Field name made lowercase.
    currentlocation_type = models.TextField(db_column='currentLocation_type', blank=True,
                                            null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'mileapp'
